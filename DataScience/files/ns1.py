import numpy as np
import pandas as pd
import mimetypes


array = np.linspace(start=100,stop=120,num=50)
array = array.reshape(10,5)


new_arr = np.identity(5)

df = pd.DataFrame(data=new_arr, dtype=int)
print(df)

