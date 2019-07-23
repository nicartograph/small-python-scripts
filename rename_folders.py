import os

path_tif = input('Give me a path, please:')

for root, dirs, files in os.walk(path_tif):
    for dir in dirs:
        print(os.path.join(root, dir))
        if 'МСС' in dir:
            os.rename(os.path.join(root, dir), os.path.join(root, dir).replace('_Новгородская область_МСС', '_Novgorodskaya_MCC'))
        elif 'ПСС' in dir:
            os.rename(os.path.join(root, dir), os.path.join(root, dir).replace('_Новгородская область_ПСС', '_Novgorodskaya_PCC'))