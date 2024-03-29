from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula
from escola.validators import *


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "o Cpf não é valido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "nao inclua números neste campo"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': " o RG deve conter 9 digitos"})
        return data


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
       
        model = Matricula
        exclude = []


class ListaMatriculasAlunosSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')

    class Meta:
        model = Matricula
        fields = ['aluno_nome']
