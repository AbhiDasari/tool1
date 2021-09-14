print("Reading The Data, Please Wait!!")
import sys
import pandas as pd
import Choice as ch
name=sys.argv[1]

data=pd.read_csv(name)
filereports=[name]
ch.ChoiceMaker(data,filereports)
exit()
