from enmapbox.exampledata import enmap
from enmapboxprocessing.algorithm.rasterlayerzonalaggregationalgorithm import RasterLayerZonalAggregationAlgorithm
from enmapboxprocessing.test.algorithm.testcase import TestCase
from testdata import landcover_map_l3


class TestRasterLayerZonalAggregationAlgorithm(TestCase):

    def test(self):
        alg = RasterLayerZonalAggregationAlgorithm()
        parameters = {
            alg.P_RASTER: enmap,
            alg.P_CATEGORIZED_RASTER: landcover_map_l3,
            alg.P_OUTPUT_TABLE: self.filename('table.csv'),
        }
        result = self.runalg(alg, parameters)

    def test_issue1406(self):
        alg = RasterLayerZonalAggregationAlgorithm()
        parameters = {
            alg.P_RASTER: enmap,
            alg.P_CATEGORIZED_RASTER: landcover_map_l3,
            alg.P_OUTPUT_TABLE: self.filename('table.gpkg'),
        }
        result = self.runalg(alg, parameters)
