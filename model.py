from transformers import Wav2Vec2Processor, AutoModelForCTC

def get_model(device="cpu"):
    return AutoModelForCTC.from_pretrained(
        "YOUR_REPO_ID", 
        cache_dir="huggingface_models"
    ).to(device)


def get_processor():
    return Wav2Vec2Processor.from_pretrained(
        "YOUR_REPO_ID",
        cache_dir="huggingface_models"
    )
