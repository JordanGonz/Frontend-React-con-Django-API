# from django.test import TestCase

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Medico, Paciente


class MedicoViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Medico.objects.create(nombre="Jordan", apellido="Villao", edad=21, especialidad="Doctor")

    def test_obtener_todos_los_medicos(self):
        # Prueba para obtener todos los médicos
        response = self.client.get('http://localhost:8000/api/Medical/Medico/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifica que se haya devuelto una lista con al menos un médico
        self.assertTrue(len(response.data) > 0)

class PacienteViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Paciente.objects.create(nombre="Anthony", apellido="Ramirez", edad=22, correo="anthony@gmail.com", alergia="Dolor de la vista")

    def test_obtener_todos_los_pacientes(self):
        # Prueba para obtener todos los pacientes
        response = self.client.get('http://localhost:8000/api/Medical/Paciente/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifica que se haya devuelto una lista con al menos un paciente
        self.assertTrue(len(response.data) > 0)