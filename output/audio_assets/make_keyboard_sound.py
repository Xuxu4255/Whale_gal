"""Create a short, original synthesized keyboard-typing effect for the game."""
from pathlib import Path
import wave
import numpy as np
from scipy.signal import butter, sosfilt

ROOT = Path(__file__).resolve().parents[2]
DESTINATION = ROOT / "game/libs/敲键盘.wav"
if DESTINATION.exists():
    raise FileExistsError(DESTINATION)

rate = 44100
duration = 4.2
rng = np.random.default_rng(61106)
audio = np.zeros(round(rate * duration), dtype=np.float64)
filter_sos = butter(2, [700, 10500], btype="bandpass", fs=rate, output="sos")

def strike(start, strength):
    t = np.arange(round(rate * 0.11)) / rate
    noise = sosfilt(filter_sos, rng.normal(size=t.size))
    attack = 1 - np.exp(-t / 0.00045)
    click = noise * np.exp(-t / 0.0045) * 0.50
    body = np.sin(2 * np.pi * rng.uniform(175, 240) * t) * np.exp(-t / 0.018) * 0.33
    shell = np.sin(2 * np.pi * rng.uniform(1300, 2000) * t) * np.exp(-t / 0.007) * 0.14
    key = (click + body + shell) * attack * strength
    offset = round(start * rate)
    count = min(key.size, audio.size - offset)
    if count > 0:
        audio[offset:offset + count] += key[:count]

time = 0.14
count = 0
while time < duration - 0.22:
    strength = rng.uniform(0.58, 0.92)
    strike(time, strength)
    strike(time + rng.uniform(0.035, 0.060), strength * 0.25)
    time += rng.uniform(0.095, 0.18)
    count += 1
    if count % 8 == 0:
        time += 0.21

audio *= 0.63 / max(np.max(np.abs(audio)), 1e-10)
pcm = (np.clip(audio, -1, 1) * 32767).astype("<i2")
with wave.open(str(DESTINATION), "wb") as out:
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(rate)
    out.writeframes(pcm.tobytes())
print(f"Created {DESTINATION.name}: {duration:.1f}s, {rate}Hz, {count} keystrokes")
