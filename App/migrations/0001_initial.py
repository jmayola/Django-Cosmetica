# Generated by Django 5.0.6 on 2024-10-04 04:27

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nom_producto', models.TextField(max_length=50)),
                ('desc_producto', ckeditor.fields.RichTextField(null=True)),
                ('precio_producto', models.IntegerField()),
                ('precioreb_producto', models.IntegerField(null=True)),
                ('stock_producto', models.IntegerField()),
                ('imagen_producto', models.ImageField(default='', upload_to='productos')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('carrito_id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Carrito_detalle',
            fields=[
                ('pk_carritodet', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('carrito_det', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.carrito')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.productos')),
            ],
        ),
    ]
