import pandas as pd
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split
from sklearn import metrics
def suggester(file):
    pima=pd.read_csv(file)
   
    dict={'OnePlan':1, 'VPlan':2, 'ICGS':3, 'COEP':4, 'GFIM':5, 'PRS':6, 'WFM':7, 'COEA':8,
       'vATOM':9, 'DNM':10}
    pima['mAppName']=pima['AppName'].map(dict)
    dict1={"Pass":1,"Fail":0}
    pima['mSTATUS']=pima['STATUS'].map(dict1)
    pima['mPASSED']=pima['PASSED'].apply(lambda x: int(x*10))
    pima['mEXEDATE']=pima['EXEDATE'].apply(lambda x: str(x).replace('.',""))
    feature_cols = [ 'mAppName','TCID', 'mSTATUS','mEXEDATE']
    X = pima[feature_cols] # Features
    y = pima.mPASSED # Target variable
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)
    clf = clf.fit(X_train,y_train)
    y_pred = clf.predict(X_test)
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
