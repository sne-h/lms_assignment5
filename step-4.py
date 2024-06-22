#Step 4: Transformation
#We may need to transform some features, such as creating new features from existing ones.


# Create a new feature 'FamilySize' from 'SibSp' and 'Parch'
data['FamilySize'] = data['SibSp'] + data['Parch'] + 1

# Create a new feature 'IsAlone' based on 'FamilySize'
data['IsAlone'] = 1
data['IsAlone'].loc[data['FamilySize'] > 1] = 0