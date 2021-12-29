from sklearn import tree


def hello():
    X = [[0, 0], [1, 1]]
    Y = [0, 1]
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)


    aaa = clf.predict([[2., 2.]])
    bbb = clf.predict([[-1., -1.]])
    print(aaa, bbb)


def muti_select():
    from sklearn.datasets import load_iris

    iris = load_iris()
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(iris.data, iris.target)
    draw_graph(clf=clf, iris=iris)
    
def draw_graph(clf, feature_names="fName", target_names="tName", pdf_name="clf", out2file=""):
    import graphviz
    if out2file:
        pass
    else:
        # dot_data = tree.export_graphviz(clf, out_file=None)
        # graph = graphviz.Source(dot_data)
        # graph.render("iris")
        
        dot_data = tree.export_graphviz(clf, out_file=None,
            feature_names=feature_names,  
            class_names=target_names,  
            filled=True, rounded=True,  
            special_characters=True)  
        graph = graphviz.Source(dot_data)
        graph.render(pdf_name)
        print(graph)
        
        # save_model(clf)

def train_CLF():
    import pandas as pd
    train_data = pd.read_csv("./data/tl_t.csv")
    
    features = ["DataID","CanSeeAim","CanSeeZL","CanSeeXZ","CanSeeXSR"]
    train_features = train_data[features]
    train_labels = train_data['DoID']
    
    clf = tree.DecisionTreeClassifier()
    # train
    clf.fit(train_features, train_labels)
    return clf

def test_CLF(clf):
    import pandas as pd
    test_data = pd.read_csv("./data/tl_test.csv")
    features = ["DataID","CanSeeAim","CanSeeZL","CanSeeXZ","CanSeeXSR"]
    test_features = test_data[features]
    pred_labels = clf.predict(test_features)
    print(pred_labels)


def save_model(clf, path):
    import pickle
    with open(path, "wb") as f:
        pickle.dump(clf, f)
        return True

def load_model(path):
    import pickle
    with open(path, "rb") as f:
        clf = pickle.load(f)
        return clf

if __name__ == "__main__":
    # hello()
    # muti_select()
    
    # clf = train_CLF()
    # save_model(clf, "./test.pickle")
    clf_load = load_model("./test.pickle")
    draw_graph(clf_load, pdf_name="hello")
    test_CLF(clf_load)