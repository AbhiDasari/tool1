import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import Runner as rn
import Changer as chn
import TrendPlotter as tpl
def analyse(data,choice,filereports):
    
    q1=data.set_index(["AppName","EXEDATE"])
    q1=q1.sort_index()
    print()
    print()
    print("Plotting and Saving Trend Lines for "+str(choice)+ " app, Please Wait!!!")
    tpl.plotter(data,choice)
    
        
    print()
    print()
    print("All files saved!.... Proceeding with further analysis")

    """Second Analysis"""
    q2=data[data.AppName==choice].loc[:,:]

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
    
    print("App analysis done")
    print("The Initial report is generated for version 2.0")
    rerun=input(" Do You want to run the failed versions of app on Another version of Environment(Y/N): ")
    if(rerun.lower()=='y'):
        chn.ChangeInitiater(data[data.AppName==choice],filereports,True,choice)
   
        
