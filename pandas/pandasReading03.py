import pandas as pd

countryInformation = pd.read_csv("resource/countryInformation.csv")

# describe
# print(countryInformation.describe())


# sort_values
# print(countryInformation.sort_values(['country_name','phone_code'], ascending=True))
print(
    countryInformation.sort_values(["country_name", "phone_code"], ascending=[True, 82])
)
# print(countryInformation.sort_values('country_name', ascending=False))
