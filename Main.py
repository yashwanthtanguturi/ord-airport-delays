import pandas as pd


# making the dataframe for the data
airport_df = pd.read_csv('data/ORD_flights_june2026.csv')

print(airport_df.shape)
print(airport_df.head())
print(airport_df['ORIGIN_AIRPORT_ID'].unique()[:10])


# filtering and cleaning the data up
cols = ['FL_DATE', 'OP_CARRIER', 'DEP_DELAY', 'ORIGIN_AIRPORT_ID', 'DEST_AIRPORT_ID']
airport_df = airport_df[cols]
airport_df = airport_df.dropna(subset=['DEP_DELAY'])

print(airport_df.shape)
