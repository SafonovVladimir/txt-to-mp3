import pyttsx3
import fitz

s = pyttsx3.init()

with fitz.open("Programming task.pdf") as doc:
    text = ''
    for page in doc.pages(3, 219):
        text += page.get_text()

s.say(text)
s.runAndWait()
