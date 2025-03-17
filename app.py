import streamlit as st
import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load model and processor
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_model()

st.title("Image Captioning with BLIP")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])
text_prompt = st.text_input("Enter a prompt for conditional captioning", "here...")

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Conditional captioning
    inputs = processor(image, text_prompt, return_tensors="pt")
    out = model.generate(**inputs)
    conditional_caption = processor.decode(out[0], skip_special_tokens=True)
    
    # Unconditional captioning
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    unconditional_caption = processor.decode(out[0], skip_special_tokens=True)
    
    st.subheader("Generated Captions")
    st.write(f"**Conditional Caption:** {conditional_caption}")
    st.write(f"**Unconditional Caption:** {unconditional_caption}")