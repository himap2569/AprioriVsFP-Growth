import pandas as pd
from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules
import time
import tracemalloc

# Load SNS dataset
def load_sns_dataset():
    url = 'https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/refs/heads/master/snsdata.csv'
    snsdata = pd.read_csv(url, delimiter=',', on_bad_lines='skip')
    #print(snsdata.head())  # Inspect the first few rows of the DataFrame
    #print(snsdata.columns)  # Check the columns in the DataFrame
    return snsdata

# Preprocess dataset into one-hot encoding format (for categorical data only)
def preprocess_sns_data(snsdata):
    # Replace NaN values in categorical columns with 'None'
    snsdata.fillna('None', inplace=True)

    # Select only the categorical columns for analysis (excluding numeric ones like age, friends, etc.)
    categorical_columns = ['basketball', 'football', 'soccer', 'softball', 'volleyball', 'swimming', 'cheerleading',
                           'baseball', 'tennis', 'sports', 'cute', 'sex', 'sexy', 'hot', 'kissed', 'dance', 'band',
                           'marching', 'music', 'rock', 'god', 'church', 'jesus', 'bible', 'hair', 'dress', 'blonde',
                           'mall', 'shopping', 'clothes', 'hollister', 'abercrombie', 'die', 'death', 'drunk', 'drugs']

    basket = snsdata[categorical_columns]
    
    # Convert all values to binary (0 or 1) where any value > 1 is converted to 1
    basket = basket.applymap(lambda x: 1 if int(x) > 0 else 0)
    
    return basket

# Run Apriori Algorithm
def run_apriori(snsdata, min_support):
    basket = preprocess_sns_data(snsdata)

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
def run_fpgrowth(snsdata, min_support):
    basket = preprocess_sns_data(snsdata)

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
snsdata = load_sns_dataset()
min_support_value = 0.01  # Adjust this support value as needed

# Run Apriori
frequent_itemsets_apriori, rules_apriori, exec_time_apriori, memory_stats_apriori = run_apriori(snsdata, min_support_value)

# Run FP-Growth
frequent_itemsets_fpgrowth, rules_fpgrowth, exec_time_fpgrowth, memory_stats_fpgrowth = run_fpgrowth(snsdata, min_support_value)

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
