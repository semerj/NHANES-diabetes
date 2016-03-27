from sklearn.grid_search import GridSearchCV

def GridSearchCVWrapper(model, param_grid, X, y):
    clf_cv = GridSearchCV(
        model,
        param_grid=param_grid,
        n_jobs=-1,
        cv=10,
        scoring='recall_weighted'
    )
    clf = clf_cv.fit(X, y)
    best_params = clf.best_params_
    best_score = round(clf.best_score_, 3)
    print('Best Params: {}\nBest Score: {}'.format(best_params, best_score))
    return best_params, best_score
