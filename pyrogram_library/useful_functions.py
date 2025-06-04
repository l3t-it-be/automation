import os


def get_folder_size_and_count(filepath):
    count = sum(len(files) for root, dirs, files in os.walk(filepath))
    total_size = sum(
        os.path.getsize(os.path.join(root, f))
        for root, dirs, files in os.walk(filepath)
        for f in files
    )
    return count, total_size
