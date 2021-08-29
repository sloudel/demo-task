# Generated by Django 3.2.6 on 2021-08-29 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ContentBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('view_counter', models.PositiveBigIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('contentbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='index.contentbase')),
                ('data_file', models.FileField(upload_to='audio/%Y/%m/%d/')),
            ],
            options={
                'abstract': False,
            },
            bases=('index.contentbase',),
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('contentbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='index.contentbase')),
                ('data', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('index.contentbase',),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('contentbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='index.contentbase')),
                ('data_file', models.FileField(upload_to='video/%Y/%m/%d/')),
                ('subtitles_file', models.FileField(upload_to='subtitles/%Y/%m/%d/')),
            ],
            options={
                'abstract': False,
            },
            bases=('index.contentbase',),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('content', models.ManyToManyField(to='index.Content')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='content',
            name='audios',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content', to='index.audio'),
        ),
        migrations.AddField(
            model_name='content',
            name='texts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content', to='index.text'),
        ),
        migrations.AddField(
            model_name='content',
            name='videos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content', to='index.video'),
        ),
    ]
