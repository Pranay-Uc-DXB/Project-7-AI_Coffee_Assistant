import os
import numpy as np
from scipy.io import wavfile
from faster_whisper import WhisperModel
import speech_recognition as sr
import T_T_S as vs
from rag.S_T_T import AIVoiceAssistant
import torch

# The main components of the script are:

# Audio recording and processing
# Speech-to-text transcription using the Whisper model
# AI processing of the transcribed text
# Text-to-speech conversion of the AI's response



DEFAULT_MODEL_SIZE = "medium"
DEFAULT_CHUNK_LENGTH = 10

ai_assistant = AIVoiceAssistant()
num_cores = os.cpu_count()

def is_silence(data, max_amplitude_threshold=3000):
    """Check if audio data contains silence."""
    max_amplitude = np.max(np.abs(data))
    return max_amplitude <= max_amplitude_threshold

def record_audio_chunk(recognizer, source, chunk_length=DEFAULT_CHUNK_LENGTH):
    try:
        audio = recognizer.record(source, duration=chunk_length)
        temp_file_path = 'temp_audio_chunk.wav'
        with open(temp_file_path, "wb") as f:
            f.write(audio.get_wav_data())

        # Check if the recorded chunk contains silence
        try:
            samplerate, data = wavfile.read(temp_file_path)
            if is_silence(data):
                os.remove(temp_file_path)
                return True
            else:
                return False
        except Exception as e:
            print(f"Error while reading audio file: {e}")
            return False
    except sr.WaitTimeoutError:
        print("No speech detected")
        return True

def transcribe_audio(model, file_path):
    segments, info = model.transcribe(file_path, beam_size=7)
    detected_language = info.language
    transcription = ' '.join(segment.text for segment in segments)
    return detected_language, transcription


def main():
    model_size = DEFAULT_MODEL_SIZE
    # Change the model initialization to use GPU
    model = WhisperModel(model_size, device="cuda", compute_type="float16")
    
    #print(torch.cuda.get_device_name(0))
    print(f"Is CUDA Availble?",torch.cuda.is_available())
    
    
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    customer_input_transcription = ""

    try:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")

            while True:
                chunk_file = "temp_audio_chunk.wav"
                print("Listening...")
                

                if not record_audio_chunk(recognizer, source):
                    # Transcribing audio
                    
                    detected_language, transcription = transcribe_audio(model, chunk_file)
                    os.remove(chunk_file)
                    #print("Detected Lang:{}".format(detected_language))
                    print("Customer:{}".format(transcription))
                    
                    # Adding customer input to transcript
                    customer_input_transcription += "Customer: " + transcription + "\n"
                    
                    # Processing customer input and getting response from AI assistant
                    output = ai_assistant.interact_with_llm(transcription)
                    if output:                    
                        output = output.lstrip()
                        vs.multilingual_text_to_speech(output, detected_language)

    except KeyboardInterrupt:
        print("\nStopping...")

if __name__ == "__main__":
    main()    





# import os
# import numpy as np
# from scipy.io import wavfile
# from faster_whisper import WhisperModel
# import speech_recognition as sr

# import voice_service as vs
# from rag.AIVoiceAssistant import AIVoiceAssistant

# DEFAULT_MODEL_SIZE = "medium"
# DEFAULT_CHUNK_LENGTH = 10

# ai_assistant = AIVoiceAssistant()
# num_cores = os.cpu_count()

# def is_silence(data, max_amplitude_threshold=3000):
#     """Check if audio data contains silence."""
#     max_amplitude = np.max(np.abs(data))
#     return max_amplitude <= max_amplitude_threshold

# def record_audio_chunk(recognizer, source, chunk_length=DEFAULT_CHUNK_LENGTH):
#     try:
#         audio = recognizer.record(source, duration=chunk_length)
#         temp_file_path = 'temp_audio_chunk.wav'
#         with open(temp_file_path, "wb") as f:
#             f.write(audio.get_wav_data())

#         # Check if the recorded chunk contains silence
#         try:
#             samplerate, data = wavfile.read(temp_file_path)
#             if is_silence(data):
#                 os.remove(temp_file_path)
#                 return True
#             else:
#                 return False
#         except Exception as e:
#             print(f"Error while reading audio file: {e}")
#             return False
#     except sr.WaitTimeoutError:
#         print("No speech detected")
#         return True

# def transcribe_audio(model, file_path):
#     segments, info = model.transcribe(file_path, beam_size=7)
#     transcription = ' '.join(segment.text for segment in segments)
#     return transcription

# def main():
#     model_size = DEFAULT_MODEL_SIZE
#     model = WhisperModel(model_size, device="cpu", compute_type="int8", cpu_threads=num_cores // 2, num_workers=num_cores // 2)

#     recognizer = sr.Recognizer()
#     microphone = sr.Microphone()

#     customer_input_transcription = ""

#     try:
#         with microphone as source:
#             recognizer.adjust_for_ambient_noise(source)
#             print("Listening...")

#             while True:
#                 chunk_file = "temp_audio_chunk.wav"
                
#                 print("_")
#                 if not record_audio_chunk(recognizer, source):
#                     # Transcribe audio
#                     transcription = transcribe_audio(model, chunk_file)
#                     os.remove(chunk_file)
#                     print("Customer:{}".format(transcription))
                    
#                     # Add customer input to transcript
#                     customer_input_transcription += "Customer: " + transcription + "\n"
                    
#                     # Process customer input and get response from AI assistant
#                     output = ai_assistant.interact_with_llm(transcription)
#                     if output:                    
#                         output = output.lstrip()
#                         vs.multilingual_text_to_speech(output, 'english')

#     except KeyboardInterrupt:
#         print("\nStopping...")

# if __name__ == "__main__":
#     main()
