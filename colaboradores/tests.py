from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status
from .models import Colaboradores
from rest_framework.test import APIClient
from .serializers import ColaboradoresSerializer
from django.forms.models import model_to_dict

class ColaboradoresTestSuccess(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('colaboradores/', include('colaboradores.urls')),
    ]

    @classmethod
    def setUpTestData(cls):
        cls.colaborador = Colaboradores.objects.create(
            cpf="427.383.270-44",
            nome="Mateus",
            dt_nascimento="2004-02-17"
        )

    def setUp(self):
        self.client = APIClient()

    def test_criar_colaborador(self):
        url = reverse('colab-create')
        data = {
            "cpf":"248.604.240-77", 
            "nome":"Novo Colaborador",
            "dt_nascimento":"2006-04-05"
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data['id_colaborador'] = None
        self.assertEqual(response.data, data)
        self.assertIsNotNone(Colaboradores.objects.filter(cpf=data['cpf']).first())

    def test_listar_colaboradores(self):
        Colaboradores.objects.create(
            cpf="744.454.470-05",
            nome="Novo colaborador 2",
            dt_nascimento="2006-04-05"
        )
        Colaboradores.objects.create(
            cpf="725.658.550-01", 
            nome="Novo colaborador 3",
            dt_nascimento="2006-04-05"
        )
        url = reverse('colab-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_visualizar_colaborador(self):
        url = reverse('colab-retrieve', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['cpf'], self.colaborador.cpf)
        self.assertEqual(
            response.data['dt_nascimento'],
            self.colaborador.dt_nascimento
        )

    def test_editar_colaborador(self):
        url_editar = reverse('colab-patch', kwargs={"pk":1})
        data = {
            "nome":"Nome atualizado",
            "dt_nascimento":"2004-10-12"
        }
        response_editar = self.client.patch(url_editar, data=data)
        self.assertEqual(response_editar.status_code, status.HTTP_200_OK)
        self.assertEqual(response_editar.data['nome'], data['nome'])
        self.assertEqual(response_editar.data['dt_nascimento'], data['dt_nascimento'])
        
        url_visualizar = reverse('colab-retrieve', kwargs={'pk':1})
        response_visualizar = self.client.get(url_visualizar)
        data['id_colaborador'] = 1
        data['cpf'] = self.colaborador.cpf
        self.assertEqual(response_visualizar.data, data)

    def test_excluir_colaborador(self):
        url = reverse('colab-delete', kwargs={'pk':1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertIsNone(Colaboradores.objects.filter(id_colaborador=1).first())
