#
# @ https://www.geeksforgeeks.org/merge-two-pandas-dataframes-on-certain-columns/


# importing modules
import pandas as pd

# creating a dataframe
df1 = pd.DataFrame({'Name':['Raju', 'Rani', 'Geeta', 'Sita', 'Sohit', 'Raju'],
					'Marks':[80, 90, 75, 88, 59, 69]})

# creating another dataframe with different data
df2 = pd.DataFrame({'Name':['Raju', 'Divya', 'Geeta', 'Sita'],
					'Grade':['A', 'A', 'B', 'A'],
					'Rank':[3, 1, 4, 2 ],
					'Gender':['Male', 'Female', 'Female', 'Female']})
# display
print(df1, "\n", df2, "\n")


# applying merge
#df_merged = df1.merge(df2[['Name', 'Grade', 'Rank']])
df_merged = df1.merge(df2)
print(df_merged)

