import os
import shutil
from datetime import datetime

def move_downloaded_images(source_folder):
    # Setze den Basisordner auf den Windows-Download-Ordner
    base_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

    # Holen des aktuellen Datums als Zeichenfolge im Format YYYY-MM-DD
    today_date = datetime.today().strftime('%Y-%m-%d')

    # Finde den nächsten verfügbaren Ordner mit einem numerischen Namen
    destination_folder = get_destination_folder(base_folder)

    # Durchsuche alle Dateien im Quellverzeichnis
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Überprüfe, ob es sich um eine Bilddatei handelt und ob sie heute erstellt wurde
        if os.path.isfile(file_path) and is_image(filename) and is_created_today(file_path, today_date):
            # Erzeuge den Ziel-Pfad und verschiebe die Datei
            destination_path = os.path.join(destination_folder, filename)

            try:
                shutil.move(file_path, destination_path)
                print(f"Datei verschoben: {filename}")
            except Exception as e:
                print(f"Fehler beim Verschieben der Datei {filename}: {e}")

def is_image(filename):
    # Überprüfe, ob die Datei eine Bilddatei ist (du kannst diese Bedingung erweitern)
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.avif']
    return any(filename.lower().endswith(ext) for ext in image_extensions)

def is_created_today(file_path, today_date):
    # Überprüfe, ob die Datei heute erstellt wurde
    file_creation_date = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d')
    return file_creation_date == today_date

def get_destination_folder(base_folder):
    # Finde den nächsten verfügbaren Ordner mit einem numerischen Namen
    i = 1
    while True:
        destination_folder = os.path.join(base_folder, f"{i:02d}")
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            print(f"Ordner {destination_folder} wurde erstellt.")
            return destination_folder
        i += 1

if __name__ == "__main__":
    # Setze den Quellpfad auf den Windows-Download-Ordner
    source_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

    move_downloaded_images(source_folder)
