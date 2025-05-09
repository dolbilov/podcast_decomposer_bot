from podcast_decomposer_bot.nlp import quotes


def test_extract_quotes_returns_list_of_sentences(monkeypatch):
    # Пример текста
    text = "Первое предложение. Второе предложение. Третье предложение."

    # Заглушка для summa.summarizer.summarize
    dummy_quotes = ["Первое предложение.", "Второе предложение."]
    import summa.summarizer as summa_summarizer

    monkeypatch.setattr(
        summa_summarizer, "summarize", lambda t, split, words: dummy_quotes
    )

    # Вызываем функцию и проверяем
    result = quotes.extract_quotes(text, words=10)
    assert isinstance(result, list), "Ожидался список"
    assert result == dummy_quotes, "Ожидались цитаты, возвращённые из заглушки"
    # Убедимся, что каждая цитата действительно присутствует в исходном тексте
    for quote in result:
        assert quote in text, f"Цитата {quote!r} должна быть частью исходного текста"
