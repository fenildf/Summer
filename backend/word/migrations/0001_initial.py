# Generated by Django 2.0.6 on 2018-06-21 07:14

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
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50, unique=True)),
                ('phonetic', models.CharField(max_length=50, null=True)),
                ('definitation', models.TextField(null=True)),
                ('translation', models.TextField(null=True)),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WordBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('zk', '中考'), ('gk', '高考'), ('ky', '考研'), ('cet4', '四级'), ('cet6', '六级'), ('ielts', '雅思'), ('toefl', '托福'), ('gre', 'GRE')], max_length=4)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('introduction', models.CharField(blank=True, max_length=500)),
                ('cover', models.ImageField(default='user/aa.jpg', upload_to='wordbook')),
                ('creator', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='word',
            name='wordbook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='word.WordBook'),
        ),
    ]
