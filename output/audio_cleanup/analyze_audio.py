from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "output" / "audio_tools"))
import imageio_ffmpeg
from mutagen.mp3 import MP3

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
records = []
for path in sorted((ROOT / "game" / "libs").glob("*.mp3")):
    info = MP3(path).info
    offset = max(0, info.length - 60)
    proc = subprocess.run(
        [ffmpeg, "-hide_banner", "-nostdin", "-ss", str(offset), "-i", str(path),
         "-af", "silencedetect=noise=-40dB:d=0.65", "-f", "null", "-"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True,
    )
    log = proc.stderr.decode("utf-8", "replace")
    silences = []
    for line in log.splitlines():
        match = re.search(r"silence_start: ([\d.]+)", line)
        if match:
            silences.append({"start": round(float(match[1]) + offset, 3)})
        match = re.search(r"silence_end: ([\d.]+).*silence_duration: ([\d.]+)", line)
        if match and silences:
            silences[-1].update(end=round(float(match[1]) + offset, 3), duration=round(float(match[2]), 3))
    records.append({"file": path.name, "seconds": round(info.length, 3),
                    "sample_rate": info.sample_rate, "bitrate": info.bitrate,
                    "tail_silences": silences})

report = ROOT / "output" / "audio_cleanup" / "analysis.json"
report.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(records, ensure_ascii=False, indent=2))
