"""Runnable Pandas cleaning and aggregation example."""
import pandas as pd

def main():
    df=pd.DataFrame({'city':['A','A','B','B'],'sales':[10,15,8,20],'customer':['x','y','x','z']})
    summary=df.groupby('city',as_index=False)['sales'].agg(total='sum',average='mean')
    print(summary)

if __name__=='__main__': main()
