import pandas as pd

countryInformation = pd.read_csv('resource/countryInformation.csv')

#looping row
#for index,row in countryInformation.iterrows():
    #print(index, row['country_name'])


print(countryInformation.loc[countryInformation['country_name'] == 'india'])