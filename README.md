# <h1 align=center>**`MEDICAL DATA VISUALIZER`**</h1>


## **Introduction**

In this project, they visualized and performed calculations from medical examination data using matplotlib, seaborn, and pandas. Dataset values were collected during medical examinations. This project was carried out by ELOY ARMAO, a student of the DATA SCIENCE career at the HENRY academy. More information about the academy in the following link https://www.soyhenry.com/carrera-data-science

You will also find a file called `medical_data_visualizer.ipynb` where the questions of the work proposal will be resolved in a more dynamic way.

## **Job offer**
The rows in the dataset represent patients and the columns represent information like body measurements, results from various blood tests, and lifestyle choices. You will use the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

File name: medical_examination.csv

| Feature |  Variable Type	| Variable | Value Type |
|---------|-----------------|----------|------------|
|  Age     | Objective Feature |   age   | int (days) |
| Height	  | Objective Feature |  height |  int (cm)  |
| Weight	  | Objective Feature |	weight	|float (kg)  |
| Gender	|  Objective Feature  |	gender | categorical code
| Systolic blood pressure |	Examination Feature | ap_hi | int
|Diastolic blood pressure |	Examination Feature | ap_lo	| int
Cholesterol	| Examination Feature | cholesterol	| 1: normal, 2: above normal, 3: well above normal |
| Glucose | Examination Feature	| gluc	 | 1: normal, 2: above normal, 3: well above normal|
|Smoking	| Subjective Feature  | smoke	 |  binary
|Alcohol intake	| Subjective Feature |	alco	| binary
|Physical activity| 	Subjective Feature |	active	| binary
|Presence or absence of cardiovascular disease |	Target Variable |	cardio	| binary

## **Tasks**

Use the data to complete the following tasks in: medical_data_visualizer.py

+ Add an column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.overweight

+ Normalize the data by making 0 always good and 1 always bad. If the value of or is 1, make the value 0. If the value is more than 1, make the value 1. cholesterolgluc

+ Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's . The dataset should be split by 'Cardio' so there is one chart for each value. The chart should look like. catplot() cardioexamples/Figure_1.png

+ Clean the data. Filter out the following patient segments that represent incorrect data:

  + diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))

  + height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))

  + height is more than the 97.5th percentile

  + weight is less than the 2.5th percentile

  + weight is more than the 97.5th percentile

+ Create a correlation matrix using the dataset. Plot the correlation matrix using seaborn's . Mask the upper triangle. The chart should look like .heatmap()examples/Figure_2.png

More information can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer

## **Used libraries**

+ Pandas

+ Numpy

+ Seaborn

+ Motplotlib