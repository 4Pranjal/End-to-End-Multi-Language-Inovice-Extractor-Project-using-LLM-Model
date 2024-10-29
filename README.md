# End to End Multi Language Inovice Extractor Project using LLM Model

This is a simple web application built using Streamlit and Google Generative AI (`gemini-pro-vision`) to analyze uploaded images, particularly invoices, and provide relevant responses based on the input prompt. 

## Features
- Users can upload an image in `.jpg`, `.jpeg`, or `.png` format.
- The application sends the uploaded image along with a text prompt to the `gemini-pro-vision` AI model.
- The AI model processes the image and prompt, and then returns a text-based response.

This is a simple web application built using **Streamlit** and **Google Generative AI** (`gemini-pro-vision`) to analyze uploaded images, particularly invoices, and provide relevant responses based on the input prompt. 

## 🚀 Features
- 📂 Upload images in `.jpg`, `.jpeg`, or `.png` format.
- 🧠 Uses Google’s `gemini-pro-vision` AI model to analyze the image and text prompt.
- 💬 Provides text-based responses based on the uploaded image (such as invoices).

## 📋 Requirements

### 🔧 Prerequisites
Before running the application, make sure you have the following dependencies installed:

- 🐍 **Python 3.x**
- **Streamlit**
- **Pillow** (PIL)
- **Google Generative AI SDK**
- **python-dotenv**

You can install the required packages using `pip`:
### 1. Clone the repository
```bash 
git clone https://github.com/4Pranjal/End-to-End-Multi-Language-Inovice-Extractor-Project-using-LLM-Model.git
```

## 2. Set up a Python virtual environment 
   ```bash
   python3 -m venv venv
   ```
or you can use conda to create environment.
On Windows use
   ```bash
venv\Scripts\activate
   ```
## 3. Install dependencies

Open the code folder
```bash
cd code
```
Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## 4. Set up environment variables
Create a .env file in the root directory of your project.
Inside this file, set your Google API key:
To get the API key sign with google account and create a new key from the project.
https://ai.google.dev/aistudio
   ```bash
GOOGLE_API_KEY=your_google_api_key_here
   ```
You can get your API key from the Google Cloud Console.

## 5. Run the applications
You can run  application by navigating to the project folder and executing the following command:
   ```bash
   streamlit run vision.py
   ```

## 🎯 Application Flow
1. The user inputs a text prompt and uploads an an invoice image.
2. Upon clicking the **"Tell me about the image"** button, the application sends the image and prompt to the Google Generative AI model.
3. The AI processes the input and returns a response, which is displayed to the user as per required by the user prompt.

---

## 📂 Code Overview

### `get_gemini_response(input_text, image, prompt)`:
- This function sends the input text, image data, and a predefined prompt to the `gemini-pro-vision` model and returns the response.

### `input_image_setup(uploaded_file)`:
- This function handles the uploaded image file, converts it into the appropriate format, and prepares it for the AI model.

### `Streamlit`:
- Used for creating the web-based user interface, which includes:
  - An input box for text prompts.
  - A file uploader for images.
  - Displaying the output response from the AI model.

---

## 🌐 Screenshot
![i1](https://github.com/user-attachments/assets/15c85b85-e120-47b7-95f0-b082d44fa87d)

---

## 💡 Notes
- Ensure that you have a valid **Google API key** for `gemini-pro-vision` to access the AI model.
- This app is primarily designed to work with **invoices**, but it can be adapted for other use cases by modifying the prompt.

---

## 🛠️ Troubleshooting

- **File upload errors**: Ensure that the file is in a supported format (`.jpg`, `.jpeg`, `.png`).
- **No response from the model**: Double-check your **Google API Key** in the `.env` file to ensure it's valid and correctly loaded.

---

## 👥 Contributing

Contributions are welcome! If you find any issues or want to enhance the code, feel free to open an issue or submit a pull request.

1. **Fork the repository**.
2. **Create a new branch** with a descriptive name:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Commit your changes**:
   ```bash
   git commit -m "Added new feature: your-feature-name"
   ```
6. **Push to the branch**:
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**.

---

## 👤 Credits

This repository is maintained by **4Pranjal**. Feel free to use and modify the code for educational and research purposes.

For any questions or suggestions, you can contact me through my GitHub profile: [@4Pranjal](https://github.com/4Pranjal).

Made with ❤️ by Pranjal Jain
 
---
 
