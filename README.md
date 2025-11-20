# Data_Science_Portfolio
Key Data Science projects and work completed as part of the MS Data Science Program at Bellevue University. My goal with the program was to expand my knowledge around the ever-growing data field learning new techniques to understand and utilize data. 

## About Me
  - BS Biology/Chemistry University of Wisconsin-La Crosse (2008)
  - MS Data Science Bellevue University (Expected 2025)
  - 15+ Years in Food Safety and Quality Assurance in the food manufacturing industry
## Contact
  - LinkedIn https://www.linkedin.com/in/ryan-krenke-b2bab018a/ 

## Projects:

### ChildCareDataAnalysis3Mediums
  - Analysis of national childcare, company data, and national test data for a daycare center company. 
  - Data preparation and cleaning
    - Kept data from only Midwest states and median childcare costs. Merged with company cost dataset. Updated national test dataset based on school subjects
  - Three mediums
    - Medium 1 – Powerpoint presentation
      - Target audience of company leadership team. Bar charts created to show company costs by child age and differences between center and family-based childcare. 
    - Medium 2 – PowerBI Dashboard
      - Target audience of company leadership team. Tracking metrics of household income, unemployment rates, population, and number of households with kids/both parents work. Also a United States map of current and prospective locations
    - Medium 3 – Social media post
      - Target audience of current families and general public. Bar charts created to show average child test scores and comparable childcare costs. 
  - Libraries/Programs used
    - Python, NumPy, Pandas, Matplotlib, PowerBI

### Cleaning_FormattingAPIData
  - Cleaning and formatting data from an API data source
  - API Source – weather sensor data from purpleair.com
  - Methods
    - Pulled data from eight random sensors via an API call. 
    - Used JSON language processing to convert data into pandas datasets. 
    - Combined datasets from all states into one and kept only state and raw data. 
    - Cleaned data to remove brackets and whitespaces and unnecessary unique values associated with each values.
  - Libraries/Programs used
    -Python, BeautifulSoup, Pandas, NumPy, urllib, JSON 

### Cleaning_FormattingWebsiteTableData
  - Cleaning and formatting data from a website table source
  - Website source - https://www.cdc.gov/asthma/most_recent_data_states.htm 
  - Methods
    - Pulled recent state data from two HTML tables and convert data into pandas datasets.
    - Cleaned and analyzed data to understand aspects and ensure it is usable.
    - Pulled in another data table of location coordinates and combined the two datasets. 
  - Libraries/Programs used
    - Python, BeautifulSoup, Pandas, NumPy, Requests, Scipy

### Food_Fat_Level_Regression_Project
  - Cleaning and formatting data, performing exploratory data analysis, and predictive analysis with Logistic and Linear Regression modeling
  - Methods
    - Imported flat file source and convert into pandas datasets.
    - Exploratory data analysis with visualizations to understand potential correlations.
    - Binning data and creating dummy variables prior to modeling. 
    - Training and executing Logistic Regression model and evaluating with key metrics and confusion matrix. 
    - Performing feature selection to determine possible best features.
    - Training and executing Linear Regression models with value scaling and evaluating with key metrics.
  - Libraries/Programs used
    - Python, Pandas, NumPy, Matplotlib, Seaborn, Sklearn, SelectKBest, Chi2, Cross_Val_Score

### SQLMergeDatasets_Visualizations
  - Using SQL language to merge three datasets and creating appropriate visualizations
  - Methods
    - Creating three SQL tables and adding records
    - Merging tables
    - Cleaning and standardizing data
    - Creating visualizations for exploratory data analysis
  - Libraries/Programs used
    - Python, Pandas, SQLite, Matplotlib

### VehicleTheftsAnalysisProject
  - Used R language to clean and format data and produce visualizations related to Kia and Hyundai vehicle thefts in the Midwest United States region
  - Methods
    - Read data from flat file and remove blank data
    - Creating map visualization with color gradient of vehicle thefts
    - Updating data to focus on various regions
    - Creating area charts, pie graphs, and donut charts of vehicle thefts
  - Libraries/Programs used
  - R, GGplot2, Maps, Dplyr, Readr, Scales, Maptools, SP, Tidyverse, Lubridate, Tidyr

### Weather_Python_Project
  - Created an interactive Python program where a user can choose to enter either a zip code or a city and state and the program will output various current weather details.
  - Methods
    - Main program allowing user to choose to look up weather by zip code or city and state and receive temperature results in fahrenheit or celcius
    - Creating functions for pulling data from API source for zip code or city/state
    - Creating functions to handle fahrenheit or celcius results
    - Error handling throughout
  - Libraries/Programs used
    - Python, API, JSON, Requests


### MeatConsumptionRegressionProject
  - Cleaned and formatted worldwide meat consumption and informational data and performed predictive analysis with Linear Regression and Random Forest modeling.
  - Methods
    - Reading data from flat file
    - Data cleaning, exploratory data analysis, and transformation
    - Training and executing a Linear Regression model
    - Plotting a correlation matrix to investigate top correlated predictors
    - Training and executing Linear Regression and Random Forest models for different target variables
    - Evaluating models with key metrics
    - Creating new datasets with values predicted from models
    - Creating visualizations of predicted data
  - Libraries/Programs used
    - Python, Pandas, NumPy, Matplotlib, Sklearn, LinearRegression, RandomForest, Math, Seaborn
  

### WildfirePredictionClassificationProject
  - Cleaned and formatted wildfire data and used to create optimal model for prediction of future wildfires
  - Methods
    - Reading data from flat file
    - Data cleaning, exploratory data analysis, and transformation
    - Training and executing Logistic Regression and Random Forest models and evaluating with key metrics
    - Using pipelines to balance and scale data
    - Using SelectKBest and Chi2 to choose top five predictor variables
    - Using SMOTE to sample data
    - Creating visualizations to support analysis
  - Libraries/Programs used
    - Python, NumPy, Matplotlib, Seaborn, Sklearn, LogisticRegression, RandomForest, Pipeline, SelectKBest, Chi2, SMOTE, Preprocesing


### BeerRatingsPredictionProject
  - Cleaned and formatted beer review rating data and used to create optimal model for prediction of future beer ratings
  - Methods
    - Reading data from flat file
    - Exploratory data analysis
    - Training and executing Linear Regression and Random Forest models and evaluating with key metrics
    - Evaluating correlation to attempt model improvements
    - Training and executing Lasso Regression model and evaluating with key metrics
    - Utilizing Feature_Importances with Random Forest Model to understand important model features
    - Creating visualizations to support analysis
  - Libraries/Programs used
    - Python, NumPy, Seaborn, Sklearn, LinearRegression, RandomForest, Lasso

