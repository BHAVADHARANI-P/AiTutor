# AI Tutor Project

## Overview

AI Tutor is a web-based learning assistant built using Python and Streamlit.
It helps students learn programming, maths, and other subjects using AI-generated explanations and quizzes.

The project uses the Groq API with Llama models to generate fast responses.

---

## Features

* AI-based question answering
* Programming help
* Maths problem solving
* PDF Tutor
* Quiz Generator
* Voice Tutor
* Simple and interactive UI
* Multi-page Streamlit application

---

## Technologies Used

* Python
* Streamlit
* Groq API
* Llama AI Models
* dotenv
* PyPDF2

---

## Project Structure

```text id="1um72r"
ai_tutor_project/
│
├── app.py
├── requirements.txt
├── .env
│
├── pages/
│   ├── pdf_tutor.py
│   ├── quiz.py
│   └── voice_tutor.py
│
├── utils/
│   ├── ai_response.py
│   ├── pdf_reader.py
│   └── quiz_generator.py
```

---

## How It Works

1. User enters a question.
2. Streamlit sends the question to backend Python functions.
3. Groq API processes the request using an AI model.
4. AI-generated answer is displayed instantly.

---

## Applications

* Student learning assistant
* Coding practice helper
* Quiz preparation
* PDF-based learning
* Interactive tutoring system

---

## Future Improvements

* User login system
* Chat history
* Dark mode UI
* More AI models
* Deployment to cloud
* Database integration

---

## Conclusion

AI Tutor is an easy-to-use educational assistant that combines AI and web technologies to provide fast and interactive learning support for students.

## Run Project

```bash
pip install -r requirements.txt
streamlit run app.py
```
