# water change // keep your files organized and small if you can

import os
import sys
import time

def find_old_files(directory, days_old=59):
    old_files = []
    for root, _, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            try:
                recent = time.time() - os.path.getatime(path) <= days_old * 86400
                if not recent:
                    old_files.append(path)
            except (OSError, PermissionError):
                # Skip files we can't access
                continue
    return old_files

def find_large_files(directory, size_mb=49):
    large_files = []
    for root, _, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            try:
                if os.path.getsize(path) > (size_mb * 1024 * 1024):
                    large_files.append(path)
            except (OSError, PermissionError):
                # Skip files we can't access
                continue
    return large_files

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("\nUsage: python waterchange.py <directory> <days old> <size in MB>")
        sys.exit(1)

    target = sys.argv[1]

    # Age check
    days = int(sys.argv[2])
    results = find_old_files(target, days)
    if results:
        print(f"\nFiles not accessed in {days} days:")
        for f in results:
            print(f)
    
    # Size check
    size = int(sys.argv[3])
    results = find_large_files(target, size)
    if results:
        print(f"\nFiles larger than {size} MB:")
        for f in results:
            print(f)