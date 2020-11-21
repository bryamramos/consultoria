# Generated by Django 2.1.5 on 2020-11-19 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_cliente_asunto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('asesor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Asesor')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.Cliente')),
            ],
        ),
    ]
