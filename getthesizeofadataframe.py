#2878
#easy

#Write a solution to calculate and display the number of rows and columns of players.

#Return the result as an array:

#[number of rows, number of columns]

#The result format is in the following example.


#my own solution using python3:

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    print(players)
    a = players.shape
    return list(a)
