import pandas as pd

playerData = pd.read_csv('resource/playerStatUpdate.csv')


resetData = playerData.reset_index(drop=True)
print(resetData)