from pydub import AudioSegment


def ogg_to_wav(input_path: str, output_path: str) -> None:
    audio = AudioSegment.from_file(input_path, format="ogg")
    audio = audio.set_frame_rate(16_000).set_channels(1)
    audio.export(output_path, format="wav")
