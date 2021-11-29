import pandas as pd

folder="C:/myPyExcel/"
excel_file=folder+'함수.xlsx'

df=pd.read_excel(excel_file, sheet_name="합계평균개수", skiprows=1, usecols="B:H")

lst1=[]
lst2=[]

df4=df.to_dict('records')

for i in range(0,20):
    if df4[i]['학과']=="컴퓨터공학과":
        lst1.append(df4[i])
    elif df4[i]['학과']=="전자공학과":
        lst2.append(df4[i])


df5=pd.DataFrame(lst1)
df6=pd.DataFrame(lst2)

df5.to_excel(folder+'new_엑셀파일.xlsx',sheet_name='컴공', startrow=1, startcol=1)
df6.to_excel(folder+'new_엑셀파일.xlsx',sheet_name='전자', startrow=1, startcol=1)