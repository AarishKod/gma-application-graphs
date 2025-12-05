import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read the CSV file
df = pd.read_csv('Book2.csv')

# Clean and extract the data, dropping any rows with missing values
df = df.dropna()

# Extract the years (first column) - now safe to convert to int
years = df.iloc[:, 0].astype(int)

# Extract and clean the data
exports = df['Exports'].str.replace('$', '').str.replace('B', '').astype(float)
lng_share = df['LNG Market Share'].str.rstrip('%').astype(float)

# Create figure with dual y-axes
fig, ax1 = plt.subplots(figsize=(12, 7))

# Plot bars for exports on primary y-axis
color_bars = '#4A90E2'
bars = ax1.bar(years, exports, width=0.6, color=color_bars, alpha=0.7, 
               label='Ship Exports', edgecolor='black', linewidth=0.5)

ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Total Ship Exports (USD Billions)', fontsize=12, fontweight='bold', color=color_bars)
ax1.tick_params(axis='y', labelcolor=color_bars)
ax1.set_ylim(0, max(exports) * 1.15)

# Create secondary y-axis for LNG market share
ax2 = ax1.twinx()
color_line = '#E74C3C'
line = ax2.plot(years, lng_share, marker='o', linewidth=3, markersize=10, 
                color=color_line, label='LNG Carrier Market Share', linestyle='-')

ax2.set_ylabel('LNG Carrier Market Share (%)', fontsize=12, fontweight='bold', color=color_line)
ax2.tick_params(axis='y', labelcolor=color_line)
ax2.set_ylim(0, 80)

# Add percentage signs to right y-axis
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{int(y)}%'))

# Title
plt.title("South Korea Ship Exports & LNG Carrier Dominance (2020-2024)", 
          fontsize=14, fontweight='bold', pad=20)

# Add grid for better readability
ax1.grid(True, alpha=0.2, linestyle='--', axis='y')

# Combine legends from both axes
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10, framealpha=0.9)

# Format x-axis
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=0)

# Add value labels on top of bars
for i, (year, export, share) in enumerate(zip(years, exports, lng_share)):
    ax1.text(year, export + 0.5, f'${export:.1f}B', 
             ha='center', va='bottom', fontsize=9, fontweight='bold')

# Tight layout
plt.tight_layout()

# Save the figure
plt.savefig('korea_exports_lng_share.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')

print("Chart saved successfully as 'korea_exports_lng_share.png'!")

# Display the plot
plt.show()