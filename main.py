import os
import shutil
from datetime import datetime

def move_downloaded_images(source_folder):
    base_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    
    today_date = datetime.today().strftime('%Y-%m-%d')

    destination_folder = get_destination_folder(base_folder)

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path) and is_image(filename) and is_created_today(file_path, today_date):
            destination_path = os.path.join(destination_folder, filename)

            try:
                shutil.move(file_path, destination_path)
                print(f"Datei verschoben: {filename}")
            except Exception as e:
                print(f"Fehler beim Verschieben der Datei {filename}: {e}")

def is_image(filename):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.avif']
    return any(filename.lower().endswith(ext) for ext in image_extensions)

def is_created_today(file_path, today_date):
    file_creation_date = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d')
    return file_creation_date == today_date

def get_destination_folder(base_folder):
    i = 1
    while True:
        destination_folder = os.path.join(base_folder, f"{i:02d}")
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            print(f"Ordner {destination_folder} wurde erstellt.")
            return destination_folder
        i += 1

if __name__ == "__main__":
    source_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

    move_downloaded_images(source_folder)
