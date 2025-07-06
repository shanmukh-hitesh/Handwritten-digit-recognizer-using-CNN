# Handwritten-digit-recognizer-using-CNN
This project demonstrates a simple Convolutional Neural Network (CNN) that is trained on the MNIST dataset to recognize handwritten digits. It also allows you to input your own digit image (28x28 grayscale) [0-9] and predict the digit using the trained model.
## 📁 Project Structure

```
Handwritten-digit-recognizer-using-CNN/
├── cnn_digit_predict.py      # Python script for training and prediction
├── requirements.txt          # List of required Python packages
├── example_digit.png         # (Optional) Example digit image for testing
└── README.md                 # Project overview and instructions
├── License                   # License allows to view and copy only
```

---

## 🚀 How to Run

### 🔧 1. Clone the repository
```bash
git clone https://github.com/shanmukh-hitsh/Handwritten-digit-recognizer-using-CNN.git
cd Handwritten-digit-recognizer-using-CNN

```

### 🧠 2. Install dependencies
```bash
pip install -r requirements.txt
```

### ▶️ 3. Run the script
```bash
python cnn_digit_predict.py
```
When prompted, enter the full path to your digit image.

---

## 🖼️ Image Requirements
- Format: PNG, JPG, or JPEG
- Type: Grayscale preferred
- Size: Any size (it will be resized to 28x28)

---

## 📊 Model Details
- **Dataset**: MNIST (28x28 grayscale handwritten digits)
- **Architecture**:
  - Conv2D(32) → MaxPooling2D
  - Conv2D(64) → MaxPooling2D
  - Flatten → Dense(128) → Dense(10)
- **Loss**: Sparse Categorical Crossentropy
- **Optimizer**: Adam

---

## ✍️ Author
**Shanmukhananda Hitesh Karri**

---

## 📄 License
This project is licensed under the **Creative Commons BY-ND 4.0** license.  
You may view and share this project with credit, but you may not modify or remix it.

🔗 [View License Details](https://creativecommons.org/licenses/by-nd/4.0/)

---
---
