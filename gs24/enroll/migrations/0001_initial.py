# Generated by Django 3.1.7 on 2021-04-02 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField()),
                ('stuname', models.CharField(max_length=100)),
                ('stuemail', models.EmailField(max_length=100)),
                ('stupass', models.CharField(max_length=100)),
            ],
        ),
    ]
