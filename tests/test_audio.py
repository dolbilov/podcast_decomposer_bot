from pydub import AudioSegment
from pydub.generators import Sine

from podcast_decomposer_bot.audio import ogg_to_wav


def test_ogg_to_wav(tmp_path):
    # 1. Генерируем 2-секундный чистый тон 440 Hz
    sine = Sine(440).to_audio_segment(duration=2000)

    # 2. Пишем его в .ogg
    ogg_path = tmp_path / "test_tone.ogg"
    sine.export(ogg_path, format="ogg")

    # 3. Запускаем конвертацию в WAV
    wav_path = tmp_path / "test_tone.wav"
    ogg_to_wav(str(ogg_path), str(wav_path))

    # 4. Загружаем полученный WAV и проверяем параметры
    out = AudioSegment.from_file(wav_path, format="wav")
    assert out.frame_rate == 16000, f"Expected 16 kHz, got {out.frame_rate}"
    assert out.channels == 1, f"Expected mono (1 channel), got {out.channels}"
    # Проверим, что длина примерно та же (±10 ms)
    duration_ms = len(out)
    assert 1990 <= duration_ms <= 2010, f"Expected ~2000 ms, got {duration_ms} ms"
