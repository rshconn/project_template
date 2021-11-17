# California Fire Detection

### Group Members
- Farah Sultana
- Nishanth Prajith

### Repository Structure
- `data`
  - `California_Fire_Incidents.csv`: Raw data from the kaggle for all fires in california from 2013 - 2019
  - `California_Fire_Cleaned.csv`: Cleaned 'California_Fire_Cleaned.csv`
  - `weather_data.csv`: Raw data weather data from the World Weather Online API
  - `cleaned.csv` : Combined dataset for modeling
- `code`
  - `etl_california_fire.py`: Cleans `California_Fire_Incidents.csv`
  - `etl_weather.py`: Cleans `weather_data.csv`
  - `cleaned.py` : Combines the two datasets
  - `exploratory_data_analysis.ipynb`: Includes descriptive statistics and charts. 

### Exploratory Analysis
Describe what work you have done so far and include the code. 

### Challenges
One of the biggest challenges we faced so far was getting the weather information. Many weather API's did not have historical weather data information we were looking to use in our model. It was very difficult to find a reliable yet free API that will give us the information we required. But luckily World Weather Online API did manage to work out in the end. Another challenge we encountered was definitely with the jupyter notebook as we were trying to plot certain graphs on state maps which did not work out as planned, as google colab for some reason did detect the necessary libraries even though they were installed. But after some heavy debugging it did manage to work and resolve itself.

### Future Work
We are looking to explore more using the data and try differnt classification models to test which model is best. One of the things we will be looking to do is add data of time and places where there did not occur any fires so as to make the dataset more realistc. This should prevent the model from overfitting and help the model to be more accurate.

### Contributions
We both worked on the dataset cleaning and exploratory analysis. Nishanth mainly worked on data cleaning/fetching and Farah worked on some cleaing as well as the exploratory data analysis notebook.
