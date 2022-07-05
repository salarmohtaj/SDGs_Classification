import pandas as pd

df = pd.read_csv("../Dataset/Test_data.csv")

df.columns = ['id','source', 'header', 'text', 'SDG']
df_without_label = df.drop(columns=["SDG"])
df_without_label.to_csv("../Dataset/Test_data_without_label.csv",index=False)

df_label = df[["id","SDG"]]
df_label.to_csv("../Dataset/Test_data_just_label.csv",index=False)