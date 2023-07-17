
from typing import List
import uvicorn
from fastapi import File, FastAPI, UploadFile
import numpy as np
import keras_ocr
import streamlit as st

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}


@app.post("/ocr")
def upload(files: List[UploadFile] = File(...)):
    pipeline = keras_ocr.pipeline.Pipeline()
    images = [np.array(Image.open(file.file)) for file in files]
    prediction = pipeline.recognize(images)
    st.write("Success")
    return "IAMALIVE"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
