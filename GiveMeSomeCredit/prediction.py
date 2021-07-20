import joblib
import pandas as pd
def prediction_test():
    df = pd.read_csv('../raw_data/BankChurners.csv')
    df.drop(['Attrition_Flag','CLIENTNUM','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2','Avg_Open_To_Buy'],axis=1, inplace=True)
    X_test = df.head(1).copy()
    model = joblib.load('credit_rf.joblib')
    prediction = model.predict(X_test)
    return prediction

def prediction (test):
    df = pd.DataFrame(test)
    model = joblib.load('credit_rf.joblib')
    prediction = model.predict(df)
    df['Prediction'] = prediction
    return df

def recommodation(churning):
    proba = rf.predict_proba(churning)[0][1]*100
    fac = 1
    while proba < 50:
      fac += 0.01
      X_temp = churning
      X_temp.Total_Trans_Ct = X_temp.Total_Trans_Ct*fac
      X_temp.Total_Trans_Amt = X_temp.Total_Trans_Amt*fac
      proba = rf.predict_proba(X_temp)[0][1]*100
      state = rf.predict(X_temp)[0]
    change = (fac-1)*100
    return change, proba, state
