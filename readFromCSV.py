import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style

style.user("ggplot")

readData = pd.read_csv("..\SalesData.csv")
x = readData["SalesID"].as_matrix()
y = readData["ProductPrice"].as_matrix()
plt.xlabel("SalesID")
plt.ylabel("ProductPrice")
plt.title("SalesAnlysis")
plt.plot(x, y)
plt.show()