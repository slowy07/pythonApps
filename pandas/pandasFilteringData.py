import pandas as pd

playerData = pd.read_csv("resource/playerStat.csv")

# print(playerData.loc[(playerData['type'] == 'mage') & (playerData['second_type'] == 'disabler')])
# print(playerData.loc[playerData['player_name'].str.contains('slowy07')])

import re

# print(playerData.loc[playerData['player_name'].str.contains('slowy07|catur')])

print(
    playerData.loc[
        playerData["player_name"].str.contains("ab[a-z]*", flags=re.I, regex=True)
    ]
)
