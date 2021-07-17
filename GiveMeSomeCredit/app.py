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
    Customer_Age = st.text_input('Customer_Age', "Type Here")
    Dependent_count= st.text_input('Dependent_count', "Type Here")
    Education_Level= st.text_input('Education_Level', "Type Here")
    Income_Category= st.text_input('Income_Category', "Type Here")
    Months_on_book = st.text_input('Months_on_book', "Type Here")
    Total_Relationship_Count= st.text_input('Total_Relationship_Count', "Type Here")
    Months_Inactive_12_mon= st.text_input('Months_Inactive_12_mon', "Type Here")
    Contacts_Count_12_mon= st.text_input('Contacts_Count_12_mon', "Type Here")
    Credit_Limit= st.text_input('Credit_Limit', "Type Here")
    Total_Revolving_Bal= st.text_input('Total_Revolving_Bal', "Type Here")
    Total_Amt_Chng_Q4_Q1= st.text_input('Total_Amt_Chng_Q4_Q1', "Type Here")
    Total_Trans_Amt= st.text_input('Total_Trans_Amt', "Type Here")
    Total_Trans_Ct= st.text_input('Total_Trans_Ct', "Type Here")
    Total_Amt_Chng_Q4_Q1= st.text_input('Total_Amt_Chng_Q4_Q1', "Type Here")
    Total_Ct_Chng_Q4_Q1= st.text_input('Total_Ct_Chng_Q4_Q1', "Type Here")
    Avg_Utilization_Ratio= st.text_input('Avg_Utilization_Ratio', "Type Here")



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
