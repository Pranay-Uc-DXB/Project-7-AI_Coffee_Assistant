import os
import time
from deep_translator import GoogleTranslator
from gtts import gTTS
import pygame

# Function to translate English text to the target language
def translate_text(text, target_lang):
    translator = GoogleTranslator(source='auto', target=target_lang)
    return translator.translate(text)

# Function to convert text to speech using gTTS
def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=lang, slow=False)
    temp_audio_file = "temp_audio.mp3"
    tts.save(temp_audio_file)
    return temp_audio_file

# Function to play the generated audio file using pygame
def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.quit()
    time.sleep(1)
    os.remove(file_path)  # Clean up the temporary audio file

# Supported language codes 
SUPPORTED_LANGS = {
    'en': 'en', #english
    'hi': 'hi', #hindi
    'ar': 'ar', #arabic
    'ru': 'ru', #russian
    'fr': 'fr', #french
    'es': 'es', #spanish
    'de': 'de', #german
    'ml': 'ml', #malayalam
    'zh-CN': 'zh-CN', #Mandarin
    'tr': 'tr', #turkish
}

# Main function to translate and convert text to speech
def multilingual_text_to_speech(text, target_lang):
    if target_lang not in SUPPORTED_LANGS:
        raise ValueError(f"Language '{target_lang}' is not supported.")
    
    # Translate text to the target language
    translated_text = translate_text(text, SUPPORTED_LANGS[target_lang])
    print(f"Translated text: {translated_text}")
    
    # Convert the translated text to speech
    audio_file = text_to_speech(translated_text, SUPPORTED_LANGS[target_lang])
    
    # Play the generated speech
    play_audio(audio_file)

# # Example Check
# if __name__ == "__main__":
#     text = "Welcome to the multilingual text to speech service."
#     target_language = "hindi"  # Choose the target language ('hindi', 'arabic', etc.)
#     multilingual_text_to_speech(text, target_language)


from deep_translator import GoogleTranslator
langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
langs_dict