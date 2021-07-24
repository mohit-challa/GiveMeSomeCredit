import pipeline
from prediction import *
import streamlit as st
def main():
      # giving the webpage a title
    st.title("Credit card churn prediction")
    st.subheader("_Please fill the fields below with the Customer's information_")
    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    #['Customer_Age', 'Dependent_count', 'Education_Level', 'Income_Category',
       #'Months_on_book', 'Total_Relationship_Count', 'Months_Inactive_12_mon',
       #'Contacts_Count_12_mon', 'Credit_Limit', 'Total_Revolving_Bal',
       #'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt', 'Total_Trans_Ct',
       #'Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio']
    Customer_Age = st.number_input('Age', min_value=1, max_value=150, value=1, step=1)
    Dependent_count= st.selectbox('Number of dependents',(1,2,3,4,5,6,7,8,9))
    Education_Level= st.selectbox('Education level', ('Uneducated', 'High School', 'College', 'Graduate', 'Post-Graduate', 'Doctorate','Unknown'))
    Income_Category= st.selectbox('Annual income category', ('Less than $40K', '$40K - $60K','$60K - $80K', '$80K - $120K', '$120K +','Unknown'))
    Months_on_book = st.number_input('Membership duration (in Months)', min_value=1, max_value=1000, value=1, step=1)
    Total_Relationship_Count= st.number_input('Number of products held', min_value=1, max_value=1000, value=1, step=1)
    Contacts_Count_12_mon= st.number_input('No. of contacts in the last 12 months',min_value=1, max_value=1000, value=1, step=1)
    Credit_Limit= st.number_input('Credit card credit limit', min_value=1, max_value=100000, value=1, step=1)
    Total_Revolving_Bal= st.number_input('Total revolving balance on the Credit Card', min_value=1, max_value=100000, value=1, step=1)
    Total_Trans_Amt= st.number_input('Total transaction amount (Last 12 months)', min_value=1, max_value=100000, value=1, step=1)
    Total_Trans_Ct= st.number_input('Total transaction count (Last 12 months)', min_value=1, max_value=1000, value=1, step=1)
    Total_Amt_Chng_Q4_Q1= st.number_input('Change in transaction amount (Q4 over Q1)', min_value=1, max_value=100000, value=1, step=1)
    Total_Ct_Chng_Q4_Q1= st.number_input('Change in transaction count (Q4 over Q1)', min_value=1, max_value=100000, value=1, step=1)
    Avg_Utilization_Ratio= st.number_input('Average card utilization ratio', min_value=0.000, max_value=1.000, value=0.001, step=0.001)
    Months_Inactive_12_mon= st.selectbox('No. of months inactive in the last 12 months',(1,2,3,4,5,6,7,8,9,10,11,12))
    Gender = ''
    Marital_Status = ''
    Card_Category = ''

    column_name = ['Customer_Age','Gender','Dependent_count','Education_Level','Marital_Status','Income_Category','Card_Category','Months_on_book','Total_Relationship_Count',
    'Months_Inactive_12_mon','Contacts_Count_12_mon','Credit_Limit','Total_Revolving_Bal','Total_Amt_Chng_Q4_Q1','Total_Trans_Amt',
    'Total_Trans_Ct','Total_Ct_Chng_Q4_Q1','Avg_Utilization_Ratio']



    input_list = [[Customer_Age,Gender,Dependent_count,Education_Level,Marital_Status,Income_Category,Card_Category,Months_on_book,Total_Relationship_Count,
    Months_Inactive_12_mon,Contacts_Count_12_mon,Credit_Limit,Total_Revolving_Bal,Total_Amt_Chng_Q4_Q1,Total_Trans_Amt,
    Total_Trans_Ct,Total_Ct_Chng_Q4_Q1,Avg_Utilization_Ratio]]


    model = joblib.load('credit_new_model.joblib')

     # and store it in the variable result
     # Added if statement for improving UI (The customer will (0 churn) (1 not churn)) Mirko
    if st.button("Predict"):
        result_input = prediction_input(input_list,model)
        if result_input['Prediction'] == 0:
            st.success('The Customer will churn')
        else:
            st.success('The Customer will not churn')
        
        X = result_input[column_name]
        y = result_input['Prediction']

        #if y.values == 0:
        change, proba, state = recommendation(X,model)
        st.write('The recommendation is {},{},{}'.format(change, proba, state))




    #dropdown = st.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))



    uploaded_files = st.file_uploader('Choose a CSV file', accept_multiple_files=True)

    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    if st.button("Predict using CSV file"):
        result = prediction(uploaded_files)
        print(result[result.Prediction == 0 ])
        st.success('The output is {}'.format(result.Prediction))

if __name__=='__main__':
    main()
