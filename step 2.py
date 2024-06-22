#Step 2: Initial exploration and cleaning
#We will explore the dataset to understand its structure and look for any initial cleaning requirements.


# Display basic information
print(data.info())

# Display summary statistics
print(data.describe())

# Check for duplicates
data = data.drop_duplicates()