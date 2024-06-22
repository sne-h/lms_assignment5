#Complete Preprocessing Script
#Here's the entire script for preprocessing

import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv('titanic.csv')

# Initial exploration
print(data.info())
print(data.describe())

# Handle missing values
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data.drop(columns=['Cabin'], inplace=True)

# Feature engineering
data['FamilySize'] = data['SibSp'] + data['Parch'] + 1
data['IsAlone'] = 1
data['IsAlone'].loc[data['FamilySize'] > 1] = 0

# Normalize numerical features
scaler = StandardScaler()
data[['Age', 'Fare']] = scaler.fit_transform(data[['Age', 'Fare']])

# Encode categorical variables
data = pd.get_dummies(data, columns=['Sex', 'Embarked'], drop_first=True)

# Title extraction and simplification
data['Title'] = data['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
data['Title'] = data['Title'].replace(['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', \
                                       'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
data['Title'] = data['Title'].replace('Mlle', 'Miss')
data['Title'] = data['Title'].replace('Ms', 'Miss')
data['Title'] = data['Title'].replace('Mme', 'Mrs')
data = pd.get_dummies(data, columns=['Title'], drop_first=True)

# Drop irrelevant features
data.drop(columns=['Name', 'Ticket'], inplace=True)

# Final dataset overview
print(data.head())
print(data.info())
