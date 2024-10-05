import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

df2 = pd.DataFrame({
    'A': [7, 8, 9],
    'B': [10, 11, 12]
})

# Concatenate by rows (axis=0)
result = pd.concat([df1, df2], axis=0)

s = 'jasd jasdj DASF asdf'
print(s.replace(' ','').lower())
