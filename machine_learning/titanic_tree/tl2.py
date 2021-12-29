#天龙2角色决策预测

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn import tree
import graphviz
 
#数据加载
train_data = pd.read_csv("./data/tl_t.csv")
test_data = pd.read_csv("./data/tl_test.csv")

#特征选择
features = ["DataID","CanSeeAim","CanSeeZL","CanSeeXZ","CanSeeXSR"]
train_features = train_data[features]
#print(train_features)
train_labels = train_data['DoID']
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
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.view()
