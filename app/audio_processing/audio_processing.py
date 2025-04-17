from googletrans import Translator

class AudioProcessing:
    def __init__(self, target_language='en'):
        self.target_language = target_language
        self.translator = Translator()

    def process_audio(self, input_text):
        return self.translate_text(input_text)

    def translate_text(self, text):
        try:
            translated = self.translator.translate(text, dest=self.target_language)
            return translated.text
        except Exception as e:
            print(f"Erro ao traduzir texto: {e}")
            return text