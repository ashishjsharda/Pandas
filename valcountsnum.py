import pandas as pd
import numpy as np
arr=np.array([2,4,1,0,1,3,4])
ser=pd.Series(arr)
print(ser.value_counts())
