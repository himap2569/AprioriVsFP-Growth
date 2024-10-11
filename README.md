# AprioriVsFP-Growth
Comparing the frequent pattern mining algorithms - Apriori & FP-Growth

CONTEXT & TERMINOLOGY:

Frequent pattern mining algorithms are designed to discover patterns, associations, correlations, or commonly occuring combinations among large data sets of items in transactional databases, relational databases, or other data repositories. These algorithms have become very important in data mining, finding considerable application in market basket analysis to identify products frequently appearing in the same transaction.

In this assignment, we implement most commonly used frequent pattern mining algorithms - Apriori and Frequent Pattern Growth (FP-Growth) and compare the results in terms of execution time and memory usage.
  
Apriori Algorithm: This uses prior knowledge of frequent itemset properties. Frequent itemsets are items in a dataset that appear together in a certain frequency. This frequency of the items is termed as "Support". Support represents the number of times a certain item occurred throughout the entire dataset. For example, in the output if the support for a certain item is given as 0.03, it implies that the dataset comprises 3% of this particular item.

Apriori Algorithm also returns apriori rules - which represents the popular combinations that frequently occurred together in the dataset. Suppose A->B is an apriori rule, 'A' in this relationship is called 'Antecedent' whereas 'B' is termed as 'Consequent'. For such rules, we measure the following metrics through this algorithm:

a) Antecedent Support: The frequency of the combination of A,B occuring together is termed as 'Antecednt support'.

b) Leverage: It represents the coincidence of apriori relationships. A higher leverage implies stronger relationship (i.e., more likely that the two items occur together and its not a mere coincidence). This metric is calculated by calculating the difference between the observed co-occurrence and the expected co-occurrence of the antecedents and the consequents. 

c) Conviction: Measured by the ratio of the number of occurrences of antecedents and the number  of occurrences of the antecedents and the consequents combined together. If the ratio is greater than 1, it implies a positive relationship - higher chances of the combination of items occurrin together. If the ratio is equal to 1, no  meaning inference can be deduced from the relationship. Whereas if the ratio is less than 1, then it implies that the occurrences in that combination is less likely to appear together in the dataset.  

d) Zhangs_metric: This measures the strength of the relationship as well by evaluating the chances of occurrences of the consequent when the antecednet occurs and when it does not. This is calculated by dividing the probability of both the antecedent and consequent occurring together by the product of their individual probabilities,

These metrics together help evalute the strength of apriori relationships, henceg giving meaningful interepretation from the datasets.

FP-Growth Algorithm: While FP-Growth essentially returns the same results and outputs are evaluated using the same metrics (support, leverage, conviction, zhang_metrics) , the key  difference between these algorithms is the relative efficiency improvement in the FP-Growth algorithm. In the Apriori algorithm, the algorithm scans the entire database at each step to select the candidate sets, making it inefficient and signficantly slow. FP-Growth algorithm  efficiently overcomes these drawbacks by implementing a trie data structure storing the items and its frequency in a key-value set and in descending order while removing those below a specified minimum support threshold.Here, each transaction is represented as a path in the tree, where nodes are items, and edges indicate the presence of items in a transaction. Nodes are linked together to represent common prefixes, allowing for a compact representation of the dataset. The frequent patterns are then mined from this data structure. Here, the entire datset is parsed only once making it faster than apriori as the dataset in that case is parsed large number of times, making the FP-Growth algorithm more appropriate for large-scale data sets. 

DATASETS:

For this implementaion, we consider two datasets to effectively compare both the algorithms:

1. Open source Grocery Dataset (9835 entries) -  https://github.com/stedy/Machine-Learning-with-R-datasets/blob/master/groceries.csv

and another larger dataset  (x3) 

2. Open source SNS data (30,003 entries) - https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/refs/heads/master/snsdata.csv




