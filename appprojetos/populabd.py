from django.db import transaction,IntegrityError
from appprojetos.models import *

me01 = Membros(nome="Hallessandro", matricula="123")
me02 = Membros(nome="Juliana", matricula="321")
me01.save()
me02.save()

pf01 = Professor(nome="Givanaldo", matricula=456, area_atuacao="Estrutura de Dados")
pf01.save()

nv01 = Nv_desenvolvimento(estagio="C", descricao="Adicionar alguns dados no Banco", dt_registro="2016-6-12")
nv01.save()

at01 = Atividade(descricao="Fazendo consultas", dt_inicio="2016-1-1", dt_termino="2016-6-1",
                 custo= 10, dsvol=nv01)
at01.save()

pj01 = Projeto_pesquisa(titulo="Lista de atividade", dt_inicio="2016-6-8", dt_termino="2016-6-12",
                        justificativa="Praticar os conceitos vistos em sala",
                        metodologia="Atividade prática",
                        resultados_esperados="Terminar antes do prazo",
                        atividade=at01)
pj01.save()
pj01.membros.add(me01,me02,pf01)
