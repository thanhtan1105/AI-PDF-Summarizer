from transformers import T5ForConditionalGeneration, T5Tokenizer
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
class AISummary:
    def __init__(self):
        self.model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-cnn_dailymail")
        self.tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-cnn_dailymail")

    def encode_text(self, text):
        return self.tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1000000, truncation=True)

    def generate_summary(self, inputs):
        return self.model.generate(inputs, max_length=1000000, min_length=100, length_penalty=2.0, num_beams=4, early_stopping=False)

    def decode_summary(self, outputs):
        summary = self.tokenizer.decode(outputs[0])
        return summary
