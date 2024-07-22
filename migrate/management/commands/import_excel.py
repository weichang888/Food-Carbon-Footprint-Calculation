import pandas as pd
from django.core.management.base import BaseCommand
from migrate.models import Food

class Command(BaseCommand):
    help = 'Import data from Excel file into the Food model'

    def handle(self, *args, **options):
        file_path = "C:\\web\\myweb\\食物碳足跡.xlsx"  # 确保这是正确的路径
        data = pd.read_excel(file_path)
        for index, row in data.iterrows():
            Food.objects.create(
                name=row['Name'],
                quantity=0,  # 注意字段名称的大小写
                carbon_footprint=row['Carbon footprint'],
                unit=row['Unit']
            )
        self.stdout.write(self.style.SUCCESS('Successfully imported data from Excel'))

