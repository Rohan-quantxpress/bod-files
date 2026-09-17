import os
import re

# Current directory where this script is running
BOD_ZIP_DIR = os.path.dirname(os.path.abspath(__file__))

deleted = 0

for filename in os.listdir(BOD_ZIP_DIR):

    # Match files like:
    # 01-06-2026
    # 01-07-2026
    # 01-06-2026.zip
    # 01-07-2026.zip
    match = re.match(
        r"^(\d{2})-(\d{2})-(\d{4})(?:\.zip)?$",
        filename,
        re.IGNORECASE
    )

    if not match:
        continue

    day, month, year = match.groups()

    # Delete June and July 2026 files
    if month in {"08"} and year == "2026":

        file_path = os.path.join(BOD_ZIP_DIR, filename)

        try:
            os.remove(file_path)
            print(f"Deleted: {filename}")
            deleted += 1

        except Exception as e:
            print(f"Failed: {filename} -> {e}")

print("----------------------------------------")
print(f"Total files deleted: {deleted}")
print("----------------------------------------")