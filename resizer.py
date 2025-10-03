import os
from PIL import Image

# Configuration
input_folder = "images"       # Folder containing images
output_folder = "resized"     # Folder to save resized images
new_size = (300, 300)         # Resize width x height (pixels)
output_format = "JPEG"        # Output format (JPEG, PNG, etc.)

def resize_images():
    # Create output folder if not exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in input folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Skip if not a file
        if not os.path.isfile(file_path):
            continue

        try:
            # Open image
            img = Image.open(file_path)

            # Resize image
            img_resized = img.resize(new_size)

            # Prepare new filename (same name but new folder & format)
            base_name, _ = os.path.splitext(filename)
            new_file = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")

            # Save image
            img_resized.save(new_file, output_format)
            print(f"✅ Resized and saved: {new_file}")

        except Exception as e:
            print(f"❌ Failed to process {filename}: {e}")

if __name__ == "__main__":
    resize_images()
    print("\nAll images processed successfully!")
