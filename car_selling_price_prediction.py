# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 13:13:14 2021

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('car data.csv')

'''
from pandas_profiling import ProfileReport
prof = ProfileReport(df)
prof.to_file(output_file='df.html')

fig = plt.figure(figsize=[10,5])
plt.subplot(2,2,1)
sns.boxplot(df['Selling_Price'])
plt.subplot(2,2,2)
sns.boxplot(df['Present_Price'])
plt.subplot(2,2,3)
sns.boxplot(df['Year'])
plt.subplot(2,2,4)
sns.boxplot(df['Kms_Driven'])
plt.tight_layout()

df.loc[df['Present_Price'] == df['Present_Price'].max()]
df.loc[df['Selling_Price'] == df['Selling_Price'].max()]
df.loc[df['Kms_Driven'] == df['Kms_Driven'].max()]

'''
df['age'] = 2020 - df['Year']
df.drop(columns=['Car_Name', 'Year'], inplace=True)

'''
from pandas_profiling import ProfileReport
prof = ProfileReport(df_dummies)
prof.to_file(output_file='df_dummies.html')
'''

df_dummies = pd.get_dummies(data=df, drop_first=True)

y = df_dummies['Selling_Price']
X = df_dummies.drop(columns='Selling_Price')

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

def model_selection(X_train, y_train, X_test, y_test, models):
    
    from sklearn.metrics import max_error, mean_absolute_error, mean_squared_error, r2_score
    
    R2_result = []
    MSE_result = []
    str_models = []
    
    for model in models:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        MSE = mean_squared_error(y_test, y_pred)
        R2 = r2_score(y_test, y_pred)       
        R2_result.append(R2)
        MSE_result.append(MSE)  
        str_models.append(str(model))
    
    fig, (ax1, ax2) = plt.subplots(2, 1)

    ax1.plot(R2_result)
    ax1.set_ylabel('R2_score')


    ax2.plot(str_models,np.sqrt(MSE_result))
    ax2.set_ylabel('RMSE_result')
    ax2.set_xticklabels(str_models, rotation=45)
    plt.tight_layout()
    
    return pd.DataFrame({'models':models, 'R2':R2_result, 'RMSE':np.sqrt(MSE_result)})            

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import BayesianRidge
from sklearn.linear_model import SGDRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

models = [LinearRegression(), Ridge(), Lasso(), BayesianRidge(), SGDRegressor(), SVR(), KNeighborsRegressor(),
          DecisionTreeRegressor(), RandomForestRegressor(), GradientBoostingRegressor()]
model_selection(X_train, y_train, X_test, y_test, models)   







def model_randomCV(X, y):
    
    from sklearn.model_selection import RandomizedSearchCV
    from sklearn.ensemble import RandomForestRegressor
    
    model_parameter = {'model':RandomForestRegressor(), 'parameters':{'n_estimators': np.arange(100, 500, 10),
                                                                              'max_features':['auto', 'sqrt'], 
                                                                              'max_depth':np.arange(10,110, 10)}}
    
    randCV = RandomizedSearchCV(estimator=model_parameter['model'], param_distributions=model_parameter['parameters'], n_jobs=-1, 
                                cv=5)
    randCV.fit(X, y)
    
    print('best_parameters: ' + str(randCV.best_params_))
    print('best_score: ' + str(randCV.best_score_))
    
    
    
    
    
    
    
def tuning_param(X, y, model, parameters):
    
    from sklearn.model_selection import GridSearchCV   
        
    scores = []
   
    fig, axs = plt.subplots(len(parameters))
    k = 0   
    for parameter in parameters:
        
        clf = GridSearchCV(estimator = model, param_grid = parameter, cv=5, scoring='r2')
        clf.fit(X, y)
        

        for name_param, val_param in parameter.items():
            
            grid_mean_scores = clf.cv_results_['mean_test_score']

            axs[k].plot(val_param, grid_mean_scores)
            axs[k].set_xlabel(name_param)
            axs[k].set_ylabel('R2')
            k+=1
            
            
        scores.append({'parameter':name_param,
                       'best_R2':clf.best_score_,
                       'best_value':clf.best_params_})
            
    plt.tight_layout()       
    return pd.DataFrame(scores, columns=['parameter', 'best_R2', 'best_value'])


from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
parameters = [{'n_estimators': np.arange(100, 150, 10)}, {'max_features':['auto', 'sqrt']}, {'max_depth':np.arange(10,60, 10)}]
tuning_param(X_train, y_train, model, parameters)




def model_tuning(X, y):
    from sklearn.linear_model import LinearRegression
    from sklearn.linear_model import Ridge
    from sklearn.linear_model import Lasso
    from sklearn.model_selection import GridSearchCV   
    
    model_parameter = {'linear_regression' : {'model':LinearRegression(), 'parameter' : {'normalize':['True', False]}},
                       'Lasso': {'model':Lasso(), 'parameter':{'alpha': np.arange(1, 51, 1)}},
                       'Ridge':{'model':Ridge(), 'parameter':{'alpha': np.arange(1, 51, 1)}}}
    
    scores = []
    
    for model_name, mp in model_parameter.items():
        clf = GridSearchCV(estimator = mp['model'], param_grid = mp['parameter'], cv=10, scoring='r2')
        clf.fit(X, y)
            
        scores.append({'model':model_name,
                       'best_R2':clf.best_score_,
                       'best_parameter':clf.best_params_})
        
        par_dict = mp['parameter']
        fig, ax = plt.subplots(len(par_dict), 1, figsize=(7,5))
        for name_param, val_param in par_dict.items():
            grid_mean_scores = clf.cv_results_['mean_test_score']
            
            plt.plot(val_param, grid_mean_scores)
    
            plt.xlabel('Parameter Sequences')
            plt.ylabel('R2')
            plt.title((model_name))
    
   
    return pd.DataFrame(scores, columns=['model', 'best_R2', 'best_parameter'])






def car_price_predict(reg_model):
   
    reg_model.fit(X_train, y_train)
    
    y_pred = reg_model.predict(X_test)

    from sklearn.metrics import max_error, mean_absolute_error, mean_squared_error, r2_score
    ME = max_error(y_test, y_pred)
    MEA = mean_absolute_error(y_test, y_pred)
    MSE = mean_squared_error(y_test, y_pred)
    R2 = r2_score(y_test, y_pred)
    
    print('maximum error: {:.3f}'.format(ME))
    print('mean absolute error: {:.3f}'.format(MEA))
    print('root mean squared error: {:.3f}'.format(np.sqrt(MSE)))
    print('R2 Score: {:.3f}'.format(R2))
    
    ax = sns.relplot(y_test, y_pred)
    ax.set(title='y_test vs y_pred', xlabel='actual', ylabel='prediksi')
    plt.tight_layout()



