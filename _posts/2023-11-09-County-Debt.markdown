---
layout: post
title:  "A study of American Debt by County"
date:   2023-11-08 13:17:35 -0800
categories: jekyll update
---

#### Lets look at different type of debt visualized by American County

For this quick study I combined a simple data set of centroid data for all american counties with a 
Dataset containing many different metrics, most of them surrounding debt. With these two different points of view
I was able to visualizes what types of qualities and issues different parts of the USA hold.

Lets take a look at a few of them below.

First lets look at the average household income. You can see higher incomes centered around large cities, specifically on the Eastern seabord and in California.

![Average Household Income by County](/images/CountyDebt/HouseholdIncomeByCounty.png){:class="img-responsive"}

Next we can look at the percent of people across the nation who have Auto Loans at all. This metric could depend on many different things such as the wealth of a region, the car ownership necessity of a region and more.

We see below how on both the county and state level, loan delinquency is correlated with household income.

![Income Vs Loan Delinquency by State](/images/CountyDebt/IncomeVLoanDefByState.png){:class="img-responsive"}
![Income Vs Loan Delinquency by County](/images/CountyDebt/IncomeVLoanDefByCounty.png){:class="img-responsive"}

Naturally, we see the delinquency rate fall significantly as the average household income rises. Lets take a look visually.

![Percent of people with Auto Loan Delinquency](/images/CountyDebt/PercentAutoLoanDelinquency.png){:class="img-responsive"}

We can see that the darker green is more concentrated in the southeast of the United States than the regions with low household income, which are very spread out.

![Percent of people with Auto Loans](/images/CountyDebt/PercentOfPeopleWithAutoLoans.png){:class="img-responsive"}

This graph, the percent of people with Auto Loans looks quite different than the percent of loan delinquency. See below that the correlation between the two variables is extremely week or perhaps non - existent.

![Loan rate Vs Loan Delinquency](/images/CountyDebt/LoanRateVLoanDef.png){:class="img-responsive"}

Finally lets look at the percent of people by county with Auto or Retail Debt. We see an average of 38.5% nationally, with 27 counties across the nation exceeding 50% in some kind of Auto or Retail Debt.

![Percent of people with Auto or Retail Debt](/images/CountyDebt/PercentWithAutoRetailLoanDebt.png){:class="img-responsive"}




#### Thanks for reading!

 Check out my sources for the [geographic data](https://www.kaggle.com/datasets/canonicalized/county-centroids)  and the [economic data](https://datacatalog.urban.org/dataset/debt-america-2023)

See the source code on my github [here](https://github.com/amschechter/amschechter.github.io/blob/main/DataScience/censusData/AutoDebt.ipynb)