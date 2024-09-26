
# import os
# import subprocess
# import eel

# from engine.features import *
# from engine.command import *
# from engine.auth import recoganize
# def start():
    
#     eel.init("www")

#     playAssistantSound()
#     @eel.expose
#     def init():
#         subprocess.call([r'device.bat'])
#         eel.hideLoader()
#         speak("Ready for Face Authentication")
#         flag = recoganize.AuthenticateFace()
#         if flag == 1:
#             eel.hideFaceAuth()
#             speak("Face Authentication Successful")
#             eel.hideFaceAuthSuccess()
#             speak("Hello, Welcome Sir, How can i Help You")
#             eel.hideStart()
#             playAssistantSound()
#         else:
#             speak("Face Authentication Fail")
#     os.system('start msedge.exe --app="http://localhost:8000/index.html"')

#     eel.start('index.html', mode=None, host='localhost', block=True)
import os
import eel
import subprocess
from engine.features import playAssistantSound, openCommand, PlayYoutube
from engine.command import speak, takeCommand, processCommand
from engine.auth import recoganize
from engine.network import is_connected
from engine.db import initialize_db

def start():
    eel.init("www")
    
    initialize_db()  # Initialize the database (works offline)

    playAssistantSound()  # Play startup sound
    
    @eel.expose
    def init():
        subprocess.call([r'device.bat'])
        eel.hideLoader()
        speak("Ready for Face Authentication")
        flag = recoganize.AuthenticateFace()

        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Authentication Successful")
            eel.hideFaceAuthSuccess()
            speak("Hello, Welcome Sir, How can I help you?")
            eel.hideStart()

            playAssistantSound()

            # Now listen for voice commands
            command = takeCommand()
            if command:
                processCommand(command)  # Process the voice command
        else:
            speak("Face Authentication Failed")
    
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    
    eel.start('index.html', mode=None, host='localhost', block=True)

if __name__ == "__main__":
    start()
