from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTesteCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user('c3po', password='123456')

    def test_atenticacao_user_com_credenciais_corretas(self):
        """Teste que  verifica a autenticação de um usuario"""
        user = authenticate(username='c3po', password='123456')    
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_requisicao_get_nao_autorizada(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def autenticao_username_incorreto(self):
        self.user = User.objects.create_user('c3pp', password='123456')
        self.assertFalse(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def autenticao_senha_incorreta(self):
        self.user = User.objects.create_user('c3po', password='12345')
        self.assertFalse(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def usuario_autenticado(self):
        self.client.focr_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)