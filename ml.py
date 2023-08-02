import pandas
from pandas import DataFrame
import matplotlib.pyplot as plt


data = pandas.read_csv('cost-revenue-clean.csv')


data.describe()

plt.figure( figsize=(10,6) )
plt.scatter(x , y , alpha=0.3)
plt.title('Film Cost Vs Global Revenue')
plt.xlabel('Production Budget $')
plt.ylabel('Worldwide Budget $')
plt.ylim( 0 , 3000000000 )
plt.xlim( 0 , 450000000 )
plt.show()