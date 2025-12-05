import matplotlib.pyplot as plt
import pandas as pd

# Read the file
df = pd.read_csv('Book1.csv')

# Extract the years
years = df.iloc[:, 0]

# convert percentages to floats
korea = df['Korea'].str.rstrip('%').astype(float)
china = df['China'].str.rstrip('%').astype(float)

# create plot
plt.figure(figsize=(10, 6))

# Plot lines
plt.plot(years, korea, marker='o', linewidth=2.5, markersize=8, 
         color='#0047AB', label='South Korea', linestyle='-')
plt.plot(years, china, marker='s', linewidth=2.5, markersize=8, 
         color='#DE2910', label='China', linestyle='-')

# misc
plt.xlabel('Year', fontsize=12, fontweight='bold')
plt.ylabel('Global Market Share (%)', fontsize=12, fontweight='bold')
plt.title('Global Shipbuilding Market Share: South Korea vs China (2000-2024)', 
          fontsize=14, fontweight='bold', pad=20)
plt.ylim(0, 80)

# styling
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(loc='best', fontsize=11, framealpha=0.9)
plt.xticks(years, rotation=0)
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{int(y)}%'))
plt.tight_layout()

plt.savefig('korea_china_shipbuilding.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')

print("Chart saved successfully!")
plt.show()
