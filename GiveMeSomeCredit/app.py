import pipeline
from prediction import *
import streamlit as st
import streamlit.components.v1 as components
def main():
      # giving the webpage a title
    st.set_page_config(page_title="GIVE ME SOME CREDIT", page_icon="", layout="wide")
    #st.title("GIVE ME SOME CREDIT") Added the markdown line below as st.title does not allow center-alignment
    st.markdown("<h1 style='text-align: center; color: white;'>GIVE ME SOME CREDIT</h1>", unsafe_allow_html=True)
    st.markdown("""<br>""", unsafe_allow_html=True)
    
    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    #['Customer_Age', 'Dependent_count', 'Education_Level', 'Income_Category',
       #'Months_on_book', 'Total_Relationship_Count', 'Months_Inactive_12_mon',
       #'Contacts_Count_12_mon', 'Credit_Limit', 'Total_Revolving_Bal',
       #'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt', 'Total_Trans_Ct',
       #'Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio']
    Gender = ''
    Marital_Status = ''
    Card_Category = ''
    #Set a default value for least important feature 'Education_Level' to make the UI look beter.
    Education_Level = 'Unknown'
    result_input = pd.DataFrame()
    model = joblib.load('GiveMeSomeCredit/credit_new_model.joblib')
    
    col1,col2,col3,col4,col5 = st.beta_columns([2,3,1,3,2])
    with col1:
        st.write("")
    with col2:
        st.write("_Please enter customer information manually to get prediction._")
        st.write("")
        Customer_Age = st.number_input('Age', min_value=1, max_value=150, value=62, step=1)
        Dependent_count= st.selectbox('Number of dependents',(0,1,2,3,4,5,6,7,8,9))
        #Education_Level= st.selectbox('Education level', ('Uneducated', 'High School', 'College', 'Graduate', 'Post-Graduate', 'Doctorate','Unknown'))
        Income_Category= st.selectbox('Annual income category', ('Less than $40K', '$40K - $60K','$60K - $80K', '$80K - $120K', '$120K +','Unknown'))
        Months_on_book = st.number_input('Membership duration (in Months)', min_value=1, max_value=1000, value=49, step=1)
        Total_Relationship_Count= st.number_input('Number of products held', min_value=1, max_value=1000, value=2, step=1)
        Contacts_Count_12_mon= st.number_input('No. of contacts in the last 12 months',min_value=1, max_value=1000, value=3, step=1)
        Credit_Limit= st.number_input('Credit card credit limit', min_value=1, max_value=100000, value=1438, step=1)
    with col3:
        st.write("")
    with col4:
        st.write("")
        st.write("")
        st.write("")
        Total_Revolving_Bal= st.number_input('Total revolving balance on the Credit Card', min_value=1, max_value=100000, value=1438, step=1)
        Total_Trans_Amt= st.number_input('Total transaction amount (Last 12 months)', min_value=1, max_value=100000, value=692, step=1)
        Total_Trans_Ct= st.number_input('Total transaction count (Last 12 months)', min_value=1, max_value=1000, value=16, step=1)
        Total_Amt_Chng_Q4_Q1= st.number_input('Change in transaction amount (Q4 over Q1)', min_value=0, max_value=100000, value=0, step=1)
        Total_Ct_Chng_Q4_Q1= st.number_input('Change in transaction count (Q4 over Q1)', min_value=0, max_value=100000, value=0, step=1)
        Avg_Utilization_Ratio= st.number_input('Average card utilization ratio', min_value=0.000, max_value=1.000, value=0.996, step=0.001)
        Months_Inactive_12_mon= st.selectbox('No. of months inactive in the last 12 months',(1,2,3,4,5,6,7,8,9,10,11,12))
    with col5:
        st.write("")
    
    st.markdown("""<br>""", unsafe_allow_html=True)
    col1, col2, col3 = st.beta_columns([6,1,6])
    if col2.button("Predict"):
            input_list = [[Customer_Age,Gender,Dependent_count,Education_Level,Marital_Status,Income_Category,Card_Category,Months_on_book,Total_Relationship_Count,
            Months_Inactive_12_mon,Contacts_Count_12_mon,Credit_Limit,Total_Revolving_Bal,Total_Amt_Chng_Q4_Q1,Total_Trans_Amt,
            Total_Trans_Ct,Total_Ct_Chng_Q4_Q1,Avg_Utilization_Ratio]]
            result_input = prediction_input(input_list,model)


    column_name = ['Customer_Age','Gender','Dependent_count','Education_Level','Marital_Status','Income_Category','Card_Category','Months_on_book','Total_Relationship_Count',
    'Months_Inactive_12_mon','Contacts_Count_12_mon','Credit_Limit','Total_Revolving_Bal','Total_Amt_Chng_Q4_Q1','Total_Trans_Amt',
    'Total_Trans_Ct','Total_Ct_Chng_Q4_Q1','Avg_Utilization_Ratio']

     # Store it in the variable "result".
     # 0 = Customer will churn; 1 = Customer will not churn.

    col1, col2, col3 = st.beta_columns([2,7,2])
    with col2:
        if not result_input.empty:
            #result_input = prediction_input(input_list,model)
            if result_input['Prediction'].values == 0:
                st.error('The Customer will churn. Recommendations to prevent churning are below:')
            else:
                st.success('The Customer will not churn.')

            X = result_input[result_input.Prediction == 0 ][column_name]
            y = result_input['Prediction']
            if y.values == 0:
                change, proba, state = recommendation(X,model)
                st.info(
                    "**To prevent the churn, please consider the below actions:**\n""\n"
                    "Encourage the customer to increase Total_Transaction_Amount and Total_Transaction_Count by: {}\n"" %\n"
                    "\nThe new probability of a customer not churning is: {}\n"" %\n"
                    .format(round(change,2), round(proba,2)))

    st.markdown("""<br> <br>""", unsafe_allow_html=True)
    
    col1, col2, col3 = st.beta_columns([2,7,2])
    with col2:
        st.write("_Please upload a CSV file to get prediction for multiple customers._")
        uploaded_file = st.file_uploader('Upload a CSV:')
        print (uploaded_file)
        if st.button("Predict using CSV file"):
            if uploaded_file is not None:
                result = prediction(uploaded_file,model)
                n = (result['Prediction'].values == 0).sum()
                if n > 0:
                    st.error(f'{n} customer(s) will churn')
                    #st.dataframe(result[result.Prediction == 0 ])
                    X = result[result.Prediction == 0 ][column_name]
                    y = result['Prediction']
                    for i in range(X.shape[0]) :
                        change, proba, state = recommendation(X.iloc[[i]],model)
                        st.dataframe(X.iloc[[i]])
                        st.info(
                            "**To prevent the churn of this customer, please consider the below actions:**\n""\n"
                            "Encourage the customer to increase Total_Transaction_Amount and Total_Transaction_Count by: {}\n%\n""\n"
                            "The new probability of a customer not churning is: {}\n%\n"
                            "*************************************************************"
                            .format(round(change,2), round(proba,2)))
                else:
                    st.success('The Customer will not churn')

        #st.success('The output is {}'.format(result.Prediction))
if __name__=='__main__':
    main()
