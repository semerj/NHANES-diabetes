import json
import pandas as pd
import argparse
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from model_imports import *


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data',
                         help='location of training data in CSV format',
                         type=str)
    parser.add_argument('-b', '--best_model',
                         help='location of output in JSON format',
                         type=str)
    args = parser.parse_args()

    df = pd.read_csv(args.data)
    y = df.status.apply(lambda x: 0 if x == 'nodiab' else 1)
    X = df.drop(['status'], axis=1).fillna(0)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

    with open(args.best_model) as f:
        best_models = json.load(f)

    def combine_models(best_models, X, y, X_test):
        test_preds = []
        train_preds = []
        for mp in best_models:
            model_name = mp['model']
            params = mp['params']
            model_str =  model_name + '(**' + str(params) + ')'
            model = eval(model_str)
            # if 'predict_proba' in dir(model) and model_name != 'SVC':
            #     clf = model.fit(X, y)
            #     test_pred = clf.predict_proba(X_test)[:,1]
            #     train_pred = clf.predict_proba(X)[:,1]
            # else:
            clf = model.fit(X, y)
            test_pred = clf.predict(X_test)
            train_pred = clf.predict(X)
            train_preds.append(train_pred)
            test_preds.append(test_pred)
        X_test_pred = pd.DataFrame(test_preds).T
        X_train_pred = pd.DataFrame(train_preds).T
        return X_test_pred, X_train_pred


    X_test_pred, X_train_pred = combine_models(
            best_models,
            X_train,
            y_train,
            X_test
            )

    mode_pred = X_test_pred.apply(lambda x: x.value_counts().index[0], axis=1)
    mode_pred_acc = sum(mode_pred == y_test)/len(y_test)
    print('Mode accuracy: {}'.format(mode_pred_acc))

    clf_stage2 = LogisticRegression().fit(X_train_pred, y_train)
    stage2_pred = clf_stage2.predict(X_test_pred)
    stage2_acc = sum(stage2_pred == y_test)/len(y_test)
    print('Stage-2 accuracy: {}'.format(stage2_acc))

