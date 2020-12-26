import pandas as pd

playerData = pd.read_csv('resource/playerStat.csv')

print(playerData.loc[playerData['type'] == 'mage', 'type' ] = 'mage')