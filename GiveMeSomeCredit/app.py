import pipeline
from prediction import *
import streamlit as st
def main():
      # giving the webpage a title
    st.title("Credit card prediction")
    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    #['Customer_Age', 'Dependent_count', 'Education_Level', 'Income_Category',
       #'Months_on_book', 'Total_Relationship_Count', 'Months_Inactive_12_mon',
       #'Contacts_Count_12_mon', 'Credit_Limit', 'Total_Revolving_Bal',
       #'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt', 'Total_Trans_Ct',
       #'Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio']
    Customer_Age = st.text_input('Age as Customer (in Years)', "18")
    Dependent_count= st.text_input('Number of dependents', "2")
    Education_Level= st.selectbox('Educational Qualification of the account holder', ('Uneducated', 'High School', 'College', 'Unknown', 'Graduate', 'Post-Graduate', 'Doctorate'))
    Income_Category= st.selectbox('Annual Income Category of the account holder', ('Less than $40K', '$40K - $60K', 'Unknown','$60K - $80K', '$80K - $120K', '$120K +'))
    Months_on_book = st.text_input('Period of relationship with the bank (in Months)', "12")
    Total_Relationship_Count= st.text_input('Total no. of products held by the customer', "2")
    Contacts_Count_12_mon= st.text_input('No. of Contacts in the last 12 months', "20")
    Credit_Limit= st.text_input('Credit Limit on the Credit Card', "10000")
    Total_Revolving_Bal= st.text_input('Total Revolving Balance on the Credit Card', "20000")
    Total_Amt_Chng_Q4_Q1= st.text_input('Change in Transaction Amount (Q4 over Q1)', "21000")
    Total_Trans_Amt= st.text_input('Total Transaction Amount (Last 12 months)', "20")
    Total_Trans_Ct= st.text_input('Total Transaction Count (Last 12 months)', "1")
    Total_Ct_Chng_Q4_Q1= st.text_input('Change in Transaction Count (Q4 over Q1)', "2")
    Avg_Utilization_Ratio= st.text_input('Average Card Utilization Ratio', "0.8")
    Months_Inactive_12_mon= st.slider('No. of months inactive in the last 12 months',1,12,1)
    Gender = ''
    Marital_Status = ''
    Card_Category = ''





    input_list = [[Customer_Age,Gender,Dependent_count,Education_Level,Marital_Status,Income_Category,Card_Category,Months_on_book,Total_Relationship_Count,
    Months_Inactive_12_mon,Contacts_Count_12_mon,Credit_Limit,Total_Revolving_Bal,Total_Amt_Chng_Q4_Q1,Total_Trans_Amt,
    Total_Trans_Ct,Total_Ct_Chng_Q4_Q1,Avg_Utilization_Ratio]]

     # and store it in the variable result
    if st.button("Predict"):
        result_input = prediction_input(input_list)
        st.success(result_input)

        if result_input == 0:
            if  st.button("Recommodation"):
                change, proba, state = recommodation(result_input)
                st.success('The recommodation is {}'.format(change, proba, state))






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
