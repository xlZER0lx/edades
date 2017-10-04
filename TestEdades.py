import unittest

from edades import Edades


class EdadesTest(unittest.TestCase):

    def setUp(self):
        self.ed = Edades()

    def test_edad_menos_5_no_existes(self):
        self.assertEquals(self.ed.edad(-5), 'no existes')

    def test_edad_0_eres_un_bebe(self):
        self.assertEquals(self.ed.edad(0), 'eres un bebe')

    def test_edad_menor_13_eres_un_ninio(self):
        self.assertEquals(self.ed.edad(5), 'eres un ninio')

    def test_edad_menor_18_eres_un_adolescente(self):
        self.assertEquals(self.ed.edad(14), 'eres un adolescente')

    def test_edad_menor_65_eres_un_adulto(self):
        self.assertEquals(self.ed.edad(34), 'eres un adulto')

    def test_edad_menor_120_eres_un_adulto_mayor(self):
        self.assertEquals(self.ed.edad(119), 'eres un adulto mayor')

    def test_edad_S_no_es_numero(self):
        self.assertEquals(self.ed.edad('S'), 'no es un numero')

    def test_edad_mayor_a_120_eres_mummra(self):
        self.assertEquals(self.ed.edad('148'), 'eres Mumm-Ra')


if __name__== '__main__':
    unittest.main()