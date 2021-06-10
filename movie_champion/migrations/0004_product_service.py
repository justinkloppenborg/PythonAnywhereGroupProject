# Generated by Django 3.2.4 on 2021-06-05 04:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movie_champion', '0003_auto_20210604_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_category', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('setup_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('cleanup_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('service_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('cust_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='movie_champion.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('p_description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('pickup_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('cust_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='movie_champion.customer')),
            ],
        ),
    ]