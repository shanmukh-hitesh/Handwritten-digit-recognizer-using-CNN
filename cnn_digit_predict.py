import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#Normalize, reshape
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

#CNN model
model = Sequential([
    Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=(28,28,1)),
    MaxPooling2D(pool_size=(2,2)),
    Conv2D(64, kernel_size=(3,3), activation='relu'),
    MaxPooling2D(pool_size=(2,2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

#Train
model.fit(x_train, y_train, epochs=3, validation_data=(x_test, y_test))
path = input("Enter the path to your digit image: ")
img=Image.open(path).convert('L')
img=img.resize((28,28))
img_array=np.array(img).astype('float32')/255.0
plt.imshow(img_array,cmap='gray')
plt.axis('off')
plt.show()
img_input=img_array.reshape(1,28,28,1)
pred=model.predict(img_input)
predicted_digit=np.argmax(pred)
print(f" Predicted Digit: {predicted_digit}")
