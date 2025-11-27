import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

path = 'College_Scorecard_Most_Recent_Institutional_Data/Data_Assets/college_scorecard_enriched.csv'
df = pd.read_csv(path)

y = df['ADM_RATE']
X = df.drop(columns=['ADM_RATE'])

numeric_features = ['SAT_AVG','COSTT4_A','PCTPELL','UGDS_WHITE','UGDS_BLACK','UGDS_HISP','UGDS_ASIAN','DEBT_MDN',
                    'PELL_PCT_FTFT','PELL_AVG_AID','LOAN_PCT_FTFT','LOAN_AVG_AID','NETPRICE_INCOME_0_30',
                    'NETPRICE_INCOME_48_75','NETPRICE_INCOME_GT_110','UG_TWOORMORE_PCT','UG_RACE_UNKNOWN_PCT']
cat_features = ['CONTROL','HIGHDEG','REGION']

pre_scaled = ColumnTransformer([
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), cat_features)
])

pre_unscaled = ColumnTransformer([
    ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), cat_features)
], remainder='passthrough')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

results = {}

def rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

def collect(name, model, Xtr, Xte):
    pred_tr = model.predict(Xtr)
    pred_te = model.predict(Xte)
    results[name] = {
        'Train MAE': mean_absolute_error(y_train, pred_tr),
        'Train RMSE': rmse(y_train, pred_tr),
        'Train R2': r2_score(y_train, pred_tr),
        'Test MAE': mean_absolute_error(y_test, pred_te),
        'Test RMSE': rmse(y_test, pred_te),
        'Test R2': r2_score(y_test, pred_te)
    }

# Linear Regression
lr = Pipeline(steps=[('pre', pre_scaled), ('model', LinearRegression())])
lr.fit(X_train, y_train)
collect('Linear Regression', lr, X_train, X_test)

# Decision Tree default
pre_unscaled.fit(X_train, y_train)
Xtr_dt = pre_unscaled.transform(X_train)
Xte_dt = pre_unscaled.transform(X_test)
dt = DecisionTreeRegressor(random_state=42)
dt.fit(Xtr_dt, y_train)
collect('Decision Tree (default)', dt, Xtr_dt, Xte_dt)

grid_dt = GridSearchCV(DecisionTreeRegressor(random_state=42),
                       param_grid={'max_depth':[3,5,7,10,15,None], 'min_samples_split':[2,5,10], 'min_samples_leaf':[1,2,4,8]},
                       cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
grid_dt.fit(Xtr_dt, y_train)
dt_tuned = grid_dt.best_estimator_
collect('Decision Tree (tuned)', dt_tuned, Xtr_dt, Xte_dt)

# kNN default
knn = Pipeline(steps=[('pre', pre_scaled), ('model', KNeighborsRegressor())])
knn.fit(X_train, y_train)
collect('kNN (default)', knn, X_train, X_test)

grid_knn = GridSearchCV(Pipeline(steps=[('pre', pre_scaled), ('model', KNeighborsRegressor())]),
                        param_grid={'model__n_neighbors':[3,5,7,10,15,20], 'model__weights':['uniform','distance'], 'model__p':[1,2]},
                        cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
grid_knn.fit(X_train, y_train)
knn_tuned = grid_knn.best_estimator_
collect('kNN (tuned)', knn_tuned, X_train, X_test)

import json
print(json.dumps(results, indent=2))
print('Best DT params:', grid_dt.best_params_)
print('Best kNN params:', grid_knn.best_params_)
