# AprioriVsFP-Growth
Comparing the frequent pattern mining algorithms - Apriori & FP-Growth


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

The grocery dataset consists of transactions made by multiple customers at a supermarket, with details of items bought together in one purchase. Each of the entries in the dataset represent a basket of items (milk, eggs, bread etc. among others)– this sort of data analysis usually gives interesting information on customer buying behavior through market basket analysis. The data set is a csv file with transactions of items separated by commas and the number of items across transactions is non uniform as different customers could buy different number of items. To preprocess the data, I created a one-hot encoded dataframe with the transactions represented as rows and the items as the columns in the dataframe, while the binary format (1 or 0) is used to represent if the particular item is bought in a particular transaction. Additionally, the entire data is completely transactional, no numerical data (number of items bought, cost etc.) is given. Hence, no further processing was necessary. The SNS (Social Networking Site) dataset represents user interaction related to their interests across various social activities such as dance, basketball, smoking etc. among others is curated. It is a CSV file with each row representing a particular users’ interests while each column corresponds to the social activity. As these algorithms function on binary dataset, I used one-hot encoded dataframe to convert this data into 1s and 0s as well with 1 indicating the user is interested in the activity and 0 indicating not interested while replacing empty values with None.


IMPLEMENTATION:

1.	Programming Language: Python
2.	Libraries Used:
-	Pandas: used for loading and processing the dataset
-	mlxtend.frequent_patterns : To implement the apriori, fpgrowth, and association_rules functions for frequent pattern mining
-	time : To measure the execution time
-	tracemalloc : To track usage of memory
3.	Source Code:
-	Files saves as apvsfp1.py and apvsfp2.py in the zip file submitted. 
4.	Steps to Run the files:
-	Install required packages (if not already installed): Pandas, mlxtend (pip install pandas mlxtend).
-	Run the source codes: python <filename.py> The dataset is accessed through the URL over the public internet and hence need not be downloaded on local machine for the implementation. 
5.	Threshold for Support:
The threshold refers to the minimum support configured to test against both the algorithms. In the source code, this is set as 0.01 when the functions are called. This means the minimum support threshold is 0.01, or 1%. The frequency of the items must be at least 1% to be considered as a frequent dataitem, else the dataitem is discarded. 


EXPECTED OUTPUTS:

1.	 Frequent Itemsets
The items which are noted to be frequently generated through the dataset, along with the support (frequency).
2.	Apriori Rules
Associations between the frequent itemsets is returned along with the support and other metrics explained earlier (leverage, conviction, zhangs_metric).
3.	Execution Time:
The time taken by each algorithm is returned in seconds. 
4.	Memory usage:
Returns a list of top 10 most memory consumption of the lines in both algorithms, in descending order. 




