import cv2
import numpy as np
from tensorflow.keras.applications import DenseNet121
from tensorflow.keras.applications.densenet import preprocess_input
from tensorflow.keras.models import Model

# Load DenseNet121
base_model = DenseNet121(weights='imagenet',
                         include_top=False,
                         pooling='avg')

def extract_features(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    img = preprocess_input(img.astype(np.float32))
    img = np.expand_dims(img, axis=0)

    features = base_model.predict(img)
    return features

if __name__ == "__main__":
    image = "sample.jpg"
    features = extract_features(image)
    print("Feature Vector Shape:", features.shape)
