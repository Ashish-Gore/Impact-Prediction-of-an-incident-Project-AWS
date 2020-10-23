# Impact Prediction of an incident Project AWS

## Problem Statement 
- To predict the Impact of an Incident Raised by Customer.

### Background:

[Incidents_service.xlsx](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/Incidents_service.xlsx) as given data file.

- The dataset is having incidents raised by customers. Which contains an event log of an incident management process extracted from a service desk platform of an IT company.

- Dataset contains total 26 features, and 1.4Lac+ records. Out of which 25 features are independent and 'Impact' Feature is output variable.

- The Prediction needs to be Classified into 3 Classes:
1. High Impact
2. Medium Impact
3. Low Impact

# Project Phases:

## [1. Exploratory Data Analysis](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/tree/master/1.%20Exploratory%20Data%20Analysis)

- This Phase Includes EDA part for Project Conducted in Tableau.

- Each Categorical and Numerical variable is Visualised in Tableau session. Please find Tableau workbook [Here](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/1.%20Exploratory%20Data%20Analysis/Impact_prediction%20Project%20Stories%20And%20Insights.twbx)

- Each Feature is interacting with each other, making whole workbook fully interactive. Please find the detailed workbook here: [https://public.tableau.com/profile/ashish.gore#!/vizhome/Impact_predictionProjectStories/Story2](https://public.tableau.com/profile/ashish.gore#!/vizhome/Impact_predictionProjectStories/Story2)

- Fully Interactive Dashboards were created for both Numerical as well as Categorical Features.

- After Analysis of EDA part, the data had some hidden Insights, which are mentioned using stories:

1. Story 1

![template1](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/1.%20Exploratory%20Data%20Analysis/Story%201%20EDA.jpg)

2. Story 2

![template1](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/1.%20Exploratory%20Data%20Analysis/Story%202%20EDA.jpg)

**For More Details on Dataset Visualisation Please visit: https://public.tableau.com/profile/ashish.gore#!/vizhome

## [2. Model Building Phase](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/tree/master/2.%20Model%20Building%20Phase)

### [1. Feature_Selection](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/2.%20Model%20Building%20Phase/1.%20Feature_Selection.ipynb)
- Out of 25 Features only top few features were contributing for the output prediction. So only those Features were kept.

![template1](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/2.%20Model%20Building%20Phase/Imp_Features.JPG)

### [2. PCA_Technique](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/2.%20Model%20Building%20Phase/2.%20PCA_Technique.ipynb)

- After Conversion of categorical variables into dummies many new columns were generated. so to reduce dimensionality PCA technique is used.
**Unsupervised Learning Technique**

### [3. LDA_Technique](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/2.%20Model%20Building%20Phase/3.%20LDA_Technique.ipynb)

- After Conversion of categorical variables into dummies many new columns were generated. so to reduce dimensionality LDA technique is used.
**Supervised Learning Technique**

#### In Both PCA and LDA Dimensionality Reduction Techniques, Algorithms Used are:

1. Algorithms:

- Decision Tree
- Random Forest
- Support Vector Classifier
- Gausian NB
- KNN

2. Meta Algorithms:

- Voting Classifier
- Bagging Classifier 
- AdaBoost Classifier
- XGBoost Classifier


### [4. Neural_Networks_Impact_prediction](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/2.%20Model%20Building%20Phase/4.%20Neural_Networks_Impact_prediction.ipynb)

Please Find More Details Here: [Model Building Phase.pptx](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/2.%20Model%20Building%20Phase/Model%20Building%20Phase.pptx)


## [3. Model Deployment Phase](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/Impact_Prediction_final_Model_py.ipynb)

- Finally Model is Deployed on AWS Cloud Platform with Flask Framework.

- Link: 
1. http://ec2-18-219-185-230.us-east-2.compute.amazonaws.com:8080/
2. https://impact-prediction-deployment.herokuapp.com/

![template1](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/templates/SS1.JPG)

![template1](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/templates/SS2.JPG)

![template1](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/templates/SS3.JPG)

![template1](https://github.com/Ashish-Gore/Impact-Prediction-of-an-incident-Project/blob/master/templates/SS4.JPG)

