import pytest


# Перед импортом config нужно установить переменные окружения,
# поэтому очищаем и подменяем их в тесте.
@pytest.fixture(autouse=True)
def clear_env(monkeypatch):
    # Сбрасываем переменные, чтобы не мешали реальные .env
    monkeypatch.delenv("BOT_TOKEN", raising=False)
    monkeypatch.delenv("WHISPER_MODEL", raising=False)
    yield
    # После теста автоматически восстановятся
    # (monkeypatch сам откатит изменения)


def test_default_whisper_model(monkeypatch):
    # Если WHISPER_MODEL не задан, должна использоваться "small"
    # Компонуем окружение без WHISPER_MODEL
    monkeypatch.delenv("WHISPER_MODEL", raising=False)

    from podcast_decomposer_bot.config import config

    assert config.WHISPER_MODEL == "small"


def test_bot_token_loaded(monkeypatch):
    # Подмена переменной окружения BOT_TOKEN
    monkeypatch.setenv("BOT_TOKEN", "test-token-123")

    from podcast_decomposer_bot.config import config

    assert config.BOT_TOKEN == "test-token-123"
    # Если других переменных нет, WHISPER_MODEL всё ещё "small"
    assert config.WHISPER_MODEL == "small"


def test_custom_whisper_model(monkeypatch):
    # Подмена переменной окружения WHISPER_MODEL
    monkeypatch.setenv("WHISPER_MODEL", "tiny")

    from podcast_decomposer_bot.config import config

    assert config.WHISPER_MODEL == "tiny"
