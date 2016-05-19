# An Ensemble Model for Predicting the Onset of Diabetes using NHANES Data

#### By John Semerdjian & Spencer Frank

## Code

Our models are contained in the `NHANES.ipynb` notebook. In order to run the notebook, create a virtual environment and install the required modules.

```bash
# create a virtual environment, "nhanes"
$ mkvirtualenv --python=/usr/local/bin/python3 nhanes
$ workon nhanes

# install required modules
$ pip install -r requirements.txt

# download/merge data
$ python ./bootstrap.py

# start ipython notebook
$ ipython notebook
```

## Video & Report

You can find our report [here](./report/report.pdf).

## Abstract

Prediction of disease onset from patient survey and lifestyle data is quickly becoming an important tool for diagnosing a disease before it progresses. In this study data from the [National Health and Nutrition Examination Survey (NHANES)](http://www.cdc.gov/nchs/nhanes.htm) questionnaire is used to predict the onset of diabetes. An ensemble model using the output of several classification algorithms was developed to predict the onset on diabetes based on 16 features. The ensemble model had an AUC of 0.834 indicating high performance.

## Features and Descriptions

* `ALQ120Q`: [How often drink alcohol over past 12 mos](http://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/ALQ.htm#ALQ120Q)
* `BMXBMI`: [Body Mass Index (kg/m**2)](http://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/BMX.htm#BMXBMI)
* `BMXHT`: [Standing Height (cm)](http://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/BMX.htm#BMXHT)
* `BMXLEG`: [Upper Leg Length (cm)](http://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/BMX.htm#BMXLEG)
* `BMXWAIST`: [Waist Circumference (cm)](http://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/BMX.htm#BMXWAIST)
* `BMXWT`: [Weight (kg)](http://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/BMX.htm#BMXWT)
* `BPQ020`: [Ever told you had high blood pressure](http://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/BPQ.htm#BPQ020)
* `DMDEDUC2`: [Education Level - Adults 20+](http://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DEMO.htm#DMDEDUC2)
* `INDHHINC`: [Annual Household Income](http://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DEMO.htm#INDHHINC)
* `LBXTC`: [Total cholesterol (mg/dL)](http://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB13.htm#LBXTC)
* `MCQ250A`: [Blood relatives have diabetes](http://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/MCQ.htm#MCQ250A)
* `PAQ180`: [Avg level of physical activity each day](http://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/PAQ.htm#PAQ180)
* `RIAGENDR`: [Gender](http://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DEMO.htm#RIAGENDR)
* `RIDAGEYR`: [Age at Screening Adjudicated - Recode](http://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DEMO.htm#RIDAGEYR)
* `RIDRETH1`: [Race/Ethnicity - Recode](http://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DEMO.htm#RIDRETH1)
* `SMD030`: [Age started smoking cigarets regularly](http://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SMQ.htm#SMD030)

## Additional Variables

* [Variable search](http://wwwn.cdc.gov/Nchs/Nhanes/Search/default.aspx)
* [Demographic data](http://wwwn.cdc.gov/Nchs/Nhanes/Search/DataPage.aspx?Component=Demographics) - [variable list](http://wwwn.cdc.gov/nchs/nhanes/search/variablelist.aspx?Component=Demographics)
* [Dietary](http://wwwn.cdc.gov/Nchs/Nhanes/Search/DataPage.aspx?Component=Dietary) - [variable list](http://wwwn.cdc.gov/nchs/nhanes/search/variablelist.aspx?Component=Dietary)
* [Examination](http://wwwn.cdc.gov/Nchs/Nhanes/Search/DataPage.aspx?Component=Examination) - [variable list](http://wwwn.cdc.gov/nchs/nhanes/search/variablelist.aspx?Component=Examination)
* [Laboratory](http://wwwn.cdc.gov/Nchs/Nhanes/Search/DataPage.aspx?Component=Laboratory) - [variable list](http://wwwn.cdc.gov/nchs/nhanes/search/variablelist.aspx?Component=Laboratory)
* [Questionnaire](http://wwwn.cdc.gov/Nchs/Nhanes/Search/DataPage.aspx?Component=Questionnaire) - [variable list](http://wwwn.cdc.gov/nchs/nhanes/search/variablelist.aspx?Component=Questionnaire)
