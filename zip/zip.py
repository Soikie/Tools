import zipfile
import os
from tqdm import tqdm

def calculate_folder_size(folder_path):  
    total_size = 0  
    for root, dirs, files in os.walk(folder_path):  
        for file in files:  
            file_path = os.path.join(root, file)  
            total_size += os.path.getsize(file_path)  
    return total_size 


def create_zip_file(output_filename, source_dir):  
    dirTotalSize = calculate_folder_size(source_dir)
    processBar = tqdm(total = dirTotalSize, desc="Zip progress", ncols=100, ascii=True, bar_format="{l_bar}{bar}{r_bar}")
    with zipfile.ZipFile(output_filename, 'w') as zf:  
        for root, dirs, files in os.walk(source_dir):  
            for file in files:  
                filePath = os.path.join(root, file)
                zf.write(filePath)
                processBar.update(os.path.getsize(filePath))

def decompress_file(zip_filename, extract_dir):  
    with zipfile.ZipFile(zip_filename, 'r') as zf:  
        members = zf.infolist()  
        total_size = sum(file.file_size for file in members)  
  
        with tqdm(total=total_size, desc="Extracting", ncols=100) as pbar:  
            for member in members:  
                zf.extract(member, extract_dir)
                pbar.update(member.file_size)  
              
    print("File decompressed successfully!")

if __name__ == "__main__":
    # create_zip_file("file.zip","files")
    decompress_file("file.zip","ff")