import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
def day(date):
    return date.split('/')[1]
def month(date):
    return date.split('/')[0]
def plotter(data,app):
        data["Day"]=data["EXEDATE"].apply(day)
        data["Month"]=data["EXEDATE"].apply(month)
        dict1={'Pass':1,"Fail":0}

        dict2={'End to End':1, 'Cart Updation':2, 'Tag':3, 'login':4, 'Custom Badging':5,
       'Subscribe':6, 'Register':7, 'Promo':8, 'Badging':9, 'Unsubscribe':10}
        dict3={'Data':1, 'Environment':2, '0.0':0, 'Requirement':3, 'Functional':4}
        data["mSTATUS"]=data["STATUS"].map(dict1)
        data["mFunction"]=data["Function"].map(dict2)
        data["mDefect"]=data["Defect"].map(dict3)
        data1=pd.read_csv("future.csv")
 
        x=data[data.AppName=="OnePlan"][["Day","Month","Day Weight"]]
        y=data[data.AppName=="OnePlan"]["mSTATUS"]
        
        
        week_weight={"Sunday":4,"Monday":1,"Tuesday":1,"Wednesday":1,"Thursday":1,"Friday":3,"Saturday":3}
        data1["mWeekDay"]=data1["WeekDay"].map(week_weight)
        
        special_weight={"Christmas":6,"Haloween":4,"Independence Day":4,"New Year":5,"Thanksgiving Week":6}
        data1["mSpecial"]=data1["Special"].map(special_weight)
        data1=data1.fillna(0)
        
        l=len(data1)
        for i in range(l):
            data1.iloc[i,4]=data1.iloc[i,5]+data1.iloc[i,6]
       
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
        data1["Day"]=data["EXEDATE"].apply(day)
        data1["Month"]=data["EXEDATE"].apply(month)
        clf = DecisionTreeClassifier(max_depth=500)
        
        clf = clf.fit(x_train,y_train)
        y_pred = clf.predict(data1[["Day","Month","Day Weight"]])
        data1["mSTATUS"]=y_pred
        revdict={1:"Pass",0:"Fail"}
        data1["STATUS"]=data1["mSTATUS"].map(revdict)
        data=data.set_index(["AppName","EXEDATE"])
        data1=data1.set_index("EXEDATE")
        plt.figure(figsize=(150,15))
        plt.plot(data.loc[("OnePlan",),"STATUS"],color="black")
        plt.plot(data1.loc[:,"STATUS"],color="blue")
        plt.xticks(rotation=90)
        plt.savefig('report/'+app+'.pdf')
        data=data.reset_index()
        data=data.fillna(0)
        clf = DecisionTreeClassifier(max_depth=500)
        x=data[data.AppName=="OnePlan"][["Day","Month","Day Weight","mSTATUS"]]
        y=data[data.AppName=="OnePlan"]["mDefect"]
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
        clf = clf.fit(x_train,y_train)
        data1["mDefect"]=clf.predict(data1[["Day","Month","Day Weight","mSTATUS"]])
        revdict3={1:'Data', 2:'Environment', 0:'Passed', 3:'Requirement', 4:'Functional'}
        data1["Defect"]=data1["mDefect"].map(revdict3)
        data1[["STATUS","Defect"]].to_csv("report/trend_result.csv")
        
                
        
      
        
        
        
        
        
        
        
        
        
        

