import os
import json

def get_images_and_sounds(folder_path):
    images = []
    sounds = []

    for filename in os.listdir(f'{folder_path}/megadrumkit'):
        if filename.lower().endswith(('.jpg', '.png', '.gif')):
            images.append(filename)
        elif filename.lower().endswith('.wav'):
            sounds.append(filename)

    return images, sounds

def get_kit_name(folder_path):
    kit_json_path = os.path.join(f'{folder_path}/megadrumkit/', 'kit.json')
    if not os.path.exists(kit_json_path):
        return None

    with open(kit_json_path, 'r') as file:
        data = json.load(file)
        return data.get('name')

def generate_json_data():
    folders = sorted([folder for folder in os.listdir() if os.path.isdir(folder) and not folder.startswith('.')], key=int)

    all_folders_data = []
    for folder_name in folders:
        images, sounds = get_images_and_sounds(folder_name)
        kit_name = get_kit_name(folder_name)

        folder_data = {
            'name': kit_name,
            'folder': folder_name,
            'images': images,
            'sounds': sounds
        }

        all_folders_data.append(folder_data)

    with open('index.json', 'w') as output_file:
        json.dump(all_folders_data, output_file, indent=4)

    print("Done!")

if __name__ == "__main__":
    generate_json_data()
