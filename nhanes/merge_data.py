import pandas as pd


def merge_data(filename):
    '''
    Features To Merge:

        DEMO
            age:
                RIDAGEYR
            gender:
                RIAGENDR
            race:
                RIDRETH1   # Race/Ethnicity - Recode
            weight:
                WTINT2YR   # Full Sample 2 Year Interview Weight
                WTINT4YR   # Full Sample 4 Year Interview Weight
                WTMEC2YR   # Full Sample 2 Year MEC Exam Weight
                WTMEC4YR   # Full Sample 4 Year MEC Exam Weight
            education:
                DMDEDUC2   # Education Level - Adults 20+
            house income:
                INDHHINC   # Annual Household Income

        ALQ
            alcohol use:
                ALQ110     # Had at least 12 alcohol drinks/lifetime?
                // ALD100  # Had at least 12 alcohol drinks/1 yr?
                // ALD240  # How often drink beer (per month)

        SMQ
            smoking:
                SMD130     # Age started pipe smoking regularly
                SMD410     # Does anyone smoke in the home
                SMQ050Q    # How long since quit smoking cigarettes

        BMX
            height:
                BMXHT      # Standing Height (cm)
            waist cir:
                BMXWAIST   # Waist Circumference (cm)
            bmi:
                BMXBMI     # Body Mass Index (kg/m**2)

        BPQ
            hypertension:
                BPQ020     # Ever told you had high blood pressure

        PAQ
            phys act:
                PAQ180     # Avg level of physical activity each day

        MCQ
            family hx:
                MCQ250A    # Blood relatives have diabetes
    '''

    '''
    Import data
    '''
    DEMO = pd.read_csv('./data/1999-2000/DEMO.csv')
    DEMO_B = pd.read_csv('./data/2001-2002/DEMO_B.csv')
    DEMO_C = pd.read_csv('./data/2003-2004/DEMO_C.csv')

    DIQ = pd.read_csv('./data/1999-2000/DIQ.csv')
    DIQ_B = pd.read_csv('./data/2001-2002/DIQ_B.csv')
    DIQ_C = pd.read_csv('./data/2003-2004/DIQ_C.csv')

    LAB10AM = pd.read_csv('./data/1999-2000/LAB10AM.csv')
    L10AM_B = pd.read_csv('./data/2001-2002/L10AM_B.csv')
    L10AM_C = pd.read_csv('./data/2003-2004/L10AM_C.csv')

    ALQ = pd.read_csv('./data/1999-2000/ALQ.csv')
    ALQ_B = pd.read_csv('./data/2001-2002/ALQ_B.csv')
    ALQ_C = pd.read_csv('./data/2003-2004/ALQ_C.csv')

    SMQ = pd.read_csv('./data/1999-2000/SMQ.csv')
    SMQ_B = pd.read_csv('./data/2001-2002/SMQ_B.csv')
    SMQ_C = pd.read_csv('./data/2003-2004/SMQ_C.csv')

    BMX = pd.read_csv('./data/1999-2000/BMX.csv')
    BMX_B = pd.read_csv('./data/2001-2002/BMX_B.csv')
    BMX_C = pd.read_csv('./data/2003-2004/BMX_C.csv')

    BPQ = pd.read_csv('./data/1999-2000/BPQ.csv')
    BPQ_B = pd.read_csv('./data/2001-2002/BPQ_B.csv')
    BPQ_C = pd.read_csv('./data/2003-2004/BPQ_C.csv')

    MCQ = pd.read_csv('./data/1999-2000/MCQ.csv')
    MCQ_B = pd.read_csv('./data/2001-2002/MCQ_B.csv')
    MCQ_C = pd.read_csv('./data/2003-2004/MCQ_C.csv')

    PAQ = pd.read_csv('./data/1999-2000/PAQ.csv')
    PAQ_B = pd.read_csv('./data/2001-2002/PAQ_B.csv')
    PAQ_C = pd.read_csv('./data/2003-2004/PAQ_C.csv')

    '''
    Merge Datasets

    Age >= 20 and non-pregnant population
    '''
    age = 20

    df_00 = DEMO.loc[((DEMO.RIAGENDR == 2) & (DEMO.RIDAGEYR >= age) & (DEMO.RIDEXPRG == 2)) |
                     ((DEMO.RIAGENDR == 1) & (DEMO.RIDAGEYR >= age)),
                     ['SEQN', 'RIDAGEYR', 'RIAGENDR', 'RIDRETH1', 'WTINT2YR', 'DMDEDUC2', 'INDHHINC']] \
            .merge(ALQ[['SEQN', 'ALQ110']],
                   on='SEQN') \
            .merge(BMX[['SEQN', 'BMXHT', 'BMXWAIST', 'BMXBMI']],
                   on='SEQN') \
            .merge(BPQ[['SEQN', 'BPQ020']],
                   on='SEQN') \
            .merge(PAQ[['SEQN', 'PAQ180']],
                   on='SEQN') \
            .merge(MCQ[['SEQN', 'MCQ250A']],
                   on='SEQN')

    df_02 = DEMO_B.loc[((DEMO_B.RIAGENDR == 2) & (DEMO_B.RIDAGEYR >= age) & (DEMO_B.RIDEXPRG == 2)) |
                       ((DEMO_B.RIAGENDR == 1) & (DEMO_B.RIDAGEYR >= age)),
                       ['SEQN', 'RIDAGEYR', 'RIAGENDR', 'RIDRETH1', 'WTINT2YR', 'DMDEDUC2', 'INDHHINC']] \
            .merge(ALQ_B[['SEQN', 'ALQ110']], on='SEQN') \
            .merge(BMX_B[['SEQN', 'BMXHT', 'BMXWAIST', 'BMXBMI']], on='SEQN') \
            .merge(BPQ_B[['SEQN', 'BPQ020']], on='SEQN') \
            .merge(PAQ_B[['SEQN', 'PAQ180']], on='SEQN') \
            .merge(MCQ_B[['SEQN', 'MCQ250A']], on='SEQN')

    df_04 = DEMO_C.loc[((DEMO_C.RIAGENDR == 2) & (DEMO_C.RIDAGEYR >= age) & (DEMO_C.RIDEXPRG == 2)) |
                       ((DEMO_C.RIAGENDR == 1) & (DEMO_C.RIDAGEYR >= age)),
                       ['SEQN', 'RIDAGEYR', 'RIAGENDR', 'RIDRETH1', 'WTINT2YR', 'DMDEDUC2', 'INDHHINC']] \
            .merge(ALQ_C[['SEQN', 'ALQ110']], on='SEQN') \
            .merge(BMX_C[['SEQN', 'BMXHT', 'BMXWAIST', 'BMXBMI']], on='SEQN') \
            .merge(BPQ_C[['SEQN', 'BPQ020']], on='SEQN') \
            .merge(PAQ_C[['SEQN', 'PAQ180']], on='SEQN') \
            .merge(MCQ_C[['SEQN', 'MCQ250A']], on='SEQN')

    df_pop = pd.concat([df_00, df_02, df_04])


    '''
    Diagnosed Diabetes (total should be 1,266)

    The next questions are about specific medical conditions.
    {Other than during pregnancy, {have you/has SP}/{Have you/Has SP}}
    ever been told by a doctor or health professional that
    {you have/{he/she/SP} has} diabetes or sugar diabetes?
    '''

    df_00_diag = df_00.merge(DIQ.loc[DIQ.DIQ010 == 1, ['SEQN', 'DIQ010']],
                             on="SEQN")
    df_02_diag = df_02.merge(DIQ_B.loc[DIQ_B.DIQ010 == 1, ['SEQN', 'DIQ010']],
                             on="SEQN")
    df_04_diag = df_04.merge(DIQ_C.loc[DIQ_C.DIQ010 == 1, ['SEQN', 'DIQ010']],
                             on="SEQN")
    diag_total = pd.concat([df_00_diag, df_02_diag, df_04_diag])
    diag_total.loc[:,'status'] = 'diag'


    '''
    Undiagnosed Diabetes (total should be 195)
    '''
    df_00_undiag = df_00.merge(DIQ.loc[DIQ.DIQ010 == 2, ['SEQN', 'DIQ010']] \
                               .merge(LAB10AM.loc[LAB10AM.LBXGLU >= 126, ['SEQN', 'LBXGLU']],
                                   on='SEQN'),
                           on='SEQN')
    df_02_undiag = df_02.merge(DIQ_B.loc[DIQ_B.DIQ010 == 2, ['SEQN', 'DIQ010']] \
                               .merge(L10AM_B.loc[L10AM_B.LBXGLU >= 126, ['SEQN', 'LBXGLU']],
                                   on='SEQN'),
                            on='SEQN')
    df_04_undiag = df_04.merge(DIQ_C.loc[DIQ_C.DIQ010 == 2, ['SEQN', 'DIQ010']] \
                               .merge(L10AM_C.loc[L10AM_C.LBXGLU >= 126, ['SEQN', 'LBXGLU']],
                                   on='SEQN'),
                            on='SEQN')
    undiag_total = pd.concat([df_00_undiag, df_02_undiag, df_04_undiag])
    undiag_total.loc[:,'status'] = 'diag'

    '''
    Pre-diabetes (total should be 1,576)
    '''
    df_00_prediab = df_00.merge(LAB10AM.loc[(LAB10AM.LBXGLU >= 100) & (LAB10AM.LBXGLU <= 125),
                                            ['SEQN', 'LBXGLU']],
                                on='SEQN')
    df_02_prediab = df_02.merge(L10AM_B.loc[(L10AM_B.LBXGLU >= 100) & (L10AM_B.LBXGLU <= 125),
                                            ['SEQN', 'LBXGLU']],
                                on='SEQN')
    df_04_prediab = df_04.merge(L10AM_C.loc[(L10AM_C.LBXGLU >= 100) & (L10AM_C.LBXGLU <= 125),
                                            ['SEQN', 'LBXGLU']],
                                on='SEQN')
    prediab_total = pd.concat([df_00_prediab, df_02_prediab, df_04_prediab])
    prediab_total.loc[:,'status'] = 'nodiab'


    '''
    No Diabetes (total should be 3,277)
    '''
    df_00_nodiab = df_00.merge(LAB10AM.loc[LAB10AM.LBXGLU < 100, ['SEQN', 'LBXGLU']],
                               on='SEQN')
    df_02_nodiab = df_02.merge(L10AM_B.loc[L10AM_B.LBXGLU < 100, ['SEQN', 'LBXGLU']],
                               on='SEQN')
    df_04_nodiab = df_04.merge(L10AM_C.loc[L10AM_C.LBXGLU < 100, ['SEQN', 'LBXGLU']],
                               on='SEQN')
    nodiab_total = pd.concat([df_00_nodiab, df_02_nodiab, df_04_nodiab])
    nodiab_total.loc[:,'status'] = 'nodiab'


    '''
    Join everything
    '''
    df = pd.concat([diag_total, undiag_total, prediab_total, nodiab_total], ignore_index=True)
    df.drop(['SEQN', 'LBXGLU','DIQ010'], axis=1).to_csv(filename, index=False)
