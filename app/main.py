from audio_input.audio_input import AudioInputChannel
from audio_output.audio_output import AudioOutputChannel
from audio_processing.audio_processing import AudioProcessing

def main():
    # Configura o canal de entrada de áudio em português
    input_audio_instance_pt = AudioInputChannel(language='pt')
    
    # Configura o serviço de tradução para inglês
    translator_instance = AudioProcessing(target_language='en')
    
    # Configura o canal de saída de áudio em inglês
    output_audio_instance_en = AudioOutputChannel(language='en')

    # Inicia o processo
    print("Iniciando captura de áudio...")
    transcribed_text = input_audio_instance_pt.start()  # Captura e transcreve o áudio
    
    # Traduz o texto transcrito
    translated_text = translator_instance.process_audio(transcribed_text)
    print(f"Texto traduzido: {translated_text}")
    
    # Fala o texto traduzido
    output_audio_instance_en.speak(translated_text)

if __name__ == "__main__":
    main()