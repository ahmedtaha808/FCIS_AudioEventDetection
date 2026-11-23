from pathlib import Path

# ====== CONFIGURATION (Edit these two lines) ======
FOLDER_PATH = Path(r"D:\FCIS\Now\DSP\datasets\dataset\Train\DoorCreaking")
BASE_NAME = "doorcreak"  # Produces: alarm_001.wav, alarm_002.wav, ...
# ==================================================


def rename_files(folder: Path, base_name: str):
    if not folder.exists() or not folder.is_dir():
        print(f"Error: Folder not found -> {folder}")
        return

    # Collect files only (ignore subfolders), sorted for predictable order
    files = sorted([f for f in folder.iterdir() if f.is_file()])

    if not files:
        print(f"No files found in '{folder}'.")
        return

    # Step 1: Rename to temporary names first to avoid name collisions
    temp_entries = []
    for idx, file_path in enumerate(files, start=1):
        temp_path = folder / f"__temp_rename_{idx:04d}{file_path.suffix.lower()}"
        file_path.rename(temp_path)
        temp_entries.append((temp_path, file_path.suffix.lower()))

    # Step 2: Rename temporary files to final "name_001.ext" format
    for idx, (temp_path, ext) in enumerate(temp_entries, start=1):
        final_path = folder / f"{base_name}_{idx:03d}{ext}"
        temp_path.rename(final_path)
        print(f"Renamed -> {final_path.name}")

    print(f"\nDone! Renamed {len(temp_entries)} files using prefix '{base_name}_'.")


if __name__ == "__main__":
    rename_files(FOLDER_PATH, BASE_NAME)
