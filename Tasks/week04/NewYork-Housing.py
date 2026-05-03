import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

####################################
'''cd into week04 directory first'''
####################################

# ==========================================
# 1. Load and Filter CSV Data (Pandas)
# ==========================================
# Load the dataset
df = pd.read_csv('NY-House-Dataset.csv')

# Create the 'Price per Sqft' column if it doesn't already exist
if 'Price per Sqft' not in df.columns:
    df['Price per Sqft'] = df['PRICE'] / df['PROPERTYSQFT']

# This removes the extreme properties that are squashing your chart
df = df[df['Price per Sqft'] < 30000]

# Filter data: drop missing values in key columns to ensure clean plotting
df = df.dropna(subset=['LATITUDE', 'LONGITUDE', 'Price per Sqft'])



# Calculate overall Min and Max for context
min_price_sqft = df['Price per Sqft'].min()
max_price_sqft = df['Price per Sqft'].max()
print(f"Price per Sqft - Min: ${min_price_sqft:.2f}, Max: ${max_price_sqft:.2f}\n")


# ==========================================
# 2. Charts with Price, Longitude, and Latitude
# ==========================================
# Create side-by-side subplots
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Left Plot: Longitude vs. Price per Sqft (Red)
axes[0].scatter(df['LONGITUDE'], df['Price per Sqft'], color='red', alpha=0.8)
axes[0].set_title('Longitude vs. Price per Sqft')
axes[0].set_xlabel('Longitude')
axes[0].set_ylabel('Price per Sqft')
axes[0].grid(True, linestyle='--', alpha=0.6)

# Right Plot: Latitude vs. Price per Sqft (Blue)
axes[1].scatter(df['LATITUDE'], df['Price per Sqft'], color='blue', alpha=0.8)
axes[1].set_title('Latitude vs. Price per Sqft')
axes[1].set_xlabel('Latitude')
axes[1].set_ylabel('Price per Sqft')
axes[1].grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()


# ==========================================
# 3. Create Price Bins (0 to 4)
# ==========================================
# Use pandas qcut to divide the data into 5 equal-sized quantile bins
df['Price_Bin'], bin_edges = pd.qcut(df['Price per Sqft'], q=5, labels=[0.0, 1.0, 2.0, 3.0, 4.0], retbins=True)

# Print the bin ranges to match the provided image
print("Price per Sqft Bins:")
for i in range(5):
    print(f"Bin {i}: ${bin_edges[i]:.2f} - ${bin_edges[i+1]:.2f}")


# ==========================================
# 4. Latitude & Longitude Scatter Plot by Bin
# ==========================================
plt.figure(figsize=(12, 6))
sns.scatterplot(
    data=df, 
    x='LONGITUDE', 
    y='LATITUDE', 
    hue='Price_Bin', 
    palette='crest', # 'crest' or 'viridis' matches the green/blue scale shown
    s=30,
    edgecolor=None
)
plt.title('Property Locations Colored by Price Bin')
plt.xlabel('LONGITUDE')
plt.ylabel('LATITUDE')
plt.legend(title='Price Bin')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


# ==========================================
# 5. Interactive Map: Cheapest Apartments
# ==========================================
# Filter for the cheapest apartments (Bin 0)
cheapest_apartments = df[df['Price_Bin'] == 0.0]

# Initialize a Folium map centered around the average location of these apartments
map_center = [cheapest_apartments['LATITUDE'].mean(), cheapest_apartments['LONGITUDE'].mean()]
nyc_map = folium.Map(location=map_center, zoom_start=11)

# Add markers for the cheapest apartments
# Note: If the dataset is very large, consider plotting a sample (e.g., .head(200)) to prevent the map from freezing
for index, row in cheapest_apartments.iterrows():
    folium.Marker(
        location=[row['LATITUDE'], row['LONGITUDE']],
        tooltip=f"Price/Sqft: ${row['Price per Sqft']: .2f}"
    ).add_to(nyc_map)

# Display the map (In Jupyter Notebooks, simply calling the object renders the interactive map)
nyc_map