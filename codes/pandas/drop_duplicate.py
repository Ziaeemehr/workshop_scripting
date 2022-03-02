import pandas as pd
df = pd.DataFrame({
    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 3.5, 15, 5]
})

print(df) 

print("")

print(df.drop_duplicates())

print("")

print(df.drop_duplicates(subset=['brand']))

print("")

print(df.drop_duplicates(subset=['brand', 'style'], keep='last'))