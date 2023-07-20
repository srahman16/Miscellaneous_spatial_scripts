'''Creating an extent shapefile from the upper and lower coordinates
# Script: Shahriar Rahman
# Email: shahriar.env12@gmail.com
# Application: For everyday work, we need to convert our upper and lower coordinates to an extent shape file. 
              This script will be helpful to create a shapefile from the upper and lower coordinates. Please check
              my another script "Getting_upper_lower_coordinates_of_a_shapefile.py" in this repo if required.
'''
import arcpy # import arcpy if you are running from an IDE

workspace = r"Shahriar:\xxxxx" # Set the workspace where the shapefile will be saved
output_shapefile = r"Shahriar:\xxxx\output_extent.shp" # Set the name and path of the output shapefile

ulx, uly, lrx, lry = (148.90, -32.01, 150.77, -35.51) # Create a polygon geometry based on the example coordinates (set your coordinates but order is *very important*)
array = arcpy.Array([arcpy.Point(ulx, uly),
                     arcpy.Point(lrx, uly),
                     arcpy.Point(lrx, lry),
                     arcpy.Point(ulx, lry)])
polygon = arcpy.Polygon(array)

arcpy.CreateFeatureclass_management(workspace, "output_extent.shp", "POLYGON", spatial_reference=arcpy.SpatialReference(4326)) # Create a feature class for the shapefile and setting spatial reference

# Open an insert cursor to add the polygon feature
with arcpy.da.InsertCursor(output_shapefile, ["SHAPE@"]) as cursor:
    cursor.insertRow([polygon])
# END OF THE SCRIPT
	
# Please subscribe to my youtube channel (https://www.youtube.com/channel/UCvH8JoH8zMLPjyT2S0T8s9g)
# Thank you
