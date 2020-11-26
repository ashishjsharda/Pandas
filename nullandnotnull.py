import pandas as pd
import numpy as np
ser=pd.Series([1,5,0,-1,np.nan,12])
print(ser)
print(ser.isnull())
print(ser.isna())
print(ser.notnull())

