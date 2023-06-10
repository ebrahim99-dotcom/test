# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 18:21:01 2022

@author: kaza meza
"""

# import numpy as np
# import pandas as pd
# degrees=np.array([75,90,99,70,70,60,65,58,74,69,83,18,72,54,69,87,56,98,25,66,55,99,33,17,69.96]).reshape(5,5)
# # y=len(degrees)
# # print(y)
# stu_name=['mohamed','ali','amr','omar','jo']
# subjects=['math','english','arabic','physics','chemistry']
# df=pd.DataFrame(degrees,index= stu_name,columns=subjects)
# print(df)
# import pandas as pd
# x=pd.Series({'amr':30,'hossam':70,'amir':55,'mody':70})
# y=pd.Series({'amr':38,'hossam':90,'amir':95,'mody':70})
# z=pd.Series({'amr':36,'hossam':85,'amir':68,'mody':57})
# f=pd.Series({'amr':90,'hossam':80,'amir':59,'mody':14})
# df=pd.DataFrame({'math':x,'english':y,"physics":z,'chmestiry':f})
# df['total']=(df['math']+df['english']+df['physics']+df['chmestiry'])
# a=df.query('math >30 and physics>30')
# print(df)
# print(a)

# print(df['math'])
# print('math' in df.keys())
# print(df.stack())
# print(df.loc['amr':'hossam','math'])'
# print(df.sort_values('math',ascending=(False)))
import pandas as pd
def df(ind,cols):
    data={c:[str(c)+str(i)for i in ind]for c in cols}
    a=pd.DataFrame(data,ind)
    return a
print(df(range(3),'abc'))
    