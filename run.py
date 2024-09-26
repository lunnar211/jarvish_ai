 

# import multiprocessing
# import subprocess

# # To run Jarvis
# def startJarvis():
#         # Code for process 1
#         print("Process 1 is running.")
#         from main import start
#         start()

# # To run hotword
# def listenHotword():
#         # Code for process 2
#         print("Process 2 is running.")
#         from engine.features import hotword
#         hotword()


#     # Start both processes
# if __name__ == '__main__':
#         p1 = multiprocessing.Process(target=startJarvis)
#         p2 = multiprocessing.Process(target=listenHotword)
#         p1.start()
#         p2.start()
#         p1.join()

#         if p2.is_alive():
#             p2.terminate()
#             p2.join()

#         print("system stop")
import multiprocessing
import subprocess
import time
from engine.features import playAssistantSound, speak

# To run Jarvis
def startJarvis():
    # Process 1: Jarvis system
    print("Process 1 is running: Starting Jarvis.")
    from main import start
    start()

# To run hotword detection
def listenHotword():
    # Process 2: Hotword detection
    print("Process 2 is running: Listening for hotword.")
    
    try:
        import pvporcupine
        import pyaudio
        
        # Initialize Porcupine with your Access Key and the hotword model
        access_key = "qn6kWxW77ODH75DcpCKZPuENv/JNU5LHWgzi4tbYQcionvSuPI3Gvg=="
        porcupine = pvporcupine.create(access_key=access_key, keyword_paths=['porcupine.ppn'])
        
        audio_stream = pyaudio.PyAudio().open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )
        
        print("Listening for hotword...")

        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = [int.from_bytes(pcm[i:i + 2], byteorder='little', signed=True) for i in range(0, len(pcm), 2)]
            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print("Hotword detected!")
                playAssistantSound()  # Play sound when hotword is detected
                speak("How can I assist you?")  # Speak out after detecting the hotword
                time.sleep(1)  # Add delay to simulate task handling

    except ImportError:
        print("Porcupine is not installed. Please install it via 'pip install pvporcupine'")

    except Exception as e:
        print(f"An error occurred in the hotword detection process: {e}")

# Start both processes
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=startJarvis)
    p2 = multiprocessing.Process(target=listenHotword)

    p1.start()
    p2.start()

    p1.join()  # Ensure Jarvis process continues to run

    # If the hotword detection is still running, terminate it cleanly
    if p2.is_alive():
        p2.terminate()
        p2.join()

    print("System stopped.")
