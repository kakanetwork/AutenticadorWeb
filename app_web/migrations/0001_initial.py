# Generated by Django 4.2.5 on 2023-09-30 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario_BD',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=128)),
            ],
        ),
    ]
