import unittest
from paciente import Paciente

class TestPaciente(unittest.TestCase):

    def test_crear_paciente_valido(self):
        p = Paciente("Juan Perez", "12345678", "15/04/1980")
        self.assertEqual(p.obtener_dni(), "12345678")
        self.assertIn("Juan Perez", str(p))

    def test_nombre_vacio_raises(self):
        with self.assertRaises(ValueError):
            Paciente("", "12345678", "15/04/1980")

    def test_dni_vacio_raises(self):
        with self.assertRaises(ValueError):
            Paciente("Ana Lopez", "", "15/04/1980")

    def test_fecha_invalida_raises(self):
        with self.assertRaises(ValueError):
            Paciente("Ana Lopez", "12345678", "1980/04/15")

    def test_fecha_formato_correcto(self):
        self.assertTrue(Paciente._validar_fecha("01/01/2000"))
        self.assertFalse(Paciente._validar_fecha("31-12-1999"))
        self.assertFalse(Paciente._validar_fecha(""))

if __name__ == "__main__":
    unittest.main()
