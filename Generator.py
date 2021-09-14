import pandas as pd
import numpy as np
import Zipper as zi
import mailer as mail
import Suggester as su

def Generator(filereports):
    
    COLUMN_NAMES=['AppName','TCID','STATUS','EXEDATE','PASSED']
    temp=pd.DataFrame(columns=COLUMN_NAMES)
    temp1=pd.DataFrame(columns=COLUMN_NAMES)
    
    count=0
    for i in filereports:
        data1=pd.read_csv(i)
        
        passc=data1.STATUS=="Pass"
        if(count==0):
            tempf=data1[passc]
            temp['AppName']=tempf['AppName']
            temp['TCID']=tempf['TCID']
            temp['STATUS']=tempf['STATUS']
            temp['EXEDATE']=tempf['EXEDATE']
            temp['PASSED']=2.0
            count=1
        else:
            temp1['AppName']=data1[passc]['AppName']
            temp1['TCID']=data1[passc]['TCID']
            temp1['STATUS']=data1[passc]['STATUS']
            temp1['EXEDATE']=data1[passc]['EXEDATE']
            temp1['PASSED']=data1[passc][data1.columns[-1]]
            
            temp=pd.concat([temp,temp1])
            temp=temp.dropna()
    temp.to_csv("pass_data.csv",index=False)
    zi.zip()
    mail.sender()
    su.suggester("pass_data.csv")

def Generatorapp(filereports,choice):
    
    COLUMN_NAMES=['AppName','TCID','STATUS','EXEDATE','PASSED']
    temp=pd.DataFrame(columns=COLUMN_NAMES)
    temp1=pd.DataFrame(columns=COLUMN_NAMES)
    
    count=0
    for i in filereports:
        data1=pd.read_csv(i)
        
        passc=data1.STATUS=="Pass"
        if(count==0):
            tempf=data1[passc]
            
            tempr=tempf[tempf["AppName"]==choice]
            temp['AppName']=tempr['AppName']
            temp['TCID']=tempr['TCID']
            temp['STATUS']=tempr['STATUS']
            temp['EXEDATE']=tempr['EXEDATE']
            temp['PASSED']=2.0
            count=1
        else:
            temp1['AppName']=data1[passc]['AppName']
            temp1['TCID']=data1[passc]['TCID']
            temp1['STATUS']=data1[passc]['STATUS']
            temp1['EXEDATE']=data1[passc]['EXEDATE']
            temp1['PASSED']=data1[passc][data1.columns[-1]]
            
            temp=pd.concat([temp,temp1])
            temp=temp.dropna()
    
    temp.to_csv("pass_data.csv",index=False)
    zi.zip()
    mail.sender()
    
    
