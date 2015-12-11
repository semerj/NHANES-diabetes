import pandas as pd
from sklearn.cross_validation import train_test_split


def merge_data(filename):
    '''
    Import data
    '''
    DEMO   = pd.read_csv('./data/1999-2000/DEMO.csv')
    DEMO_B = pd.read_csv('./data/2001-2002/DEMO_B.csv')
    DEMO_C = pd.read_csv('./data/2003-2004/DEMO_C.csv')
    DEMO_cols = ['SEQN', 'RIDAGEYR', 'RIAGENDR', 'RIDRETH1', 'DMDEDUC2', 'INDHHINC']

    DIQ   = pd.read_csv('./data/1999-2000/DIQ.csv')
    DIQ_B = pd.read_csv('./data/2001-2002/DIQ_B.csv')
    DIQ_C = pd.read_csv('./data/2003-2004/DIQ_C.csv')
    DIQ_cols = ['SEQN', 'DIQ010']

    LAB10AM   = pd.read_csv('./data/1999-2000/LAB10AM.csv')
    LAB10AM_B = pd.read_csv('./data/2001-2002/LAB10AM_B.csv')
    LAB10AM_C = pd.read_csv('./data/2003-2004/LAB10AM_C.csv')
    LAB10AM_cols = ['SEQN', 'LBXGLU']

    ALQ   = pd.read_csv('./data/1999-2000/ALQ.csv')
    ALQ_B = pd.read_csv('./data/2001-2002/ALQ_B.csv')
    ALQ_C = pd.read_csv('./data/2003-2004/ALQ_C.csv')
    ALQ_cols = ['SEQN', 'ALQ120Q']

    SMQ   = pd.read_csv('./data/1999-2000/SMQ.csv')
    SMQ_B = pd.read_csv('./data/2001-2002/SMQ_B.csv')
    SMQ_C = pd.read_csv('./data/2003-2004/SMQ_C.csv')
    SMQ_cols = ['SEQN', 'SMD030']

    BMX   = pd.read_csv('./data/1999-2000/BMX.csv')
    BMX_B = pd.read_csv('./data/2001-2002/BMX_B.csv')
    BMX_C = pd.read_csv('./data/2003-2004/BMX_C.csv')
    BMX_cols = ['SEQN', 'BMXHT', 'BMXWAIST', 'BMXBMI', 'BMXWT', 'BMXLEG']

    BPQ   = pd.read_csv('./data/1999-2000/BPQ.csv')
    BPQ_B = pd.read_csv('./data/2001-2002/BPQ_B.csv')
    BPQ_C = pd.read_csv('./data/2003-2004/BPQ_C.csv')
    BPQ_cols = ['SEQN', 'BPQ020']

    MCQ   = pd.read_csv('./data/1999-2000/MCQ.csv')
    MCQ_B = pd.read_csv('./data/2001-2002/MCQ_B.csv')
    MCQ_C = pd.read_csv('./data/2003-2004/MCQ_C.csv')
    MCQ_cols = ['SEQN', 'MCQ250A']

    PAQ   = pd.read_csv('./data/1999-2000/PAQ.csv')
    PAQ_B = pd.read_csv('./data/2001-2002/PAQ_B.csv')
    PAQ_C = pd.read_csv('./data/2003-2004/PAQ_C.csv')
    PAQ_cols = ['SEQN', 'PAQ180']

    LAB13   = pd.read_csv('./data/1999-2000/LAB13.csv')
    LAB13_B = pd.read_csv('./data/2001-2002/LAB13_B.csv')
    LAB13_C = pd.read_csv('./data/2003-2004/LAB13_C.csv')
    LAB13_cols = ['SEQN', 'LBXTC']

    '''
    Merge Datasets

    Age >= 20 and non-pregnant population
    '''
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


    '''
    Diagnosed Diabetes (total should be 1,266)

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

    '''
    Undiagnosed Diabetes (total should be 195)
    '''
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

    '''
    Pre-diabetes (total should be 1,576)
    '''
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


    '''
    No Diabetes (total should be 3,277)
    '''
    df_00_nodiab = df_00.merge(LAB10AM.loc[LAB10AM.LBXGLU < 100, LAB10AM_cols], on='SEQN')
    df_02_nodiab = df_02.merge(LAB10AM_B.loc[LAB10AM_B.LBXGLU < 100, LAB10AM_cols], on='SEQN')
    df_04_nodiab = df_04.merge(LAB10AM_C.loc[LAB10AM_C.LBXGLU < 100, LAB10AM_cols], on='SEQN')
    nodiab_total = pd.concat([df_00_nodiab, df_02_nodiab, df_04_nodiab])
    nodiab_total.loc[:,'status'] = 0


    '''
    Join everything
    '''
    df = pd.concat([diag_total, undiag_total, prediab_total, nodiab_total], ignore_index=True)
    df = df.drop(['SEQN', 'LBXGLU','DIQ010'], axis=1)
    df_train, df_test = train_test_split(df, test_size=0.2, random_state=289)

    df_train.to_csv(filename + '_train.csv', index=False)
    df_test.to_csv(filename + '_test.csv',index=False)

