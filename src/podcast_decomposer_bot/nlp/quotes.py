from summa import summarizer


def extract_quotes(text: str, words: int = 50):
    return summarizer.summarize(text, split=True, words=words)
