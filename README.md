# NHANES Diabetes & Pre-Diabetes Prediction

> ### [Variable search](http://wwwn.cdc.gov/Nchs/Nhanes/Search/default.aspx)
> ### [Demographic data](http://wwwn.cdc.gov/Nchs/Nhanes/Search/DataPage.aspx?Component=Demographics) - [variable list](http://wwwn.cdc.gov/nchs/nhanes/search/variablelist.aspx?Component=Demographics)
> ### [Dietary](http://wwwn.cdc.gov/Nchs/Nhanes/Search/DataPage.aspx?Component=Dietary) - [variable list](http://wwwn.cdc.gov/nchs/nhanes/search/variablelist.aspx?Component=Dietary)
> ### [Examination](http://wwwn.cdc.gov/Nchs/Nhanes/Search/DataPage.aspx?Component=Examination) - [variable list](http://wwwn.cdc.gov/nchs/nhanes/search/variablelist.aspx?Component=Examination)
> ### [Laboratory](http://wwwn.cdc.gov/Nchs/Nhanes/Search/DataPage.aspx?Component=Laboratory) - [variable list](http://wwwn.cdc.gov/nchs/nhanes/search/variablelist.aspx?Component=Laboratory)
> ### [Questionnaire](http://wwwn.cdc.gov/Nchs/Nhanes/Search/DataPage.aspx?Component=Questionnaire) - [variable list](http://wwwn.cdc.gov/nchs/nhanes/search/variablelist.aspx?Component=Questionnaire)

# Methods from [article](./articles/1472-6947-10-16.pdf)

### Data source
> In this study, we used a 1999-2004 data set from the National Health and Nutrition Examination Survey (NHANES) to generate the SVM algorithm. NHANES is an ongoing, cross-sectional, probability sample survey of the U.S. population. It collects demographic, health history, and behavioral information from participants in home interviews. Participants are also invited for detailed physical, physiological, and laboratory examinations that are performed by trained personnel in specially equipped mobile centers [15].

> We limited our study to non-pregnant participants aged 20 or older. Participants were considered to have diagnosed diabetes if they answered “yes” to the question “Have you ever been told by a doctor or health professionals that you have diabetes?” Participants who answered “no” to this question but who had a measured fasting plasma glucose ≥ 126 mg/dl were considered to have undiagnosed diabetes; those with a fasting plasma glucose 100-125 mg/dl were considered to have pre-diabetes. Participants with fasting glucose <100 mg/dl were considered to not have diabetes

> We devised two different classification schemes (Table 1). In Classification Scheme I, the group of persons with diabetes (diagnosed or undiagnosed) was distinguished from those without diabetes, including persons with pre-diabetes. In Classification Scheme II, the group of persons with either undiagnosed diabetes or pre-diabetes was distinguished from those without diabetes. The models were developed using a sample of 80% of the individuals in each group and validated in the remaining 20%.

### Variable selection
> We selected 14 simple variables commonly associated with the risk for diabetes: family history, age, gender, race and ethnicity, weight, height, waist circumference, BMI, hypertension, physical activity, smoking, alcohol use, education, and household income. Variable selection was performed according to an automatic approach developed by Chen et al. [16]. The significance of the automatically selected set of variables was further manually evaluated by fine tuning parameters. The variables included in the final selection were those with the best discriminative performance.

### Table 1
<img src="./img/table1.png">

# Features

```
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
```