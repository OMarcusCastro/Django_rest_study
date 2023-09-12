from rest_framework import viewsets,generics
from escola.models import Aluno, Curso,Matricula
from escola.serializer import AlunoSerializer, CursoSerializer,MatriculaSerializer,ListaMatriculasAlunoSerializer
from escola.serializer import ListaAlunosMatriculadosSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculasViewSet(viewsets.ModelViewSet):
    """Listando todas as matriculas """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculasAluno(generics.ListAPIView):
    def get_queryset(self):
        queryset=Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class=ListaMatriculasAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos matriculados em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer