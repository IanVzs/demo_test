#泰坦尼克号乘客生存预测
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn import tree
import graphviz
 
#数据加载
train_data = pd.read_csv("./data/train.csv")
test_data = pd.read_csv("./data/test.csv")
 
#数据探索
# print(train_data.info())
# print("-"*30)
# print(train_data.describe())
# print("-"*30)
# print(train_data.describe(include=['O']))
# print("-"*30)
# print(train_data.head())
# print("-"*30)
# print(train_data.tail())
 
# 使用平均年龄来填充年龄中的nan值(age)
train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(),inplace=True)
# 使用票价的均值填充票价中的nan值（Fare）
train_data['Fare'].fillna(train_data['Fare'].mean(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(),inplace=True)
 
#船舱
print(train_data['Embarked'].value_counts())
train_data['Embarked'].fillna('S', inplace=True)
test_data['Embarked'].fillna('S',inplace=True)
 
#特征选择
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
train_features = train_data[features]
#print(train_features)
train_labels = train_data['Survived']
test_features = test_data[features]
 
#使用 sklearn 特征选择中的 DictVectorizer 类，
# 用它将可以处理符号化的对象，将符号转成数字 0/1 进行表示
dvec=DictVectorizer(sparse=False)
train_features=dvec.fit_transform(train_features.to_dict(orient='record'))
print(dvec.feature_names_)
 
# 构造ID3决策树
clf = DecisionTreeClassifier(criterion='entropy')
# 决策树训练
clf.fit(train_features, train_labels)
print("train finish")
 
import ipdb; ipdb.set_trace()
#转化测试数据类型
test_features=dvec.transform(test_features.to_dict(orient='record'))
# 决策树预测
pred_labels = clf.predict(test_features)
 
# 得到决策树准确率
acc_decision_tree = round(clf.score(train_features, train_labels), 6)
print(u'score准确率为 %.4lf' % acc_decision_tree)
 
# 使用K折交叉验证 统计决策树准确率
print(u'cross_val_score准确率为 %.4lf' % np.mean(cross_val_score(clf, train_features, train_labels, cv=10)))
 
# 决策树可视化
with open("ttnk.dot", "w") as f:
    f = tree.export_graphviz(clf, out_file=f)
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.view()
