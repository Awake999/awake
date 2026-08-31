#!/usr/bin/env python3
"""Standing audio transcriber for the APW archive — works on ANY machine (cloud lane or Alan's PC).

Per Alan's SOP (2026-08-30): "we do need to physically download audios and transcribe those.
Transcribe them yourself" + "the longer ones, please split them up and transcribe them."

What it does — for every .m4a/.mp3/.wav/.mp4 in slack/audio/files/ that has no .transcript.md yet:
  1. transcribes with faster-whisper (small model, int8, CPU — no ffmpeg needed, PyAV is bundled)
  2. writes <same-name>.transcript.md BESIDE the audio (audio stays the source of truth)
  3. LONG recordings are split into 10-minute chapters in the transcript, with a table of
     contents at the top — so even an hour-long call reads as navigable sections, never a wall of text
  4. logs progress to transcribe_progress.log in the same folder; ends with ALL DONE

Setup (once per machine):  pip install faster-whisper
Run:                       python3 ops/archive/tools/transcribe.py
Then:                      git add -A ops/archive/slack/audio && git commit && git push
                           (a lane run will link the new transcripts into audio/README.md)
"""
import os, sys, glob, time

CHAPTER_SECONDS = 600
AUDIO_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "slack", "audio", "files"))
LOG = os.path.join(AUDIO_DIR, "..", "transcribe_progress.log")

def log(msg):
    line = time.strftime("%H:%M:%S ") + msg
    print(line, flush=True)
    open(LOG, "a").write(line + "\n")

def fmt(sec):
    sec = int(sec)
    if sec >= 3600:
        return f"{sec // 3600}:{sec % 3600 // 60:02d}:{sec % 60:02d}"
    return f"{sec // 60:02d}:{sec % 60:02d}"

def slug(text):
    import re
    s = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"\s+", "-", s.strip())

def main():
    from faster_whisper import WhisperModel
    model = WhisperModel("small", device="cpu", compute_type="int8", cpu_threads=4)
    log("model loaded")
    todo = [f for ext in ("m4a", "mp3", "wav", "mp4")
            for f in sorted(glob.glob(os.path.join(AUDIO_DIR, f"*.{ext}")))
            if not os.path.exists(os.path.splitext(f)[0] + ".transcript.md")]
    for path in todo:
        name = os.path.basename(path)
        try:
            segments, info = model.transcribe(path, vad_filter=True)
            lines, chapters, boundary, n = [], [], 0, 0
            for seg in segments:
                if seg.start >= boundary:
                    n += 1
                    start = int(seg.start) - int(seg.start) % CHAPTER_SECONDS
                    title = f"Chapter {n} ({fmt(start)} to {fmt(start + CHAPTER_SECONDS)})"
                    lines += ["", f"## {title}", ""]
                    chapters.append(title)
                    boundary = start + CHAPTER_SECONDS
                lines.append(f"[{fmt(seg.start)}] {seg.text.strip()}")
            header = [f"# Transcript — {name}", "",
                      f"Machine transcription (faster-whisper small model, int8) per the archive audio SOP. "
                      f"Companion to the ORIGINAL audio file `{name}` in this folder — the audio is the source of truth. "
                      f"Detected language: {info.language}; duration: {int(info.duration)}s.", ""]
            if len(chapters) > 1:
                header += ["### Contents", ""] + [f"- [{t}](#{slug(t)})" for t in chapters] + [""]
            out = os.path.splitext(path)[0] + ".transcript.md"
            open(out, "w", encoding="utf-8").write("\n".join(header + lines) + "\n")
            log(f"done: {name} ({int(info.duration)}s audio, {len(chapters)} chapters)")
        except Exception as e:
            log(f"FAILED: {name} — {e}")
    log("ALL DONE")

if __name__ == "__main__":
    main()
