# Generated by Django 3.2 on 2021-04-22 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0003_auto_20210422_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=64)),
                ('dob', models.DateField(null=True)),
                ('school_class', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='school_app.schoolclass')),
            ],
        ),
        migrations.CreateModel(
            name='StudentGrades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField(choices=[(1, '1'), (1.5, '1+'), (1.75, '2-'), (2, '2'), (2.5, '2+'), (2.75, '3-'), (3, '3'), (3.5, '3+'), (3.75, '4-'), (4, '4'), (4.5, '4+'), (4.75, '5-'), (5, '5'), (5.5, '5+'), (5.75, '6-'), (6, '6')])),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_app.subject')),
            ],
        ),
    ]
