# Image Captioning Web Application

This is a Streamlit web application that allows users to upload an image and generate captions for it using the BLIP (Bootstrapped Language-Image Pretraining) model. The application provides both unconditional captioning and conditional captioning based on a user-provided prompt.

## Features

- **Upload Image**: Users can upload images in JPG, PNG, or JPEG formats.
- **Unconditional Captioning**: The model generates a caption based only on the image.
- **Conditional Captioning**: Users can provide a text prompt to guide the model in generating a caption.
- **Interactive UI**: Built using Streamlit for an easy-to-use interface.

## Installation

### Prerequisites
Ensure you have Python installed (recommended: Python 3.8 or later).

### Steps
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the application:
   ```sh
   streamlit run app.py
   ```

## Dependencies

The application uses the following Python libraries:
- `streamlit` - For creating the web interface
- `requests` - For making HTTP requests (if needed)
- `PIL (Pillow)` - For handling images
- `transformers` - For using the BLIP model

Install them using:
```sh
pip install streamlit requests pillow transformers
```

## Usage

1. Upload an image by clicking on the **Upload an Image** button.
2. Optionally, enter a prompt for conditional captioning.
3. The model will generate two captions:
   - **Unconditional Caption**: Caption generated without any user input.
   - **Conditional Caption**: Caption generated based on the user's text prompt.
4. The captions will be displayed below the uploaded image.

## Model Used

This application uses the **Salesforce BLIP Image Captioning Model**:
- Model Name: `Salesforce/blip-image-captioning-base`
- Trained on vision-language datasets for generating meaningful captions from images.

## Example Output

**Uploaded Image:** 🖼️

**Conditional Caption:** *"A beautiful sunset over a beach."* (User Prompt: "Describe the scene")

**Unconditional Caption:** *"A sunset over the ocean with waves crashing."*

## Author
Developed by **[Your Name]**.

## License
This project is licensed under the MIT License.

