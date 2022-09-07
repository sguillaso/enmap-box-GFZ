from enmapbox.exampledata import library_gpkg
from enmapboxprocessing.algorithm.savelibraryasgeojsonalgorithm import SaveLibraryAsGeoJsonAlgorithm
from enmapboxprocessing.test.algorithm.testcase import TestCase


class TestPrepareClassificationDatasetFromCategorizedLibrary(TestCase):

    def test_default(self):
        alg = SaveLibraryAsGeoJsonAlgorithm()
        parameters = {
            alg.P_LIBRARY: library_gpkg,
            alg.P_OUTPUT_FILE: self.filename('profiles.geojson')
        }
        self.runalg(alg, parameters)
        # dump = Utils.jsonLoad(parameters[alg.P_OUTPUT_FILE])
        # self.assertEqual(75, len(dump))
        # self.assertEqual(
        #     "{'fid': 1, 'name': 'red clay tile 1', 'profiles': {'x': [0.46, 0.465, 0.47, 0.475, 0.479, 0.484, 0.489, 0.494, 0.499, 0.503, 0.508, 0.513, 0.518, 0.523, 0.528, 0.533, 0.538, 0.543, 0.549, 0.554, 0.559, 0.565, 0.57, 0.575, 0.581, 0.587, 0.592, 0.598, 0.604, 0.61, 0.616, 0.622, 0.628, 0.634, 0.64, 0.646, 0.653, 0.659, 0.665, 0.672, 0.679, 0.685, 0.692, 0.699, 0.706, 0.713, 0.72, 0.727, 0.734, 0.741, 0.749, 0.756, 0.763, 0.771, 0.778, 0.786, 0.793, 0.801, 0.809, 0.817, 0.824, 0.832, 0.84, 0.848, 0.856, 0.864, 0.872, 0.88, 0.888, 0.896, 0.915, 0.924, 0.934, 0.944, 0.955, 0.965, 0.975, 0.986, 0.997, 1.007, 1.018, 1.029, 1.04, 1.051, 1.063, 1.074, 1.086, 1.097, 1.109, 1.12, 1.132, 1.144, 1.155, 1.167, 1.179, 1.191, 1.203, 1.215, 1.227, 1.239, 1.251, 1.263, 1.275, 1.287, 1.299, 1.311, 1.323, 1.522, 1.534, 1.545, 1.557, 1.568, 1.579, 1.59, 1.601, 1.612, 1.624, 1.634, 1.645, 1.656, 1.667, 1.678, 1.689, 1.699, 1.71, 1.721, 1.731, 1.742, 1.752, 1.763, 1.773, 1.783, 2.044, 2.053, 2.062, 2.071, 2.08, 2.089, 2.098, 2.107, 2.115, 2.124, 2.133, 2.141, 2.15, 2.159, 2.167, 2.176, 2.184, 2.193, 2.201, 2.21, 2.218, 2.226, 2.234, 2.243, 2.251, 2.259, 2.267, 2.275, 2.283, 2.292, 2.3, 2.308, 2.315, 2.323, 2.331, 2.339, 2.347, 2.355, 2.363, 2.37, 2.378, 2.386, 2.393, 2.401, 2.409], 'y': [589.9561196565628, 655.9781730175018, 656.5987318754196, 662.0189547538757, 665.8215820789337, 672.0291823148727, 679.5640289783478, 687.4214857816696, 696.4243203401566, 704.2206078767776, 717.2011584043503, 729.4847816228867, 741.8657094240189, 754.2887330055237, 768.3415710926056, 793.1562513113022, 821.5638995170593, 849.9668538570404, 911.5239232778549, 958.9775651693344, 1010.2821886539459, 1106.4240336418152, 1176.8579483032227, 1249.8243898153305, 1354.5115292072296, 1458.0203592777252, 1521.5547382831573, 1608.2829236984253, 1682.4758052825928, 1734.430342912674, 1782.0806801319122, 1818.9404904842377, 1850.498765707016, 1880.255788564682, 1908.0016016960144, 1933.8889420032501, 1967.0139253139496, 1991.775780916214, 2018.6464488506317, 2055.0067722797394, 2088.9735221862793, 2112.14616894722, 2143.469601869583, 2173.4149754047394, 2203.3461928367615, 2233.3262860774994, 2263.3177042007446, 2293.3219373226166, 2323.2994973659515, 2351.6756296157837, 2383.5673928260803, 2397.4907398223877, 2410.1611971855164, 2425.793558359146, 2432.3204159736633, 2428.8032948970795, 2424.858510494232, 2419.6678400039673, 2414.676696062088, 2409.5095694065094, 2405.594438314438, 2400.479018688202, 2395.610809326172, 2392.238825559616, 2394.5313692092896, 2398.27498793602, 2404.9825966358185, 2426.4512956142426, 2456.516921520233, 2488.3639812469482, 2556.4375519752502, 2589.409351348877, 2627.0699501037598, 2664.174735546112, 2705.8514952659607, 2742.0559525489807, 2776.966094970703, 2817.2022104263306, 2853.1214594841003, 2907.458543777466, 2978.883981704712, 3030.6047201156616, 3086.5323543548584, 3137.117624282837, 3180.8480620384216, 3204.079568386078, 3240.0718331336975, 3272.6112008094788, 3312.3376965522766, 3344.307243824005, 3381.021022796631, 3418.704569339752, 3449.314534664154, 3488.611876964569, 3539.2722487449646, 3592.521548271179, 3649.4937539100647, 3685.98610162735, 3717.866539955139, 3762.093484401703, 3815.47749042511, 3858.0304384231567, 3852.0818948745728, 3838.292360305786, 3841.175436973572, 3838.8723134994507, 3824.4059681892395, 3995.0203895568848, 4045.5397963523865, 4069.228172302246, 4078.6924958229065, 4092.6894545555115, 4104.94327545166, 4113.836586475372, 4125.199615955353, 4131.361544132233, 4128.446280956268, 4124.26620721817, 4122.012257575989, 4117.9439425468445, 4115.795791149139, 4129.941463470459, 4105.718731880188, 4110.104441642761, 4100.624322891235, 4083.890914916992, 4065.536856651306, 4033.980071544647, 4007.1681141853333, 3924.025297164917, 3848.077654838562, 3816.5080547332764, 4214.15239572525, 4228.495955467224, 4261.7058753967285, 4281.130731105804, 4288.092851638794, 4286.93026304245, 4280.451536178589, 4279.137551784515, 4281.850159168243, 4278.820157051086, 4262.973070144653, 4249.923229217529, 4235.023856163025, 4221.272170543671, 4211.986064910889, 4200.007617473602, 4191.010594367981, 4186.638295650482, 4201.875627040863, 4221.5001583099365, 4216.966331005096, 4210.110306739807, 4210.619032382965, 4217.097163200378, 4229.2845249176025, 4244.22025680542, 4248.799681663513, 4240.562915802002, 4230.033457279205, 4214.686751365662, 4203.523099422455, 4193.455278873444, 4182.856976985931, 4153.34939956665, 4119.803011417389, 4068.4404969215393, 4016.0611271858215, 3981.025815010071, 3948.993682861328, 3917.909860610962, 3874.0652799606323, 3845.791816711426, 3830.5431604385376, 3781.3812494277954, 3691.815435886383], 'xUnit': 'Micrometers', 'yUnit': None, 'bbl': None}, 'level_1': 'impervious', 'level_2': 'impervious', 'level_3': 'roof'}",
        #     str(dump[0])
        # )
