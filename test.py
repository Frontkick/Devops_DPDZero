import pandas as pd

# Sample DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
}
df = pd.DataFrame(data, index=['a', 'b', 'c'])


df.loc['b']     # Gets the row with label 'b'
print(df.iloc[1])     # Gets the second row (index 1)
ls