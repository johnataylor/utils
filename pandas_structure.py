import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['London', 'Paris', 'Berlin']
}

df = pd.DataFrame(data)
print(df)
