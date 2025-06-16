# test_clinica.py

import unittest
from clinica import Clinica
from paciente import Paciente
from medico import Medico
from turno import Turno
from historia_clinica import HistoriaClinica
from excepciones import (
    PacienteYaExisteError, PacienteNoEncontradoError,
    MedicoYaExisteError, MedicoNoEncontradoError,
    TurnoYaExisteError, HistoriaClinicaNoEncontradaError
)
from datetime import datetime

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("12345678", "Ana", "Perez", 30)
        self.medico = Medico("MAT001", "Dr. Juan", "Gomez", "Cardiología")
        self.turno = Turno(self.paciente, self.medico, datetime(2025, 6, 12, 10, 30))

    def test_agregar_y_obtener_paciente(self):
        self.clinica.agregar_paciente(self.paciente)
        paciente_obtenido = self.clinica.obtener_paciente("12345678")
        self.assertEqual(paciente_obtenido.dni, "12345678")

    def test_agregar_paciente_duplicado_error(self):
        self.clinica.agregar_paciente(self.paciente)
        with self.assertRaises(PacienteYaExisteError):
            self.clinica.agregar_paciente(self.paciente)

    def test_obtener_paciente_no_existente_error(self):
        with self.assertRaises(PacienteNoEncontradoError):
            self.clinica.obtener_paciente("99999999")

    def test_agendar_turno_y_prevenir_duplicado(self):
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        self.clinica.agendar_turno(self.turno)
        self.assertIn(self.turno, self.clinica.obtener_turnos())
        with self.assertRaises(TurnoYaExisteError):
            self.clinica.agendar_turno(self.turno)

    def test_obtener_historia_clinica(self):
        self.clinica.agregar_paciente(self.paciente)
        historia = self.clinica.obtener_historia_clinica(self.paciente.dni)
        self.assertIsInstance(historia, HistoriaClinica)

    def test_obtener_historia_clinica_no_existente(self):
        with self.assertRaises(HistoriaClinicaNoEncontradaError):
            self.clinica.obtener_historia_clinica("00000000")

    def test_agregar_y_obtener_medico(self):
        self.clinica.agregar_medico(self.medico)
        medico_obtenido = self.clinica.obtener_medico("MAT001")
        self.assertEqual(medico_obtenido.matricula, "MAT001")

    def test_agregar_medico_duplicado_error(self):
        self.clinica.agregar_medico(self.medico)
        with self.assertRaises(MedicoYaExisteError):
            self.clinica.agregar_medico(self.medico)

if __name__ == '__main__':
    unittest.main()
