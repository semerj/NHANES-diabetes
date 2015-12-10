import json
import pandas as pd
import argparse
from utils import parse_json_model, GridSearchCVWrapper
from model_imports import *


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data',
                         help='location of training data in CSV format',
                         type=str)
    parser.add_argument('-m', '--model_specifications',
                         help='location of models and hyperparameters in JSON format',
                         type=str)
    parser.add_argument('-b', '--best_model',
                         help='location of output in JSON format',
                         type=str)
    args = parser.parse_args()

    # ./data/diabetes_data.csv
    df = pd.read_csv(args.data)
    y = df.status
    X = df.drop(['status'], axis=1).fillna(0)

    # ./models/model_definition.json
    with open(args.model_specifications) as model_file:
        models_str = json.load(model_file)
        models = parse_json_model(models_str)

    best_params = GridSearchCVWrapper(X, y, models)

    model_names = [m[0].__class__.__name__ for m in models]
    model_info = []
    for m, p in zip(model_names, best_params):
        model_dict = {}
        model_dict['model'] = m
        model_dict['params'] = dict(p)
        model_info.append(model_dict)

    with open(args.best_model, 'w') as fp:
        json.dump(model_info, fp, indent=4, sort_keys=True)
