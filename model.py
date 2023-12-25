from transformers import Wav2Vec2Processor, AutoModelForCTC

def get_model(device="cpu"):
    return AutoModelForCTC.from_pretrained(
        "jonatasgrosman/wav2vec2-xls-r-1b-russian", 
        cache_dir="huggingface_models"
    ).to(device)


def get_processor():
    return Wav2Vec2Processor.from_pretrained(
        "jonatasgrosman/wav2vec2-xls-r-1b-russian",
        cache_dir="huggingface_models"
    )