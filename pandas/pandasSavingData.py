import pandas as pd

playerData = pd.read_csv("resource/playerStat.csv")


playerData["total"] = (
    playerData["strengh"] + playerData["agility"] + playerData["intelligence"]
)

playerData.to_csv("resource/playerStatUpdate.csv", index=False)
# playerData.to_excel('resource/playerStatUpdate.xls', index=False)
# playerData.to_excel('resource/playerStatUpdate.txt', index=False)
print(playerData.head())
