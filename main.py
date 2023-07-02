# TODO: Mettre en place un bouton "Nouvelle prédiction"
import streamlit as st

from ultralytics import YOLO

from PIL import Image
import cv2


def makePrediction(image):
    # Modèle (déjà entrainé)
    model = YOLO("./labos/ultralytics/yolov8n.pt")

    # Prédiction
    result = model(image)

    # Get result image
    result_array = result[0].plot()
    # Fix BGR2RGB issue
    result_rgb = cv2.cvtColor(result_array, cv2.COLOR_BGR2RGB)
    # Save image to PIL format
    result_image = Image.fromarray(result_rgb)

    return result_image


st.title("Upload + Classification Example")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
print("ok")

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image.", use_column_width=True)
    st.write("")
    st.write("Predicting...")

    result_image = makePrediction(image)

    st.image(
        result_image,
        caption="result image with bounding boxes",
        use_column_width=True,
    )
