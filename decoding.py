from model import get_model, get_processor
import torch

device = "cuda:0" if torch.cuda.is_available() else "cpu"
model = get_model(device=device)
print("model loaded")

processor = get_processor()
print("processor loaded")
print("=" * 80 + "\n")


def transcribe_audio(audio):
    with torch.no_grad():
        model_input = processor(audio, return_tensors="pt", sampling_rate=16000).input_values
        model_output = model(model_input.to(device=device, dtype=torch.float32))
        text = processor.decode(model_output.logits.argmax(dim=-1)[0])

    return text
