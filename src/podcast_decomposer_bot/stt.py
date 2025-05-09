import whisper

model = None


def load_model(name: str = "small"):
    global model
    model = whisper.load_model(name)


def transcribe(path: str):
    if model is None:
        load_model()

    result = model.transcribe(path, language="ru")
    return result["text"], result["segments"]
