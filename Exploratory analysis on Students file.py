import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("college_1&2.csv")
def su(df):
    if df['CodeKata Score'] < 7000:
        val = 'Unsatisfactory'
    elif df['CodeKata Score'] < 10000:
        val = 'Needs_Improvement'
    elif df['CodeKata Score'] < 15000:
        val = 'Reached_Improvement'
    else:
        val="Exceeded expectations"
    return val

df['Status'] = df.apply(su, axis=1)

print(df.columns)
#Average of previous week geekions vs this week geekions
Av1=df['Previous Geekions'].mean()
print("Average of previous week geekions",round(Av1,0))
Av2=df['CodeKata Score'].mean()
print("Average of this week geekions",round(Av2,0))
#No of students participated
ttal=df['Name'].count()
print("No of students participated",ttal)
#Average completion of python course or my_sql or python english or computational thinking
Av3=df['python'].mean()
print("Average completion of python course",round(Av3,0))
Av4=df['mysql'].mean()
print("Average completion of my_sql course",round(Av4,0))
Av5=df['python_en'].mean()
print("Average completion of python en",round(Av5,0))
Av6=df['computational_thinking'].mean()
print("Average completion of computational thinking",round(Av6,0))
#rising star of the week (top 3 candidate who performed well in that particular week)
tp=(np.where(df['CodeKata Score'].nlargest(3)))
print("Rising star of the week (top 3 candidate who performed well in that particular week and followed by others",df['Name'],tp)
tp1=(np.where(df['Previous Geekions'].nlargest(3)))
print("shiningg star of the week (top 3 candidates who has highest geekions) and followed by others",df['Name'],tp1)
#Department wise codekata performence
x=df['Department']
y= df["CodeKata Score"]
plt.bar(x,y)
plt.title("Department wise codekata performence")
plt.show()

#"Overview of performance status"
z=df['Status']
e=df['Name']
sns.histplot(z)
plt.ylabel("Students count ")
plt.title("Overview of performance status")
plt.show()
