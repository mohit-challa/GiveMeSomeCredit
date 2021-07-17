import pipeline
import prediction
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
    Customer_Age = st.text_input('Age as Customer (in Years)', "Type Here")
    Dependent_count= st.text_input('Number of dependents', "Type Here")
    Education_Level= st.text_input('Educational Qualification of the account holder', "Type Here")
    Income_Category= st.text_input('Annual Income Category of the account holder', "Type Here")
    Months_on_book = st.text_input('Period of relationship with the bank (in Months)', "Type Here")
    Total_Relationship_Count= st.text_input('Total no. of products held by the customer', "Type Here")
    Months_Inactive_12_mon= st.text_input('No. of months inactive in the last 12 months', "Type Here")
    Contacts_Count_12_mon= st.text_input('No. of Contacts in the last 12 months', "Type Here")
    Credit_Limit= st.text_input('Credit Limit on the Credit Card', "Type Here")
    Total_Revolving_Bal= st.text_input('Total Revolving Balance on the Credit Card', "Type Here")
    Total_Amt_Chng_Q4_Q1= st.text_input('Change in Transaction Amount (Q4 over Q1)', "Type Here")
    Total_Trans_Amt= st.text_input('Total Transaction Amount (Last 12 months)', "Type Here")
    Total_Trans_Ct= st.text_input('Total Transaction Count (Last 12 months)', "Type Here")
    Total_Ct_Chng_Q4_Q1= st.text_input('Change in Transaction Count (Q4 over Q1)', "Type Here")
    Avg_Utilization_Ratio= st.text_input('Average Card Utilization Ratio', "Type Here")



    #dropdown = st.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))



    uploaded_files = st.file_uploader('Choose a CSV file', accept_multiple_files=True)
    result =""
    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(uploaded_files)
        print(result[result.prediction == 0 ])
    st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()
