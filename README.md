# used_car_price_prediction
# Dataset
Iam using vehivle.csv in used car dataset from kaggle, [https://www.kaggle.com/austinreese/craigslist-carstrucks-data](https://www.kaggle.com/austinreese/craigslist-carstrucks-data) to predict second hand price based on the condition of the car within dataset. This dataset is scraped from craiglist website
the dataset contains 25 columns, they are:

1. id = entry id 
2. url = listing URL
3. region = craiglist region
4. region_url
5. price = entry price
6. year = entry year
7. manufacturer = manufacturer of vehicle
8. model = model of vehicle
9. condition = condition of vehicle
10. cylinders = number of cylinders
11. fuel = type of fuel for vehicle
12. odometer
13. title_status
14. transmission
15. VIN = Vehicle Identification Number
16. drive = drivetrain of vehicle
17. size 
18. type
19. paint_color
20. image_url
21. description
22. county
23. state
24. lat = latitude
25. long = longitude

# Data Cleaning and Feature Engineering

- drop the unnecessary columns for the model, there are id, url, region, region_url, VIN, image_url, description, lat, long, model, county, state, title_status, paint_color
- Filter the price between $1000 to $50000
- transform the year column to the age column
- set the >= 1 threshold for the age column
- set the >=14000 threshold for the odometer column, and rid off the outlier with max data 9999999
- drop the duplicates data
- fill Not Available data with 'other' in manufacturer column

# Machine Learning Model

- Change the Categorical data to numerical for machine learning using labelencoder for the better performance than using dummy, cause it will create more features and affecting the computation cost
- because the range of the data like age, odometer are very diffenrent, so we need to do Normalization or Standarization. here Iam using Standarization.
- split the dataset to 80% training and 20% test
- compare the regression models in default setting and pick the top 3 performance using R2 in regression problems
- do the cross validation to do a performance comparison using cross validation and not.
- tuning each parameter using the GridSearchCV to see the effect in the model and see the optimal range for searching the global optimal using RandomizedSearchCV later
- do the Hyperparameter Tuning using RandomizedSearchCV using the optimal range of the each parameters in previous process
- check the overfitting / underfitting for the model best estimator
- do the exactly the same process for the other models
- recap the final result
- Final predicted model

Reference: 

- [https://github.com/codebasics/py/blob/master/ML/15_gridsearch/15_grid_search.ipynb](https://github.com/codebasics/py/blob/master/ML/15_gridsearch/15_grid_search.ipynb)
- [https://github.com/justmarkham/scikit-learn-videos/blob/master/08_grid_search.ipynb](https://github.com/justmarkham/scikit-learn-videos/blob/master/08_grid_search.ipynb)
