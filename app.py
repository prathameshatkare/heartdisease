import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import pickle as pk
import matplotlib.pyplot as plt
from itertools import count
from matplotlib.animation import FuncAnimation

pickle_in = open("Random_trained.pkl","rb")
model = pk.load(pickle_in)


def main():
    #st.title("Heart disease prediction and remedies")
    html_temp="""
    <div style = "background-color:tomato;padding:10px">
    <h2 style="color:white;text-align-center;">Heart disease prediction and remedies ML app </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    #age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
    fbs = 0
    restecg =0
    exang = 0
    slope = 1
    result = ""

    st.write(""" ### Age""")
    age = st.slider("Slide me")
    st.write("""### Sex""")
    sex = st.checkbox("Male")
    sex = st.checkbox("Female")
    if sex == "Female":
        sex = 0
    if sex == "Male":
        sex = 1
    st.write("### Chest Pain Type")
    cp = st.selectbox("Select the suitable option",["Typical Angina","Atypical Angina","Non-Anginal Pain","Asymptomatic"])
    if cp == "Typical Angina":
        cp = 1
    elif cp == "Atypical Angina":
        cp = 2
    elif cp == "Non-Anginal Pain":
        cp = 3
    elif cp == "Asymptomatic":
        cp = 4
    st.write("### Resting Blood Pressure")
    trestbps = st.number_input("Enter the value: ",0,None)
    st.write("### Cholestrol")
    chol = st.number_input("Enter the value:",0,None)
    st.write("### Fasting Blood Sugar")
    fbs1 = st.selectbox("Select the suitable option",["Greater than 120 mg/dl","Less than 120 mg/dl"])
    if fbs1 == "Greater than 120 mg/dl":
        fbs = 1
    elif fbs1 == "Less than 120 mg/dl":
        fbs = 0
    st.write("### Resting Electrocardiographic Results")
    restecg1 = st.selectbox("Select the suitable option",["Normal","ST_T wave abnormality","Showing probable or definite left ventricular hypertrophy by Estes' criteria"])
    if restecg1 == "Normal":
        restecg = 0
    elif restecg1 == "ST_T wave abnormality":
        restecg = 1
    elif restecg1 == "Showing probable or definite left ventricular hypertrophy by Estes' criteria":
        restecg = 2 
    st.write("### Maximum Heart Rate Achieved")
    thalach = st.number_input("Enter the value:",71,202)
    st.write("### Exercise induced angina")
    exang1 = st.selectbox("Select the suitable option",["Yes","No"])
    if exang1 == "Yes":
        exang = 1
    elif exang1 == "No":
        exang = 0 
    st.write("### ST Depression Induced by Exercise Relative to Rest")
    oldpeak = st.number_input("Enter the value:",0.0,None)
    st.write("### The Slope of the Peak Exercise ST Segment")
    slope1 = st.selectbox("Select the suitable option",["Upsloping","Flat","Downsloping"])
    if slope1 == "Upsloping":
        slope = 1
    elif slope1 == "Flat":
        slope = 2
    elif slope1 == "Downsloping":
        slope = 3
    

    
    
    
    #Documentation for webapp usage
    st.sidebar.header("Some Important terms: ")
    st.sidebar.write("""
     
    - **[Chest Pain Type](https://www.heart.org/en/health-topics/heart-attack/angina-chest-pain)** 
    - **[Resting Blood Pressure](https://www.nhs.uk/common-health-questions/lifestyle/what-is-blood-pressure/)**
        - Enter Systolic Value
    - **[Cholesterol](https://www.healthline.com/health/high-cholesterol/levels-by-age)**
        - Enter serum cholestoral in mg/dl
    - **[Fasting Blood Sugar](https://www.mayoclinic.org/diseases-conditions/diabetes/diagnosis-treatment/drc-20371451)**
    - **[Resting Electrocardiographic Results](https://www.healthline.com/health/electrocardiogram#:~:text=An%20electrocardiogram%20is%20a%20simple,electrical%20activity%20of%20your%20heart.)**
    - **[Maximum Heart rate achieved](https://www.hopkinsmedicine.org/health/wellness-and-prevention/understanding-your-target-heart-rate#:~:text=The%20maximum%20rate%20is%20based,or%2085%20beats%20per%20minute.)**
        - Measured per minute.
    - **[Exercise Induced Angina](https://www.mayoclinic.org/diseases-conditions/angina/symptoms-causes/syc-20369373#:~:text=Stable%20angina%20is%20usually%20triggered,arteries%20slow%20down%20blood%20flow.) **
    - **[ST Depression Induced by Exercise Relative to Rest](https://en.wikipedia.org/wiki/ST_depression#:~:text=In%20a%20cardiac%20stress%20test,to%20significantly%20indicate%20reversible%20ischaemia.)**
        - Value found from ECG report
    - **[The Slope of the Peak Exercise ST Segment](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1123032/#:~:text=Normal%20trace%20during%20exercise,exercise%20therefore%20slopes%20sharply%20upwards)**
    
    """)
    # x_value = []
    # y_value = []
    
    #Prediction
    if st.button("Predict"):
        
        result = prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope) 
        if result == 1:
            st.error('Chance of Heart attack')
        else:
            st.success('Not having Heart attack')
        # x_value.append(result)
        # y_value.append(count())


    # Visualization  
    #if st.button("Visualization"):
        # data = np.append(np.array(x_value), np.array(y_value))
        # st.line_chart(data)
    
    #Remedies
    if st.button("Remedies"):
        if cp == 1 or cp == 2 or cp == 3:
            st.write("""
            **Occurance of Chest Pain:**
         - If you smoke, stop smoking. Avoid exposure to secondhand smoke.
         - Angina is often brought on by exertion, it's helpful to pace yourself and take breaks.
         - Limit alcohol consumption to two drinks or fewer a day for men, and one drink a day or less for women.
         - Consult a doctor.
         """)
        if trestbps >=140:
            st.write("""
            **High Resting Blood Pressure:** 
        - Stop smoking.
        - Limit alcohol and sodium content in your food.
        - Keep your weight at check
        - Take breaks and avoid stress.
        """)
        if chol>=200:
            st.write("""
            **High Cholesterol level:**
        - Exercise regualrly for atleast 30 minutes everyday.
        - Monounsaturated fat, found in olive and canola oils is a healthier option.
         """)
        if fbs == 1 :
            st.write("""
            **High fasting blood sugar:**
        - If you take diabetes medicine, change the timing or type by consulting a doctor
        - Take lighter breakfast.
        - Choose food with low glycemic value
         """)
        if thalach> 220-age:
            st.write("""
            **Relatively high maximum heart rate achieved:**
            - Reduce coffee, tea and soda consumption.
            - Try and reduce stress.
            - Exercise regularly.
             """)
        if exang == 1:
            st.write("""
            **Occurance of exercise induced angina** 
            - Consult a doctor.
            """)



def prediction(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope):

    predicted_output = model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope]])
    print(predicted_output)
    return(predicted_output)


if __name__ == '__main__':
        main()

