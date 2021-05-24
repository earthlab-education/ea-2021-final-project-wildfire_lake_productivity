import geopandas as gpd
import io
import requests
import zipfile

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
    local_path = 'tmp/'
    print('Downloading shapefile...')
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(path=local_path)  # extract to folder
    filenames = [y for y in sorted(z.namelist()) for ending in [
        'dbf', 'prj', 'shp', 'shx'] if y.endswith(ending)]
    print(filenames)
    dbf, prj, shp, shx = [filename for filename in filenames]
    gpdfile = gpd.clip(gpd.read_file(
        local_path + shp).to_crs(shapefile.crs), shapefile)
    print("Done")
    print("Shape of the dataframe: {}".format(gpdfile.shape))
    print("Projection of dataframe: {}".format(gpdfile.crs))
    return(gpdfile)