import pandas
import matplotlib

df = pandas.read_csv('power.csv', parse_dates=['Date'])
print(df)
print(df['Wind'])
print(df.describe())
# Positive corelation : >0.....1 towards 1 is strong positive corelation
# negative corelation when one goes up one comes down < 0....-1 towards -1 is a strong negative corelation
print(df.corr()) # co relation can we say solar was low wind was high

#corelate both solar and wind
# subset the df
subset = df[['Solar','Wind']]
print(subset.corr())

#scatter, histogram
import matplotlib.pyplot as plt
print(plt.style.available)
plt.style.use('seaborn-dark-palette')
#method 1
figure, ax = plt.subplots()
ax.hist(df['Consumption'], color = 'blue')
ax.set_xlabel('Consumption (GWh)')
ax.set_ylabel('Freq.')
ax.set_title('Consumption distribution in GWh')
plt.show()

#method2 use ax or kind
df['Consumption'].plot(kind='hist', color='red')
plt.xlabel('Consumption (GWh)')
plt.ylabel('Freq.')
plt.title('Consumption distribution in GWh')
plt.show()

#method 3 scatter plots need at least 2 numeric variables
figure, ax = plt.subplots()
ax.scatter(df['Consumption'], df['Solar'], color = 'orange')
ax.set_xlabel('Consumption (GWh)')
ax.set_ylabel('Freq.')
ax.set_title('Consumption distribution in GWh')
plt.show()

# method 2 for kind
df.plot(kind='scatter', x= 'Consumption', y= 'Solar', color= 'green')
plt.xlabel('Consumption (GWh)')
plt.ylabel('Solar')
plt.title('Consumption solar distribution in GWh using kind')
plt.show()

#line graphs we need date how was power consumption over time/ ..time series 2006...2017
df = df.set_index('Date')
df.loc['2013', 'Consumption'].plot(kind= 'line', color= 'brown')
plt.xlabel('Year 2013')
plt.ylabel('Consumption')
plt.title('Power usage in 2017')
plt.show()

#solar
       #year-month
df.loc['2015-05', ['Consumption', 'Solar', 'Wind']].plot(kind= 'line')
plt.xlabel('Year 2015 May')
plt.ylabel('Consumption and solar and wind')
plt.title('Power usage in 2015')
plt.show()

#by a range of dates if date had time '2007-06-01 05:45
df.loc['2007-06-01':'2008-06-09', ['Consumption', 'Solar', 'Wind']].plot(kind= 'line')
plt.xlabel('Year 2007- 2008')
plt.ylabel('Consumption and solar and wind')
plt.title('Power usage between 2007 to 2008')
plt.show()










