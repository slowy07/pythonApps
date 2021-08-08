import os
from zipfile import ZipFile


def create_zip(path):
    """
    target folder or path name
    """
    folder_name = split("\\")[-1]
    rel_path = path.strip(folder_name)

    # save file to the target folder path
    os.chdir(rel_path)

    zip_file = ZipFile(f"{folder_name}.zip", "w")

    for root, dirs, files in os.walk(folder_name, topdown=False):
        # file in subfolder
        for name in files:
            file = os.path.join(root, name)
            zip_file.write(file)
        for name in dirs:
            folders = os.path.join(root, name)
            zip_file.write(folders)
    zip_file.close()


if __name__ == "__main__":
    path = input("path to target folder")
    create_zip(path)
