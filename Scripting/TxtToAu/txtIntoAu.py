from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
language = 'en'
sp = gTTS(text="Intentional Love asks you to view your love life as a series of choices rather than accidents", lang=language, slow=False)

sp.save(audio)
playsound(audio)