# Generated by Django 3.2.12 on 2022-02-19 11:08

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_auto_20210126_0403'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='EducationalLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_link', models.CharField(blank=True, max_length=300, null=True)),
                ('company_name', models.CharField(default=None, max_length=300)),
                ('hide_company_name', models.BooleanField()),
                ('job_title', models.CharField(default=None, max_length=200)),
                ('job_description', models.TextField()),
                ('gender', models.NullBooleanField(choices=[(None, 'other'), (True, "'male"), (False, 'female')])),
                ('salary', models.IntegerField(default=0)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('nationality', django_countries.fields.CountryField(blank=True, max_length=746, multiple=True)),
                ('remote', models.BooleanField(default=False)),
                ('years_of_experience', models.IntegerField(default=1)),
                ('skill_set1', models.CharField(max_length=300)),
                ('skill_set2', models.CharField(blank=True, max_length=300, null=True)),
                ('skill_set3', models.CharField(blank=True, max_length=300, null=True)),
                ('cv_required', models.BooleanField(default=False)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('featuredjobs', models.BooleanField(default=False)),
                ('career_level', models.ManyToManyField(to='jobs.CareerLevel')),
            ],
        ),
        migrations.CreateModel(
            name='MonthlySalary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='jobadmin',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='jobcategory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='JobPost',
        ),
        migrations.AddField(
            model_name='jobs',
            name='category',
            field=models.ManyToManyField(to='jobs.JobCategory'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='educational_level',
            field=models.ManyToManyField(to='jobs.EducationalLevel'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='employment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.employmenttype'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='job_admin_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.jobadmin'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='monthly_salary',
            field=models.ManyToManyField(to='jobs.MonthlySalary'),
        ),
    ]
