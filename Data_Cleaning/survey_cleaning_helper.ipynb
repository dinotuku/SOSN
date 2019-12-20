# -*- coding: utf-8 -*-
"""some helper functions for cleaning the stackoverflow user survey data."""
import pandas as pd
import numpy as np
import country_converter as coco


# functions of modifying the hobby field
def map_hobby(col, year): 
    if year == 2016:
        return col.map(lambda x: 'No' if x == 'None' else 'Yes', na_action='ignore').fillna('No')
    elif year == 2017:
        return col.map(lambda x: 'Yes' if 'Yes' in x else 'No')
    elif year == 2018 or year == 2019:
        return col
    else:
        print('No such year:', year) 

        
# map country to iso3 for easier comparison with user data
def map_country(col): 
    return pd.Series(coco.convert(names=col.tolist(), to='ISO3', not_found='NA'))


# map the years of coding experience into 4 categories
def map_yearsCoding(col, year):
    if year == 2016:
        return col.map(lambda x: '0 - 2 years' if x == 'Less than 1 year' or x == '1 - 2 years' else x,\
                       na_action='ignore').fillna('NA')
    elif year == 2017:
        return col.map(lambda x: 'Less than 1 year' if x == 'Less than a year' else '1 - 2 years' if x == '1 to 2 years'\
                                 else '2 - 5 years' if x == '2 to 3 years' or x == '3 to 4 years' or x == '4 to 5 years'\
                                 else '6 - 10 years' if x == '6 to 7 years' or x == '7 to 8 years' or x == '8 to 9 years'\
                                 or x == '9 to 10 years' else '11+ years', na_action='ignore').fillna('NA')
    elif year == 2018:
        yearMap = {'0-2 years': '0 - 2 years', '3-5 years': '2 - 5 years', '6-8 years': '6 - 10 years', \
           '9-11 years': '6 - 10 years', '12-14 years': '11+ years', '15-17 years': '11+ years', \
           '18-20 years': '11+ years', '21-23 years': '11+ years', '24-26 years': '11+ years', \
           '27-29 years': '11+ years', '30 or more years': '11+ years'}
        return col.map(lambda x: yearMap[x], na_action='ignore').fillna('NA')
    elif year == 2019:
        return col.map(lambda x: '11+ years' if x == 'More than 50 years' else '0 - 2 years' if x == 'Less than 1 year' \
                                 or int(x) < 2 else '2 - 5 years' if int(x) >= 2 and int(x) <= 5 else '6 - 10 years' \
                                 if int(x) >= 6 and int(x) <= 10 else '11+ years', na_action='ignore').fillna('NA')
    else:
        print('No such year:', year) 
        
        
# unifying representations of the job satisfaction field
def map_jobSat(df, year):
    if year == 2016:
        jobSatMap = {'I don\'t have a job': -1, 'Other (please specify)': 0, 'I hate my job': 1, \
             'I\'m somewhat dissatisfied with my job': 2.5, 'I\'m neither satisfied nor dissatisfied': 4,\
             'I\'m somewhat satisfied with my job': 5.5, 'I love my job': 7}
        df['temp'] = df['JobSatisfaction'].map(lambda x: jobSatMap[x], na_action='ignore')
        mean2016 = df[df.temp > 0].mean()
        df.loc[df.temp == 0, 'temp'] = mean2016
        return df['temp'].fillna(0)
    elif year == 2017:
        return df['JobSatisfaction'].map(lambda x: 1 + 6 / 10 * x, na_action='ignore').fillna(0)
    elif year == 2018:
        SATISFACTION_MAP_2018 = {'Extremely satisfied': 7, 'Moderately satisfied': 6, 'Slightly satisfied': 5, 
                    'Neither satisfied nor dissatisfied': 4, 'Slightly dissatisfied': 3, 'Moderately dissatisfied': 2,
                    'Extremely dissatisfied': 1}
        return df['JobSatisfaction'].map(lambda x: SATISFACTION_MAP_2018[x], na_action='ignore').fillna(0)
    elif year == 2019:
        SATISFACTION_MAP_2019 = {'Very dissatisfied': 1, 'Slightly dissatisfied': 2.5, 'Neither satisfied nor dissatisfied': 4,
                         'Slightly satisfied': 5.5, 'Very satisfied': 7}
        return df['JobSatisfaction'].map(lambda x: SATISFACTION_MAP_2019[x], na_action='ignore').fillna(0)
    else:
        print('No such year:', year) 
    
    
# map salary na fields to 0
def clean_salary(col):
    return col.fillna(0)


# general split function
def split_or_empty(x, sep=';'):
    return [] if pd.isna(x) else x.split(sep)

# split the languages worked with
def split_languages(col, year):
    if year == 2018 or year == 2019: 
        return col.map(lambda x: split_or_empty(x))
    elif year == 2016 or year == 2017:
        return col.map(lambda x: split_or_empty(x, sep='; '))
    else: 
        print('No such year:', year)
        

# clean the gender field
def map_gender(col, year):
    if year == 2016:
        return col.map(lambda x: 'Prefer not to disclose' if x == 'Other' else x, na_action='ignore')\
                  .fillna('Prefer not to disclose')
    elif year == 2017:
        return col.map(lambda x: 'Prefer not to disclose' if len(x.split(';')) >= 3 or 'Gender non-conforming' in x \
                                 or x == 'Other' or x == 'Male; Female' else (x if len(x.split(';')) == 1 else 'Female'\
                                 if 'Female' in x else 'Male'), na_action='ignore').fillna('Prefer not to disclose')
    elif year == 2018:
        return col.map(lambda x: 'Prefer not to disclose' if len(x.split(';')) >= 3 or 'gender non-conforming' in x or\
                                 x == 'Female;Male' else (x if len(x.split(';')) == 1 else 'Female' if 'Female' in x \
                                 else 'Male') , na_action='ignore').fillna('Prefer not to disclose')
    elif year == 2019:
        return col.map(lambda x: 'Prefer not to disclose' if x == 0 or len(x.split(';')) >= 3 or 'gender non-conforming' in x\
                                 or x == 'Woman;Man' else 'Female' if 'Woman' in x else 'Male', na_action='ignore')\
                  .fillna('Prefer not to disclose')
    else:
        print('No such year:', year) 
        
        
# clean the vist frequency field
def clean_visit(df, year): 
    if year == 2016:
        visitMap = {'I have never been on Stack Overflow. I just love taking surveys.': \
                    'I have never visited Stack Overflow (before today)', 'Multiple times a day': 'Multiple times per day',
                    'Once a day': 'Daily or almost daily', 'Once a week': 'A few times per week', \
                    'Once a month': 'A few times per month or weekly', 'Very rarely': 'Less than once per month or monthly'}
        df['temp'] = df['StackOverflowVisit'].map(lambda x: visitMap[x], na_action='ignore')
        return df['temp'].fillna('NA')
    elif year == 2017:
        reverseMap = {0: 'I have never visited Stack Overflow (before today)', 8: 'Multiple times per day', \
                      7: 'Multiple times per day', 6: 'Multiple times per day', 5: 'Daily or almost daily', \
                      4: 'Daily or almost daily', 3: 'A few times per week', \
                      2: 'A few times per month or weekly', 1: 'Less than once per month or monthly'} 
        visitMap = {"Haven't done at all": 0, 'Once or twice': 1, 'Several times': 2, 'At least once each day': 4, \
                    'At least once each week': 3}
        return df.apply(lambda row: 'NA' if pd.isna(row['StackOverflowFoundAnswer']) or pd.isna(row['StackOverflowCopiedCode'])\
                                    else reverseMap[visitMap[row['StackOverflowFoundAnswer']] +\
                                                    visitMap[row['StackOverflowCopiedCode']]], axis=1)
    elif year == 2018 or year == 2019:
        return df['StackOverflowVisit'].fillna('NA')
    else:
        print('No such year:', year) 
        
        
# clean the participate rate field
def clean_participate(df, year):
    if year == 2017:
        reverseMap = {0: 'I have never participated in Q&A on Stack Overflow', 8: 'Multiple times per day', \
                      7: 'Multiple times per day', 6: 'Multiple times per day', 5: 'Multiple times per day', \
                      4: 'Daily or almost daily', 3: 'A few times per week', \
                      2: 'A few times per month or weekly', 1: 'Less than once per month or monthly'} 
        visitMap = {"Haven't done at all": 0, 'Once or twice': 1, 'Several times': 2, 'At least once each day': 4, \
                    'At least once each week': 3}
        return df.apply(lambda row: 'NA' if pd.isna(row['StackOverflowNewQuestion']) or pd.isna(row['StackOverflowAnswer'])\
                                    else reverseMap[visitMap[row['StackOverflowNewQuestion']] + \
                                                    visitMap[row['StackOverflowAnswer']]], axis=1)
    elif year == 2018 or year == 2019:
        return df['StackOverflowParticipate'].fillna('NA')
    else:
        print('No such year:', year)
        
        
        
        
        
        