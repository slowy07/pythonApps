import pandas as pd



playerData = pd.read_csv('resource/playerStat.csv')


playerData['total'] = playerData['strengh'] + playerData['agility'] + playerData['intelligence']
#print(playerData.head())


#playerData.drop(columns=['intelligence'])
#print(playerData.drop(columns=['intelligence']))


#playerData['total'] = playerData.iloc[:, 1:2].sum(axis=1)



print(playerData.head())
