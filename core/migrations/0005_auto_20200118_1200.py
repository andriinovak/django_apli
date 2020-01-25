# Generated by Django 3.0.2 on 2020-01-18 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_feedback_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('bot_name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='feedback',
            options={'ordering': ['-created_at']},
        ),
    ]
