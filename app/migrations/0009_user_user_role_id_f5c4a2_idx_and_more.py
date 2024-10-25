# Generated by Django 5.1.1 on 2024-09-28 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_user_user_id_5161ab_idx_user_user_email_ffa2e0_idx'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['role'], name='User_role_id_f5c4a2_idx'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['vendor'], name='User_vendor__66aeac_idx'),
        ),
    ]
