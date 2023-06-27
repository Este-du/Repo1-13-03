# Generated by Django 4.2.2 on 2023-06-24 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('categoria_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('sku', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=150)),
                ('stock', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
                ('fecha_vencimiento', models.DateField(blank=True, null=True)),
                ('image_url', models.ImageField(upload_to='imagenesProductos')),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SentryAni.categoria')),
            ],
        ),
    ]
