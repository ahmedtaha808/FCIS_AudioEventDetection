import wave
from pathlib import Path

DATASET_DIR = Path(r"D:\FCIS\Now\DSP\datasets\dataset")


def inspect_wav_files(root_dir: Path):
    wav_files = sorted(root_dir.rglob("*.wav"))

    if not wav_files:
        print(f"No .wav files found inside '{root_dir}'.")
        return

    sample_rates = set()
    channel_counts = set()
    durations = []

    print(f"{'File':<45} {'Rate (Hz)':>10} {'Ch':>4} {'Duration (s)':>13}")
    print("-" * 76)

    for wav_path in wav_files:
        try:
            with wave.open(str(wav_path), "rb") as wf:
                channels = wf.getnchannels()
                sample_rate = wf.getframerate()
                num_frames = wf.getnframes()
                duration = num_frames / float(sample_rate) if sample_rate > 0 else 0.0

                sample_rates.add(sample_rate)
                channel_counts.add(channels)
                durations.append(duration)

                rel_path = wav_path.relative_to(root_dir)
                print(
                    f"{str(rel_path):<45} {sample_rate:>10} {channels:>4} {duration:>13.2f}"
                )
        except wave.Error as e:
            print(f"{str(wav_path):<45} ERROR reading WAV: {e}")

    print("-" * 76)
    print(f"Total WAV files inspected: {len(wav_files)}")
    print(f"Unique sample rates (Hz):  {sorted(sample_rates)}")
    print(f"Unique channel counts:     {sorted(channel_counts)} (1 = Mono, 2 = Stereo)")
    if durations:
        print(
            f"Duration range (seconds):  {min(durations):.2f}s – {max(durations):.2f}s"
        )


if __name__ == "__main__":
    inspect_wav_files(DATASET_DIR)
