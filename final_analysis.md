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
  - `etl_california_fire.py` : Cleans `California_Fire_Incidents.csv`
  - `etl_weather.py` : Cleans `weather_data.csv`
  - `cleaning.py` : Combines the two datasets
  - `exploratory_data_analysis.ipynb` : Includes descriptive statistics and charts. 
  - `models.ipynb` : Machine learning models notebook

### Challenges (Optional)
Describe any challenges you encountered.

### Contributions
We both worked on the dataset cleaning, modeling and exploratory analysis. Nishanth mainly worked on data cleaning/fetching and Farah worked on some cleaing but mainly worked on the exploratory data analysis notebook. For the modeling notebook we both worked together to build different models and verify their accuracy.
