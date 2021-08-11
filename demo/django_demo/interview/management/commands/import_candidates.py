import csv
from django.core.management import BaseCommand
from interview.models import Candidate

class Command(BaseCommand):
    help = '从 csv 文件导入信息到数据库中。'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)
    
    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                Candidate.objects.create(
                    username = row[0],
                    city = row[1],
                    phone = row[2],
                    email = row[3],
                )