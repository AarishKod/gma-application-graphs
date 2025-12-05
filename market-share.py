import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
df = pd.read_csv('Book1.csv')

# Extract the years (first column)
years = df.iloc[:, 0]

# Extract Korea and China data, convert percentages to floats
korea = df['Korea'].str.rstrip('%').astype(float)
china = df['China'].str.rstrip('%').astype(float)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot lines for both countries
plt.plot(years, korea, marker='o', linewidth=2.5, markersize=8, 
         color='#0047AB', label='South Korea', linestyle='-')
plt.plot(years, china, marker='s', linewidth=2.5, markersize=8, 
         color='#DE2910', label='China', linestyle='-')

# Customize the plot
plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Global Market Share (%)', fontsize=12, fontweight='bold')
plt.title('Global Shipbuilding Market Share: South Korea vs China (2000-2024)', 
          fontsize=14, fontweight='bold', pad=20)

# Set y-axis range
plt.ylim(0, 80)

# Add grid for better readability
plt.grid(True, alpha=0.3, linestyle='--')

# Add legend
plt.legend(loc='best', fontsize=11, framealpha=0.9)

# Format x-axis to show all years
plt.xticks(years, rotation=0)

# Add percentage signs to y-axis
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{int(y)}%'))

# Tight layout to prevent label cutoff
plt.tight_layout()

# EXPORT OPTIONS:

# Option 1: PNG (best for one-pagers, presentations)
plt.savefig('korea_china_shipbuilding.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')

print("Chart saved successfully!")

# Display the plot (optional - comment out if you just want to save)
plt.show()