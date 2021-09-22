# Generated by Django 3.0.5 on 2021-06-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('eno', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=50)),
                ('esal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('eddr', models.CharField(max_length=100)),
            ],
        ),
    ]
