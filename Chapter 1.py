import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('display.width', 75)
pd.set_option('display.max_columns', 5)

# import the land temperature data
landtemps = pd.read_csv('C:\\Users\\jenny\\venvs\\py39\\Python-Data-Cleaning-Cookbook-master\\Chapter01\\data\\landtempssample.csv',
    names=['stationid','year','month','avgtemp','latitude',
      'longitude','elevation','station','countryid','country'],
    skiprows=1,
    parse_dates=[['month','year']],
    low_memory=False)

type(landtemps)

# show enough data to get a sense of how the import went
landtemps.head(7)
landtemps.dtypes
landtemps.shape

# fix the column name for the date
landtemps.rename(columns={'month_year':'measuredate'}, inplace=True)
landtemps.dtypes
landtemps.avgtemp.describe()
landtemps.isnull().sum()

# remove rows with missing values
landtemps.dropna(subset=['avgtemp'], inplace=True)
landtemps.shape



import os
import pandas as pd
os.chdir("C:\\Users\\jenny\\venvs\\py39\\Python-Data-Cleaning-Cookbook-master\\Chapter03\\data")
nls97 = pd.read_csv("nls97.csv")
# nls97.head(10)
# nls97.info()
oo = nls97[['personid', 'gender', 'birthmonth', 'birthyear', 'highestgradecompleted', 'maritalstatus', 'childathome', 'childnotathome', 'wageincome', 'weeklyhrscomputer']]
oo