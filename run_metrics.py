import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor

path = Path('College_Scorecard_Most_Recent_Institutional_Data/Data_Assets/college_scorecard_enriched.csv')
df = pd.read_csv(path)

numeric_features = [
    'SAT_AVG', 'COSTT4_A', 'PCTPELL', 'UGDS_WHITE', 'UGDS_BLACK', 'UGDS_HISP',
    'DEBT_MDN', 'PELL_PCT_FTFT', 'LOAN_PCT_FTFT', 'NETPRICE_INCOME_0_30',
    'NETPRICE_INCOME_GT_110', 'UG_TWOORMORE_PCT',
    'PELL_RECIPIENTS_TOTAL', 'PELL_DISBURSEMENTS_TOTAL',
    'DL_TOTAL_RECIPIENTS', 'DL_TOTAL_DISBURSEMENTS', 'DL_PARENT_PLUS_DISBURSEMENTS'
]
categorical_features = ['CONTROL', 'HIGHDEG', 'REGION']
target_col = 'ADM_RATE'

X = df[numeric_features + categorical_features]
y = df[target_col]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

num_transformer = StandardScaler()
cat_transformer = OneHotEncoder(drop='first', handle_unknown='ignore')
preprocessor = ColumnTransformer([
    ('num', num_transformer, numeric_features),
    ('cat', cat_transformer, categorical_features)
])
preprocessor_dt = ColumnTransformer([
    ('cat', cat_transformer, categorical_features)
], remainder='passthrough')

def rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

def evaluate(model, Xtr, Xte, ytr, yte):
    pred_tr = model.predict(Xtr)
    pred_te = model.predict(Xte)
    return {
        'Train MAE': mean_absolute_error(ytr, pred_tr),
        'Train RMSE': rmse(ytr, pred_tr),
        'Train R2': r2_score(ytr, pred_tr),
        'Test MAE': mean_absolute_error(yte, pred_te),
        'Test RMSE': rmse(yte, pred_te),
        'Test R2': r2_score(yte, pred_te)
    }

results = {}

lr_model = Pipeline([('pre', preprocessor), ('model', LinearRegression())])
lr_model.fit(X_train, y_train)
results['Linear Regression'] = evaluate(lr_model, X_train, X_test, y_train, y_test)

preprocessor_dt.fit(X_train, y_train)
X_train_dt = preprocessor_dt.transform(X_train)
X_test_dt = preprocessor_dt.transform(X_test)

dt_model = DecisionTreeRegressor(random_state=42)
dt_model.fit(X_train_dt, y_train)
results['Decision Tree (Default)'] = evaluate(dt_model, X_train_dt, X_test_dt, y_train, y_test)

param_grid_dt = {
    'max_depth': [3, 5, 7, 10, 15, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4, 8]
}
grid_dt = GridSearchCV(DecisionTreeRegressor(random_state=42), param_grid_dt, cv=5,
                       scoring='neg_mean_squared_error', n_jobs=-1)
grid_dt.fit(X_train_dt, y_train)
dt_tuned = grid_dt.best_estimator_
results['Decision Tree (Tuned)'] = evaluate(dt_tuned, X_train_dt, X_test_dt, y_train, y_test)

knn_model = Pipeline([('pre', preprocessor), ('model', KNeighborsRegressor())])
knn_model.fit(X_train, y_train)
results['kNN (Default)'] = evaluate(knn_model, X_train, X_test, y_train, y_test)

param_grid_knn = {
    'model__n_neighbors': [3, 5, 7, 10, 15, 20],
    'model__weights': ['uniform', 'distance'],
    'model__p': [1, 2]
}
grid_knn = GridSearchCV(knn_model, param_grid_knn, cv=5,
                        scoring='neg_mean_squared_error', n_jobs=-1)
grid_knn.fit(X_train, y_train)
knn_tuned = grid_knn.best_estimator_
results['kNN (Tuned)'] = evaluate(knn_tuned, X_train, X_test, y_train, y_test)

summary = pd.DataFrame(results).T[['Test MAE','Test RMSE','Test R2']]
print(summary)
print('\nBest DT params:', grid_dt.best_params_)
print('Best kNN params:', grid_knn.best_params_)
