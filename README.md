# Project-7-ASR_Voice_Assistant

In Dubai, UAE, you may have seen one of these coffee robots. This coffee barista is already independent enough but something was missing.... I decided to help her out!



<div align="center">
  <video src=https://github.com/user-attachments/assets/3374d9b5-77cc-4cac-9c4e-45ff0863dcfe width="400" height="100"/>
</div>



## So What's the Project About?

This app is about a multilingual AI-powered voice assistant that will be used to provide personalized services to its intended users. To highlight one of the many use cases in the domain of personalized services, I am going to be showcasing a café barista who will be assisting its customers in the following ways:

1)	Greeting the customer
2)	Recording their personal details such as name & number
3)	Showcasing different menu(s) & their respective items
4)	Recording preferences & allergies (if any)
5)	Summarizing their final order with total price
6)	Directing towards payment

The series of steps mentioned above intends to host customers, record their orders, and assist them towards final payment. It is to be noted that this project is a 2-fold AI project where 2 different AI models orchestrate together to provide a seamless customer experience. This 2-fold project consist of the following:

1)	Uses an ASR model to detect spoken language and assist with customer queries
2)	Uses LLM model's respective chat engine to interact and render services in the same language
   
*Please note that this project does not intend to solve a café or customer hosting issue. This app is designed to showcase personalized services. These services can be rendered in almost any industry.*

<img width="980"  height="450" alt="image" src="https://github.com/user-attachments/assets/46656188-39ca-421e-a057-392234b1aec2">

This project is run on-premise using Ollama in synergy with available model libraries within the framework. Below are project's TTS and STT libraries

1)	The speech-to-text library utilizes Whisper Medium model from OpenAI to automatically detect spoken language and transcribe it into it's respected language
2)	The text-to-speech function intended to use Meta’s powerful language repository (MMS) to translate detected languages back into user’s language for seamless experience, but due to prolific integration issues, Google Translator was ultimately chosen.
3)	Project's chat engine is powered by Llama's latest *3.2 Text Preview* (as of Sep 2024) wrapped by Groq in synergy with RAG to synthesize response
   
## Project Demo:

Demo Link: https://www.linkedin.com/posts/pranayu_ai-asr-llms-activity-7248904904960884736-WO9n?utm_source=share&utm_medium=member_desktop

## Configuration & Usage:

*Prerequisites such as Ollama, Docker Desktop, & NVIDIA Toolkit are a must*

Start a virtual environment and in the environment do the following:

1) Clone the repo:
   
   git clone https://github.com/Pranay-Uc-DXB/Project-7-AI_Voice_Assistant.git
3) Install the dependencies via the cmd terminal
   
   pip install -r requirements.txt
4) Pull and run the Qdrant database via Docker Desktop
   
   docker pull qdrant/qdrant
   
   docker run -p 6333:6333 qdrant/qdrant
6) Initialize Ollama server in the cmd terminal
   
   Ollama serve
7) Use the cmd terminal where main script is located and run
    
   python app.py    
      


