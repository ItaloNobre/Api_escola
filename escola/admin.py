from django.contrib import admin
from escola.models import Aluno, Curso, Matricula


class Alunos(admin.ModelAdmin):
    """  Quais os Campos que eu quero exibir no display do meu admin """
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    """ Sempre que eu quiser alterar algum aluno posso clicar ou no id ou no nome """
    list_display_links = ('id', 'nome')
    """ eu quero também um campo de busca de alunos por nome """
    search_fields = ('nome',)
    """ paginação na quantidade de alunos """
    list_per_page = 20
    
    """ o primeiro parametro é o modelo, e o segundo e a configuração
       do model admin que foi feito"""


admin.site.register(Aluno, Alunos)


class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_link = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)


admin.site.register(Curso, Cursos)


class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_link = ('id')


admin.site.register(Matricula, Matriculas)