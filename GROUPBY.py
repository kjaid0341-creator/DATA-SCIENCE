import pandas as pd
df = pd.DataFrame({
    "Name": ["Ali", "Zara", "John"],
    "Marks": [80, 95, 70]
})
print(df.sort_values(by="Marks"))
df.sort_values(
    by="Marks",
    key=lambda x: -x
)

# syntax of lambda function in pandas in python
df.sort_values(by="column_name", key=lambda x: ...)

df = pd.DataFrame({
    "Name": ["Ali", "Alexander", "Bob", "John"]
})

print(df.sort_values(
    by="Name",
    key=lambda x: x.str.len()
))

# 12th june ds
import pandas as pd
df=pd.read_csv('student_data.csv')

# df.groupby('placement_status')['placement_status'].agg('count')
# df.groupby('placement_status')['exam_score'].agg('mean')
# df.groupby('placement_status')['exam_score'].agg('max')
# df.groupby('placement_status')['exam_score'].agg('min')
# df.groupby('placement_status')['exam_score'].agg(['count', 'mean', 'max', 'min'])
# df.groupby('study_hours')['exam_score'].agg('mean')

import pandas as pd
df=pd.read_csv('student_data.csv')

def grades(marks):
  if marks>=90:
    return 'A'

  elif marks>80:
    return 'B'
  elif marks>60:
    return 'C'
  elif marks>50:
    return 'D'
  else:
    return 'F'
df['grade']=df['exam_score'].apply(grades)
df

#APPLYING JOINS ON TABLES THERE ARE MAINLY FOUR TYPES OF JOINS
# (I) INNER JOIN. (II) OUTER JOIN  (III) LEFT JOIN (IV) RIGHT JOIN
import pandas as pd
df1=pd.DataFrame({
    'id': [1,2,3,4],
    'name':['raja', 'rani', 'rahul', 'rhea'],
    'age':[25,30,35,40]
})
df2=pd.DataFrame({
    'id': [3,4,5,6],
    'name':['rahul', 'rhea', 'rani', 'reena'],
    'age':[35,40,25,30]
})
# df3=pd.merge(df1,df2, on='id', how='inner')
# df3.rename(columns={'name_x':'table_1'}, inplace=True)
# print(df3)
#⭐ pd.merge(df1,df2, on='id', how='left')
#⭐ pd.merge(df1,df2, on='id', how='right')
#⭐ pd.merge(df1,df2, on='id', how='outer')
#⭐ pd.merge(df1,df2, how='cross')
df3=pd.concat([df1, df2])
df3=df3.drop_duplicates(subset = ['id'], keep='first')
display(df3)

import pandas as pd

df = pd.read_csv('student_data.csv')
df.pivot_table(columns='placement_status',index='sleep_hours',values='exam_score',aggfunc='mean')

# LEETCODE
# 1327
# 511
# 586
# 1050
# 175
# 181
# 183
# 262
# 184
# 185
# 1179
