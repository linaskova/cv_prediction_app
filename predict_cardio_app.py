import streamlit as st
import pickle

st.title('Heart diseases prediction app') 

st.subheader('Данное приложение определяет вероятность сердечно-сосудистых заболеваний в зависимости от ряда признаков. Вам необходимо ввести все признаки ниже') 

def load():
    with open('final_cv_predict_model.pcl','rb') as fid:
        return pickle.load(fid)
    
def add_IMT(x:int, y:int):
    return x/(y**2)
    

age = st.slider('Возраст',0,80, key = 'age')
gender = st.selectbox('Ваш пол', [0,1], key = 'gender')
ap_hi = st.slider('Максимальное давление',60,200, key = 'ap_hi')
ap_lo = st.slider('Минимальное давление',60,200, key = 'ap_lo')
height = st.slider('Рост',120,210, key = 'height')
weight = st.slider('Вес',30,200, key = 'weight')
cholesterol = st.selectbox('Ваш уровень холестерина',[1,2,3,], key = 'cholesterol')
gluc = st.selectbox('Ваш уровень глюкозы',[1,2,3,], key = 'gluc')
smoke = st.checkbox('Вы курите?', key = 'smoke')
alco = st.checkbox('Вы употребляете спиртные напитки?', key = 'alco')
active = st.checkbox('Вы занимаетесь спортом?', key = 'active')

IMT = add_IMT(weight,height)


model = load()
y_pd = model.predict_proba([[age, gender, ap_hi,ap_lo, cholesterol, gluc, smoke, alco, active, IMT]])[0,1]

st.write(f'Ваша вероятность сердечно-сосудистых заболеваний {y_pd}')


st.write(f'При высоких значениях вероятности, постарайтесь снизить максимальное артериальное давление, холестерин. Следите за соотношением вашего роста и веса. С увеличением возраста скрининг необходимо делать чаще.')
