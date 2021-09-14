import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import TrendPlotter as tpl
import Runner as rn
import seaborn as sns

import Changer as chn
def analyse(data,filereports):
    apps=list(data["AppName"].unique())
    print(apps)
    q1=data.set_index(["AppName","EXEDATE"])
    q1=q1.sort_index()
    print()
    print()
    print("Plotting and Saving Trend Lines for each app, Please Wait!!! ")
    l=len(apps)
    count=0
    for app in apps:
        tpl.plotter(q1,app)
        count+=1
        print(str(int(100/l*count))+"% Done!")
        
    print()
    print()
    print("All files saved!.... Proceeding with further analysis")

    """Second Analysis"""
    q2=data.loc[:,:]

    fail=q2.STATUS=="Fail"
    plt.figure(figsize=(10,10))
    sns.set_palette("pastel")
    sns.countplot("ENV|CODE|DATA|REQ",data=q2,palette="RdBu")
    plt.xticks(rotation=90)
    plt.savefig('report/error_occurence.pdf')
    """textual feed Back"""
    print()
    print()
    print("Top five error occurences are")
    print()
    print()

    print("++++++++++++++++++++++++++++++++++++++")
    print()

    
    print(q2['ENV|CODE|DATA|REQ'].value_counts().head(5))
    print()
    print("++++++++++++++++++++++++++++++++++++++")
    """Thrid Analysis"""
    q3=data

    plt.figure(figsize=(10,10))
    sns.catplot(y='ENV|CODE|DATA|REQ',data=q3,kind='count',row='AppName',height=8.27, aspect=11.7/8.27,palette="GnBu")
    plt.xticks(rotation=90)
    plt.savefig('report/Appwise_error.pdf')
    print("The Initial report is generated for version 2.0")
    rerun=input(" Do You want to run the failed versions of apps on Another version of Environment(Y/N): ")
    if(rerun.lower()=='y'):
        chn.ChangeInitiater(data,filereports,False,"")
  
        
    
