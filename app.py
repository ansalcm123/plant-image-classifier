import gradio as gr
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Load the trained model
model = tf.keras.models.load_model("image_classifier_model.h5")

# Class names (update this list to match your actual categories from /train folder)
categories = ['daisy', 'dandelion']  # 🛠️ EDIT THIS LIST

# Prediction function
def predict(img):
    # Resize image
    img = img.resize((128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)[0]
    confidence_scores = {categories[i]: float(prediction[i]) for i in range(len(categories))}
    return confidence_scores

# Build Gradio interface
interface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=3),
    title="Plant Image Classifier 🌿",
    description="Upload a leaf image to detect the plant disease."
)

# Launch app
interface.launch()
