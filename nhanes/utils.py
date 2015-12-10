import pandas as pd
from model_imports import *


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


def parse_json_model(json_models):
    n_models = len(json_models)
    models = []
    for jm in json_models:
        # params = str_to_bool(jm['params'])
        params = jm['params']
        model = eval(jm['model'] + '()')
        models.append((model, params))
    return models


def GridSearchCVWrapper(X, y, models):
    best_model_params = []
    for model, parameters in models:
        clf = GridSearchCV(model,
                           parameters,
                           n_jobs=-1,
                           cv=10)
        clf.fit(X, y)
        best_params = clf.best_params_.items()
        best_model_params.append(best_params)
        best_score = round(clf.best_score_, 3)
        model_name = model.__class__.__name__

        print('Model: {}'.format(model_name))
        print('  Best Score: {}'.format(best_score))
        print('  Best Params')
        for k, v in best_params:
            print('    {}: {}'.format(k, v))
        print()

    return best_model_params
