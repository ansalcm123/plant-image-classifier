# 🌿 Plant Disease Image Classifier

This is a deep learning-based image classifier that detects different types of plant diseases from leaf images using a Convolutional Neural Network (CNN). It was developed using TensorFlow, trained in Google Colab, and deployed using Gradio + Hugging Face.

✅ Built as part of an internship project by **Ansal CM**.

---

## 🚀 Live Demo

👉 [🟢 Try the App on Hugging Face Spaces](https://ansalcm-image-classifier.hf.space/?__theme=system&deep_link=gXI3XOzaG8A)

---

## 📓 Google Colab Notebook

🧪 [Open Training Notebook in Google Colab](https://colab.research.google.com/drive/1tCyfHH22Fho_g7qipaWmNjq-lPrp8I9s?usp=sharing)

This notebook contains the full training pipeline for the image classifier including dataset preprocessing, model training, evaluation, and saving.

---

## 📦 Project Contents

| File                        | Description                              |
|-----------------------------|------------------------------------------|
| `app.py`                   | Gradio interface code                    |
| `requirements.txt`         | List of required Python libraries        |
| `README.md`                | You're reading it                        |
| `image_classifier_model.h5`| ⛔ Not included (see below for download) |

---

## 📥 Download the Model (`.h5`)

GitHub does not support large files over 25MB, so the model is hosted externally.

🔗 [Download image_classifier_model.h5 from Google Drive](https://drive.google.com/uc?id=1dAlFElq4-0Y_IwzWcY-xLM8x0rS8IYHz)

After downloading, place the file in the same folder as `app.py`.

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/your-username/plant-disease-classifier.git
cd plant-disease-classifier
pip install -r requirements.txt
python app.py
