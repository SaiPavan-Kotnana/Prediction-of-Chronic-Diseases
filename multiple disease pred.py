import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models
# path in this format C://Users//name//Desktop//mulitd//saved models//diabetes_model.sav 

diabetes_model = pickle.load(open('E:/Multiple disease prediction system/Project B10/colab files-20230622T140535Z-001/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('E:/Multiple disease prediction system/Project B10/colab files-20230622T140535Z-001/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('E:/Multiple disease prediction system/Project B10/colab files-20230622T140535Z-001/parkinsons_model.sav', 'rb'))


selected = ""
def validate_positive_number(input_string):
  """Returns True if the input string is a valid positive number, False otherwise."""
  try:
    number = float(input_string)
    if number >= 0:
      return True
    else:
      return False
  except ValueError:
    return False

# Validate the input.

def main_menu():
    selected = option_menu('Prediction of Chronic diseases using ML Algorithms',
                          
                          ['Home',
                            'Diabetes Prediction',
                           'Heart Disease Prediction',
                           "Parkinson's Disease Prediction"],
                          icons=['house','activity','heart','person'],
                         default_index=0 )
    return selected

selected=main_menu()

if (selected == 'Home'):
    
    # page title
    st.title('Major project Members')
    
    
    # getting the input data from the user
    col1 ,col2= st.columns(2)

    with col1:
        st.write("Name: M. SWATHI")
    with col2:
        st.write("JNTU no: 20341A04C3")
    with col1:
        st.write("Name: R. KARTHIKEYA")
    with col2:
        st.write("JNTU no: 21345A0411")
    with col1:
        st.write("Name: K. VISHNU VARDHAN")
    with col2:
        st.write("JNTU no: 20341A0496")
    with col1:
        st.write("Name: K. SAI PAVAN")
    with col2:
        st.write("JNTU no: 20341A0491")
    with col1:
        st.write("Name: K. PREM CHAND")
    with col2:
        st.write("JNTU no: 20341A0490")
    with col1:
        st.write("Under guidence of") 
   
    with col2:
        st.write("Name:  Dr. T. PRABHAKAR SIR")  

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction ')

    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        test = st.selectbox('Gender',('0','1','2'),placeholder="select",)

        
        gender =0
        
        # print(gender)    
        # gender = st.text_input('Gender')
        
    with col2:
        age = st.text_input('Age','0')
        
        if not validate_positive_number(age):
            st.error("Please enter a valid age.")
    
    with col3:
        test = st.selectbox('Hypertension',('0','1'),placeholder="select",)
        hypertension = 0
    
    with col1:
         test = st.selectbox('Heart Disease',('0','1'),placeholder="select",)
         heart_disease=0

       
    
    with col2:
        bmivalue = st.text_input('BMI Value')

       
    
    with col3:
        hba1clevel = st.text_input('HBA1C Level')
    
    with col1:
        blood_glucose_level = st.text_input('Blood Glucose Level')
    
    
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[ gender, age, hypertension, heart_disease, bmivalue, hba1clevel, blood_glucose_level]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is prone to diabetes'
        else:
          diab_diagnosis = 'The person is not prone to diabetes'
        
    st.success(diab_diagnosis)



# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        bmivalue = st.text_input('BMI')

    with col2:
        test = st.selectbox('Smoking',('0','1'),placeholder="select",)
        smoking = 0
        
    with col3:
        test = st.selectbox('AlcoholDrinking',('0','1'),placeholder="select",)
        alcoholdrinking =0
    with col1:
        test = st.selectbox('Stroke',('0','1'),placeholder="select",)
        stroke = 0
        
    with col2:
        physicalhealth= st.text_input(' PhysicalHealth')
        
    with col3:
        mentalhealth = st.text_input('MentalHealth')
        
        
    with col1:
        diffwalking = st.text_input('DiffWalking')
        
    with col2:
        test = st.selectbox('Sex',('0','1'),placeholder="select",)

       
        sex =0
        
        
    with col3:
        test = st.selectbox('PhysicalActivity',('0','1'),placeholder="select",)
        physicalactivity = 0
        
    with col1:
        genhealth = st.text_input(' GenHealth')
        
    with col2:
        sleeptime = st.text_input('SleepTime')
        
     
        
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[ float(bmivalue) ,float(smoking) , float(alcoholdrinking), float(stroke),  float(physicalhealth), float(mentalhealth),  float(diffwalking),float(sex),float(physicalactivity),float(genhealth),float(sleeptime)]])   
        # heart_prediction = heart_disease_model.predict([[0,1,2,3,4,5,6,7,8,9,1]])                          

        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is prone to heart disease'
        else:
          heart_diagnosis = 'The person does not prone to any heart disease'
        
    st.success(heart_diagnosis)
        
    
    
    
    

# Parkinson's Prediction Page
if (selected == "Parkinson's Disease Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction ")
    
    col1, col2, col3 = st.columns(3)  
    
    with col1:
        fo = st.text_input('MDVP : Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP : Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP : Flo(Hz)')
        
    with col1:
        nhr = st.text_input('NHR')
        
    with col2:
        hnr = st.text_input('HNR')
        
    with col3:
         dfa = st.text_input('DFA')
        
        
    with col1:
        rpde = st.text_input('RPDE')
        
    with col2:
        spread1 = st.text_input('spread1')
        
    with col3:
        spread2= st.text_input('spread2')
        
   
        
   
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo,nhr, hnr,  rpde,dfa, spread1,spread2]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person is prone to  Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person is not prone to Parkinson's disease"
        
    st.success(parkinsons_diagnosis)


