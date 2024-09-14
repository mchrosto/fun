import pandas as pd 


city_df = {
    'city_id': [1, 2, 3, 4, 5],
    'city_name': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'city_population': [8419000, 3980000, 2716000, 2328000, 1690000]
}

# Create the DataFrame
cities = pd.DataFrame(city_df)

# Set the city_id as the primary key
cities.set_index('city_id', inplace=True)

# Display the DataFrame
print(cities)


import pandas as pd

# Define the data for the mayors DataFrame
mayors_data = {
    'city_id': [1, 2, 3, 4, 5],
    'mayor_name': ['Eric Adams', 'Karen Bass', 'Brandon Johnson', 'Sylvester Turner', 'Kate Gallego'],
    'age': [63, 70, 47, 69, 41],
    'gender': ['Male', 'Female', 'Male', 'Male', 'Female'],
    'years_in_office': [2, 1, 1, 7, 4]  # Years in office as of 2024
}

# Create the DataFrame
mayors = pd.DataFrame(mayors_data)

# Display the DataFrame
print(mayors)``


#joining mayors with cities 

city_mayor_combo = pd.merge(cities, mayors, how='left', on='city_id')
print(city_mayor_combo)


