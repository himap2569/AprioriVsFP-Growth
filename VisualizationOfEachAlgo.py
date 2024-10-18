import pandas as pd
import matplotlib.pyplot as plt

# Sample data for Apriori and FP-Growth
apriori_data = {
    'conviction': [1.289730, 1.302793, 1.168068, 1.095021, 1.277314],
    'zhangs_metric': [0.647326, 0.643754, 0.479208, 0.511776, 0.578360]
}

fpgrowth_data = {
    'conviction': [1.066093, 1.211632, 1.142655, 1.115553, 1.184142],
    'zhangs_metric': [0.322939, 0.230509, 0.343716, 0.359283, 0.448439]
}

# Convert to DataFrames
apriori_df = pd.DataFrame(apriori_data)
fpgrowth_df = pd.DataFrame(fpgrowth_data)

# Set up subplots for visualizing the comparisons
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Bar Plot: Conviction Comparison
axes[0, 0].bar(range(len(apriori_df)), apriori_df['conviction'], color='b', width=0.4, label='Apriori', align='center')
axes[0, 0].bar([x + 0.4 for x in range(len(fpgrowth_df))], fpgrowth_df['conviction'], color='r', width=0.4, label='FP-Growth', align='center')
axes[0, 0].set_title('Conviction Comparison')
axes[0, 0].set_ylabel('Conviction')
axes[0, 0].legend()

# Bar Plot: Zhang's Metric Comparison
axes[0, 1].bar(range(len(apriori_df)), apriori_df['zhangs_metric'], color='b', width=0.4, label='Apriori', align='center')
axes[0, 1].bar([x + 0.4 for x in range(len(fpgrowth_df))], fpgrowth_df['zhangs_metric'], color='r', width=0.4, label='FP-Growth', align='center')
axes[0, 1].set_title("Zhang's Metric Comparison")
axes[0, 1].set_ylabel("Zhang's Metric")
axes[0, 1].legend()

# Scatter Plot: Conviction vs Zhang's Metric
axes[1, 0].scatter(apriori_df['conviction'], apriori_df['zhangs_metric'], color='blue', label='Apriori', s=100, marker='o')
axes[1, 0].scatter(fpgrowth_df['conviction'], fpgrowth_df['zhangs_metric'], color='red', label='FP-Growth', s=100, marker='x')
axes[1, 0].set_title("Conviction vs Zhang's Metric")
axes[1, 0].set_xlabel('Conviction')
axes[1, 0].set_ylabel("Zhang's Metric")
axes[1, 0].legend()

# Line Plot: Conviction Trend
axes[1, 1].plot(range(len(apriori_df)), apriori_df['conviction'], color='blue', label='Apriori', marker='o', linestyle='-', linewidth=2)
axes[1, 1].plot(range(len(fpgrowth_df)), fpgrowth_df['conviction'], color='red', label='FP-Growth', marker='x', linestyle='--', linewidth=2)
axes[1, 1].set_title('Conviction Trend Comparison')
axes[1, 1].set_ylabel('Conviction')
axes[1, 1].legend()

# Adjust layout for better spacing
plt.tight_layout()
plt.show()
