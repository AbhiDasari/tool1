import seaborn as sns
import matplotlib.pyplot as plt
def plotter(data,app):
        plt.figure(figsize=(50,15))
        sns.set()
        
        plt.plot(data.loc[(app,),"STATUS"],color="black")
        plt.xticks(rotation=90)
        plt.savefig('report/'+app+'.pdf')
