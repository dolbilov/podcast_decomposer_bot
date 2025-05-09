from podcast_decomposer_bot.nlp import summarizer


def test_summarize_returns_nonempty_and_shorter(monkeypatch):
    # Длинный входной текст
    input_text = "Длинный текст. " * 20

    # Заглушка для _summarizer
    class DummySummarizer:
        def __call__(self, text, max_length, min_length):
            assert text == input_text
            # Возвращаем список с одним словарём в формате HF-pipeline
            return [{"summary_text": "Краткий итог"}]

    # Мокаем глобальный _summarizer
    monkeypatch.setattr(summarizer, "_summarizer", DummySummarizer())

    output = summarizer.summarize(input_text, max_length=50)

    assert isinstance(output, str), "Ожидалась строка"
    assert output != "", "Резюме не должно быть пустым"
    assert len(output) < len(input_text), "Резюме должно быть короче исходного текста"
