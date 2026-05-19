def presort():
        from pathlib import Path
        import shutil

        download_path = Path.home() / "Downloads"

        file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "pdf": [".pdf"],
    "videos":[".mp4", ".mov", ".avi", ".mkv"],
    "documents": [".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "music": [".mp3", ".wav", ".aac", ".flac"],
    "archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
        }

        for file in download_path.iterdir():

         if file.is_file():
            suffix = file.suffix.lower()
            for folder_name, extensions in file_types.items():
                if suffix in extensions:
                    target_folder = download_path / folder_name
                    target_folder.mkdir(exist_ok=True)
                    target_file = target_folder / file.name
                    shutil.move(str(file), str(target_folder / file.name))
                    print(f"{file.name}を{folder_name}に移動しました。")
                    break
