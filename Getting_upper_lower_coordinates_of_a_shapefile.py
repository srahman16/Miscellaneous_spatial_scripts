'''Getting the upper and lower coordinates of a shapefile
# Script: Shahriar Rahman
# Email: shahriar.env12@gmail.com
# Application: For everyday works, we need to get the upper and lower coordinates of a shape file to clip any raster stack. 
              This script will be helpful to know upper and lower coordinates of a shape file.
'''

import arcpy # importing arcpy if not running on ArcGIS Pro
shapefile_path = r"Shahriar:\xxxxx\xxxxx.shp" # path of the shape file

desc = arcpy.Describe(shapefile_path) # getting the extent of the shape file
extent = desc.extent

ulx, uly = extent.XMin, extent.YMax # Retrieve the coordinates of the upper limit (x-min & y-max)
lrx, lry = extent.XMax, extent.YMin # Retrieve the coordinates of the lower limit (x-max & y-min)

# now the following lines will print the upper and lower coordinates on the console
print("Upper Left X-coordinate (ulx):", ulx)
print("Upper Left Y-coordinate (uly):", uly)
print("Lower Right X-coordinate (lrx):", lrx)
print("Lower Right Y-coordinate (lry):", lry)

# Remember this is the correct order to set these upper and lower coordinates in a python script, example: ulx, uly, lrx, lry = (147.45, -31.46, 156.28, -32.05)
# Please subscribe to my youtube channel (https://www.youtube.com/channel/UCvH8JoH8zMLPjyT2S0T8s9g)
# Thank you
