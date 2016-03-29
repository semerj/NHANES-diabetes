#!/usr/bin/env python

import os
import urllib
import logging
import pandas as pd
from sklearn.cross_validation import train_test_split


logging.basicConfig(level=logging.INFO)

def download_data(data_dir):
    file_list = [
        ('1999-2000', 'DEMO'),    ('2001-2002', 'DEMO_B'),  ('2003-2004', 'DEMO_C'),
        ('1999-2000', 'DIQ'),     ('2001-2002', 'DIQ_B'),   ('2003-2004', 'DIQ_C'),
        ('1999-2000', 'LAB10AM'), ('2001-2002', 'L10AM_B'), ('2003-2004', 'L10AM_C'),
        ('1999-2000', 'ALQ'),     ('2001-2002', 'ALQ_B'),   ('2003-2004', 'ALQ_C'),
        ('1999-2000', 'SMQ'),     ('2001-2002', 'SMQ_B'),   ('2003-2004', 'SMQ_C'),
        ('1999-2000', 'BMX'),     ('2001-2002', 'BMX_B') ,  ('2003-2004', 'BMX_C'),
        ('1999-2000', 'BPQ'),     ('2001-2002', 'BPQ_B'),   ('2003-2004', 'BPQ_C'),
        ('1999-2000', 'MCQ'),     ('2001-2002', 'MCQ_B'),   ('2003-2004', 'MCQ_C'),
        ('1999-2000', 'PAQ'),     ('2001-2002', 'PAQ_B'),   ('2003-2004', 'PAQ_C'),
        ('1999-2000', 'LAB13'),   ('2001-2002', 'L13_B'),   ('2003-2004', 'L13_C'),
    ]

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    for (year, data_file) in file_list:
        sub_dir = os.path.join(data_dir, year)
        if not os.path.exists(sub_dir):
            os.makedirs(sub_dir)
        url = 'http://wwwn.cdc.gov/Nchs/Nhanes/{0}/{1}.XPT'.format(year, data_file)
        file_name = os.path.join(sub_dir, data_file + '.XPT')
        if not os.path.exists(file_name):
            logging.info('Downloading: {}'.format(url))
            urllib.request.urlretrieve(url, file_name)
        else:
            logging.info('File exists: {}'.format(file_name))


def merge_data(data_dir):
    '''Import data'''
    logging.info('Loading XPT data...')
    DEMO   = pd.read_sas(os.path.join(data_dir, '1999-2000', 'DEMO.XPT'))
    DEMO_B = pd.read_sas(os.path.join(data_dir, '2001-2002', 'DEMO_B.XPT'))
    DEMO_C = pd.read_sas(os.path.join(data_dir, '2003-2004', 'DEMO_C.XPT'))
    DEMO_cols = ['SEQN', 'RIDAGEYR', 'RIAGENDR', 'RIDRETH1', 'DMDEDUC2', 'INDHHINC']

    DIQ   = pd.read_sas(os.path.join(data_dir, '1999-2000', 'DIQ.XPT'))
    DIQ_B = pd.read_sas(os.path.join(data_dir, '2001-2002', 'DIQ_B.XPT'))
    DIQ_C = pd.read_sas(os.path.join(data_dir, '2003-2004', 'DIQ_C.XPT'))
    DIQ_cols = ['SEQN', 'DIQ010']

    LAB10AM   = pd.read_sas(os.path.join(data_dir, '1999-2000', 'LAB10AM.XPT'))
    LAB10AM_B = pd.read_sas(os.path.join(data_dir, '2001-2002', 'L10AM_B.XPT'))
    LAB10AM_C = pd.read_sas(os.path.join(data_dir, '2003-2004', 'L10AM_C.XPT'))
    LAB10AM_cols = ['SEQN', 'LBXGLU']

    ALQ   = pd.read_sas(os.path.join(data_dir, '1999-2000', 'ALQ.XPT'))
    ALQ_B = pd.read_sas(os.path.join(data_dir, '2001-2002', 'ALQ_B.XPT'))
    ALQ_C = pd.read_sas(os.path.join(data_dir, '2003-2004', 'ALQ_C.XPT'))
    ALQ_cols = ['SEQN', 'ALQ120Q']

    SMQ   = pd.read_sas(os.path.join(data_dir, '1999-2000', 'SMQ.XPT'))
    SMQ_B = pd.read_sas(os.path.join(data_dir, '2001-2002', 'SMQ_B.XPT'))
    SMQ_C = pd.read_sas(os.path.join(data_dir, '2003-2004', 'SMQ_C.XPT'))
    SMQ_cols = ['SEQN', 'SMD030']

    BMX   = pd.read_sas(os.path.join(data_dir, '1999-2000', 'BMX.XPT'))
    BMX_B = pd.read_sas(os.path.join(data_dir, '2001-2002', 'BMX_B.XPT'))
    BMX_C = pd.read_sas(os.path.join(data_dir, '2003-2004', 'BMX_C.XPT'))
    BMX_cols = ['SEQN', 'BMXHT', 'BMXWAIST', 'BMXBMI', 'BMXWT', 'BMXLEG']

    BPQ   = pd.read_sas(os.path.join(data_dir, '1999-2000', 'BPQ.XPT'))
    BPQ_B = pd.read_sas(os.path.join(data_dir, '2001-2002', 'BPQ_B.XPT'))
    BPQ_C = pd.read_sas(os.path.join(data_dir, '2003-2004', 'BPQ_C.XPT'))
    BPQ_cols = ['SEQN', 'BPQ020']

    MCQ   = pd.read_sas(os.path.join(data_dir, '1999-2000', 'MCQ.XPT'))
    MCQ_B = pd.read_sas(os.path.join(data_dir, '2001-2002', 'MCQ_B.XPT'))
    MCQ_C = pd.read_sas(os.path.join(data_dir, '2003-2004', 'MCQ_C.XPT'))
    MCQ_cols = ['SEQN', 'MCQ250A']

    PAQ   = pd.read_sas(os.path.join(data_dir, '1999-2000', 'PAQ.XPT'))
    PAQ_B = pd.read_sas(os.path.join(data_dir, '2001-2002', 'PAQ_B.XPT'))
    PAQ_C = pd.read_sas(os.path.join(data_dir, '2003-2004', 'PAQ_C.XPT'))
    PAQ_cols = ['SEQN', 'PAQ180']

    LAB13   = pd.read_sas(os.path.join(data_dir, '1999-2000', 'LAB13.XPT'))
    LAB13_B = pd.read_sas(os.path.join(data_dir, '2001-2002', 'L13_B.XPT'))
    LAB13_C = pd.read_sas(os.path.join(data_dir, '2003-2004', 'L13_C.XPT'))
    LAB13_cols = ['SEQN', 'LBXTC']

    '''Merge Datasets

    Age >= 20 and non-pregnant population
    '''
    logging.info('Merging data...')
    age = 20
    df_00 = DEMO.loc[((DEMO.RIAGENDR == 2) & (DEMO.RIDAGEYR >= age) & (DEMO.RIDEXPRG == 2)) |
                     ((DEMO.RIAGENDR == 1) & (DEMO.RIDAGEYR >= age)),
                     DEMO_cols] \
            .merge(ALQ[ALQ_cols], on='SEQN') \
            .merge(BMX[BMX_cols], on='SEQN') \
            .merge(BPQ[BPQ_cols], on='SEQN') \
            .merge(PAQ[PAQ_cols], on='SEQN') \
            .merge(MCQ[MCQ_cols], on='SEQN') \
            .merge(SMQ[SMQ_cols], on='SEQN') \
            .merge(LAB13[LAB13_cols], on='SEQN')

    df_02 = DEMO_B.loc[((DEMO_B.RIAGENDR == 2) & (DEMO_B.RIDAGEYR >= age) & (DEMO_B.RIDEXPRG == 2)) |
                       ((DEMO_B.RIAGENDR == 1) & (DEMO_B.RIDAGEYR >= age)),
                       DEMO_cols] \
            .merge(ALQ_B[ALQ_cols], on='SEQN') \
            .merge(BMX_B[BMX_cols], on='SEQN') \
            .merge(BPQ_B[BPQ_cols], on='SEQN') \
            .merge(PAQ_B[PAQ_cols], on='SEQN') \
            .merge(MCQ_B[MCQ_cols], on='SEQN') \
            .merge(SMQ_B[SMQ_cols], on='SEQN') \
            .merge(LAB13_B[LAB13_cols], on='SEQN')

    df_04 = DEMO_C.loc[((DEMO_C.RIAGENDR == 2) & (DEMO_C.RIDAGEYR >= age) & (DEMO_C.RIDEXPRG == 2)) |
                       ((DEMO_C.RIAGENDR == 1) & (DEMO_C.RIDAGEYR >= age)),
                       DEMO_cols] \
            .merge(ALQ_C[ALQ_cols], on='SEQN') \
            .merge(BMX_C[BMX_cols], on='SEQN') \
            .merge(BPQ_C[BPQ_cols], on='SEQN') \
            .merge(PAQ_C[PAQ_cols], on='SEQN') \
            .merge(MCQ_C[MCQ_cols], on='SEQN') \
            .merge(SMQ_C[SMQ_cols], on='SEQN') \
            .merge(LAB13_C[LAB13_cols], on='SEQN')

    df_pop = pd.concat([df_00, df_02, df_04])


    '''Diagnosed Diabetes (total should be 1,266)

    The next questions are about specific medical conditions.
    {Other than during pregnancy, {have you/has SP}/{Have you/Has SP}}
    ever been told by a doctor or health professional that
    {you have/{he/she/SP} has} diabetes or sugar diabetes?
    '''
    df_00_diag = df_00.merge(DIQ.loc[DIQ.DIQ010 == 1, DIQ_cols], on="SEQN")
    df_02_diag = df_02.merge(DIQ_B.loc[DIQ_B.DIQ010 == 1, DIQ_cols], on="SEQN")
    df_04_diag = df_04.merge(DIQ_C.loc[DIQ_C.DIQ010 == 1, DIQ_cols], on="SEQN")
    diag_total = pd.concat([df_00_diag, df_02_diag, df_04_diag])
    diag_total.loc[:,'status'] = 1
    logging.info('Diagnosed subject count: {}'.format(diag_total.shape[0]))

    '''Undiagnosed Diabetes (total should be 195)'''
    df_00_undiag = df_00.merge(DIQ.loc[DIQ.DIQ010 == 2, DIQ_cols] \
                               .merge(LAB10AM.loc[LAB10AM.LBXGLU >= 126, LAB10AM_cols], on='SEQN'),
                           on='SEQN')
    df_02_undiag = df_02.merge(DIQ_B.loc[DIQ_B.DIQ010 == 2, DIQ_cols] \
                               .merge(LAB10AM_B.loc[LAB10AM_B.LBXGLU >= 126, LAB10AM_cols], on='SEQN'),
                            on='SEQN')
    df_04_undiag = df_04.merge(DIQ_C.loc[DIQ_C.DIQ010 == 2, DIQ_cols] \
                               .merge(LAB10AM_C.loc[LAB10AM_C.LBXGLU >= 126, LAB10AM_cols], on='SEQN'),
                            on='SEQN')
    undiag_total = pd.concat([df_00_undiag, df_02_undiag, df_04_undiag])
    undiag_total.loc[:,'status'] = 1
    logging.info('Undiagnosed subject count: {}'.format(undiag_total.shape[0]))

    '''Pre-diabetes (total should be 1,576)'''
    df_00_prediab = df_00.merge(LAB10AM.loc[(LAB10AM.LBXGLU >= 100) & \
                                            (LAB10AM.LBXGLU <= 125),
                                            LAB10AM_cols], on='SEQN')
    df_02_prediab = df_02.merge(LAB10AM_B.loc[(LAB10AM_B.LBXGLU >= 100) & \
                                            (LAB10AM_B.LBXGLU <= 125),
                                            LAB10AM_cols], on='SEQN')
    df_04_prediab = df_04.merge(LAB10AM_C.loc[(LAB10AM_C.LBXGLU >= 100) & \
                                            (LAB10AM_C.LBXGLU <= 125),
                                            LAB10AM_cols], on='SEQN')
    prediab_total = pd.concat([df_00_prediab, df_02_prediab, df_04_prediab])
    prediab_total.loc[:,'status'] = 0
    logging.info('Pre-diabetic subject count: {}'.format(prediab_total.shape[0]))

    '''No Diabetes (total should be 3,277)'''
    df_00_nodiab = df_00.merge(LAB10AM.loc[LAB10AM.LBXGLU < 100, LAB10AM_cols], on='SEQN')
    df_02_nodiab = df_02.merge(LAB10AM_B.loc[LAB10AM_B.LBXGLU < 100, LAB10AM_cols], on='SEQN')
    df_04_nodiab = df_04.merge(LAB10AM_C.loc[LAB10AM_C.LBXGLU < 100, LAB10AM_cols], on='SEQN')
    nodiab_total = pd.concat([df_00_nodiab, df_02_nodiab, df_04_nodiab])
    nodiab_total.loc[:,'status'] = 0
    logging.info('Diabetes-free subject count: {}'.format(nodiab_total.shape[0]))

    '''Join and split data'''
    df = pd.concat([diag_total, undiag_total, prediab_total, nodiab_total], ignore_index=True)
    df = df.drop(['SEQN', 'LBXGLU','DIQ010'], axis=1)
    df_train, df_test = train_test_split(df, test_size=0.2, random_state=289)

    '''Save data'''
    fname_train = os.path.join(data_dir, 'diabetes_data_train.csv')
    fname_test = os.path.join(data_dir, 'diabetes_data_test.csv')
    df_train.to_csv(fname_train, index=False, float_format='%.1f')
    logging.info('Training set saved: {}'.format(fname_train))
    df_test.to_csv(fname_test, index=False, float_format='%.1f')
    logging.info('Test set saved: {}'.format(fname_test))


if __name__ == '__main__':
    data_dir = 'data'
    download_data(data_dir)
    merge_data(data_dir)
