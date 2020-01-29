import pandas as pd
import datetime
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn import svm

consump_data = pd.read_csv("hourly-energy-consumption/AEP_hourly.csv")
consump_data.head()
str(consump_data)
consump_data['Datetime'] = pd.to_datetime(consump_data['Datetime'])

consump_data.isnull().sum()


consump_data['Month'] = pd.DatetimeIndex(consump_data['Datetime']).month
consump_data['Year'] = pd.DatetimeIndex(consump_data['Datetime']).year
consump_data['Day'] = pd.DatetimeIndex(consump_data['Datetime']).day
consump_data['Hour'] = pd.DatetimeIndex(consump_data['Datetime']).hour
consump_data['day_of_year'] = consump_data['Datetime'].dt.dayofyear


#Generate baseline predictions (currently for whole dataset not just testing)

consump_data= consump_data.assign(Datetime1=consump_data['Datetime'].dt.strftime("%m-%d-%H"))

mean_col = consump_data.groupby('Datetime1')['AEP_MW'].mean()

#append group means by (month,day,hour)
consump_data = consump_data.set_index('Datetime1')
consump_data['average'] = mean_col
consump_data = consump_data.reset_index()

#consump_data = consump_data.assign(baseline_error=abs(consump_data['average'] - consump_data['AEP_MW']))

#np.mean(consump_data['baseline_error'])

#plt.plot(consump_data['Datetime'], consump_data['AEP_MW'], 'b-', label='actual')
#plt.plot(consump_data['Datetime'], consump_data['average'], 'ro', label='baseline prediction')


#Split Columns
features = consump_data.iloc[:,3:10]
features.head()
labels = np.array(consump_data['AEP_MW'])

feature_list = list(features.columns)
features = np.array(features)



#Split Data
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.2, random_state=326)




baseline_preds = test_features[:, feature_list.index('average')]
baseline_errors = abs(baseline_preds - test_labels)

train_features = np.delete(train_features, 5, axis=1)
test_features = np.delete(test_features, 5, axis=1)

print('Average baseline error: ', round(np.mean(baseline_errors), 2))


#Fit Random Forest Model
rf = RandomForestRegressor(n_estimators=1000, random_state=326)


rf.fit(train_features, train_labels);

predictions = rf.predict(test_features)

errors = abs(predictions - test_labels)

np.mean(errors)

mape = 100 * (errors/test_labels)

100 - np.mean(mape)

# Get numerical feature importances
importances = list(rf.feature_importances_)
# List of tuples with variable and importance
feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]
# Sort the feature importances by most important first
feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)
# Print out the feature and importances
[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances];

#test_features[:, feature_list.index('Month')]

