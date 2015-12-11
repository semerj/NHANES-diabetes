import pandas as pd


def fetch_NHANES(year, database, data_dir='./data'):
    '''
    Retrieve NHANES data as a Pandas DataFrame.

    Years of available data:
        1999-2000, 2001-2002, 2003-2004, 2005-2006,
        2007-2008, 2009-2010, 2011-2012, 2013-2014
    '''
    suffix = {
        '1999-2000': '',   '2001-2002': '_B',
        '2003-2004': '_C', '2005-2006': '_D',
        '2007-2008': '_E', '2009-2010': '_F',
        '2011-2012': '_G', '2013-2014': '_H'
    }

    url = 'http://wwwn.cdc.gov/Nchs/Nhanes/{0}/{1}{2}.XPT' \
        .format(year, database, suffix[year])

    # if save_csv and download:
    #     df = pd.read_sas(url)
    #     fname = '{0}/{1}/{2}{3}.csv' \
    #         .format(data_dir, year, data[data_type], suffix[year])
    #     df.to_csv(fname, index=False)
    #     return df

    return pd.read_sas(url)

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
