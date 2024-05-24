import os
from PIL import Image
import config

def print_files_in_dir(directory):
    if not os.path.exists(directory):
        print(f"Directory does not exist: {directory}")
        return []
    else:
        files = os.listdir(directory)
        image_files = []
        for file in files:
            if file.lower().endswith(".jpg"):
                image_files.append(os.path.join(directory, file))
        return image_files

# read image file
def resize_images(image_files, output_dir, size=(300, 300)):
    for file in image_files:
        try:
            with Image.open(file) as img:
                img_resized = img.resize(size, Image.LANCZOS)
                base_name = os.path.basename(file)
                new_file_path = os.path.join(output_dir, base_name)
                img_resized.save(new_file_path)
                print(f"Resized {file} and saved to {new_file_path}")
        except Exception as e:
            print(f"Error opening image {file}: {e}")

if __name__ == "__main__":
    image_files = print_files_in_dir(config.IMAGE_DIR)
    resize_images(image_files, config.RESIZED_DIR)
