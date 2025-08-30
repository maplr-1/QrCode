import os
from pyzbar.pyzbar import decode
from PIL import Image


def open_QrCodes():
    defualt_storing_files_name = 'QrCodes'
    os.chdir('..')
    os.chdir(f'{defualt_storing_files_name}')
    pwd = os.getcwd()
    file_names = os.listdir()
    complete_file_loc = []
    for i in file_names:
        complete_file_loc.append(f'{pwd}/{i}')
    for j in complete_file_loc:
        if j.endswith('.png'):
            img = Image.open(j)
            decoded = decode(img)
            for k in decoded:
                print('\n',j)
                print("Data:", k.data.decode("utf-8"),"\n") 

def main():
    open_QrCodes()

if __name__ == "__main__":
    main()
