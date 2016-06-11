from django.db import transaction,IntegrityError
from appprojetos.models import *


me01=Membros(nome="Hallessandro",matricula="123")
me02=Membros(nome='Monic',matricula='321')

me01.save()
me02.save()

