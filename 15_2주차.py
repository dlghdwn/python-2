import matplotlib.pyplot as plt

#x_years = ['2020', '2021', '2022']
#y_data = [100, 400, 900]

#막대 문양 채우기
#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="/")
#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="/////")
#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="\\\\\")
#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="+")
#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="*")
#plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch=".")

#===========선점도 그래프 그리기==================== 부족

#x = ['2020', '2021', '2022']
#y = [100, 400, 900]

#plt.scatter(1, 1)
#plt.scatter(x+1.5, y+1.5, 100, 2, alpah=0.5)

#컬러맵 설정
#plt.scatter(x+4.5, y+1.5, 200, 4, alpha=0.5, cmap="cividis")
#plt.colorbar()

#==============히스토그램 도수 분표========= 부족
#import numpy as np

#rn = np.randaom.

#plt.hist(rn, bins=10)
#plt.legend()

#그래프 스타일 설정
# 라벨 설정
#plt.hist(rn,  bins=10, label="def") 

# 투명도 설정
#plt.hist(rn,  bins=10, label="def", alpha=0.5)

# 그래프 스타일 설정
#plt.hist(rn,  bins=10, label="def", alpha=0.5, histtype="step")

#===========파이챠트 그리기====================
rate = [30, 40, 20, 10]
labels = ["Alpha", "Beta", "Gamma", "Delta"]

#plt.pie(rate)
#plt.pie(rate, labels=labels)

#퍼센트 표시 
#plt.pie(rate, labels=labels, autopct='%.1d%%')
#plt.pie(rate, labels=labels, autopct='%.1f%%') #float type
#plt.pie(rate, labels=labels, autopct='%.3f%%') #float type, 소수점 3자리까지

#시작각도 설정 (counterclock - true(default) : 반시계방향, false : 시계방향)
#plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=0, counterclock=True)
#plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=0, counterclock=False)
#plt.pie(rate, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False)

#공백 설정
#plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0, 0, 0, 0])
#plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0, 0.2, 0.5, 1])
#plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0.1, 0.1, 0.1, 0.1])
#plt.pie(rate, labels=labels, autopct='%.1f%%', explode=[0.1, 0.1, 0.1, 0.5])

#===========패널 스타일 설정====================
# 사용가능한 스타일 키
#print(plt.style.available)

#plt.plot([2,3,6,7,10], [1,4,5,8,9])
#plt.style.use("bmh")
#plt.style.use("ggplot")
#plt.style.use("classic")
#plt.style.use("Solarize_Light2")
#plt.style.use("dark_background")
#plt.style.use("fast")
#plt.style.use("bmh")
#plt.style.use("bmh")
#plt.style.use("bmh")
#plt.style.use("bmh")



plt.show()