# Generated by Django 4.0.5 on 2022-06-24 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_maincategory_category_main_cat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maincategory',
            options={'verbose_name': 'main category', 'verbose_name_plural': 'Main Category'},
        ),
        migrations.AlterField(
            model_name='category',
            name='main_cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='category.maincategory'),
        ),
    ]