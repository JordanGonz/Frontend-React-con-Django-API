# Generated by Django 4.2.3 on 2023-07-06 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('contraseña', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
