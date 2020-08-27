import pandas as pd
import numpy as np
s=pd.Series([10,20,30,'a','Sai'])
print(s)
arr=np.array([10,20,30])
s1 = pd.Series(arr)
s2=pd.Series(arr,index=[100,101,102])
print(s1)
print(s2)
