# Women in Data Science 2023 - Codeup Submission

![6012764](https://user-images.githubusercontent.com/112418599/215001160-da469522-b0e3-4f17-8189-931d0ecf354a.jpg)

## Project Description
Extreme weather events are sweeping the globe and range from heat waves, wildfires and drought to hurricanes, extreme rainfall, and flooding. These weather events have multiple impacts on agriculture, energy, transportation, as well as low resource communities and disaster planning in countries across the globe.

Accurate long-term forecasts of temperature and precipitation are crucial to help people prepare and adapt to these extreme weather events. Currently, purely physics-based models dominate short-term weather forecasting. But these models have a limited forecast horizon. The availability of meteorological data offers an opportunity for data scientists to improve sub-seasonal forecasts by blending physics-based forecasts with machine learning. Sub-seasonal forecasts for weather and climate conditions (lead-times ranging from 15 to more than 45 days) would help communities and industries adapt to the challenges brought on by climate change.

Participants will submit forecasts of temperature and precipitation for one year, competing against the other teams as well as official forecasts from NOAA.

## Project Goals
* Determine which columns to use for our data exploration.
* Explore to find features that indicate the ```mean_temp```.
* Based on the findings predict the ```mean_temp``` for the test_data.
* Submit our finidings to the WiDS 2023 competition.

## Initial Thoughts
My initial hypothesis is that location, elevation, and wind measurements will be indicators of the ```mean_temp```.

## The Plan
* Acquire the data from [Kaggle](https://www.kaggle.com/competitions/widsdatathon2023/data)

* Prepare data
    * Binned regions (Dry, Temperate, Continental) 
    * Binned elevation ('bottom_low', 'top_low', 'mid', 'high')
    * Split data into train, validate and test (approx. 60/25/15)
    * Scaled continuous variables (min/max scaler)
    * Outliers have not been removed for this iteration of the project

* Explore data in search of indicators of ```mean_temp``` 
    * Answer the following initial questions
        * Are the climate regions significant?
        * Does elevation impact temperature?
        * Is there a correlation between precipitation and mean_temp?
        * Is there a correlation between potential evap and mean_temp?
        * Is there a correlation between mean_temp and geopotential at different heights?

* Develop a model to predict ```mean_temp``` ?
    * Use indicators identified through exploration to build different predictive models
    * Evaluate models on train and validate data
    * Evaluate the best model on the test data

* Draw conclusions

### Features
| Target | Definition | Data Type | Unit |
| :---- | :---- | :---- | :---- |
| **mean_temp**| the arithmetic mean | *float64* | Celsius |

| Feature Name | Definition | Data Type | Unit |
| :---- | :---- | :---- | :---- |
| region | Köppen-Geigerclimate classifications | object | specified regions |
| elevation | elevation | int64 | meters |
| lat| latitude of location (anonymized) | float64 | latitude |
| lon | longitude of location (anonymized) | float64 | longitude |
| startdate | start date of the 14 day period | object | dates |
| potential_evap| potential evaporation | float64 | mL |
| precip| measured precipitation | float64 | mm |
| barometric_pressure | pressure | float64 |Hg (inches of mercury) |
| all_atmos_precip | precipitable water for entire atmosphere | float64 | mm |
| relative humidity | relative humidity | float64 | percent of atmospheric capacity |
| sea level pressure | sea level pressure at surface | float64 | hectoPascals (hPa), also called millibars |
| geopotential height at 10 millibars | actual height of a pressure surface above mean sea-level | float64 | millibars |
| geopotential height at 100 millibars | actual height of a pressure surface above mean sea-level | float64 | millibars |
| geopotential height at 500 millibars | actual height of a pressure surface above mean sea-level | float64 | millibars |
| geopotential height at 850 millibars | actual height of a pressure surface above mean sea-level | float64 | millibars |
| zonal wind at 250 millibars | east-west wind velocity| float64 | meters per second |
| zonal wind at 925 millibars | east-west wind velocity | float64 | meters per second|
| longitudinal wind at 250 millibars | north-south velocity | float64 | meters per second|
| longitudinal wind at 925 millibars | north-south velocity | float64 |meters per second |


## Steps to Reproduce
1. Clone this repo
2. Get data from [Kaggle](https://www.kaggle.com/competitions/widsdatathon2023/data) and put the ```train_data.csv``` in the same directory as the repo.
3. Run notebook.

## Takeaways and Conclusions
### Exploration
* We saw that all the continuous variables have a correlation with our target variable. 
* We looked at our regions and saw that there is a difference in the average mean_temp in each region.
* We binned our elevations, splitting into 4 bins based on quantiles. We saw that there is a difference in average mean_temp of each bin.
### Modeling

* We looked at three different kinds of models; OLS, Lasso Lars and Quadratic.
* Quadratic model performed best on both train and validate.
* We used that model to predict on test and our RMSE remained at a **1.27**.

### Recommendations
* We can use this model to predict the mean temp for the next 14d.

### Next Steps
* We want to investigate creating a model based on the region.
* We want to continue looking at other features in the data set to see if they have correlation with the target variable.
* We want to look into other models that might help improve our model.
