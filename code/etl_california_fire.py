
import pandas as pd # need to have pandas installed
import addfips #AddFIPS is a tool for adding state or county FIPS codes to files that contain just the names of those geographies.

# Cleaning California_Fire_Incidents.csv


dataset = pd.read_csv('../data/California_Fire_Incidents.csv')
print(dataset.columns)

remove_column_names = ['SearchDescription', 'SearchKeywords', 'StructuresDamaged', 'StructuresDestroyed',
       'StructuresEvacuated', 'StructuresThreatened', 'UniqueId', 'Updated',
       'WaterTenders', 'AirTankers', 'CanonicalUrl', 'ConditionStatement', 'ControlStatement',  'CrewsInvolved', 'Dozers',
       'Engines', 'FuelType', 'Helicopters', 'PersonnelInvolved', 'Active', 'Public']   # remove columns we do not need

dataset = dataset.drop(columns = remove_column_names)

format_String = "%Y-%m-%dT%H:%M:%SZ"
dataset['Extinguished'] = pd.to_datetime(dataset['Extinguished'], format = format_String) # Format time

# Remove microseconds
for i in dataset.index:
  if (len(dataset['Started'][i]) > 20):
    dataset['Started'][i] = dataset['Started'][i][:19] + "Z"

dataset['Started'] = pd.to_datetime(dataset['Started'], format = format_String)

print(dataset.dtypes)

dataset['Active Time'] = dataset['Extinguished'] - dataset['Started']

dataset['FIPS'] = int(0)

af = addfips.AddFIPS()

for i in dataset.index:
  a = af.get_county_fips(dataset['Counties'][i], state='California')
  if a != None:
    dataset['FIPS'][i] = int(af.get_county_fips(dataset['Counties'][i], state='California'))
  else :
    dataset['FIPS'][i] = None

dataset.to_csv('../data/California_Fire_Cleaned.csv')