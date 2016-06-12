from django.db import models

class Membros(models.Model):
    nome = models.CharField("Nome", max_length=150)
    matricula = models.CharField("Matricula", max_length=12)

    def __str__(self):
        return self.nome

class Professor(Membros):
    area_atuacao = models.CharField("Area de atuação", max_length=255)

class Nv_desenvolvimento(models.Model):
    ESTAGIO = (
        ('I', 'Iniciada'),
        ('D', 'Desenvolvimento'),
        ('C', 'Concluida'),
    )
    estagio = models.CharField(max_length=1, choices=ESTAGIO)
    descricao = models.CharField("Descrição", max_length=255)
    dt_registro = models.DateField("Data do registro")

    def __str__(self):
        return self.descricao

class Atividade(models.Model):
    descricao = models.CharField("Descrição", max_length=255)
    dt_inicio = models.DateField("Data de inicio da atividade")
    dt_termino = models.DateField("Data de termino da atividade")
    custo = models.FloatField("Custo da atividade")
    dsvol = models.ForeignKey(Nv_desenvolvimento, on_delete=models.PROTECT, verbose_name="Nivel de desenvolvimento")

    def __str__(self):
        return self.descricao

class Projeto_pesquisa(models.Model):
    titulo = models.CharField("Titulo", max_length=255)
    dt_inicio = models.DateField("Data de inicio")
    dt_termino = models.DateField("Data de termino")
    justificativa = models.CharField("Justificativa", max_length=255)
    metodologia = models.CharField("Metodologia", max_length=255)
    resultados_esperados = models.CharField("Resultados Esperados", max_length=255)
    atividade = models.ForeignKey(Atividade, on_delete=models.PROTECT, verbose_name="Atividade desenvolvida")
    membros = models.ManyToManyField(Membros)

    def __str__(self):
        return self.titulo

