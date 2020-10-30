
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams.update({'font.size': 16, 'font.family': 'sans'})

#import modules 

death_2014 = pd.read_csv('/home/allen/Galva/capstones/capstone1/Weekly_Counts_of_Deaths_by_State_and_Select_Causes__2014-2018.csv')
death_2019 = pd.read_csv('/home/allen/Galva/capstones/capstone1/Weekly_Counts_of_Deaths_by_State_and_Select_Causes__2019-2020.csv')
death_master = pd.concat([death_2014 , death_2019])

#import weekly death rate csv
#Concat dfs

death_columns = death_master.columns 
death_cols_to_remove = ['Natural Cause','Jurisdiction of Occurrence','Malignant neoplasms (C00-C97)', 'Septicemia (A40-A41)','Symptoms, signs and abnormal clinical and laboratory findings, not elsewhere classified (R00-R99)']
for i in death_columns:
    if i[0] == 'f':
        death_cols_to_remove.append(i)
    if "COVID" in i:
        death_cols_to_remove.append(i)

death_master.drop(death_cols_to_remove, axis =1 , inplace=True)
#reduce columns in weekly death rates

death_master.columns =  ['MMWR_Year', 'MMWR_Week', 'Week_End_Date', 'All_Cause',
       'Diabetes',
       'Alzheimer', 'Influenza_pneumonia',
       'Chronic_lower_respiratory',
       'Other_diseases_of_respiratory',
       'Nephritis, nephrotic_syndrome',
       'Diseases_of_heart',
       'Cerebrovascular_diseases', 'All Cause',
       'Influenza_and_pneumonia']
#Rename Columns 

pm25_2014 = pd.read_csv('/home/allen/Galva/capstones/capstone1/pm_25_2014.csv')
pm25_2015 = pd.read_csv('/home/allen/Galva/capstones/capstone1/pm_25_2015.csv')
pm25_2016 = pd.read_csv('/home/allen/Galva/capstones/capstone1/pm_25_2016.csv')
pm25_2017 = pd.read_csv('/home/allen/Galva/capstones/capstone1/pm_25_2017.csv')
pm25_2018 = pd.read_csv('/home/allen/Galva/capstones/capstone1/pm_25_2018.csv')
pm25_2019 = pd.read_csv('/home/allen/Galva/capstones/capstone1/pm_25_2019.csv')

pm25_master = pd.concat([pm25_2014,pm25_2015,pm25_2016,pm25_2017,pm25_2018,pm25_2019])
#create pm25 dfs

pm10_2014 = pd.read_csv('/home/allen/Galva/capstones/capstone1/pm10_2014.csv')
pm10_2015 = pd.read_csv('/home/allen/Galva/capstones/capstone1/pm10_2015.csv')
pm10_2016 = pd.read_csv('/home/allen/Galva/capstones/capstone1/pm10_2016.csv')
pm10_2017 = pd.read_csv('/home/allen/Galva/capstones/capstone1/pm10_2017.csv')
pm10_2018 = pd.read_csv('/home/allen/Galva/capstones/capstone1/pm10_2018.csv')
pm10_2019 = pd.read_csv('/home/allen/Galva/capstones/capstone1/pm10_2019.csv')

pm10_master = pd.concat([pm10_2014, pm10_2015,pm10_2016,pm10_2017,pm10_2018,pm10_2019])
#Create pm10 dfs

pm10_master['Date'] = pd.DatetimeIndex(pm10_master['Date']).date
pm25_master['Date'] = pd.DatetimeIndex(pm25_master['Date']).date
#convert date column to date object

cols_2_drop = ['DAILY_OBS_COUNT','Source' , 'Site Name','PERCENT_COMPLETE' ,'AQS_PARAMETER_DESC','CBSA_CODE', 'STATE_CODE', 'STATE', 'COUNTY_CODE','COUNTY', 'SITE_LATITUDE', 'SITE_LONGITUDE'  ] 
#Drop columns from pm_dfs

pm25_master.drop(cols_2_drop, axis =1 , inplace=True)
pm10_master.drop(cols_2_drop, axis =1 , inplace=True)
#Dropping Columns 

pm25_master['Date'] = pd.to_datetime(pm25_master['Date'])
pm25_master1 = pm25_master.set_index('Date').resample('W-Sun').mean()
#

###SAMPLE
pm25_site1a = pm25_master1[pm25_master1['Site ID'] == 80310026]
###SAMPLE

heart = death_master['Diseases_of_heart'].values 
heart1 = [int(x) for x in heart[0:314]]
lowerRes = death_master['Chronic_lower_respiratory'].values  
otherRes = death_master['Other_diseases_of_respiratory'].values 
pm_pm25_1aa = pm25_site1a['Daily Mean PM2.5 Concentration'].values


print(len(heart1))
##Plotting Try
fig, ax = plt.subplots(1, figsize=(16, 4))
x = list(range(1, 315)) 

ax.plot(x, heart1, label="Heart Events")
ax.plot(x, pm_pm25_1aa , label="PM 2.5 (ug/m3)")

ax.legend()
ax.set_xlabel("Day")
ax.set_ylabel("Number of Event & PM")

ax.set_title("Cumulative Number of Comments over Two Months")
plt.show() 
#### End of plotting Try 


'''
Class Make_Site

lst_of_sites = [ 80310026 , 80930002 , 80010008 ]
the class will run once for each of the above,

Given a site , Auto Mate the following:
1. 
Create a 25_df from master df
Create a 10_df 

2. reset index
pm25_1a = pm25_site1a.set_index('Date').resample('W-Sun').mean()

3. Calculate sig figures for columns from the dfs made above


4. Graphing / Plots
-Make a dist plot from for the columns for PM_10 and PM_25 
-- sns.distplot(death_master['Diseases_of_heart'])

-Make tripple line graph for health events and PM_site 

'''