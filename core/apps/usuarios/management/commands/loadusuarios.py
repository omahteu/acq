from django.core.management.base import BaseCommand
from django.core import management

from apps.usuarios.models import Perfil


class Command(BaseCommand):

    help = 'Populate specific tables for the first time.'

    def handle(self, *args, **kwargs):
        if Perfil.objects.all():
            self.stdout.write('Perfil already populated.')
        else:
            management.call_command(
                'loaddata', 'perfil', format='json', verbosity=0
            )
            self.stdout.write('Perfis adicionados com sucesso!')

        # if Usuario.objects.all():
        #     self.stdout.write('Usuario already populated.')
        # else:
        #     management.call_command(
        #         'loaddata', 'usuario', format='json', verbosity=0
        #     )
        #     self.stdout.write('Successfully populated Usuario!')
