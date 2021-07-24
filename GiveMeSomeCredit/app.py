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
        if result_input['Prediction'].values == 0:
            st.error('The Customer will churn')
        else:
            st.success('The Customer will not churn')

        X = result_input[result_input.Prediction == 0 ][column_name]
        y = result_input['Prediction']
        #if y.values == 0:
        change, proba, state = recommendation(X,model)
        st.write(
            "**To prevent the churn, please consider the below actions:**\n""\n"
            "I don't know what is this: {}\n""\n"
            "I don't know what is this: {}\n""\n"
            .format(change, proba))

    uploaded_file = st.file_uploader('Choose a CSV file')
    print (uploaded_file)
    if st.button("Predict using CSV file"):
      if uploaded_file is not None:
        result = prediction(uploaded_file,model)
        n = (result['Prediction'].values == 0).sum()
        if n > 0:
          st.error(f'{n} customer(s) will churn')
        else:
          st.success('The Customer will not churn')

        st.dataframe(result[result.Prediction == 0 ])
        X = result[result.Prediction == 0 ][column_name]
        y = result['Prediction']
        print(X)
        for i in range(X.shape[0]) :
            change, proba, state = recommendation(X.iloc[i],model)
            st.write(
              "**To prevent the churn, please consider the below actions:**\n""\n"
              "I don't know what is this: {}\n""\n"
              "I don't know what is this: {}\n""\n"
              .format(change, proba))
        #st.success('The output is {}'.format(result.Prediction))
if __name__=='__main__':
    main()
