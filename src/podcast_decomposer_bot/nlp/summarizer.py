from transformers import pipeline

_summarizer = pipeline("summarization", model="IlyaGusev/mbart_ru_sum_gazeta")


def summarize(text: str, max_length: int = 150):
    return _summarizer(text, max_length=max_length, min_length=50)[0]["summary_text"]
