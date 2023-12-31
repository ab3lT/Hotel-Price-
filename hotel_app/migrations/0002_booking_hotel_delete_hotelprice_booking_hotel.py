# Generated by Django 4.2.7 on 2024-01-01 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('num_persons', models.IntegerField()),
                ('flexible_cancellation', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('weekday_price', models.FloatField()),
                ('weekend_price', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='HotelPrice',
        ),
        migrations.AddField(
            model_name='booking',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_app.hotel'),
        ),
    ]
