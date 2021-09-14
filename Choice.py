import Diverter as di
def ChoiceMaker(data,filereports):
    print("Done with data reading, Ready To start Analysis")
    print()
    print()
    

    Choice=input("Which report  you want to generate? (enter choice All/Single) ")
    if(Choice.lower()=="all" or Choice.lower()=="all"):
        di.diverter(data,"all",filereports)
    elif(Choice.lower()=="single"):
        print("These are the apps in the data:")
        print()
        print(list(data["AppName"].unique()))
        AppChoice=input("Which App you want to analyse from the above list( Enter the app name as shown above): ")
        if(AppChoice not in list(data["AppName"].unique())):
            print("App Choice is not in present in data,try again with valid input")
            ChoiceMaker(data,filereports)
            
        di.diverter(data,AppChoice,filereports)
    else:
        print("Not A valid Input, Try Again !")
        
        ChoiceMaker(data,filereports)
        exit()
        
    
