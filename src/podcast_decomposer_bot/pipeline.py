from podcast_decomposer_bot.audio import ogg_to_wav
from podcast_decomposer_bot.nlp.quotes import extract_quotes
from podcast_decomposer_bot.nlp.summarizer import summarize
from podcast_decomposer_bot.stt import transcribe


def process(input_ogg: str, temp_wav: str):
    ogg_to_wav(input_ogg, temp_wav)
    text, segments = transcribe(temp_wav)
    summary = summarize(text)
    quotes = extract_quotes(text)

    return summary, quotes, segments
