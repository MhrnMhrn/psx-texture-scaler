import os
import sys
import argparse
from PIL import Image

def resize_image(input_path, output_path, size):
    img = Image.open(input_path)
    img = img.resize((size, size), Image.LANCZOS)
    img.save(output_path)
    print(f"Resized: {input_path} → {output_path}")

def process_folder(folder_path, target_size):
    for filename in os.listdir(folder_path):
        lower_name = filename.lower()
        ext = os.path.splitext(filename)[1].lower()
        if ext not in ['.png', '.jpg', '.jpeg']:
            print(f"Unsupported format, skipping: {filename}")
            continue

        if any(x in lower_name for x in ['normal', 'roughness', 'metallic', 'displacement']):
            print(f"Skipping: {filename}")
            continue

        if 'color' in lower_name or 'albedo' in lower_name:
            input_path = os.path.join(folder_path, filename)
            backup_path = os.path.join(folder_path, filename.replace('.', '_color_backup.'))
            # Save backup
            Image.open(input_path).save(backup_path)
            print(f"Backup saved: {backup_path}")
            # Resize in-place
            resize_image(input_path, input_path, target_size)
        else:
            print(f"Ignored: {filename}")

def main():
    parser = argparse.ArgumentParser(
        description="Resize color/albedo textures to a square size and save backups."
    )
    parser.add_argument(
        "folder",
        help="Folder to process (use '.' for current folder)"
    )
    parser.add_argument(
        "--size",
        type=int,
        default=256,
        help="Target square size for resizing (e.g., 128, 256). Default is 256."
    )
    args = parser.parse_args()

    folder_path = os.path.abspath(args.folder)
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a directory")
        sys.exit(1)

    if args.size <= 0:
        print("Error: size must be a positive integer")
        sys.exit(1)

    process_folder(folder_path, args.size)

if __name__ == "__main__":
    main()
