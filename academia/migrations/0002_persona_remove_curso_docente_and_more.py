# Generated by Django 5.0.2 on 2024-03-24 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('dni', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('apellidos', models.CharField(max_length=50)),
                ('nombres', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('X', 'No Binario')], default='F', max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='curso',
            name='docente',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='apellidos',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='dni',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='fecha_nacimiento',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='genero',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='nombres',
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='academia.persona')),
                ('categoria', models.CharField(choices=[('1', 'Ayudante de Catedra'), ('2', 'Jefe de Trabajos Practicos'), ('3', 'Profesor Adjunto'), ('4', 'Profesor Asociado'), ('5', 'Titular de Catedra')], default='1', max_length=1)),
                ('dedicacion', models.CharField(choices=[('1', 'Simple'), ('2', 'Semi Exclusiva'), ('3', 'Exclusiva')], default='1', max_length=1)),
                ('curso_a_cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academia.curso')),
            ],
            bases=('academia.persona',),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='persona_ptr',
            field=models.OneToOneField(auto_created=True, default='...', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='academia.persona'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Matricula',
        ),
        migrations.AddField(
            model_name='curso',
            name='docente_a_cargo',
            field=models.ForeignKey(default='...', on_delete=django.db.models.deletion.CASCADE, to='academia.docente'),
            preserve_default=False,
        ),
    ]
