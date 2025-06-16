import unittest
from medico import Medico

class TestMedico(unittest.TestCase):

    def test_crear_medico_valido(self):
        m = Medico("Dr. Juan Gómez", "MAT1234", "Cardiología")
        self.assertEqual(m.obtener_matricula(), "MAT1234")
        self.assertIn("Dr. Juan Gómez", str(m))

    def test_nombre_vacio_raises(self):
        with self.assertRaises(ValueError):
            Medico("", "MAT1234", "Cardiología")

    def test_matricula_vacia_raises(self):
        with self.assertRaises(ValueError):
            Medico("Dr. Ana López", "", "Cardiología")

    def test_especialidad_vacia_raises(self):
        with self.assertRaises(ValueError):
            Medico("Dr. Ana López", "MAT1234", "")

    def test_str_retorna_informacion(self):
        medico = Medico("Dr. Pedro", "MAT9999", "Pediatría")
        texto = str(medico)
        self.assertIn("Dr. Pedro", texto)
        self.assertIn("MAT9999", texto)
        self.assertIn("Pediatría", texto)

if __name__ == "__main__":
    unittest.main()
