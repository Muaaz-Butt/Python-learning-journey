import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
news_api = "Your_news_api_key"  # Ensure this is a valid API key

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
  tts = gTTS(text)
  tts.save('temp.mp3')
 
  pygame.mixer.init()
  pygame.mixer.music.load("temp.mp3")
  pygame.mixer.music.play()
 
  while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
   
  os.remove("temp.mp3")
    
def aiProcess(command):
  client = OpenAI(
    api_key = "Your_api_key"      #Generate your own api key for openAI
  )
  completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant, skilled in general tasks like Alexa and Google CLoud"},
    {"role": "user", "content": command}
  ]
  )

  return completion.choices[0].message 
    
def process_command(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in command.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")  
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song}")
    elif "news" in command.lower():
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}"  # Use f-string for URL formatting
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            if articles:
                for article in articles:
                    speak(article.get('title', 'No title available'))
            else:
                speak("No news articles found")
        else:
            speak("Failed to retrieve news")
    else:
      #let openAi handle the request
      output = aiProcess(command)
      speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening....")
                try:
                    audio = r.listen(source, timeout=5, phrase_time_limit=3)
                except sr.WaitTimeoutError:
                    print("Listening timed out while waiting for phrase to start")
                    continue
            word = r.recognize_google(audio)
            print(f"You said: {word}\n")
            if word.lower() == "jarvis":
                speak("Yeah")
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = recognizer.recognize_google(audio)
                    process_command(command)
        except sr.UnknownValueError:
            print("Google Web Speech could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech service; {e}")
