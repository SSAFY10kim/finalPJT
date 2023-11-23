# Generated by Django 4.2.4 on 2023-11-23 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='like_deposit',
            field=models.ManyToManyField(blank=True, null=True, related_name='like_deposit', to='articles.depositproducts'),
        ),
        migrations.AddField(
            model_name='user',
            name='like_saving',
            field=models.ManyToManyField(blank=True, null=True, related_name='like_saving', to='articles.savingproducts'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
