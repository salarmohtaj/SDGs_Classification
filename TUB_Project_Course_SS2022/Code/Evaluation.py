import pandas as pd
from sklearn.metrics import f1_score, classification_report


solution_df = pd.read_csv("../Dataset/Test_data_just_label.csv")
prediction_df = pd.read_csv("../Dataset/my_test.csv")

merged = pd.merge(solution_df, prediction_df, left_on='id', right_on='id', suffixes=['_ref','_ans'])
if(merged.shape[0] != solution_df.shape[0]):
    print("Something is wrong")
else:
    print(classification_report(merged["SDG_ref"], merged["SDG_ans"]))
    result = f1_score(merged["SDG_ref"], merged["SDG_ans"], average='macro')
    print(f'The macro average F1 is {result*100:.3f}')