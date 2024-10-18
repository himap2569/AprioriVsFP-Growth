import matplotlib.pyplot as plt
import pandas as pd

# Sample data for visualization
# Ensure that Apriori and FP-Growth results include all metrics for both datasets

# Grocery dataset metrics

grocery_data = {
    'Itemsets': ['(yogurt)', '(tropical fruit)', '(coffee)', '(whole milk)', '(pip fruit)'],
    'Association Rules': ['(Milk-Vegetables)', '(Roll/buns - Soda)', '(Water-Soda)', '(Sausage-Rolls/Buns)', 'Bread-Milk'],
    'Apriori Support': [0.062899, 0.039803, 0.033743, 0.140704, 0.030958],
    'FP-Growth Support': [0.072, 0.045, 0.035, 0.150, 0.028],
    'Apriori Conviction': [1.02, 1.01, 1.04, 1.06,1.10],
    'FP-Growth Conviction': [1.02, 1.01, 1.04, 1.06,1.10],
    'Apriori Zhang': [0.18, 1.02, 1.04, 1.2, 1.4],
    'FP-Growth Zhang': [0.18, 1.02, 1.04, 1.2, 1.4],
}

# SNS dataset metrics
sns_data = {
    'Itemsets': ['(basketball)', '(football)', '(soccer)', '(softball)', '(dance)'],
    'Apriori Support': [0.160333, 0.164967, 0.103267, 0.080067, 0.220633],
    'FP-Growth Support': [0.220633, 0.443700, 0.263200, 0.224467, 0.205667],
    'Apriori Conviction': [2.1, 2.5, 1.8, 1.6, 2.2],
    'FP-Growth Conviction': [2.0, 2.3, 1.9, 1.5, 2.1],
    'Apriori Zhang': [0.6, 0.5, 0.55, 0.45, 0.65],
    'FP-Growth Zhang': [0.65, 0.55, 0.5, 0.4, 0.6],
}

# Create DataFrames
grocery_df = pd.DataFrame(grocery_data)
sns_df = pd.DataFrame(sns_data)

# Plotting
plt.figure(figsize=(18, 6))

# Grocery Dataset
plt.subplot(1, 3, 1)
plt.plot(grocery_df['Itemsets'], grocery_df['Apriori Support'], marker='o', label='Apriori Support', color='b')
plt.plot(grocery_df['Itemsets'], grocery_df['FP-Growth Support'], marker='o', label='FP-Growth Support', color='r')
plt.title('Grocery Dataset - Support Comparison')
plt.xlabel('Itemsets')
plt.ylabel('Support')
plt.xticks(rotation=45)
plt.legend()
plt.grid()

# Grocery Dataset - Conviction
plt.subplot(1, 3, 2)
plt.plot(grocery_df['Association Rules'], grocery_df['Apriori Conviction'], marker='o', label='Apriori Conviction', color='b')
plt.plot(grocery_df['Association Rules'], grocery_df['FP-Growth Conviction'], marker='o', label='FP-Growth Conviction', color='r')
plt.title('Grocery Dataset - Conviction Comparison')
plt.xlabel('Itemsets')
plt.ylabel('Conviction')
plt.xticks(rotation=45)
plt.legend()
plt.grid()

# Grocery Dataset - Zhang's Metric
plt.subplot(1, 3, 3)
plt.plot(grocery_df['Association Rules'], grocery_df['Apriori Zhang'], marker='o', label='Apriori Zhang', color='b')
plt.plot(grocery_df['Association Rules'], grocery_df['FP-Growth Zhang'], marker='o', label='FP-Growth Zhang', color='r')
plt.title('Grocery Dataset - Zhang Metric Comparison')
plt.xlabel('Itemsets')
plt.ylabel('Zhang Metric')
plt.xticks(rotation=45)
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# Now plotting for SNS Dataset

plt.figure(figsize=(18, 6))

# SNS Dataset - Support
plt.subplot(1, 3, 1)
plt.plot(sns_df['Itemsets'], sns_df['Apriori Support'], marker='o', label='Apriori Support', color='b')
plt.plot(sns_df['Itemsets'], sns_df['FP-Growth Support'], marker='o', label='FP-Growth Support', color='r')
plt.title('SNS Dataset - Support Comparison')
plt.xlabel('Itemsets')
plt.ylabel('Support')
plt.xticks(rotation=45)
plt.legend()
plt.grid()

# SNS Dataset - Conviction
plt.subplot(1, 3, 2)
plt.plot(sns_df['Itemsets'], sns_df['Apriori Conviction'], marker='o', label='Apriori Conviction', color='b')
plt.plot(sns_df['Itemsets'], sns_df['FP-Growth Conviction'], marker='o', label='FP-Growth Conviction', color='r')
plt.title('SNS Dataset - Conviction Comparison')
plt.xlabel('Itemsets')
plt.ylabel('Conviction')
plt.xticks(rotation=45)
plt.legend()
plt.grid()

# SNS Dataset - Zhang's Metric
plt.subplot(1, 3, 3)
plt.plot(sns_df['Itemsets'], sns_df['Apriori Zhang'], marker='o', label='Apriori Zhang', color='b')
plt.plot(sns_df['Itemsets'], sns_df['FP-Growth Zhang'], marker='o', label='FP-Growth Zhang', color='r')
plt.title('SNS Dataset - Zhang Metric Comparison')
plt.xlabel('Itemsets')
plt.ylabel('Zhang Metric')
plt.xticks(rotation=45)
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
