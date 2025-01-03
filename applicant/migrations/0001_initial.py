# Generated by Django 3.0.3 on 2020-02-23 18:28

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
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.TextField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('south_african', models.BooleanField(default=True)),
                ('id_number', models.SlugField()),
                ('population_group', models.SlugField()),
                ('marital_status', models.SlugField()),
                ('home_language', models.SlugField()),
                ('religious_affiliation', models.SlugField()),
                ('nok_relationship', models.TextField(max_length=30)),
                ('school', models.TextField(max_length=70)),
                ('location', models.TextField(max_length=70)),
                ('writing_loc', models.TextField(blank=True, max_length=70)),
                ('exam_number', models.SlugField(blank=True)),
                ('authority', models.TextField(max_length=50)),
                ('qualification_complete', models.BooleanField(blank=True)),
                ('exam_month', models.SlugField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(blank=True, max_length=30)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_subject', to='applicant.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='StudyHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_programme', models.TextField(max_length=70)),
                ('institution', models.TextField(max_length=70)),
                ('student_number', models.SlugField()),
                ('full_time', models.BooleanField(default=True)),
                ('registration_date0', models.DateField()),
                ('registration_date1', models.DateField()),
                ('graduation_date', models.DateField()),
                ('status', models.SlugField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_history', to='applicant.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.TextField(max_length=30)),
                ('level', models.TextField(max_length=50)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_sport', to='applicant.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='SpecialNeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('special_need', models.TextField(max_length=30)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_special', to='applicant.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.SlugField()),
                ('document', models.ImageField(upload_to='documents')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_document', to='applicant.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_type', models.SlugField()),
                ('title', models.TextField(max_length=30)),
                ('surname', models.TextField(max_length=30)),
                ('full_names', models.TextField(max_length=30)),
                ('street', models.TextField(max_length=70)),
                ('city', models.TextField(max_length=70)),
                ('province', models.TextField(max_length=70)),
                ('country', models.TextField(max_length=70)),
                ('code', models.SlugField()),
                ('number_1', models.SlugField()),
                ('number_2', models.SlugField(blank=True)),
                ('number_3', models.SlugField(blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_details', to='applicant.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.TextField(max_length=30)),
                ('choice_order', models.IntegerField(default=0)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_choice', to='applicant.Applicant')),
            ],
        ),
    ]
