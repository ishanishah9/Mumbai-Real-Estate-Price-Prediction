import streamlit as st
import pandas as pd
import numpy as np


def check(text):
    if text=='Yes':
        return 1
    else:
        return 0

import pickle
infile = open('OneHot.pkl','rb')
one_hot = pickle.load(infile)

model=open('RF.pkl','rb')
rf=pickle.load(model)

st.header('Predicting Price')

st.markdown("#### Location")
Location = st.selectbox('Select Location',("Andheri","Bandra","Borivali","Chembur","Dadar","Powai","South Mumbai","Thane"))

st.markdown("#### Area")
Area=st.number_input('Enter in Sqr.ft')

st.markdown("#### No of Bedrooms")
No_of_Bedrooms=st.number_input('Enter No of Bedrooms')

st.markdown("#### Condition")
Condition = st.radio("Is the property New? ", ('Yes', 'No'))
 
st.markdown("#### Lift")
Lift = st.radio("Does the building have a Lift? ", ('Yes', 'No'))

st.markdown("#### Parking")
Parking = st.radio("Does the Building have a Parking'", ('Yes', 'No'))

st.markdown("#### Playing Area")
Playground= st.radio("Does the Building have a Playing area for kids'", ('Yes', 'No'))

st.markdown("#### Club House")
Club_house=st.radio("Does the Building have a Club house'", ('Yes', 'No'))

button=st.button('Predict')


Condition=check(Condition)
Lift=check(Lift)
Parking=check(Parking)
Playground=check(Playground)
Club_house=check(Club_house)


if button:
    if Area==0.00 or No_of_Bedrooms==0.00:
        st.error('Please enter valid Area and No of Bedrooms')
    else:
        
        if Location!="":
            data={'Location':[Location]}
            data1=pd.DataFrame(data)
            predict_1={'L1':[],'L2':[],'L3':[],'L4':[],'L5':[],'L6':[],'L7':[],'L8':[],
                       'Area':[],'N0_beds':[],'New/Resale':[],'Lift':[],'Car_Parking':[],'Playing Ares':[],'Cloubhouse':[]}
            Pred_data=pd.DataFrame(predict_1)
            pred=one_hot.transform(data1).toarray()
            Pred_data = Pred_data.append({'L1':pred[0][0],'L2':pred[0][1],'L3':pred[0][2],'L4':pred[0][3],'L5':pred[0][4],
                                                          'L6':pred[0][5],'L7':pred[0][6],'L8':pred[0][7],
                                                          'Area':Area,'N0_beds':No_of_Bedrooms,
                                                          'New/Resale':Condition,'Lift':Lift,
                                                          'Car_Parking':Parking,
                                                          'Playing Ares':Playground,
                                                          'Cloubhouse':Club_house},ignore_index=True)
            
            Pred_data=Pred_data.append({'L1':pred[0][0],'L2':pred[0][1],'L3':pred[0][2],'L4':pred[0][3],'L5':pred[0][4],
                                                         'L6':pred[0][5],'L7':pred[0][6],'L8':pred[0][7],
                                                         'Area':Area+100,'N0_beds':No_of_Bedrooms,
                                                         'New/Resale':Condition,'Lift':Lift,
                                                         'Car_Parking':Parking,
                                                         'Playing Ares':Playground,
                                                         'Cloubhouse':Club_house},ignore_index=True)
            
            
            predict=rf.predict(Pred_data)
            #st.write(f"{predict[0]}-{predict[1]}")
            #pred_cost1 = round(rf.predict(Pred_data),2)
            cost1=round(predict[0],2)
            cost2=round(predict[1],2)
            if cost1>cost2:
                x=cost2
                cost2=cost1
                cost1=x

            st.success(f"The Minimum Cost Expecteed with the above Facilities is : {cost1} Cr-{cost2} Cr")
        




