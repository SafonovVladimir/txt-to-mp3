import pyttsx3

s = pyttsx3.init()
data = "Это обычный текст"
s.say(data)
s.runAndWait()
