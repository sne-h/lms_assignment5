#Step 7: Feature engineering
#Adding or modifying features can often help improve model performance.


# Title extraction
data['Title'] = data['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)

# Simplify titles
data['Title'] = data['Title'].replace(['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', \
                                       'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
data['Title'] = data['Title'].replace('Mlle', 'Miss')
data['Title'] = data['Title'].replace('Ms', 'Miss')
data['Title'] = data['Title'].replace('Mme', 'Mrs')

# Encode title feature
data = pd.get_dummies(data, columns=['Title'], drop_first=True)

# Drop irrelevant features
data.drop(columns=['Name', 'Ticket'], inplace=True)

# Final dataset overview
print(data.head())
print(data.info())