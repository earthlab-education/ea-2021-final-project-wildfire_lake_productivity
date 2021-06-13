import os
import geopandas as gpd
import io
import requests
import zipfile
from zipfile import BadZipfile

def open_zips(url, shapefile):
    """opens zipped shapefiles from a url and clips data according to a 
    region of interest defined by a shapefile before saving as a geopandas dataframe
    Parameters
    -----------
    url : path to a zipped shapefile
    shapefile: a shapefile for region of interest

    Returns
    -----------
    gpd : a clipped geopandas geodataframe 
    """
    local_path = os.path.join('data')
    if url.endswith(".zip"):
        print("Great - this is a .zip file")
        r = requests.get(url)
        if r.status_code == 404:
            print('Status code 404, check that correct url is provided')
        else:
            try:
                z = zipfile.ZipFile(io.BytesIO(r.content))
                z.extractall(path=local_path)  # extract to folder
                filenames = [y for y in sorted(z.namelist()) for ending in ['dbf', 'prj', 'shp', 'shx'] if y.endswith(ending)]
                print(filenames)
                dbf, prj, shp, shx = [filename for filename in filenames]
                gpdfile = gpd.overlay(gpd.read_file(local_path + '/' + shp).to_crs(shapefile.crs), shapefile, how = 'intersection')
                print("Done")
                print("Shape of the dataframe: {}".format(gpdfile.shape))
                print("Projection of dataframe: {}".format(gpdfile.crs))
                return(gpdfile)
            except BadZipfile:
                print("url and data format (.zip) should be OK, check for other errors")
    else:
        print("Url does not end in .zip. Check file format, open_zips wants to open zipped files")




def df_to_gdf(input_df, shapefile):
    """
    Convert a DataFrame with longitude and latitude columns
    to a GeoDataFrame.
    """
    geometry = [Point(xy) for xy in zip(input_df.long, input_df.lat)]
    return gpd.clip(gpd.GeoDataFrame(input_df, crs=shapefile.crs, geometry=geometry), shapefile)

