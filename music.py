import pandas as pd

musicData  = pd.read_csv("June_payment (1).csv")
print(musicData.head())
print(musicData.columns)
print(musicData[["Land","Belopp",'Avrakningsomrade']].head())
print(musicData.loc[3:10,"Belopp"])
print(musicData[musicData["Avr.Omr"]==4])

df_sum_area_contry=musicData.groupby(["Land", "Avrakningsomrade"])["Belopp"].sum()

print("Total revenue per country and avräkningsområde:")
print(df_sum_area_contry)