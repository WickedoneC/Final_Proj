# Final_Proj

# Credit Analysis
Predicting Moody's credit ratings from a selection of stocks from the Russell 1000 based on their financial data and ratios.

Data taken from markets.businessinsider.com, ishares.com, and yahoo finance.

Several models were run with varying degress of success:
-ordinal logistic
-knn
-kmeans clustering
-random forest
 
<br/>

# Model Results:

Random Forest performed the best, followed by KNN. However, both models worked much better on a smaller sample of the data.

GridSearch and Cross Validation were used to refine the models and YellowBrick was used to visually explore the results.


<br/>


# Uses of the model:

The model can be used to predict the Moody's credit rating of a bond, and then compare it to the actual rating for an indication of riskiness.

Compare model predictions to actual ratings and combine this with fundamental and qualitative research to fuel investment decisions. 

Run the models on a quarterly basis to detect any trends in the predicted ratings, and use that as a basis for further research and decisions.

Look at predicted ratings to take action prior to a ratings change.

Can be used on a large, more general scale as an economic indicator.

Level of predicted ratings can be compared to current and past trends to see how ratings relate to economic strength.

The models and their results can be useful to investors, lenders, and issuers.

<br/>


# Improvement and Future Work:

-better data, cleaner data (paid for data)

-more model types, parameter refinement

-predicting when a credit rating change will occur, if at all

-more accurate data, more up-to-date data

-fit models to rating groups one at a time 

-compare predictions at different points in time

<br/>

[Presentation Link](https://docs.google.com/presentation/d/1sD9j9UId8A327t2zLGiCv_yOPxw0g1Y4AUgDFs2Q1LI/edit?usp=sharing)


