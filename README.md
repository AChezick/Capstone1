# Denver Metro Air Quality: Influence on overall Hospital Death Rates for Inflammatory related events?
# Introduction

The link between air-quality and heath outcomes has been known ,essentially, forever; humans likely observed death from excessive smoke inhalation prior to mastering fire. More recently the link between less observable poor air quality and harmful health outcomes has been estabolished (1). The chemical reaction of combistion decreases the sample size of matter and changes the nature of reactants into small harmful gases, some of which are measured and referred to as particulate matter (PM). Inhalation of PM can interfer with cellular processes by being mistaken for forgein bodies leading to inflammatory events and from direct damage to cellular proteins leading to abbarent processes.

# Question:
Can I detect any relationships among the air quality measures of PM 2.5 & PM 10 with emergencey room visits for all of Colorado?

## Rational:

*According to data form Wikipedia(4) roughly 3 million of Colorado's six-million residents reside within the Denver-Aurora-Lakewood Metropolitan area.

If there are any impacts from poor air quality on hospital death rates, this area is *more likely* than any other to have impacts on the overall death rates.


# Data:
The Environmental Protection Adgencey (EPA) has archives of air quality measures with columns of interest for various measures (2). I used data from their AirNow program, which uses a mix of fully and non-fully verrifed data. Not all data was certifed through the regulatory processes associated with the EPA Air Quality System and **cannot** be used to inform regulation decisions.

Impacts on death rates was assessed data from the Centers for Disease Control (CDC). I was able to locate national hospital data for weekly death counts by cause (3). These data **do not represent the total amount of deaths in Colorado during that week**. 

The data was well organized and did not require much text cleaning. However, determining how to grab data to perform the hypothesis test was considerable.

### First 5 rows of Weekly Death Events
| MMWR_Year | MMWR_Week | Week_End_Date | All_Cause | Diabetes | Alzheimer | Influenza_pneumonia | Chronic_lower_respiratory | Other_diseases_of_respiratory | Nephritis, nephrotic_syndrome | Diseases_of_heart | Cerebrovascular_diseases | All Cause | Influenza_and_pneumonia |
|-----------|-----------|---------------|-----------|----------|-----------|---------------------|---------------------------|-------------------------------|-------------------------------|-------------------|--------------------------|-----------|-------------------------|
| 2014      | 1         | 01/04/2014    | 416.0     | 12.0     |           | 14.0                | 33                        |                               |                               | 96                | 22                       |           |                         |
| 2014      | 2         | 01/11/2014    | 764.0     | 16.0     | 21.0      | 30.0                | 59                        | 14.0                          | 11.0                          | 145               | 41                       |           |                         |
| 2014      | 3         | 01/18/2014    | 702.0     | 15.0     | 31.0      | 28.0                | 47                        |                               | 10.0                          | 136               | 36                       |           |                         |
| 2014      | 4         | 01/25/2014    | 638.0     | 16.0     | 22.0      | 28.0                | 53                        | 10.0                          |                               | 129               | 36                       |           |                         |
| 2014      | 5         | 02/01/2014    | 725.0     | 15.0     | 25.0      | 27.0                | 44                        |                               | 12.0                          | 164               | 44                       |           |                         |


--Note how the data are multi-dimensional.

# Visulation



# Further exploration


Refereces

1.Retrieved from World Health Organiztion 
https://www.who.int/airpollution/ambient/health-impacts/en/

2. EPA Data
https://www.epa.gov/outdoor-air-quality-data/download-daily-data

3. Weekly Death Counts
https://data.cdc.gov/NCHS/Weekly-Counts-of-Deaths-by-State-and-Select-Causes/muzy-jte6/data 

4. Dener-Auroa-Lakewood Population 
https://en.wikipedia.org/wiki/Denver_metropolitan_area 

5. 
