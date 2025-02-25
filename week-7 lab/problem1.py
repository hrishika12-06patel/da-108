import os
import shutil
import glob
from datetime import datetime

def ensure_directory_exists(directory):
    """Ensure the given directory exists, creating it if necessary."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def list_files(directory):
    ensure_directory_exists(directory)
    files = os.listdir(directory)
    print(f"Total number of files: {len(files)}")
    return files

def categorize_files(directory):
    extensions = ["txt", "csv", "json", "jpg", "png", "log"]
    categorized_files = {ext: glob.glob(os.path.join(directory, f"*.{ext}")) for ext in extensions}
    
    for ext, files in categorized_files.items():
        print(f"{ext.upper()} files: {len(files)}")
    
    return categorized_files

def create_directories(base_dir):
    sub_dirs = {
        "txt": "text_files", "csv": "csv_files", "json": "json_files", 
        "jpg": "images", "png": "images", "log": "logs"
    }
    ensure_directory_exists(base_dir)
    for sub_dir in set(sub_dirs.values()):
        ensure_directory_exists(os.path.join(base_dir, sub_dir))
    return sub_dirs

def move_files(directory, categorized_files, organized_path, sub_dirs):
    total_moved = 0
    sample_files = {}
    
    for ext, files in categorized_files.items():
        if files:
            sample_files[ext] = os.path.basename(files[0])
        for file in files:
            filename = os.path.basename(file)
            dest_folder = os.path.join(organized_path, sub_dirs[ext])
            if ext == "log":
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{os.path.splitext(filename)[0]}_{timestamp}.log"
            shutil.move(file, os.path.join(dest_folder, filename))
            total_moved += 1
    return total_moved, sample_files

def generate_summary(summary_path, categorized_files, total_moved, sample_files):
    with open(summary_path, "w") as f:
        f.write("File Management Summary\n=======================\n")
        for ext, files in categorized_files.items():
            f.write(f"{ext.upper()} files: {len(files)}\n")
        f.write(f"Total files moved: {total_moved}\n\nSample file names:\n")
        for ext, sample in sample_files.items():
            f.write(f"{ext.upper()}: {sample}\n")

def main():
    data_directory = "data_repository"
    organized_directory = "organized_data"
    
    print("Step 1: Listing files")
    list_files(data_directory)
    
    print("\nStep 2: Categorizing files")
    categorized_files = categorize_files(data_directory)
    
    print("\nStep 3: Creating directories")
    sub_dirs = create_directories(organized_directory)
    
    print("\nStep 4 & 5: Moving files and renaming logs")
    total_moved, sample_files = move_files(data_directory, categorized_files, organized_directory, sub_dirs)
    
    print("\nStep 6: Generating summary report")
    generate_summary(os.path.join(organized_directory, "summary.txt"), categorized_files, total_moved, sample_files)
    print("Summary report created.")

if __name__ == "__main__":
    main()
