from transformers import (Wav2Vec2ForCTC,Wav2Vec2Processor)
from utils import load_file_to_data, predict
from models import Wav2Vec2ClassificationModel
from processor import CustomWav2Vec2Processor

class SpeechRecognition:

    def __init__(self, lang = 'egy', path = None):
        if path is None:
            model_dir = 'Zaid/wav2vec2-large-xlsr-53-arabic-egyptian'
        else:
            model_dir = path
        self.model = Wav2Vec2ForCTC.from_pretrained(model_dir).to("cuda")
        self.processor = Wav2Vec2Processor.from_pretrained(model_dir)
    
    def transcribe(self, wav_file):
        return predict(load_file_to_data(wav_file), self.model, self.processor)

class SpeechClassification:

    def __init__(self, path = None):
        if path is None:
            dir = 'Zaid/wav2vec2-large-xlsr-dialect-classification'
        else:
            dir = path
        self.model = Wav2Vec2ClassificationModel.from_pretrained(dir).to("cuda")
        self.processor = CustomWav2Vec2Processor.from_pretrained(dir)
    
    def classify(self, wav_file):
        return predict(load_file_to_data(wav_file), self.model, self.processor)
