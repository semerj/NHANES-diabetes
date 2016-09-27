import numpy as np
import pandas as pd
import matplotlib.pylab as plt

from sklearn.grid_search import GridSearchCV
from sklearn import metrics


def one_hot_encode(feature, prefix):
    return pd.get_dummies(data=feature,
                          prefix=prefix,
                          drop_first=True,
                          dummy_na=True).astype('int')


def GridSearchCVWrapper(model, param_grid, X, y, n_jobs=-1, cv=10):
    clf_cv = GridSearchCV(model, param_grid=param_grid,
                          n_jobs=n_jobs, cv=cv,
                          scoring='recall_weighted')
    clf = clf_cv.fit(X, y)
    best_params = clf.best_params_
    best_score = round(clf.best_score_, 3)
    print('Best Params: {}\n'
          'Best Score: {}'.format(best_params, best_score))
    return best_params, best_score


def precision_recall_thershold(pred_proba, y_test):
    t_recall_nodiab, t_recall_diab = [], []
    t_precision_nodiab, t_precision_diab = [], []

    for thresh in np.arange(0, 1, 0.01):
        precision, recall, fscore, support = \
                metrics.precision_recall_fscore_support(
                        y_test,
                        np.where(pred_proba[:,0] > thresh, 0, 1))
        recall_nodiab, recall_diab = recall
        precision_nodiab, precision_diab = precision

        t_recall_nodiab.append(recall_nodiab)
        t_recall_diab.append(recall_diab)

        t_precision_nodiab.append(precision_nodiab)
        t_precision_diab.append(precision_diab)

    return t_precision_nodiab, t_precision_diab, \
            t_recall_nodiab, t_recall_diab


def bootstrap_model(model, X, y, X_test, y_test, n_bootstrap, thresh):
    total_recall = []
    total_precision = []
    total_fscore = []
    total_fpr_tpr = []
    size = X.shape[0]

    for _ in range(n_bootstrap):
        boot_ind = np.random.randint(size, size=size)
        X_boot = X.loc[boot_ind]
        y_boot = y.loc[boot_ind]

        clf = model.fit(X_boot, y_boot)
        y_pred = clf.predict_proba(X_test)[:,0]
        precision, recall, fscore, _ = metrics.precision_recall_fscore_support(
            y_test, np.where(y_pred > thresh, 0, 1))

        fpr, tpr, thresholds = metrics.roc_curve(y_test, 1 - y_pred)
        fpr_tpr = (fpr, tpr)
        total_fpr_tpr.append(fpr_tpr)
        total_recall.append(recall[1])
        total_precision.append(precision[1])
        total_fscore.append(fscore[1])

    results = dict(recall=total_recall,
                   precision=total_precision,
                   fscore=total_fscore,
                   fpr_tpr=total_fpr_tpr)

    return results


def roc_interp(fpr_tpr):
    linsp = np.linspace(0, 1, 100)
    n_boot = len(fpr_tpr)
    ys = []
    for n in fpr_tpr:
        x, y = n
        interp = np.interp(linsp, x, y)
        ys.append(interp)
    return ys


def plot_recall_vs_decision_boundary(
        t_recall_diab,
        t_recall_nodiab,
        filename='./img/Recall_score.png'):

    plt.figure(figsize=(10,7))
    plt.plot(np.arange(0, 1, 0.01), t_recall_diab,   label='Diabetics')
    plt.plot(np.arange(0, 1, 0.01), t_recall_nodiab, label='Non-Diabetics')
    plt.plot([.5, .5], [0, 1], 'k--')
    plt.plot([.77, .77], [0, 1], 'k--')
    plt.ylim([0.0, 1.01])
    plt.xlim([0.0, 1.0])
    plt.legend(loc='upper left', fontsize=14)
    plt.title('Recall vs. Decision Boundary\n'
              'using GradientBoostingClassifier',
              fontsize=14)
    plt.xlabel('Decision Boundary (T)', fontsize=14)
    plt.ylabel('Recall Rate', fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.savefig(filename)
    plt.show()


def plot_multi_recall_vs_decision_boundary(
        probas,
        y_test,
        filename='./img/Recall_score_all.png'):

    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5))
    ax1.plot([.5, .5], [0, 1], 'k--')
    ax2.plot([.5, .5], [0, 1], 'k--')
    ax1.set_ylim([0.0, 1.01])
    ax1.set_xlim([0.0, 1.0])
    ax2.set_ylim([0.0, 1.01])
    ax2.set_xlim([0.0, 1.0])
    ax1.set_xlabel('Decision Boundary (T)', fontsize=14)
    ax1.set_ylabel('Recall Rate', fontsize=14)
    ax1.tick_params(axis='both', which='major', labelsize=14)
    ax2.set_xlabel('Decision Boundary (T)', fontsize=14)
    ax2.set_ylabel('Recall Rate', fontsize=14)
    ax2.tick_params(axis='both', which='major', labelsize=14)
    for p in probas:
        t_prec_nodiab, t_prec_diab, t_recall_nodiab, t_recall_diab = \
                precision_recall_thershold(probas[p], y_test)
        ax1.plot(np.arange(0, 1, 0.01), t_recall_diab,   label=p)
        ax1.set_title('Diabetic Class\n'
                      'Recall vs. Decision Boundary',
                      fontsize=14)
        ax2.plot(np.arange(0, 1, 0.01), t_recall_nodiab, label=p)
        ax2.set_title('Non-Diabetic Class\n'
                      'Recall vs. Decision Boundary',
                      fontsize=14)
    ax1.legend(loc='upper left')
    plt.savefig(filename)
    plt.show()


def plot_roc_curves(df_preds, y_test, filename='./img/ROC_curve.png'):
    plt.figure(figsize=(8,8))
    for model in df_preds.columns:
        fpr, tpr, thresholds = metrics.roc_curve(y_test,
                                                 df_preds.loc[:,model])
        print('{}\n  AUC: {}'.format(model, round(metrics.auc(fpr, tpr), 3)))
        plt.plot(fpr, tpr, label=model)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.01])
    plt.legend(loc='lower right', fontsize=14)
    plt.xlabel('False Positive Rate', fontsize=14)
    plt.ylabel('True Positive Rate', fontsize=14)
    plt.title('ROC Curve', fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.savefig(filename)
    plt.show()


def plot_bootstrap_roc(m, ci, filename='./img/Bootstrap_ROC_confint.png'):
    x = np.linspace(0,1,100)
    plt.figure(figsize=(8,8))
    plt.plot(x, m, c='blue', label='ROC Mean')
    plt.plot(x, ci[0], c='grey', label='95% CI')
    plt.plot(x, ci[1], c='grey')
    plt.fill_between(x, ci[0], ci[1], color='grey', alpha='0.25')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.01])
    plt.legend(loc='lower right', fontsize=14)
    plt.xlabel('False Positive Rate', fontsize=14)
    plt.ylabel('True Positive Rate', fontsize=14)
    plt.title('Bootstrap ROC Curve', fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.savefig(filename)
    plt.show()
