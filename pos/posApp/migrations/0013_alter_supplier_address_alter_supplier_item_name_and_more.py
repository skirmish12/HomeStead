# Generated by Django 4.2.2 on 2024-01-27 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posApp', '0012_remove_supplier_created_date_remove_supplier_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.CharField(default='Unknown Address', max_length=255),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='item_name',
            field=models.CharField(default='Unknown Item Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='item_number',
            field=models.CharField(default='Unknown Item Number', max_length=255),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(default='Unknown Supplier', max_length=255),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]