import pandas as pd
import os


countryInformation = pd.read_csv("resource/countryInformation.csv")

# print columns
# print(countryInformation.columns)

# print columns spesific
# print(countryInformation['country_name'])
# print(countryInformation['country_name'][0:4])

# otherPrint
print(countryInformation[["country_name", "population", "phone_code"]])


# calling each row
# print(countryInformation.iloc[0:2])

# countryInformation[row,columns]
# print(countryInformation.iloc[1:2])
