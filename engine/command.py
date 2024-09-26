import pyttsx3
import speech_recognition as sr
import eel
import time
def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()


def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
       
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommands(message=1):

    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    try:

        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
        
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp, makeCall, sendMessage
            contact_no, name = findContact(query)
            if(contact_no != 0):
                speak("Which mode you want to use whatsapp or mobile")
                preferance = takecommand()
                print(preferance)

                if "mobile" in preferance:
                    if "send message" in query or "send sms" in query: 
                        speak("what message to send")
                        message = takecommand()
                        sendMessage(message, contact_no, name)
                    elif "phone call" in query:
                        makeCall(name, contact_no)
                    else:
                        speak("please try again")
                elif "whatsapp" in preferance:
                    message = ""
                    if "send message" in query:
                        message = 'message'
                        speak("what message to send")
                        query = takecommand()
                                        
                    elif "phone call" in query:
                        message = 'call'
                    else:
                        message = 'video call'
                                        
                    whatsApp(contact_no, query, message, name)

        else:
            from engine.features import chatBot
            chatBot(query)
    except:
        print("error")
    
    eel.ShowHood()
# import pyttsx3
# import speech_recognition as sr

# # Initialize the speech engine
# engine = pyttsx3.init()

# def speak(text):
#     """Use TTS engine to speak the provided text."""
#     engine.say(text)
#     engine.runAndWait()

# def takeCommand():
#     """Listen for a voice command from the user."""
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")
#         command = r.recognize_google(audio, language='en-in')
#         print(f"User said: {command}\n")
#     except Exception as e:
#         print("Say that again please...")
#         return None
#     return command.lower()

# def processCommand(command):
#     """Process the command and distinguish between online and offline tasks."""
#     from engine.features import PlayYoutube, openCommand, searchGoogle
#     from engine.network import is_connected

#     if "play" in command and "on youtube" in command:
#         PlayYoutube(command)
#     elif "open" in command:
#         openCommand(command)
#     elif "search on google" in command:
#         searchGoogle(command)
#     else:
#         if is_connected():
#             speak("Sorry, I didn't understand that. Can I help you with something online?")
#         else:
#             speak("Sorry, I didn't understand that. Try an offline command.")