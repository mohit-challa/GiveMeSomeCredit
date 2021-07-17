import joblib
import pandas as pd
df = pd.read_csv('../raw_data/BankChurners.csv')
df.drop(['Attrition_Flag','CLIENTNUM','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2','Avg_Open_To_Buy'],axis=1, inplace=True)
X_test = df.head(1).copy()
model = joblib.load('credit_rf.joblib')
print(model.predict(X_test))

