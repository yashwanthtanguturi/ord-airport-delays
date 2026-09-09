import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# making the dataframe for the data
airport_df = pd.read_csv('data/ORD_flights_june2026.csv')
print(airport_df.columns.tolist())

print(airport_df.shape)
print(airport_df.head())
print(airport_df['ORIGIN_AIRPORT_ID'].unique()[:10])


# filtering and cleaning the data up
cols = ['FL_DATE', 'OP_UNIQUE_CARRIER', 'DEP_DELAY', 'ORIGIN_AIRPORT_ID', 'DEST_AIRPORT_ID']
airport_df = airport_df[cols]
airport_df = airport_df.dropna(subset=['DEP_DELAY'])
print(airport_df.shape)

# delay by carrier
carrier_delay = airport_df.groupby('OP_UNIQUE_CARRIER')['DEP_DELAY'].mean().sort_values(ascending=False)
print(carrier_delay)

# bar chart
plt.figure(figsize=(10, 10))
sns.barplot(x=carrier_delay.index, y=carrier_delay.values)
plt.title('Average departure Delay by Carrier(ORD, June 2026)')
plt.xlabel('Carrier Delay')
plt.ylabel('Average Delay(minutes)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
