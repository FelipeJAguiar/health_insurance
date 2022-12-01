# pa_hi

## A project that predicts the number of potential customers for an insurance company's new product.

#### This project was made by Felipe Aguiar.

# 1. Business Problem.
Insurance All is a health insurance company that is looking for expand its business, introducing in the market a new product: a car insurance. To understand how potential customers' buying propensity works and optimizing contact process, the sales center requested for a data solution based on a recently research made by the departament. 
So the business problem is:
Provide a rank of clients that have more propensity to purchase a car insurance, making the less number of calls possible. 

# 2. Business Assumptions.
Some questions to understand and quantify business assumptions related with model performance, were made by the sales center:

1 - What percentage of interested customers, could the sales center contact by calling 20,000?
2 - What percentage of interested customers, could the sales center contact by calling 40,000?
3 - To contact 80% of interested customers, how many calls does the center sales needs to make?

# 3. Solution Strategy

My strategy to solve this challenge was:

**Step 01. Data Description:**Analyse descriptive statistic, data types, NA values, null values, dataset dimensions and others data attributes;

**Step 02. Feature Engineering:**Modify data values and creating new feature to improve the model; 

**Step 03. Data Filtering:**Filter dataset useless rows and/or columns;

**Step 04. Exploratory Data Analysis:**Explore dataset to understand variables impact. Look for univariate (each variable), bivariate (relations between two variables) and multivariate (correlation between all variables) analyses;

**Step 05. Data Preparation:**Prepare data to apply the model;

**Step 06. Feature Selection:**Select most importance features to apply the model;

**Step 07. Machine Learning Modelling:**Train machine learning models and evaluate it with metrics;  

**Step 08. Hyperparameter Fine Tunning:**Find the best hyperparamters for the model choose;

**Step 09. Convert Model Performance to Business Values:**Traduce model perfomance to business values;

**Step 10. Deploy Model to Production:**Make the model available in real time (cloud) to anyone use. 

# 4. Top 3 Data Insights

**Hypothesis 01:**Owners of newers vehicles are more interested in taking out insurance.

**FALSE:**Owners of vehicles that are between 1 and 2 years, are the most interested in taking out insurance.

**Hypothesis 02:**Young people are less interested in taking out insurance.

**TRUE:**Young people (age less than 30 years old) are less interested in taking out insurance, comparing with other ages (old and middle ages).

**Hypothesis 03:**Customers that have between 200 to 299 days contract time, are more interested in taking out insurance.

**TRUE:**Customers that have 200 days or more contract time, are more interested in taking out insurance, comparing others customers.

# 5. Machine Learning Model Applied

Being a Learn to Rank (rank propensity score for each customer) problem, some classifier models were tested: KNN, Logistic Regression, Extra Trees, Random Forest, XGBoost and LGBM. The next topic shows the results.

Below, the metrics for each model trained:

|Model Name		       |PRECISION @K		  |RECALL @K  	|PRECISION @K CV  |RECALL	@K CV  |
|--------------------|------------------|-------------|-----------------|--------------|
|KNN 	               |0.348 	          |0.047        |0.342            |0.057         |
|Logistic Regression |0.303             |0.041        |0.305            |0.051         |
|Extra Trees			   |0.346	            |0.047        |0.332            |0.055         |
|Random Forest	     |0.346 	          |0.047	      |0.357            |0.060         |
|XGBoost          	 |0.452             |0.061	      |0.416            |0.069         |
|LGBM	               |0.460 	          |0.062	      |0.425            |0.071         |

According metrics obtained, the model choose was LGBM. In addition other factors that motivated the choice were, the LGBM being a small size model, which requires less storage use and makes applying it more agile.

Ps.: For the results in table were used k=1000 just to evaluate and comparing the models.

# 6. Machine Learning Model Performance
After LGBM be the applied model chosen, the next step is to adjust the hyperparameters. To do it, was used Optuna, a python library that find the best hyperparameters for the model.

|Model Name		       |PRECISION @K		  |RECALL @K  	|
|--------------------|------------------|-------------|
|LGBM Tuned          |0.470 	          |0.063        |

Note that in this case, the gains comparing tuned and not tuned model, were not satisfactory.

# 7. Business Results

<b>1 - What percentage of interested customers, could the sales center contact by calling 20,000?</b>

<b>2- What percentage of interested customers, could the sales center contact by calling 40,000?</b>

<b>3 - To contact 80% of interested customers, how many calls does the center sales needs to make?</b>

# 8. Conclusions

# 9. Lessons Learned

# 10. Next Steps to Improve

# LICENSE

# All Rights Reserved - Comunidade DS 2022
"# health_insurance" 
