import gradio as gr
import tensorflow as tf
import numpy as np
import os
import requests
from tensorflow.keras.preprocessing import image

# Auto-download model from Google Drive if not present
model_path = "image_classifier_model.h5"
gdrive_url = "https://drive.google.com/uc?id=1dAlFElq4-0Y_IwzWcY-xLM8x0rS8IYHz"

if not os.path.exists(model_path):
    print("Downloading model from Google Drive...")
    response = requests.get(gdrive_url)
    with open(model_path, "wb") as f:
        f.write(response.content)
    print("Model downloaded.")

# Load model
model = tf.keras.models.load_model(model_path)

# Class labels
categories = ['daisy', 'dandelion']

# Prediction function
def predict(img):
    img = img.resize((128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)[0]
    return {categories[i]: float(prediction[i]) for i in range(len(categories))}

# Gradio interface
interface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=3),
    title="Plant Image Classifier 🌿",
    description="Upload a leaf image to detect plant type."
)

interface.launch()
