# INSURANCE ALL - CROSS SELL

<img src="https://raw.githubusercontent.com/felipejaguiar/health_insurance/main/image/insurance_all.png" alt="logo12" style="zoom:80%;" />

#### This project was based on kaggle's challenge and made by Felipe Aguiar. All context about company are fictitious.

# Business Problem.
Insurance All is a health insurance company looking for expand its business, introducing in the market a new product: a car insurance. To understand how potential customers' buying propensity works and optimizing contact process (limited in 20 thousand calls) , the sales center requested for a data solution based on a recently research made by the departament. 
So the business problem is:

👉 Provide a rank of clients that have more propensity to purchase a car insurance. 

# Business Assumptions
Business assumptions made were divided in two topics: 

1 - Provide a Google Sheets doc that, inputing a customer data, returns customer propensity. 

2 - Answer some questions to understand and quantify business assumptions related with model performance.

   🟪 What percentage of interested customers, could the sales center contact by calling 20,000?
   
   🟪 What percentage of interested customers, could the sales center contact by calling 40,000?
   
   🟪 To contact 80% of interested customers, how many calls does the center sales needs to make?

# Solution Strategy

 ### What is the solution?
 Ranking customers by the car insurance propensity purchase.
 
 ### How to provide the solution?
 Making available a Google Sheets spreadsheet, that rank and show customers by propensity purchase.  

### Strategy to solve this challenge was:

The method used to base the solution project was CRISP cicle, adopting some steps to it. Below an image representing CRISP and steps defined.

<img src="https://raw.githubusercontent.com/felipejaguiar/health_insurance/main/image/fluxogram.png" width="380" height="400" alt="logo" style="zoom:80%;" />

Font: Author, 2022.

Steps explained:

1️⃣ Data Description: Analyse descriptive statistic, data types, NA values, null values, dataset dimensions and others data attributes;

2️⃣ Feature Engineering: Modify data values and creating new feature to improve the model; 

3️⃣ Data Filtering: Filter dataset useless rows and/or columns;

4️⃣ Exploratory Data Analysis: Explore dataset to understand variables impact. Look for univariate (each variable), bivariate (relations between two variables) and multivariate (correlation between all variables) analyses;

5️⃣ Data Preparation: Prepare data to apply the model;

6️⃣ Feature Selection: Select most importance features to apply the model (Normalization, Rescaling, Transformation);

7️⃣ Machine Learning Modelling: Train machine learning models and evaluate it with metrics;  

8️⃣ Hyperparameter Fine Tunning: Find the best hyperparamters for the model choose;

9️⃣ Convert Model Performance to Business Values: Traduce model perfomance to business values;

🔟 Deploy Model to Production: Make the model available in real time (cloud) to anyone use. 

# Top 3 Data Insights

<b>Hypothesis 01</b>: Owners of newers vehicles are more interested in taking out insurance.

❌FALSE: Owners of vehicles that are between 1 and 2 years, are the most interested in taking out insurance.

<b>Hypothesis 02</b>: Young people are less interested in taking out insurance.

✅TRUE: Young people (age less than 30 years old) are less interested in taking out insurance, comparing with other ages (old and middle ages).

<b>Hypothesis 03</b>: Customers that have between 200 to 299 days contract time, are more interested in taking out insurance.

✅TRUE: Customers that have 200 days or more contract time, are more interested in taking out insurance, comparing others customers.

# Machine Learning Model Applied

Being a Learn to Rank (rank propensity score for each customer) problem, some classifier models were tested. Below, the metrics for each model trained:

|Model Name		       |PRECISION @K		  |RECALL @K  	|PRECISION @K CV  |RECALL	@K CV  |
|--------------------|------------------|-------------|-----------------|--------------|
|KNN 	               |0.348 	          |0.047        |0.342            |0.057         |
|Logistic Regression |0.303             |0.041        |0.305            |0.051         |
|Extra Trees			   |0.346	            |0.047        |0.332            |0.055         |
|Random Forest	     |0.346 	          |0.047	      |0.357            |0.060         |
|XGBoost          	 |0.452             |0.061	      |0.416            |0.069         |
|LGBM	               |0.460 	          |0.062	      |0.425            |0.071         |

To improve the comparative visualization, a cumulative gains curve was plotted. Cumulative gains curve is an evaluation curve that demonstrates the model performance. Shows percentage of targets reached when considering a certain percentage of the population most likely to be targeted according to the model. We can see in the next plot, a comparative cumulative gains curve of all trained models.

<img src="https://raw.githubusercontent.com/felipejaguiar/health_insurance/main/image/cgc.PNG" alt="logo11" style="zoom:80%;" />

According metrics obtained and comulativa gains curve, the model chosen was LGBM. In addition, other factor that motivated the choice were, the LGBM being a small size model, which requires less storage use and makes applying it more agile.

Ps.: For the results in table were used k=1000 just to evaluate and comparing the models.

# Machine Learning Model Performance
After LGBM be the applied model chosen, the next step is to adjust the hyperparameters. To do it, was used Optuna, a python library that find the best hyperparameters for the model.

|Model Name		       |PRECISION @K		  |RECALL @K  	|
|--------------------|------------------|-------------|
|LGBM Tuned          |0.470 	          |0.063        |

Note that in this case, the gains comparing tuned and not tuned model, were not satisfactory.

# Business Results

Google sheets doc request in business assumptions is available here:

https://docs.google.com/spreadsheets/d/12oexnJCRgMqstAtTf2y8CnciALNvd5rCq97DicaszHs/edit#gid=1134939231

Note: Examples in spreadsheet were got in a random way just to demonstrate how the button works.

To answer the business questions, was used the metrics (Precision and Recall @K) Cumulative Gains Curve and Lift Curve. Where Lift Curve demonstrate how much the rank obtained from applied model is better than a random choice.

<b>1 - What percentage of interested customers, could the sales center contact by calling 20,000?</b>

|Model Name		       |PRECISION @K		  |RECALL @K  	|
|--------------------|------------------|-------------|
|LGBM (20000 calls)  |0.308 	          |0.837        |

<img src="https://raw.githubusercontent.com/felipejaguiar/health_insurance/main/image/q1cgc.png" width="500" height="350" alt="logo" style="zoom:80%;" />

Looking at point that red line crosses orange curve, we realize that you could contact approximately 83.70% of interested customers, making 20000 calls. 

<img src="https://raw.githubusercontent.com/felipejaguiar/health_insurance/main/image/q1lift.png" width="500" height="350" alt="logo" style="zoom:80%;" />

The Lift Curve shows that the model to 20.000 calls, is approximately 2.6 times better than using a random choice.

<b>2 - What percentage of interested customers, could the sales center contact by calling 40,000?</b>

|Model Name		       |PRECISION @K		  |RECALL @K  	|
|--------------------|------------------|-------------|
|LGBM (40000 calls)  |0.184 	          |0.999        |

<img src="https://raw.githubusercontent.com/felipejaguiar/health_insurance/main/image/q2cgc.png" width="500" height="350" alt="logo" style="zoom:80%;" />

Looking at point that red line crosses orange curve, we realize that you could contact approximately 83.70% of interested customers, making 40000 calls. 

<img src="https://raw.githubusercontent.com/felipejaguiar/health_insurance/main/image/q2lift.png" width="500" height="350" alt="logo" style="zoom:80%;" />

The Lift Curve shows that the model to 40.000 calls, is approximately 1.5 times better than using a random choice.

<b>3 - To contact 80% of interested customers, how many calls does the center sales needs to make?</b>

|Model Name		       |PRECISION @K		  |RECALL @K  	|
|--------------------|------------------|-------------|
|LGBM (18700 calls)  |0.315 	          |0.801        |

<img src="https://raw.githubusercontent.com/felipejaguiar/health_insurance/main/image/q3cgc.png" width="500" height="350" alt="logo" style="zoom:80%;" />

Looking at point that red line crosses orange curve, we realize that you need making approximately 18700 calls to contact 80% of interested customers. 

# Conclusions

At the end of this project, it was possible answer business questions and solve business problem, giving to sales center a solution for calls restrictions and helping in decision process. Besides it, the project was a good way to improve my knowledge about classification problems (in this case specific Learn to Rank), being possible find new model types, metrics and applications. 

# Next Steps to Improve

 - Search about news machine learning classifiers models;
 - Apply another method to select features, like Boruta;
 - Search and build new features to feed the model; 
 
# References

Kaggle: https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction

Freepik: <a href="https://www.freepik.com/free-vector/gradient-logo-template-with-abstract-shape_4785284.htm#query=insurance%20logo&position=4&from_view=keyword">Image by pikisuperstar</a> on Freepik

# <b>Tools:</b>

<a href = "www.python.org"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" target="_blank"></a>
<a href = "www.jupyter.org"><img src="https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter" target="_blank"></a>
<a href = "https://flask.palletsprojects.com/en/2.2.x/"><img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"></a>
<a href = "https://docs.google.com/spreadsheets/d/12oexnJCRgMqstAtTf2y8CnciALNvd5rCq97DicaszHs/edit#gid=1134939231"><img src="https://img.shields.io/badge/Google%20Sheets-34A853?style=for-the-badge&logo=google-sheets&logoColor=white"></a>
