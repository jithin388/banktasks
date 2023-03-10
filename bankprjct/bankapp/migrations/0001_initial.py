# Generated by Django 4.1 on 2023-01-12 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Gold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gram', models.IntegerField()),
                ('carat', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female'), ('O', 'other')], max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('aadhar', models.CharField(max_length=30)),
                ('adhar_img', models.ImageField(upload_to='loan')),
                ('pan', models.CharField(max_length=30)),
                ('pan_img', models.ImageField(upload_to='loan')),
                ('loan_type', models.CharField(choices=[('h', 'housing'), ('p', 'personal'), ('g', 'gold')], max_length=30)),
                ('amount', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('slug', models.SlugField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'place',
                'verbose_name_plural': 'places',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='subplaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subplace', models.CharField(blank=True, max_length=200, null=True)),
                ('districts', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bankapp.place')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.categor')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('dob', models.CharField(max_length=30)),
                ('account', models.CharField(max_length=30)),
                ('material', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.categor')),
                ('subcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bankapp.city')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bankapp.country')),
            ],
        ),
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female'), ('O', 'other')], max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('dob', models.DateField(max_length=30)),
                ('account', models.CharField(choices=[('S', 'savings'), ('C', 'current')], max_length=30)),
                ('material', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.categor')),
                ('subcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.subcategory')),
            ],
            options={
                'verbose_name': 'detail',
                'verbose_name_plural': 'details',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankapp.country'),
        ),
    ]
