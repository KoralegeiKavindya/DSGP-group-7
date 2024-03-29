import os

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3001",
    "http://localhost:3002",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL1 = tf.keras.models.load_model("../brownspot-identification-tool/models/4")
MODEL2 = tf.keras.models.load_model("../gojarawalu-identification-tool/models/2")
CLASS_NAMES1 = ["Not Brown Spot","Mild Brown Spot", "Severe Brown Spot"]
CLASS_NAMES2 = ["Gojarawalu", "Gojarawalu", "Not Gojarawalu"]

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/brownspot")
async def predict(
    file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)

    predictions = MODEL1.predict(img_batch)

    predicted_class = CLASS_NAMES1[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])*100
    return {
        'classification': predicted_class,
        'confidence': int(confidence)
    }

@app.post("/gojarawalu")
async def predict(
    file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)

    predictions = MODEL2.predict(img_batch)

    predicted_class = CLASS_NAMES2[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])*100
    return {
            'classification': predicted_class,
        'confidence': int(confidence)
    }


if __name__ == "__main__":
    uvicorn.run(app, host='192.168.1.249', port=8000)
