# Denver Metro Air Quality: Influence on overall Hospital Death Rates for Inflammatory related events?
# Introduction

The link between air-quality and heath outcomes has been known ,essentially, forever; humans likely observed death from excessive smoke inhalation prior to mastering fire. 

![]( https://github.com/AChezick/Capstone1/blob/main/images/tame.png ) 
image from https://www.smh.com.au/world/south-america/taming-fire-let-humans-thrive-now-man-made-flames-in-the-amazon-threaten-us-all-20190828-p52lmp.html 

___ 

More recently the link between less observable air quality measures and harmful health outcomes has been established (1). 

The chemical reaction of combustion decreases the sample size of matter and changes the nature of reactants into small harmful gases, some of which are measured and referred to as particulate matter (PM). 


Inhalation of PM can interfere with cellular processes by being mistaken for foreign bodies leading to inflammatory events and from direct damage to cellular proteins leading to aberrant processes.


Chronic inhalation for the measures of PM 2.5 and PM 10 have been shown to cause inflammation of the lungs and other tissues, which can lead to secondary events such at heart attacks, strokes, even inflammation of the kidney. A few days of extremely poor air quality has been shown to cause numerious inflammatory events in rodent models. Below is an image showing transfer of metals can be observed during gestation .

![]( https://github.com/AChezick/Capstone1/blob/main/images/F2.large.jpg    )
Image credit: Uschi M. Graham (University of Kentucky, Lexington, KY) (Top) and Deborah Cory-Slechta (Bottom). 


### Size Matters

PM 2.5 measures reflect particulates that are about 1/35 the width of a human hair or as the name implies 2.5 microns (5). Particulates that measure positive for PM 2.5 are typically produced from combustion events such as metals metals. However, other organic compounds / proteins can be found in this range. PM 10 examples include dust, mold and and about 1/5th the size of a human hair (5).

### Costs 

Health care costs of chronic inflammatory diseases is in the trillions. It would be inappropriate to suggest that improving air quality would reduce all inflammatory disease outcomes for every person. However, the reduction of potential influences on costly chronic diseases would improve the quality of life for many humans and reduce health care costs associated with these diseases (7). 

# Question:

Can I detect any relationships among the air quality measures of PM 2.5 & PM 10 with emergency room visits for all of Colorado?

### Hypothesis (qualitative) 

Ho: I **will NOT** be able to detect significant increased differences in average death events at 0 or +1 weeks of high PM levels.

Ho: I **will** be able to detect significant increased differences in average death events at 0 or +1 weeks of high PM levels.

## Rational:

*According to data form Wikipedia(4) roughly 3 million of Colorado's six-million residents reside within the Denver-Aurora-Lakewood Metropolitan area.

If there are any impacts from poor air quality on hospital death rates, this area is *more likely* to show impacts on the overall death rates. This fact helped me focus my anlysis with a more managable range.


# Data & Processing:
The Environmental Protection Adgencey (EPA) has archives of air quality measures with columns of interest for various measures (2). I used data from their AirNow program, which uses a mix of fully and non-fully verrifed data. Not all data was certifed through the regulatory processes associated with the EPA Air Quality System and **cannot** be used to inform regulation decisions.

Impacts on death rates was assessed data from the Centers for Disease Control (CDC). I was able to locate national hospital data for weekly death counts by cause (3). These data **do not represent the total amount of deaths in Colorado during that week**. 

The data was well organized and did not require much text cleaning*. However, determining how to grab data to perform the hypothesis test was considerable. As having different numbers of PM measures for PM 2.5 and PM 10 at each site for each day/week equates to a complex 'standard' code block for required alignments. 

### First 5 rows of Weekly Death Events Post Cleaning

| MMWR_Year | MMWR_Week | Week_End_Date | All_Cause | Diabetes | Alzheimer | Influenza_pneumonia | Chronic_lower_respiratory | Other_diseases_of_respiratory | Nephritis, nephrotic_syndrome | Diseases_of_heart | Cerebrovascular_diseases | All Cause | Influenza_and_pneumonia |
|-----------|-----------|---------------|-----------|----------|-----------|---------------------|---------------------------|-------------------------------|-------------------------------|-------------------|--------------------------|-----------|-------------------------|
| 2014      | 1         | 01/04/2014    | 416.0     | 12.0     |           | 14.0                | 33                        |                               |                               | 96                | 22                       |           |                         |
| 2014      | 2         | 01/11/2014    | 764.0     | 16.0     | 21.0      | 30.0                | 59                        | 14.0                          | 11.0                          | 145               | 41                       |           |                         |
| 2014      | 3         | 01/18/2014    | 702.0     | 15.0     | 31.0      | 28.0                | 47                        |                               | 10.0                          | 136               | 36                       |           |                         |
| 2014      | 4         | 01/25/2014    | 638.0     | 16.0     | 22.0      | 28.0                | 53                        | 10.0                          |                               | 129               | 36                       |           |                         |
| 2014      | 5         | 02/01/2014    | 725.0     | 15.0     | 25.0      | 27.0                | 44                        |                               | 12.0                          | 164               | 44                       |           |                         |

I combined two similar data frames to create the master data frame for death events. After cleaning the data frame was 313:14. 


### First 5 Rows of Air Quality Data from AirNow
| Date       | Source | Site ID  | POC | Daily Mean PM2.5 Concentration | UNITS    | DAILY_AQI_VALUE | Site Name                              | DAILY_OBS_COUNT | PERCENT_COMPLETE | AQS_PARAMETER_CODE | AQS_PARAMETER_DESC       | CBSA_CODE | CBSA_NAME                  | STATE_CODE | STATE    | COUNTY_CODE | COUNTY | SITE_LATITUDE    | SITE_LONGITUDE      |
|------------|--------|----------|-----|--------------------------------|----------|-----------------|----------------------------------------|-----------------|------------------|--------------------|--------------------------|-----------|----------------------------|------------|----------|-------------|--------|------------------|---------------------|
| 2014-01-02 | AQS    | 80010006 | 1   | 16.2                           | ug/m3 LC | 60              | Alsup Elementry School - Commerce City | 1               | 100.0            | 88101              | PM2.5 - Local Conditions | 19740     | Denver-Aurora-Lakewood, CO | 8          | Colorado | 1           | Adams  | 39.8260070009282 | -104.93743799999999 |
| 2014-01-05 | AQS    | 80010006 | 1   | 4.4                            | ug/m3 LC | 18              | Alsup Elementry School - Commerce City | 1               | 100.0            | 88101              | PM2.5 - Local Conditions | 19740     | Denver-Aurora-Lakewood, CO | 8          | Colorado | 1           | Adams  | 39.8260070009282 | -104.93743799999999 |
| 2014-01-08 | AQS    | 80010006 | 1   | 24.8                           | ug/m3 LC | 78              | Alsup Elementry School - Commerce City | 1               | 100.0            | 88101              | PM2.5 - Local Conditions | 19740     | Denver-Aurora-Lakewood, CO | 8          | Colorado | 1           | Adams  | 39.8260070009282 | -104.93743799999999 |
| 2014-01-11 | AQS    | 80010006 | 1   | 3.2                            | ug/m3 LC | 13              | Alsup Elementry School - Commerce City | 1               | 100.0            | 88101              | PM2.5 - Local Conditions | 19740     | Denver-Aurora-Lakewood, CO | 8          | Colorado | 1           | Adams  | 39.8260070009282 | -104.93743799999999 |
| 2014-01-14 | AQS    | 80010006 | 1   | 4.1                            | ug/m3 LC | 17              | Alsup Elementry School - Commerce City | 1               | 100.0            | 88101              | PM2.5 - Local Conditions | 19740     | Denver-Aurora-Lakewood, CO | 8          | Colorado | 1           | Adams  | 39.8260070009282 | -104.93743799999999 |

Something to note is the POC column. This column and value indicates the observation number for that particular site. Since there are 13 different sites with 1-3 measures for PM 2.5 and PM 10 (and in no particular pattern for the number of measures per site per day) taking the average of all measures for each site ID for each day. My ending air quality data frame had roughly 25,000 entries post processing.

Date time indexing was completed so I could re-index this data frame and aggregate by date into weeks for each site ID. Due to large gaps and wanting the most overlap of PM 2.5 & PM 10 measures, I chose the three sites that had the most data points.

# Visualization 


The six year distribution from this data set was normally distributed

![]( https://github.com/AChezick/Capstone1/blob/main/images/normal_dist_hr_event.png )

You can see the average annual PM 10 and PM 2.5 numbers are fairlyconsistent.

![]( https://github.com/AChezick/Capstone1/blob/main/images/annual_heart_events.png )


The average for the annual PM 10 levels was 22.7

![]( https://github.com/AChezick/Capstone1/blob/main/images/annual_pm10.png)

Data from this site was missing for 2017.

![]( https://github.com/AChezick/Capstone1/blob/main/images/annual25.png ) 

___

Among the three sites tested The Daily Mean Concentration was fairly consistent 7.3 , 9.6, 7.4 

![]( https://github.com/AChezick/Capstone1/blob/main/images/variance.png ) 

___

Again, visually there appears to be some association between PM levels and heart events. It would again be important to state that its impossible to assign a causal link from a single event for a chronic disease (or any dynamical system). The goal of this capstone was to see if I could detect a statisitical association among the means for weeks on or after air quality levels in the worst 5% range from these measures.

![]( https://github.com/AChezick/Capstone1/blob/main/images/overlap1.png )

Since this data cannot be used for leglistation I considered this the entire sample of measures from a qulative perspective. This allows for extension of this project as offical data become available.

![]( https://github.com/AChezick/Capstone1/blob/main/join_plot.png ) 

#### For hypothesis testing I separated weekly events into two categories based six years of data for that Site ID. 

Ho: I **will NOT** be able to detect significant increased differences in average death events at 0 or +1 weeks of high PM levels.

Ha: I **will** be able to detect significant increased differences in average death events at 0 or +1 weeks of high PM levels.

![]( https://github.com/AChezick/Capstone1/blob/main/images/join_plot.png )

![]( https://github.com/AChezick/Capstone1/blob/main/images/scatter1.png  )
___

![]( https://github.com/AChezick/Capstone1/blob/main/images/scatter_pm10.png )

___ 

#### Results


PM_25 and Heart Events for week 0 indicate I should fail to reject the null hypothesis: -0.9, pvalue=0.38 

PM_10 and Heart Events for week 0 indicate I should fail to reject the null hypothesis: -0.53 , pvalue=0.6 


# Further exploration

This capstone is far from a complete analysis. In the end I only performed hypothesis testing on 1 of 13 sites for PM 2.5 and PM 10. There were several other air quality measures that could be assessed. Creating a complete workflow to test all hypotheses with confidence intervals is my next step. Further I was unable to successfully complete a hypothesis test for the +1 weeks. 
___

___

Refereces

1.Retrieved from World Health Organiztion 
https://www.who.int/airpollution/ambient/health-impacts/en/

2. EPA Data
https://www.epa.gov/outdoor-air-quality-data/download-daily-data

3. Weekly Death Counts
https://data.cdc.gov/NCHS/Weekly-Counts-of-Deaths-by-State-and-Select-Causes/muzy-jte6/data 

4. Dener-Auroa-Lakewood Population 
https://en.wikipedia.org/wiki/Denver_metropolitan_area 

5. PM Basics from EPA.
https://www.epa.gov/pm-pollution/particulate-matter-pm-basics

6. Proceedings of the National Academy of Sciences Jun 2020, 117 (25) 13856-13860; DOI: 10.1073/pnas.2008940117 
https://www.pnas.org/content/117/25/13856

7. The global burden of multiple chronic conditions: A narrative review
https://doi.org/10.1016/j.pmedr.2018.10.008 
