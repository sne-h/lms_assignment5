#Step 6: Encoding categorical variables
#Categorical variables need to be converted to numerical format. We can use one-hot encoding for this purpose.

# Encode categorical variables
data = pd.get_dummies(data, columns=['Sex', 'Embarked'], drop_first=True)