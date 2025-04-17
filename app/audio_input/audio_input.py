import speech_recognition as sr

class AudioInputChannel:
    def __init__(self, language='pt'):
        self.language = language
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def capture_audio(self):
        with self.microphone as source:
            print("Aguardando fala...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        return audio

    def transcribe_audio(self, audio):
        try:
            if self.language == 'pt':
                return self.recognizer.recognize_google(audio, language='pt-BR')
            elif self.language == 'en':
                return self.recognizer.recognize_google(audio, language='en-US')
            else:
                raise ValueError("Idioma não suportado")
        except Exception as e:
            print(f"Erro ao transcrever áudio: {e}")
            return ""

    def start(self):
        while True:
            audio = self.capture_audio()
            transcribed_text = self.transcribe_audio(audio)
            if transcribed_text:
                print(f"Texto transcrito: {transcribed_text}")
                return transcribed_text