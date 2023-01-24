# WiDS 2023 - Codeup Submission
## Predict the arithmetic mean of the max and min observed temperature over the next 14 days for specific locations and start dates

## Project Description
Extreme weather events are sweeping the globe and range from heat waves, wildfires and drought to hurricanes, extreme rainfall and flooding. These weather events have multiple impacts on agriculture, energy, transportation, as well as low resource communities and disaster planning in countries across the globe.

Accurate long-term forecasts of temperature and precipitation are crucial to help people prepare and adapt to these extreme weather events. Currently, purely physics-based models dominate short-term weather forecasting. But these models have a limited forecast horizon. The availability of meteorological data offers an opportunity for data scientists to improve sub-seasonal forecasts by blending physics-based forecasts with machine learning. Sub-seasonal forecasts for weather and climate conditions (lead-times ranging from 15 to more than 45 days) would help communities and industries adapt to the challenges brought on by climate change.

Participants will submit forecasts of temperature and precipitation for one year, competing against the other teams as well as official forecasts from NOAA.

## Project Goals
* Determine which columns to use for our data exploration.
* Explore to find features that indicate the ```contest-tmp2m-14d__tmp2m```.
* Based on the findings predict the ```contest-tmp2m-14d__tmp2m``` for the test_data.
* Submit our finidings to the WiDS 2023 competition.

## Initial Thoughts
My initial hypothesis is that location, elevation and wind measurements will be indicators of the temperature.

## The Plan
* Aqcuire the data from Kaggle

* Prepare data
    * Remove all columns besides those listed ```contest``` or location indicators.
    * ????
    * ????

* Explore data in search of indicators of ```contest-tmp2m-14d__tmp2m``` 
    * Answer the following initial questions
        * Does ??????? indicate ```contest-tmp2m-14d__tmp2m``` ?
        * Does ??????? indicate ```contest-tmp2m-14d__tmp2m``` ?
        * Does ??????? indicate ```contest-tmp2m-14d__tmp2m``` ?
        * Does ??????? indicate ```contest-tmp2m-14d__tmp2m``` ?

* Develop a model to predict ```contest-tmp2m-14d__tmp2m``` ?
    * Use indicators identified through exploration to build different predictive models
    * Evaluate models on train and validate data
    * Evaluate the best model on the test data

* Draw conclusions

## Data dictionary
| Feature | Definition | Type |
|:--------|:-----------|:-------
|**????**| ?????? | *string*|
|**?????**| ????? | *float*|
|**Target variable**
|**contest-tmp2m-14d__tmp2m**| the arithmetic mean of the max and min observed temperature over the next 14 days | *float* |


## Steps to Reproduce
1. Clone this repo
2. Get data.
3. Run notebook.

## Takeaways and Conclusions
* ?????
* ?????

## Recommendations
* ????
* ?????

## Next Steps
* In the next iteration:
    * Naomi will save the world by ending climate change. Watch out. She's coming for you El Niño.
    * ?????