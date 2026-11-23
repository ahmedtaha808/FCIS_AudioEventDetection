import csv
import shutil
from pathlib import Path

# Change this path to where you extracted ESC-50
ESC50_ROOT = Path(r"D:\FCIS\Now\DSP\datasets\ESC-50-master")

# Output inside your AudioEventDetection project folder
OUT_ROOT = Path(r"D:\FCIS\Now\DSP\datasets\dataset")

# Maps ESC-50 category names -> (TargetFolderName, FilePrefix)
CATEGORY_MAP = {
    "glass_breaking": ("GlassBreaking", "glass"),
    "door_knock": ("DoorKnicking", "knock"),
    "footsteps": ("Footsteps", "footsteps"),
    "door_wood_creaks": ("DoorSlaming", "slam"),
    "alarm_clock": ("SmokeAlarm", "alarm"),
    "siren": ("SmokeAlarm", "alarm"),
}

csv_path = ESC50_ROOT / "meta" / "esc50.csv"
audio_dir = ESC50_ROOT / "audio"

# Track counters separately per split and folder so filenames stay clean
counters = {}

with open(csv_path, mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        category = row["category"]
        if category not in CATEGORY_MAP:
            continue

        folder_name, prefix = CATEGORY_MAP[category]
        split = "Test" if int(row["fold"]) == 5 else "Train"

        src_file = audio_dir / row["filename"]
        if not src_file.exists():
            continue

        dest_dir = OUT_ROOT / split / folder_name
        dest_dir.mkdir(parents=True, exist_ok=True)

        key = (split, folder_name)
        counters[key] = counters.get(key, 0) + 1
        idx = counters[key]

        dest_file = dest_dir / f"{prefix}_{idx:03d}.wav"
        shutil.copy2(src_file, dest_file)

print("Done! Dataset organized into Train (folds 1-4) and Test (fold 5).")