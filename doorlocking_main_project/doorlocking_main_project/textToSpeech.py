import pyttsx3
# initialize Text-to-speech engine
engine = pyttsx3.init()
# convert this text to speech
text = "welcome kiran"
engine.say(text)
# play the speech
engine.runAndWait()