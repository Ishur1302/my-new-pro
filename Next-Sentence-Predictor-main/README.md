#  Next Sentence Prediction using Generative AI

This project implements a simple and interactive web app that predicts the **next likely sentence** based on a user-provided input, using the GPT-2 language model. It demonstrates how Generative AI can be applied to **natural language understanding and completion** tasks such as chatbots, content suggestions, and AI writing tools.

---

##  Project Overview

- Input a sentence or phrase
- GPT-2 generates multiple next sentence predictions
- Simple web interface built with **Streamlit**
- Powered by HuggingFace's **Transformers** and **PyTorch**

---

##  Technologies Used

- Python 3.x
- [Streamlit](https://streamlit.io/) – for the interactive web UI
- [HuggingFace Transformers](https://huggingface.co/transformers/) – for using the GPT-2 model
- PyTorch – as the backend framework for model inference

---

##  How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/next-sentence-prediction.git
   cd next-sentence-prediction

Install Dependencies:
pip install streamlit transformers torch

Now run the app:
python -m streamlit run ai.py
