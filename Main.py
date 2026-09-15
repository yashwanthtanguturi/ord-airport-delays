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

# convert the FL_DATE into a datetime to then extract the dates from the week
airport_df['FL_DATE'] = pd.to_datetime(airport_df['FL_DATE'])
airport_df['DAY_OF_WEEK'] = airport_df['FL_DATE'].dt.day_name()


# delay by day of the week
dow_delay = airport_df.groupby('DAY_OF_WEEK')['DEP_DELAY'].mean()

# Reorder to go monday -> sunday instead of alphabetical
day_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
dow_delay = dow_delay.reindex(day_order)

print(dow_delay)

# bar chart for day of week delay
plt.figure(figsize=(10, 6))
sns.barplot(x=dow_delay.index, y=dow_delay.values)
plt.title('Average Departure Delay by Day of Week (ORD, June 2026)')
plt.xlabel('Day of Week')
plt.ylabel('Average Delay (minutes)')
plt.tight_layout()
plt.show()

airport_df['IS_DELAYED'] = (airport_df['DEP_DELAY'] > 15).astype(int)
print(airport_df['IS_DELAYED'].value_counts())
print(airport_df['IS_DELAYED'].value_counts(normalize=True))

# feature engineering: one-hot encode categorical columns
features = pd.get_dummies(airport_df[['OP_UNIQUE_CARRIER', 'DAY_OF_WEEK']], drop_first=True)

print(features.head())
print(features.shape)
# X = features (inputs), y = target (what we're predicting)
X = features
y = airport_df['IS_DELAYED']

print(X.shape, y.shape)  # should have matching row counts