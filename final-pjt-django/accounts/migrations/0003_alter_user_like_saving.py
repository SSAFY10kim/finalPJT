# Generated by Django 4.2.4 on 2023-11-17 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_like_saving_user_id'),
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='like_saving',
            field=models.ManyToManyField(blank=True, null=True, related_name='like_saving', to='articles.savingproducts'),
        ),
    ]