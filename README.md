# 🌿 Plant Disease Image Classifier

This is a deep learning-based image classifier that detects different types of plant diseases from leaf images using a Convolutional Neural Network (CNN). It was developed using TensorFlow and deployed using Gradio.

✅ Built as part of an internship project by **Ansal CM**.

---

## 🚀 Live Demo (Hugging Face)

👉 [Try the Deployed Model on Hugging Face](https://huggingface.co/spaces/ansalcm/image-classifier)

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

🔗 **[Download image_classifier_model.h5 from Google Drive](https://drive.google.com/uc?id=1dAlFElq4-0Y_IwzWcY-xLM8x0rS8IYHz)**

After downloading, place the file in the same folder as `app.py`.

---

## 🧠 Model Details

- Framework: TensorFlow / Keras
- Input size: 128 × 128
- Output: Softmax probabilities for each class
- Activation: ReLU + Softmax
- Trained on: Leaf images from Kaggle dataset

---

## ▶️ How to Run the App Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/plant-disease-classifier.git
cd plant-disease-classifier
