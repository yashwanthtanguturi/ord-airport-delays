import pandas as pd

airport_df = pd.read_csv('data/ORD_flights_june2026.csv')

print(airport_df.shape)
print(airport_df.head())
print(airport_df['ORIGIN_AIRPORT_ID'].unique()[:10])
