import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def get_data_using_pandas():
    df = pd.read_csv("'../raw_data/BankChurners.csv'")
    df.drop(['CLIENTNUM','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2','Avg_Open_To_Buy'],
        axis=1, inplace=True)
    return df

def holdout(df):
    X = df.drop('Attrition_Flag', axis=1).copy()
    y = df[['Attrition_Flag']].copy()
    y['Existing Customer'] = LabelEncoder().fit_transform(df['Attrition_Flag'])
    y.drop('Attrition_Flag', axis=1, inplace=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    return X_train, X_test, y_train, y_test


# def save_model_to_gcp():

#     BUCKET_NAME = "le-wagon-data"
#     storage_location = "models/random_forest_model.joblib"
#     local_model_filename = "model.joblib"

#     client = storage.Client()

#     bucket = client.bucket(BUCKET_NAME)

#     blob = bucket.blob(storage_location)

#     blob.upload_from_filename(local_model_filename)
