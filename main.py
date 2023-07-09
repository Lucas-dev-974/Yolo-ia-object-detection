# TODO: Mettre en place un bouton "Nouvelle prédiction"
import streamlit as st

# from ultralytics import YOLO
from PIL import Image

import cv2


# def trainModel(dataset, fromModel):
#     # Use the model
#     model = YOLO(fromModel)  # pass any model type
#     model.train(epochs=5)
#     metrics = model.val()  # evaluate model performance on the validation set
#     print(metrics)
#     results = model(dataset)  # predict on an image
#     print(results)
#     path = model.export(format="onnx")  # export the model to ONNX format
#     print(path)
#     return model


# def makePrediction(image):
#     # Get model

#     # Prédiction
#     model = trainModel(
#         "./parking-dataset/data.yml", "./pretained-model/detection/yolov8n.pt"
#     )

#     result = model.predict(image)

#     # Get result image
#     result_array = result[0].plot()
#     # Fix BGR2RGB issue
#     result_rgb = cv2.cvtColor(result_array, cv2.COLOR_BGR2RGB)
#     # Save image to PIL format
#     result_image = Image.fromarray(result_rgb)

#     return result_image


st.title("Upload + Classification Example")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image.", use_column_width=True)
    st.write("")
    st.write("Predicting...")

    # result_image = makePrediction(image)

    st.image(
        # result_image,
        image,
        caption="result image with bounding boxes",
        use_column_width=True,
    )
