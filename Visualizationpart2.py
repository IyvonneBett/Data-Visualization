import pandas
import matplotlib

df = pandas.read_csv('school.csv', parse_dates=['enrolldate'])
print(df)

df['Gender'].fillna(2, inplace=True) # inplace makes sure its updated
df['Smoking'].fillna(3, inplace=True)
df['Major'].fillna('Not Known', inplace=True)

median = df['Reading'].median()
df['Reading'].fillna(median,inplace=True)


import matplotlib.pyplot as plt
plt.style.use('seaborn')
df.groupby('Smoking').size().plot(kind='pie', autopct='%1.1f%%',
                                 explode=(0, 0, 0.4, 0))
plt.title('Gender proportion in %')
plt.xlabel('')
plt.ylabel('')
plt.show()

#bar chart
df.groupby('Gender')['Math'].mean().plot(kind='bar', color='green')
plt.title('Gender and math score %')
plt.xlabel('Gender')
plt.ylabel('Math score %')
plt.show()

# bar chart for gender and study time
median = df['StudyTime'].median()
df['StudyTime'].fillna(median,inplace=True)

df.groupby('Gender', 'Smoking')['StudyTime'].mean().plot(kind='bar', color='blue')
plt.title('Gender, smoking and StudyTime %')
plt.xlabel('Gender')
plt.ylabel('StudyTime')
plt.show()

print(df.isnull().sum())
#create a histogram of writing
#create a scatter plot to show math and english
#pie chart for rank
#bar chart math performance by rank MACHINE LEARNING
