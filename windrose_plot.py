import pandas as pd
import matplotlib.pyplot as plt
from windrose import WindroseAxes
import numpy as np
import matplotlib.image as mpimg
from matplotlib import cm

# Read the Excel file
df = pd.read_excel('US-Bi2_Windrose.xlsx')

# Create figure with transparent background
fig = plt.figure(figsize=(10, 8), facecolor='none')
fig.patch.set_alpha(0.0)

# Read and display the site image
site_img = mpimg.imread('Bi2_Image_2.png')
plt.imshow(site_img)
plt.axis('off')  # Hide image axes

# Create windrose plot with transparent background
ax = WindroseAxes.from_ax(fig=fig, rect=[0.185, 0.17, 0.6, 0.6])  # Fine-tuned left and upward position
ax.patch.set_alpha(0.7)  # Make the windrose background semi-transparent

# Use a bright, vivid colormap
cmap = plt.cm.turbo  # Brighter and more modern
n_bins = 8  # Keep the number of bins as before

# Plot the windrose with semi-transparent bars and bright colors
ax.bar(df['WD'], df['WS'], 
       normed=True, opening=0.8, edgecolor='white', alpha=0.7,
       cmap=cmap, nsector=16, calm_limit=0.0, bins=n_bins)

# Customize the plot
ax.set_legend(title='Wind Speed (m/s)', bbox_to_anchor=(1.05, 0.02))  # Further down in bottom right corner
# plt.title('Windrose Plot - Growing Season (May-September) at 11:30 AM\nStation Location: 38.1091°N, 121.5351°W')

# Change the color of the outer ring and direction labels to white, larger, and bold
ax.set_xticklabels(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'], color='white', fontsize=16, fontweight='bold')
# Set radial (r) tick labels to white, larger, and bold
ax.set_yticklabels([str(int(label)) for label in ax.get_yticks()], color='white', fontsize=14, fontweight='bold')
# Set grid lines to white and thicker
ax.yaxis.grid(True, color='white', linestyle='-', linewidth=2)
ax.xaxis.grid(True, color='white', linestyle='-', linewidth=2)
# Set spines to white and thicker
for spine in ax.spines.values():
    spine.set_color('white')
    spine.set_linewidth(2)
ax.tick_params(colors='white', width=2)

# Save the plot with transparent background
plt.savefig('windrose_plot_with_map.png', dpi=300, bbox_inches='tight', transparent=True)
plt.close() 