import joblib
import pandas as pd

def prediction_test():
    df = pd.read_csv('../raw_data/BankChurners.csv')
    df.drop(['Attrition_Flag','CLIENTNUM','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2','Avg_Open_To_Buy'],axis=1, inplace=True)
    X_test = df.head(1).copy()
    model = joblib.load('credit_new_model.joblib')
    prediction = model.predict(X_test)
    return prediction

def prediction (test,model):
    df = pd.read_csv(test)
    prediction = model.predict(df)
    df['Prediction'] = prediction
    return df

def prediction_input(input_list,model):
    column_name = ['Customer_Age','Gender','Dependent_count','Education_Level','Marital_Status','Income_Category','Card_Category','Months_on_book','Total_Relationship_Count',
    'Months_Inactive_12_mon','Contacts_Count_12_mon','Credit_Limit','Total_Revolving_Bal','Total_Amt_Chng_Q4_Q1','Total_Trans_Amt',
    'Total_Trans_Ct','Total_Ct_Chng_Q4_Q1','Avg_Utilization_Ratio']
    df = pd.DataFrame(data = input_list, columns= column_name)
    #model = joblib.load('credit_new_model.joblib')
    prediction = model.predict(df)
    df['Prediction'] = prediction
    return df



def recommendation(churning,model):
    churning = churning.iloc[[0]]
    print(churning)
    proba = model.predict_proba(churning)[0][1]*100
    fac = 1
    state = 1
    while proba < 50:
      fac += 0.01
      X_temp = churning
      print(type(X_temp.Total_Trans_Ct.values[0]))
      X_temp.Total_Trans_Ct = X_temp.Total_Trans_Ct.values[0]*fac

      X_temp.Total_Trans_Amt = X_temp.Total_Trans_Amt.values[0]*fac
      proba = model.predict_proba(X_temp)[0][1]*100
      state = model.predict(X_temp)[0]
    change = (fac-1)*100
    return change, proba, state
