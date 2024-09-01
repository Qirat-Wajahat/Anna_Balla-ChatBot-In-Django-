# Windows-specific package for text-to-speech
import win32com.client as wc
# Windows-specific package for file management
import pythoncom

# Function for text-to-speech output
def say(query):
    pythoncom.CoInitialize()  # Initialize the COM library
    speaker = wc.Dispatch("SAPI.SpVoice")  # Initialize the SAPI.SpVoice speech engine
    speaker.Voice = speaker.GetVoices("gender=female").Item(0)  # Set voice to female
    speaker.speak(query)  # Speak the provided query

