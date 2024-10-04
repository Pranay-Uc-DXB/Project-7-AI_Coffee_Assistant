# Project-7-ASR_Voice_Assistant

In Dubai, UAE, you may have seen one of these coffee robots. This coffee barista is already independent enough but something was missing.... I decided to help her out!



<div align="center">
  <video src=https://github.com/user-attachments/assets/3374d9b5-77cc-4cac-9c4e-45ff0863dcfe width="400" height="100"/>
</div>



## So What's the project about?
This app is about a multilingual AI-powered voice assistant that will be used to provide personalized services to its intended users. To highlight one of the many use cases in the domain of personalized services, I am going to be showcasing a café barista who will be assisting its customers in the following ways:

1)	Greeting the customer
2)	Recording their personal details such as name & number
3)	Showcasing different menu(s) & their respective items
4)	Recording preferences & allergies (if any)
5)	Summarizing their final order with total price
6)	Directing towards payment

The series of steps mentioned above intends to host customers, record their orders, and assist them towards final payment. It is to be noted that this project is a 2-fold AI project where 2 different AI models orchestrate together to provide a seamless customer experience. This 2-fold project consist of the following:

1)	Uses LLM model's respective chat engine to interact and assist with customer queries
2)	Uses an ASR model to detect spoken language and render services in the same language
   
*Please note that this project does not intend to solve a café or customer hosting issue. This app is designed to showcase personalized services. These services can be rendered in almost any industry.*


<img width="992" height="500" alt="image" src="https://github.com/user-attachments/assets/8dbe42a7-2ba5-4746-82e8-306b28eeb146">

This project will be run on-premise using Ollama in synergy with available model libraries within the framework. Below are project's TTS and STT libraries

1)	The speech-to-text library utilizes Whisper Medium V3 from OpenAI to automatically detect spoken language and transcribe it in its respected language
2)	The text-to-speech function intended to use Meta’s powerful language repository (MMS) to translate detected languages back into user’s language for seamless experience, but due to prolific integration issues, Google Translator was ultimately chosen.
3)	Project's chat engine is powered by Llama's latest *3.2 Text Preview* (as of Sep 2024) wrapped by Groq in synergy with RAG to synthesize response
   




