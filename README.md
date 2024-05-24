# Image Resizer

This Python script resizes images to a uniform size for improved web performance. 

## Features
- Resizes JPEG images in a specified directory
- Saves resized images to a new directory
- Uses high-quality resizing (LANCZOS filter)

## Requirements
- Python 3.x
- Pillow library (`pip install Pillow`)

## Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/rdcheadle3/image-resizer.git
    cd image_resizer
    ```
2. Install dependencies:
    ```bash
    pip install Pillow
    ```

3. Create a `config.py` file with the following content:
    ```python
    import os

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    IMAGE_DIR = os.path.join(BASE_DIR, "path/to/your/images")
    RESIZED_DIR = os.path.join(BASE_DIR, "path/to/your/resized_images")
    ```

## Usage
Run the script:
```bash
python resize_images.py

