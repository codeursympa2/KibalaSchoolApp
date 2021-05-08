# Generated by Django 3.1.3 on 2021-05-07 23:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('Matricle', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=20)),
                ('Prenom', models.CharField(max_length=20)),
                ('DateNaiss', models.DateField(default=datetime.date.today)),
                ('LieuNaiss', models.TextField(max_length=45)),
                ('Sexe', models.CharField(max_length=20)),
                ('Taille', models.FloatField()),
                ('Photo', models.CharField(max_length=60)),
                ('Nationalite', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Tuteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=20)),
                ('Prenom', models.CharField(max_length=20)),
                ('Sexe', models.CharField(max_length=20)),
                ('StMat', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MontantMensuel', models.FloatField()),
                ('MontantInscription', models.FloatField()),
                ('Niveau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.niveau')),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateInsc', models.DateTimeField(auto_now_add=True)),
                ('Etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.etudiant')),
                ('Niveau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.niveau')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='etudiant',
            name='Tuteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.tuteur'),
        ),
    ]
