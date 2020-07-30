import pandas as pd
s_attr_methods=set(dir(pd.Series))
print(s_attr_methods)
s_df=set(dir(pd.DataFrame))
print(s_df)
