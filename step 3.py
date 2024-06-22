#Step 3: Handling missing values
#We'll identify columns with missing values and decide on an appropriate strategy to handle them.

# Check for missing values
print(data.isnull().sum())

# Fill missing values for 'Age' with median
data['Age'].fillna(data['Age'].median(), inplace=True)

# Fill missing values for 'Embarked' with mode
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)

# Drop 'Cabin' column due to high number of missing values
data.drop(columns=['Cabin'], inplace=True)