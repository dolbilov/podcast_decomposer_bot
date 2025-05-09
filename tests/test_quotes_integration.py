import pytest

from podcast_decomposer_bot.nlp import quotes

INPUT_TEXT = (
    "Первое предложение теста. "
    "Второе предложение с интересной мыслью. "
    "Третье предложение завершает текст."
)


@pytest.mark.integration
def test_quotes_integration_extracts_actual_sentences():
    extracted = quotes.extract_quotes(INPUT_TEXT, words=20)

    assert isinstance(extracted, list)
    assert extracted, "Список цитат не должен быть пустым"
    # Каждая цитата должна быть точно одним из предложений INPUT_TEXT
    for quote in extracted:
        assert (
            quote in INPUT_TEXT
        ), f"Цитата {quote!r} должна быть частью исходного текста"
