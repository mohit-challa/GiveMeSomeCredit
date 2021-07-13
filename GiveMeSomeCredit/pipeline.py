from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import FunctionTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from imblearn.pipeline import make_pipeline
#from sklearn.pipeline import Pipeline - SMOTE does not work with sklearn pipeline, thus we have used imblearn pipeline
from imblearn.pipeline import Pipeline as imbPipeline
from sklearn.compose import ColumnTransformer
from sklearn.compose import make_column_transformer

categorical_columns = ['Gender', 'Marital_Status']

ordinal_columns = ['Education_Level', 'Card_Category', 'Income_Category']

numerical_columns = ['Customer_Age', 'Dependent_count', 'Months_on_book', 'Total_Relationship_Count',
                     'Months_Inactive_12_mon','Contacts_Count_12_mon','Credit_Limit','Total_Revolving_Bal',
                    'Total_Amt_Chng_Q4_Q1','Total_Trans_Amt','Total_Trans_Ct','Total_Ct_Chng_Q4_Q1',
                    'Avg_Utilization_Ratio']
#Column categories for ordinal encoding
card_category = ['Blue', 'Silver', 'Gold', 'Platinum']
education_category = ['Uneducated', 'High School', 'College', 'Unknown', 'Graduate', 'Post-Graduate', 'Doctorate']
income_category = ['Less than $40K', '$40K - $60K', 'Unknown','$60K - $80K', '$80K - $120K', '$120K +']

def get_pipeline():
    preprocessing = ColumnTransformer(
    [('cat', OneHotEncoder(handle_unknown='ignore'), categorical_columns),
     ('ord', OrdinalEncoder(categories=[education_category, card_category, income_category]), ordinal_columns),
     ('num', StandardScaler(), numerical_columns)])
    smote = SMOTE(random_state=0)
    rf = imbPipeline([
    ('preprocess', preprocessing),
    ('smote', smote),
    ('classifier', RandomForestClassifier(criterion='entropy', min_samples_split=2, n_estimators=500, random_state=42))])
    return rf










