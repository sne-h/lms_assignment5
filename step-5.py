#Step 5: Normalization
#Normalization is crucial for certain machine learning algorithms. We'll normalize numerical features like 'Age' and 'Fare'.


from sklearn.preprocessing import StandardScaler

# Normalize 'Age' and 'Fare'
scaler = StandardScaler()
data[['Age', 'Fare']] = scaler.fit_transform(data[['Age', 'Fare']])