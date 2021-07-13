import argparse

import pandas as pd
from sklearn import tree

PATH = "./test.pickle"
Features = ["CanSeeAim","CanSeeBoss","GoodPoint","Interest"]
Targets = ["0","1","2","3","4","5"]
Lables = "DoID"
PDFName = "dt_image"

def draw_graph(clf, feature_names, target_names, pdf_name="clf"):
    import graphviz
    dot_data = tree.export_graphviz(clf, out_file=None,
        feature_names=feature_names,  
        class_names=target_names,  
        filled=True, rounded=True,  
        special_characters=True)  
    graph = graphviz.Source(dot_data)
    graph.render(pdf_name)
    print(f"draw done => {pdf_name}")

def plot_score(train_path, test_path, max_depth):
    import matplotlib.pyplot as plt

    train_data = pd.read_csv(train_path)
    test_data = pd.read_csv(test_path)
    
    train_features = train_data[Features]
    train_labels = train_data[Lables]

    test_features = test_data[Features]
    test_labels = test_data[Lables]


    for i, criterion in enumerate(("gini", "entropy")):
        acu_tr_lis = []
        acu_te_lis = []
        for depth in range(1, max_depth):
            clf = tree.DecisionTreeClassifier(criterion=criterion, max_depth=depth)
            clf.fit(train_features, train_labels)

            acu_train = clf.score(train_features, train_labels)
            acu_test = clf.score(test_features, test_labels)

            acu_tr_lis.append(acu_train)
            acu_te_lis.append(acu_test)
        
        plt.subplot(2, 1, i+1)
        plt.plot(range(1, max_depth), acu_tr_lis, "o-",label="acu-train")
        plt.plot(range(1, max_depth), acu_te_lis, "*-",label="acu-test")
        plt.xlabel("max_depth")
        plt.ylabel("accuracy")
        plt.title("Criterion = "+str(criterion))
        plt.legend(["acu-train", "acu-test"])
    plt.show()


def train_CLF():
    train_data = pd.read_csv("./data/train.csv")
    
    features = Features
    train_features = train_data[features]
    train_labels = train_data[Lables]
    
    # import ipdb; ipdb.set_trace()
    clf = tree.DecisionTreeClassifier()
    # train
    clf.fit(train_features, train_labels)
    return clf

def test_CLF(clf):
    test_data = pd.read_csv("./data/test.csv")
    features = Features
    test_features = test_data[features]
    pred_labels = clf.predict(test_features)
    # import ipdb; ipdb.set_trace()
    for i, v in enumerate(pred_labels):
        wd = f"预测: {v} | "
        vv = test_data.loc[i]
        for k in vv.keys():
            from data import dict
            wd += f"{dict.DICT[k]}: {test_data.loc[i][k]}   |   "
        
        print(wd)

def save_model(clf, path=PATH):
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
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", type=str, help="train/test/draw/plot 训练/加载已有模型运行/绘制决策树/绘制不同深度决策树分数图")
    args = parser.parse_args()
    if args.mode == "train":
        clf = train_CLF()
        save_model(clf, path=PATH)
    elif args.mode == "test":
        clf_load = load_model(PATH)
        test_CLF(clf_load)
    elif args.mode == "draw":
        clf_load = load_model(PATH)
        draw_graph(clf_load, feature_names=Features, target_names=Targets, pdf_name=PDFName)
    elif args.mode == "plot":
        plot_score("./data/train.csv", "./data/test.csv", 11)