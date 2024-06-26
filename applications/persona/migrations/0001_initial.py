# Generated by Django 3.2.16 on 2023-04-14 03:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('hobby', models.CharField(max_length=50, verbose_name='Pasa tiempo')),
            ],
            options={
                'verbose_name': 'Hobby',
                'verbose_name_plural': 'hobbies',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('full_name', models.CharField(max_length=50, verbose_name='Nombres')),
                ('job', models.CharField(blank=True, max_length=30, verbose_name='Trabajo')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='telefono')),
                ('hobbies', models.ManyToManyField(to='persona.Hobby')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
        migrations.CreateModel(
            name='Reunion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('asunto', models.CharField(max_length=100, verbose_name='Asunto de Reunión')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.person')),
            ],
            options={
                'verbose_name': 'Reunión',
                'verbose_name_plural': 'Reunión',
            },
        ),
    ]
