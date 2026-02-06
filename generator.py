
from pathlib import Path

def generate_srt(text: str, out: Path):
    lines = text.split(".")
    srt = []
    t = 0
    for i, line in enumerate(lines, 1):
        if not line.strip(): continue
        start = f"00:00:{t:02},000"
        end = f"00:00:{t+3:02},000"
        srt.append(f"{i}\n{start} --> {end}\n{line.strip()}\n")
        t += 3
    out.write_text("\n".join(srt))
    return out
