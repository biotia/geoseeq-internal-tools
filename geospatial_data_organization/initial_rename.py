import os
import shutil

script_dir = os.path.dirname(os.path.realpath(__file__))

def generate_identifier(index):
    if index < 25:
        return f"{index + 1:02d}"  # 01 to 25
    else:
        letter = chr((index - 25) // 9 + 65)  # A, B, ...
        number = (index - 25) % 9 + 1  # 1 to 9
        return f"{letter}{number}"

files = sorted(os.listdir(script_dir))
for i, filename in enumerate(files):
    file_path = os.path.join(script_dir, filename)
    if os.path.isfile(file_path) and not filename.endswith('.py'):
        identifier = generate_identifier(i)
        new_filename = f"{identifier}_{filename}.tif"
        new_path = os.path.join(script_dir, new_filename)
        shutil.move(file_path, new_path)
