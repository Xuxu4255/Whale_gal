from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "output" / "audio_tools"))
from faster_whisper import WhisperModel
import imageio_ffmpeg

analysis = json.loads((ROOT / "output/audio_cleanup/analysis.json").read_text(encoding="utf-8"))
model = WhisperModel("tiny", device="cpu", compute_type="int8", cpu_threads=4,
                     download_root=str(ROOT / "output/audio_tools/models"))
records = []
for record in analysis:
    # Only inspect tracks with a silent gap followed by a final short sound.
    gaps = [s for s in record["tail_silences"] if "end" in s and
            0.3 < record["seconds"] - s["end"] < 6]
    if not gaps:
        continue
    path = ROOT / "game/libs" / record["file"]
    offset = max(0, record["seconds"] - 22)
    tail = ROOT / "output/audio_cleanup" / (path.stem + "_tail.wav")
    subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-hide_banner", "-loglevel", "error",
                    "-nostdin", "-y", "-ss", str(offset), "-i", str(path), "-ac", "1",
                    "-ar", "16000", str(tail)], check=True)
    segments, _ = model.transcribe(str(tail), language="zh", beam_size=5,
                                   condition_on_previous_text=False)
    words = [{"start": round(s.start + offset, 3), "end": round(s.end + offset, 3),
              "text": s.text} for s in segments]
    result = {"file": path.name, "segments": words}
    records.append(result)
    print(json.dumps(result, ensure_ascii=False), flush=True)
(ROOT / "output/audio_cleanup/transcripts.json").write_text(
    json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
