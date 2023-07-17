import streamlit as st
import keras_ocr
pipeline = keras_ocr.pipeline.Pipeline()
p = "img.jpg"
images = [keras_ocr.tools.read(p)]
prediction = pipeline.recognize(images)
st.write("Success")
print("hello")
