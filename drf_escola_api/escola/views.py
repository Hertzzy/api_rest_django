from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunosViewSet(viewsets.ModelViewSet):
  """Show All Alunos"""
  queryset = Aluno.objects.all()
  serializer_class = AlunoSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
  """Show All Cursos"""
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer

  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class MatriculasViewSet(viewsets.ModelViewSet):
  """Show All Cursos"""
  queryset = Matricula.objects.all()
  serializer_class = MatriculaSerializer

  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class ListaMatriculasAluno(generics.ListAPIView): 
  """Listando as matrículas de um aluno ou aluna"""
  def get_queryset(self):
    queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
    return queryset
  serializer_class = ListaMatriculasAlunoSerializer

  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class ListaAlunosMatriculados(generics.ListAPIView):
  """Listando alunos e alunas matriculados em um curso"""
  serializer_class = ListaAlunosMatriculadosSerializer
  def get_queryset(self):
    queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
    return queryset

  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

