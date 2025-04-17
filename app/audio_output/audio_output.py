import pyttsx3

class AudioOutputChannel:
    def __init__(self, language='en'):
        self.language = language
        self.engine = pyttsx3.init()
        self.set_voice(language)

    def set_voice(self, language):
        voices = self.engine.getProperty('voices')
        
        if language == 'pt':
            for voice in voices:
                if 'brazil' in voice.name.lower():
                    self.engine.setProperty('voice', voice.id)
                    break
        elif language == 'en':
            for voice in voices:
                if 'us' in voice.name.lower():
                    self.engine.setProperty('voice', voice.id)
                    break

    def speak(self, text):
        print(f"Falando: {text}")
        self.engine.say(text)
        self.engine.runAndWait()