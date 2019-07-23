from osgeo import gdal
import os

path_tif = input('Give me a path, please:')

for root, dirs, files in os.walk(path_tif):
    for filename in files:
        tiff_file = os.path.join(root, filename)
        if (filename.endswith('.tiff') and 'PSS1' in tiff_file):
                dst_1 = os.path.dirname(tiff_file) + '\\' + filename[:-5] + '_uint16.tiff'
                os.system("gdal_translate -a_nodata 0.0 -ot Int16 -of GTiff -co COMPRESS=LZW " + tiff_file + ' ' + dst_1)        
                #dst_1 = os.path.dirname(tiff_file) + '\\' + filename[:-5] + '_red.tiff'
                #dst_2 = os.path.dirname(tiff_file) + '\\' + filename[:-5] + '_green.tiff'
                #dst_3 = os.path.dirname(tiff_file) + '\\' + filename[:-5] + '_blue.tiff'
                #os.system("gdal_translate " + tiff_file + ' ' + dst_1 + ' -b 1 -co COMPRESS=LZW')
                #os.system("gdal_translate " + tiff_file + ' ' + dst_2 + ' -b 2 -co COMPRESS=LZW')
                #os.system("gdal_translate " + tiff_file + ' ' + dst_3 + ' -b 3 -co COMPRESS=LZW')

                
                
             