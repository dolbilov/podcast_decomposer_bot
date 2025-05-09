import pytest

from podcast_decomposer_bot import stt


class DummyModel:
    def __init__(self):
        self.called_with = None

    def transcribe(self, path, language):
        self.called_with = (path, language)

        return {
            "text": "тестовый текст",
            "segments": [
                {"start": 0.0, "end": 1.2, "text": "тестовый"},
                {"start": 1.2, "end": 2.5, "text": "текст"},
            ],
        }


@pytest.fixture(autouse=True)
def reset_model():
    """Сбрасываем глобальную модель между тестами."""
    stt.model = None
    yield
    stt.model = None


def test_load_model_and_transcribe(monkeypatch, tmp_path):
    # Мокаем whisper.load_model, чтобы он возвращал DummyModel
    monkeypatch.setattr(stt.whisper, "load_model", lambda _: DummyModel())

    # Вызываем transcribe (он сам загрузит модель через load_model)
    text, segments = stt.transcribe("fake_audio.wav")

    # Проверяем, что текст и сегменты получены из DummyModel
    assert text == "тестовый текст"
    assert isinstance(segments, list)
    assert segments == [
        {"start": 0.0, "end": 1.2, "text": "тестовый"},
        {"start": 1.2, "end": 2.5, "text": "текст"},
    ]

    # Проверяем, что модель была загружена именно с именем по умолчанию
    # и что DummyModel.transcribe получил правильный путь и язык
    # (model хранится в stt.model после load_model)
    model_instance = stt.model
    assert isinstance(model_instance, DummyModel)
    assert model_instance.called_with == ("fake_audio.wav", "ru")


def test_transcribe_without_reloading(monkeypatch):
    # Если модель уже загружена, load_model не должен вызываться повторно
    dummy = DummyModel()
    stt.model = dummy

    # Мокаем load_model, чтобы при ошибочном вызове тест упал
    monkeypatch.setattr(
        stt.whisper,
        "load_model",
        lambda _: pytest.skip("load_model shouldn't be called"),
    )

    text, segments = stt.transcribe("another.wav")
    assert text == "тестовый текст"
    assert segments == dummy.transcribe("another.wav", language="ru")["segments"]
