import pandas as pd
from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules
import time
import tracemalloc

# Load Groceries dataset
def load_groceries_dataset():
    url = 'https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/groceries.csv'
    groceries = pd.read_csv(url, delimiter=',', on_bad_lines='skip')  # Updated error handling
    #print(groceries.head())  # Inspect the first few rows of the DataFrame
    #print(groceries.columns)  # Check the columns in the DataFrame
    return groceries

# Run Apriori Algorithm
def run_apriori(groceries, min_support):
    transactions = groceries.apply(lambda x: x.dropna().tolist(), axis=1).tolist()
    
    # Create a one-hot encoded DataFrame
    basket = pd.DataFrame(columns=pd.Series([item for sublist in transactions for item in sublist]).unique())
    for i, transaction in enumerate(transactions):
        basket.loc[i] = [1 if item in transaction else 0 for item in basket.columns]

    # Start measuring memory usage
    tracemalloc.start()

    # Measure memory usage before running Apriori
    snapshot_before = tracemalloc.take_snapshot()

    # Apply Apriori algorithm
    start_time = time.time()
    frequent_itemsets = apriori(basket, min_support=min_support, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
    end_time = time.time()

    # Measure memory usage after running Apriori
    snapshot_after = tracemalloc.take_snapshot()
    top_stats = snapshot_after.compare_to(snapshot_before, 'lineno')

    # Calculate execution time
    execution_time = end_time - start_time

    return frequent_itemsets, rules, execution_time, top_stats

# Run FP-Growth Algorithm
def run_fpgrowth(groceries, min_support):
    transactions = groceries.apply(lambda x: x.dropna().tolist(), axis=1).tolist()
    
    # Create a one-hot encoded DataFrame
    basket = pd.DataFrame(columns=pd.Series([item for sublist in transactions for item in sublist]).unique())
    for i, transaction in enumerate(transactions):
        basket.loc[i] = [1 if item in transaction else 0 for item in basket.columns]

    # Start measuring memory usage
    tracemalloc.start()

    # Measure memory usage before running FP-Growth
    snapshot_before = tracemalloc.take_snapshot()

    # Apply FP-Growth algorithm
    start_time = time.time()
    frequent_itemsets = fpgrowth(basket, min_support=min_support, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
    end_time = time.time()

    # Measure memory usage after running FP-Growth
    snapshot_after = tracemalloc.take_snapshot()
    top_stats = snapshot_after.compare_to(snapshot_before, 'lineno')

    # Calculate execution time
    execution_time = end_time - start_time

    return frequent_itemsets, rules, execution_time, top_stats

# Load dataset and run both algorithms
groceries = load_groceries_dataset()
min_support_apriori = 0.01

# Run Apriori
frequent_itemsets_apriori, rules_apriori, exec_time_apriori, memory_stats_apriori = run_apriori(groceries, min_support_apriori)

# Run FP-Growth
frequent_itemsets_fpgrowth, rules_fpgrowth, exec_time_fpgrowth, memory_stats_fpgrowth = run_fpgrowth(groceries, min_support_apriori)

# Print results
print("\n--- Apriori Results ---")
print("Frequent Itemsets:")
print(frequent_itemsets_apriori)
print("\nAssociation Rules:")
print(rules_apriori)
print(f"\nExecution Time: {exec_time_apriori:.2f} seconds")
print("\nMemory Usage (Top 10):")
for stat in memory_stats_apriori[:10]:
    print(stat)

print("\n--- FP-Growth Results ---")
print("Frequent Itemsets:")
print(frequent_itemsets_fpgrowth)
print("\nAssociation Rules:")
print(rules_fpgrowth)
print(f"\nExecution Time: {exec_time_fpgrowth:.2f} seconds")
print("\nMemory Usage (Top 10):")
for stat in memory_stats_fpgrowth[:10]:
    print(stat)
