from osgeo import gdal, ogr
import os


path_tif = input('Give me a tif path, please:')
path_shp = input('Give me a shp path, please:')
path_output = input('Give me an output path, please:')

shp_file = ogr.Open(path_shp)
shp_layer = shp_file.GetLayer()

for feature in shp_layer:
    name_1 = feature.GetField("NAME")
    dst_1 = path_output + '\\' + name_1 + '.tif'
    os.system("gdalwarp -cutline " + path_shp + ' -dstnodata 0 -cwhere ' + '"NAME = ' + "'" + str(name_1) + "'" + '" -crop_to_cutline -co COMPRESS=LZW ' + path_tif + " " + dst_1)
    