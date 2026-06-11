import pandas as pd
import matplotlib.pyplot as plt
import os
os.makedirs("visuals", exist_ok=True)
# Load dataset
df = pd.read_csv("data/Unemployment_india.csv")
# Clean columns
df.columns = df.columns.str.strip()
# Convert date
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
# Chart 1: Unemployment Trend

monthly = df.groupby('Date')['Estimated Unemployment Rate (%)'].mean()

plt.figure(figsize=(12,6))
plt.plot(monthly.index, monthly.values, marker='o')

plt.title("India Unemployment Trend")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.grid(True)

plt.savefig("visuals/unemployment_trend.png")
plt.close()
# Chart 2: Top 10 States

state_avg = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean()
top10 = state_avg.sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
top10.plot(kind='bar')

plt.title("Top 10 States with Highest Unemployment")
plt.xlabel("State")
plt.ylabel("Average Unemployment Rate (%)")

plt.tight_layout()

plt.savefig("visuals/top10_states.png")
plt.close()

# Chart 3: Rural vs Urban

area_avg = df.groupby('Area')['Estimated Unemployment Rate (%)'].mean()

plt.figure(figsize=(6,5))
area_avg.plot(kind='bar')

plt.title("Rural vs Urban Unemployment")
plt.ylabel("Average Unemployment Rate (%)")

plt.tight_layout()

plt.savefig("visuals/rural_vs_urban.png")
plt.close()

# Chart 4: COVID Impact

before_covid = df[df['Date'] < '2020-03-01']
during_covid = df[df['Date'] >= '2020-03-01']

comparison = pd.DataFrame({
    'Period': ['Before COVID', 'During COVID'],
    'Rate': [
        before_covid['Estimated Unemployment Rate (%)'].mean(),
        during_covid['Estimated Unemployment Rate (%)'].mean()
    ]
})

plt.figure(figsize=(6,5))
plt.bar(comparison['Period'], comparison['Rate'])

plt.title("COVID Impact on Unemployment")
plt.ylabel("Average Unemployment Rate (%)")

plt.savefig("visuals/covid_impact.png")
plt.close()
# Chart 5: Labour Participation

labour = df.groupby('Date')[
    'Estimated Labour Participation Rate (%)'
].mean()

plt.figure(figsize=(12,6))
plt.plot(labour.index, labour.values, marker='o')

plt.title("Labour Participation Trend")
plt.xlabel("Date")
plt.ylabel("Participation Rate (%)")

plt.grid(True)

plt.savefig("visuals/labour_participation.png")
plt.close()
# Insights

print("\n----- PROJECT INSIGHTS -----")

print(
    f"\nAverage Unemployment Before COVID: "
    f"{before_covid['Estimated Unemployment Rate (%)'].mean():.2f}%"
)

print(
    f"Average Unemployment During COVID: "
    f"{during_covid['Estimated Unemployment Rate (%)'].mean():.2f}%"
)

print("\nTop 5 States with Highest Unemployment:")
print(top10.head())

print("\nAll charts saved in visuals folder!")