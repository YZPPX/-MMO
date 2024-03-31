import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取医学学生数据集
data = pd.read_csv('medical_students_dataset.csv')

# 1. 使用散点图：用来展示体温和心率的关系
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Temperature', y='Heart Rate', data=data)
plt.title('Scatterplot of Temperature vs Heart Rate')
plt.xlabel('Temperature')
plt.ylabel('Heart Rate')
plt.show()

# 2. 使用箱形图：用来展示学生的血压分布情况
plt.figure(figsize=(8, 6))
sns.boxplot(x='Blood Pressure', data=data)
plt.title('Boxplot of Blood Pressure')
plt.xlabel('Blood Pressure')
plt.show()

# 3. 使用直方图：展示学生年龄的分布情况
plt.figure(figsize=(8, 6))
sns.histplot(data['Age'], bins=20, kde=True)
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# 4. 使用饼图：显示血型占总体的比例
blood_type_counts = data['Blood Type'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(blood_type_counts, labels=blood_type_counts.index, autopct='%1.1f%%')
plt.title('Pie Chart of Blood Type Distribution')
plt.show()

# 5. 使用热图：展示BMI和心率之间的相关性
plt.figure(figsize=(8, 6))
sns.heatmap(data[['BMI', 'Heart Rate']].corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap of BMI vs Heart Rate')
plt.show()