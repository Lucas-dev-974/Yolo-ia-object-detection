import streamlit as st
from PIL import Image

from ultralytics import YOLO

model = YOLO("./labos/ultralytics/yolov8n.pt")


def makePrediction(image):
    return "prediction"


st.title("Upload + Classification Example")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

print("ok")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    st.write("")
    st.write("Predicting...")
    prediction = makePrediction(uploaded_file)
    st.write(prediction)
    result_prediction_test = model(image)
    st.write(result_prediction_test)
