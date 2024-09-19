import pandas as pd 
df_titanic = pd.read_excel("titanic_passenger_data.xlsx")
gender_count = df_titanic['sex'].countvalue()
gender_count