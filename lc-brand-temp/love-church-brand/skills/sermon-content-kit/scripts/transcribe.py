#!/usr/bin/env python3
"""
Transcribe a sermon video or audio file using faster-whisper.

Usage:
    python transcribe.py <input_file> <output_dir> [--model small]

Outputs:
    <output_dir>/transcript.txt   — human-readable with [MM:SS] timestamps
    <output_dir>/transcript.json  — structured segments (start, end, text)

Accepts: .mp4, .mov, .mkv, .webm (video) or .mp3, .wav, .m4a, .flac, .aac (audio).
Video is converted to 16 kHz mono PCM via ffmpeg before transcription.

First run per environment will download the faster-whisper model (~460 MB for 'small').
Subsequent runs reuse the cached model.

Why faster-whisper and not openai-whisper: CTranslate2 backend runs ~4x faster on CPU
with the same accuracy, which matters when a creative director is waiting for chapters.
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


VIDEO_EXTS = {".mp4", ".mov", ".mkv", ".webm", ".avi"}
AUDIO_EXTS = {".mp3", ".wav", ".m4a", ".flac", ".aac", ".ogg"}


def ensure_wav(input_path: Path, work_dir: Path) -> Path:
    """If input is video or non-wav audio, extract/convert to 16 kHz mono PCM wav.
    If input is already a wav at the right format, return as-is."""
    ext = input_path.suffix.lower()
    if ext not in VIDEO_EXTS and ext not in AUDIO_EXTS:
        raise SystemExit(
            f"Unsupported input format '{ext}'. "
            f"Expected one of: {sorted(VIDEO_EXTS | AUDIO_EXTS)}"
        )

    wav_path = work_dir / "sermon_audio.wav"
    print(f"[transcribe] Extracting audio → {wav_path}", file=sys.stderr)
    cmd = [
        "ffmpeg",
        "-y",
        "-i", str(input_path),
        "-vn",
        "-ac", "1",
        "-ar", "16000",
        "-c:a", "pcm_s16le",
        str(wav_path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stderr[-2000:], file=sys.stderr)
        raise SystemExit("ffmpeg failed. Is it installed? `apt-get install ffmpeg`")
    return wav_path


def transcribe(wav_path: Path, model_size: str, out_dir: Path) -> None:
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        raise SystemExit(
            "faster-whisper not installed. Run: "
            "pip install --break-system-packages faster-whisper"
        )

    print(f"[transcribe] Loading model '{model_size}' (first run downloads ~460MB)", file=sys.stderr)
    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    print("[transcribe] Transcribing…", file=sys.stderr)
    segments, info = model.transcribe(
        str(wav_path),
        beam_size=1,
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=500),
    )
    print(
        f"[transcribe] Detected {info.language} "
        f"(confidence {info.language_probability:.2f}), "
        f"duration {info.duration:.1f}s",
        file=sys.stderr,
    )

    rows = []
    for seg in segments:
        rows.append({
            "start": round(seg.start, 2),
            "end": round(seg.end, 2),
            "text": seg.text.strip(),
        })
        if len(rows) % 25 == 0:
            print(f"  {seg.end:.1f}s processed, {len(rows)} segments", file=sys.stderr)

    # Structured JSON
    json_path = out_dir / "transcript.json"
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)

    # Human-readable TXT with [MM:SS] timestamps
    txt_path = out_dir / "transcript.txt"
    with txt_path.open("w", encoding="utf-8") as f:
        for r in rows:
            mins, secs = divmod(int(r["start"]), 60)
            f.write(f"[{mins:02d}:{secs:02d}] {r['text']}\n")

    print(f"[transcribe] Wrote {len(rows)} segments to:", file=sys.stderr)
    print(f"  {txt_path}", file=sys.stderr)
    print(f"  {json_path}", file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser(description="Sermon transcription via faster-whisper")
    parser.add_argument("input", type=Path, help="Path to sermon video or audio file")
    parser.add_argument("output_dir", type=Path, help="Directory for transcript.txt + transcript.json")
    parser.add_argument(
        "--model",
        default="small",
        choices=["tiny", "base", "small", "medium", "large-v3"],
        help="faster-whisper model size (default: small — good speed/accuracy balance)",
    )
    args = parser.parse_args()

    if not args.input.exists():
        raise SystemExit(f"Input not found: {args.input}")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    wav_path = ensure_wav(args.input, args.output_dir)
    transcribe(wav_path, args.model, args.output_dir)


if __name__ == "__main__":
    main()
