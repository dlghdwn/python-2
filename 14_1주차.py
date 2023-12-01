import pandas as pd

target = "./data/apt.csv"
df = pd.read_csv(target, encoding="CP949")
df.to_csv("./data/apttt.csv", encoding='utf8') 
print(df.head())

# 정렬
#res = df.sort_values(by="지역명",ascending=Ture) #오름
#res = df.sort_values(by="지역명",ascending=False) #내림
#res = df.sort_values("지역명")
#print(res.head(5))

#res = df.sort_values(by="연도")[:5] 
#res = df.sort_values(by="분양가")
#print(res.head(5))

#컬럼이름 출력
#res = df[["지역명", "연도"]]
#res = df[["지역명", "연도","분양가"]]
#res = df[["지역명", "연도","분양가"]][:7]
#res = df.loc[:, ["지역명", "연도"]]
#print(res)

#res = df.iloc[1]
#print(res)

#res = df.loc[:6["지역명","연도"]][:3] #6까지 중 앞 3
#res = df.loc[:6["지역명","연도"]][3:] #3
#print(res)

#필터출력
#res = df.loc[df["지역명"]=="강원"]
#res = df.loc[df["연도"] > 2020]
# #res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]]
#res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]][:10]
#print(res)

df0 = df.copy()
#print(df0)

#인덱스 지정 선택
#res = df.iloc[2]
#res = df.iloc[2][4]
#print(res)

#인덱스 필터
#res = df[df.index > 3560]
#print(res)

#필터
#res = df[df.연도 == 2023]
#res = df[df.월 == 3]
#print(res)

#비트연산 필터
#res = df[(df.연도 == 2023) & (df.지역명 == "서울") 
#res = df[(df.연도 == 2023) & (df.지역명 == "서울") & (df.월 == 7)]
#res = df[(df.연도 == 2023) & (df.지역명 == "서울") & (df.월 == 10)]
#print(res)

#컬럼추가
colums = list(df.columns)
print(colums)
df1 = df.reindex(index=df.index[:7], columns=list(df.columns) + ["extra"])
#print(df)
#print("\n======================\n")
#print(df1)

#print("\n======================\n")
#df1.loc[:6,"extra"] = "0"
#df1.loc[:4,"extra"] = False
#print(df1)

#nan행 제거
df2 = df1.copy() #복사

#res = df2.dropna(how="any")
#res = df2.fillna(value="1234")
#res = df2.fillna(value="1234",inplace=True)
#print(df2)
#print("\n======================\n")
#res = df2.dropna(how="any", inplace=True)
#print(res)
#print("\n======================\n")
#print(df2)

#nan 데이터 출력
#res = pd.isna(df)
#res = pd.isna(df1)
#res = pd.isna(df0)
#res = pd.isna(df2)
#print(res)

#데이터 종류별 출력