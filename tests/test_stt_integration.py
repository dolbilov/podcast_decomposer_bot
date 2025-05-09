import os

import pytest

from podcast_decomposer_bot import stt


# метка «integration» — такие тесты не будут запускаться по умолчанию
@pytest.mark.integration
def test_whisper_tiny_recognizes_hello(tmp_path):
    stt.load_model("tiny")

    fixtures_dir = os.path.join(os.path.dirname(__file__), "fixtures")
    audio_path = os.path.join(fixtures_dir, "hello.wav")

    if not os.path.exists(audio_path):
        pytest.skip("fixtures/hello.wav not found, skipping integration test")

    text, segments = stt.transcribe(audio_path)

    text = text.lower()
    required_words = ["привет", "кирилл"]
    for required_word in required_words:
        assert (
            required_word in text
        ), f"Expected '{required_word}' in transcript, got: {text!r}"

    assert len(text.strip()) > 0
    # сегменты должны быть списком словарей с ключами start/end/text
    assert isinstance(segments, list) and "text" in segments[0]
