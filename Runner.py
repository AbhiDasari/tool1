import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import Changer as ch
import numpy as np
import Generator as gn
import random
import warnings
warnings.filterwarnings('ignore')

def runner(data,version,filereports,apped,choice=""):
    print("Running the app using the version number = "+str(version))
    vs=version.split(".")[1]
    print()
    datam=data[data.STATUS=="Fail"]
    
    def convert(s): 
        
        upd=s[0].split('.')
        
        upd[1]=str(int(upd[1])+int(vs))
        
        s[0]=upd[0]+"."+upd[1]
        str1 = "|" 
        return(str1.join(s))
    l=len(datam)
   
    list1=[]

    for i in range(0,l):
        list1.append(i)  
        
    i=0
    for i in range(int(l/2)):
        y=random.choice(list1)
        
        #datam.iloc[y,4]=convert(datam.iloc[y,4].split('|'))
        datam.iloc[y,2]="Pass"
        list1.remove(y)
    newcol="newrun"+version
    datam[newcol]=list(np.arange(0,l))
    i=0

    for i in range(l):
        
        if(datam.iloc[i,2])=="Fail":
            datam.iloc[i,datam.columns.get_loc(newcol)]=convert(datam.iloc[i,4].split('|'))
        else:
            datam.iloc[i,datam.columns.get_loc(newcol)]=version
        
    
    

    
    datam.to_csv("env"+version+".csv",index=False)
    filereports.append("env"+version+".csv")
    print(filereports)

     


    print("The  Failed apps even after the version upgradtaion to "+version+" are saved in "+version+"_failed.html")
    datam[datam.STATUS=="Fail"].to_html("report/"+version+"_failed.html")
    print("The  Passed apps in this version upgradtaion to "+version+" are saved in "+version+"_passed.html")
    datam[datam.STATUS=="Pass"].to_html("report/"+version+"_passed.html")

    process=input("End The Analysis?(Y/N)")
    if(process=="Y" or process=="y"):
        print("Generating Pass Reports")
        
        if(apped):
            gn.Generatorapp(filereports,choice)
        else:
            gn.Generator(filereports)
      
    else:
       ch.ChangeInitiater(datam[datam.STATUS=="Fail"],filereports,apped,choice)
 
