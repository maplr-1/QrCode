import qrcode
import os


def file_name():
    file_type = 'png'
    file_name = (input("Enter The File Name: "))
    data = (input("\nEnter The text Which You Want To Make Into a Qrcode:\n"))
    store_where = int(input("""\nWhere to Store The QrCode Image:

1.default(QrCodes)
2.selected location

Choose(1 OR 2): """))

    full_file = f'{file_name}.{file_type}'
    return full_file,data,store_where

def Qrcode_gen_img():
    full_file,data,store_where = file_name()
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make()
    img = qr.make_image()

    if store_where == 1:
        defualt_storing_files_name = 'QrCodes'
        os.chdir('..')
        os.chdir(f'{defualt_storing_files_name}')
        store_at = os.getcwd()
        stores_at = f'{store_at}/{full_file}'
        img.save(stores_at)

    elif store_where == 2:
        store_at = (input("Where do you want the file to be stores at:(default:Qrcodes)"))
        stores_at = f'{store_at}/{full_file}'
        img.save(stores_at)

    else:
        print("Choose 1 OR 2")


def main():
    try:
        Qrcode_gen_img()
    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == '__main__':
    main()
