from pandas import read_csv
from numpy import array
from sys import argv
from sys import exit
from numpy import random

trainFile = argv[1]
testFile = argv[2]
classOptions = argv[3].split(",")
algorithm = argv[4]
parameterDescription = argv[5]

def readData(inFilePath):
    return read_csv(inFilePath, sep='\t', index_col=0)

def predict(algorithm, train_X, train_y, test_X):
    if algorithm == 'adaboost':
        from sklearn.ensemble import AdaBoostClassifier
        clf = AdaBoostClassifier(random_state=R_SEED)
    elif algorithm == 'bagging':
        from sklearn.ensemble import BaggingClassifier
        clf = BaggingClassifier(random_state=R_SEED)
        ####clf = BaggingClassifier(n_estimators=100, random_state=R_SEED)
    elif algorithm == 'decision_tree':
        from sklearn.tree import DecisionTreeClassifier
        clf = DecisionTreeClassifier(random_state=R_SEED)
    elif algorithm == 'extra_trees':
        from sklearn.ensemble import ExtraTreesClassifier
        clf = ExtraTreesClassifier(random_state=R_SEED)
        ####clf = ExtraTreesClassifier(n_estimators=100, random_state=R_SEED)
    elif algorithm == 'gaussian_naivebayes':
        from sklearn.naive_bayes import GaussianNB
        clf = GaussianNB()
    elif algorithm == 'gaussian_process':
        from sklearn.gaussian_process import GaussianProcessClassifier
        clf = GaussianProcessClassifier(random_state=R_SEED)
    elif algorithm == 'gradient_boosting':
        from sklearn.ensemble import GradientBoostingClassifier
        clf = GradientBoostingClassifier(random_state=R_SEED)
        ####clf = ExtraTreesClassifier(n_estimators=100, random_state=R_SEED)
    elif algorithm == 'knn':
        from sklearn.neighbors import KNeighborsClassifier
        clf = KNeighborsClassifier()
    elif algorithm == 'lda':
        from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
        clf = LinearDiscriminantAnalysis()
    elif algorithm == 'logistic_regression':
        from sklearn.linear_model import LogisticRegression
        clf = LogisticRegression(random_state=R_SEED)
    elif algorithm == 'multilayer_perceptron':
        from sklearn.neural_network import MLPClassifier
        clf = MLPClassifier(random_state=R_SEED)
    elif algorithm == 'qda':
        from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
        clf = QuadraticDiscriminantAnalysis()
    elif algorithm == 'random_forest':
        from sklearn.ensemble import RandomForestClassifier
        clf = RandomForestClassifier(random_state=R_SEED)
        ####clf = RandomForestClassifier(n_estimators=100, random_state=R_SEED)
    elif algorithm == 'sgd':
        from sklearn.linear_model import SGDClassifier
        #### It is necessary to use this loss function to produce probabilistic predictions
        clf = SGDClassifier(random_state=R_SEED, loss="modified_huber")
    elif algorithm == 'svm_linear':
        from sklearn.svm import SVC
        clf = SVC(probability=True, random_state=R_SEED, kernel='linear')
    elif algorithm == 'svm_rbf':
        from sklearn.svm import SVC
        clf = SVC(probability=True, random_state=R_SEED, kernel='rbf')
    elif algorithm == 'svm_poly':
        from sklearn.svm import SVC
        clf = SVC(probability=True, random_state=R_SEED, kernel='poly')
    elif algorithm == 'svm_sigmoid':
        from sklearn.svm import SVC
        clf = SVC(probability=True, random_state=R_SEED, kernel='sigmoid')
    elif algorithm == 'svm_nurbf':
        from sklearn.svm import NuSVC
        clf = NuSVC(probability=True, random_state=R_SEED)
    else:
        print "Invalid algorithm: %s" % algorithm
        exit(1)

    clf.fit(train_X, train_y)
    return clf.predict_proba(test_X)

R_SEED = 0
random.seed(R_SEED)

train_df = readData(trainFile)
train_X = train_df.ix[:,:-1].values
train_y = array([classOptions.index(str(y[0])) for y in train_df.loc[:,["Class"]].values.tolist()])

test_X = readData(testFile).values

probs = predict(algorithm, train_X, train_y, test_X)

for i in range(len(probs)):
    iProbs = list(probs[i])

    maxProb = max(iProbs)
    indicesMatchingMax = [i for i in range(len(iProbs)) if iProbs[i]==maxProb]
    random.shuffle(indicesMatchingMax)

    prediction = classOptions[indicesMatchingMax[0]]

    print "%s\t%s" % (prediction, "\t".join(["%.9f" % iProb for iProb in iProbs]))

exit(0)
