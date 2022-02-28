from qgis.core import *
import os
path_raster_file ='/app/raster_gis_files/'+os.getenv('TIF_FILENAME')
if os.path.exists(path_raster_file) ==False:
    print('No existe el archivo')
    exit()
raster_filename = os.path.basename(path_raster_file)
QgsApplication.setPrefixPath('/usr', True)
qgs = QgsApplication([], False)
qgs.initQgis()
import processing
from processing.core.Processing import Processing
Processing.initialize()
params ={
    'DPI' : os.getenv('DPI'),
    'EXTENT' : os.getenv('EXTEND'),
    'METATILESIZE' : os.getenv('METATILESIZE'),
    'OUTPUT_DIRECTORY' : '/app/public_gis_files',
    'OUTPUT_HTML' : '/app/public_gis_files/leaflet.html',
    'QUALITY' : os.getenv('QUALITY'),
    'TILE_FORMAT' : os.getenv('TILE_FORMAT'),
    'TILE_HEIGHT' : os.getenv('TILE_HEIGHT'),
    'TILE_WIDTH' : os.getenv('TILE_WIDTH'),
    'TMS_CONVENTION' : os.getenv('TMS_CONVENTION'),
    'ZOOM_MAX' : os.getenv('ZOOM_MAX'),
    'ZOOM_MIN' : os.getenv('ZOOM_MIN')
}
QgsProject.instance().setCrs(QgsCoordinateReferenceSystem(4326))
raster_layer =QgsRasterLayer(path_raster_file, raster_filename, 'gdal')
if raster_layer.isValid() ==False:
    print('Capa invalida')
    exit()
QgsProject.instance().addMapLayer(raster_layer)
response =processing.run('qgis:tilesxyzdirectory', params)
qgs.exitQgis()