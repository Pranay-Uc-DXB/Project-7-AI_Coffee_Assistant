from qdrant_client import QdrantClient
from llama_index.llms.ollama import Ollama
from llama_index.core import SimpleDirectoryReader
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core import Settings, VectorStoreIndex
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core.storage.storage_context import StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq

import warnings
warnings.filterwarnings("ignore")




class AIVoiceAssistant:
    def __init__(self):
        # Initialize Qdrant client
        self._qdrant_url = "http://localhost:6333"
        self._client = QdrantClient(url=self._qdrant_url, prefer_grpc=False)

        # Instantiate Groq LLM (Language Model) 
        self._llm = Groq(
            model='llama-3.2-11b-text-preview',  # Update the model name based on Groq specs
            api_key="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",  # API key if required by Groq
            request_timeout=120.0)
        
        self._embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5") #"nomic-embed-text-v1.5"

        # Assign the Groq LLM to Settings
        Settings.llm = self._llm
        Settings.embed_model = self._embed_model

        # Initialize the index and create knowledge base and chat engine
        self._index = None
        self._create_kb()

        # Ensure the index is created before initializing the chat engine
        if self._index is not None:
            self._create_chat_engine()
        else:
            print("Error: Knowledgebase not created. Cannot initialize chat engine.")

    def _create_kb(self):
        try:
            reader = SimpleDirectoryReader(input_files=[r"rag\restaurant_file.txt"])
            documents = reader.load_data()

            # Set up vector store and storage context
            vector_store = QdrantVectorStore(client=self._client, collection_name="kitchen_db")
            storage_context = StorageContext.from_defaults(vector_store=vector_store)

            # Create the index using storage_context
            self._index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)
            print("Knowledgebase created successfully!")
        except Exception as e:
            print(f"Error while creating knowledgebase: {e}")
            self._index = None

    def _create_chat_engine(self):
        # Ensure that the index is valid before proceeding
        if self._index is None:
            raise ValueError("Error: Index is not initialized. Cannot create chat engine.")
        
        # Create the chat engine using the index
        memory = ChatMemoryBuffer.from_defaults(token_limit=1500)
        self._chat_engine = self._index.as_chat_engine(
            chat_mode="context",
            memory=memory,
            system_prompt=self._prompt,)  # Ensure self._prompt is defined somewhere

    def interact_with_llm(self, customer_query):
        AgentChatResponse = self._chat_engine.chat(customer_query)
        answer = AgentChatResponse.response
        return answer

   

    @property
    def _prompt(self):
        return """
            You are a professional female AI Assistant working in Dubai's Finest Beans.
            Provide a short greet to the customer. After the greeting, collect customer's personal information. Questions regarding personal information have been 
            mentioned below in square bracket.

            PLEASE DO NOT ASK ALL THE QUESTIONS AT ONCE. Ask one question at a time and let the customer respond. Then move on to the next question. keep the conversation very short! 

            [ssk for their name, ask for their contact number, ask what menu they would prefer, present the contents of the menu and ask what they would like to order, Ask if they are allergic to anything and whether thay have any special preferences? ]
            
            If you don't know the answer, just say "I  will connect you to an operator", don't try to make up an answer.
            Provide concise and short answers not more than 10 words, and don't chat with yourself!
            """
