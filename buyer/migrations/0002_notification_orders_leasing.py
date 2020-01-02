# Generated by Django 2.0.9 on 2018-12-11 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('seller', '0006_commonnotification'),
        ('buyer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default='', max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Products_Selling')),
            ],
        ),
        migrations.CreateModel(
            name='Orders_Leasing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('isConfirmed', models.BooleanField(default=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
                ('products_leasing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Products_Leasing')),
            ],
        ),
    ]
