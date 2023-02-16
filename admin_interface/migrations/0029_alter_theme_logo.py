# Generated by Django 4.1.3 on 2023-02-16 12:18

import django.core.files.storage
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("admin_interface", "0028_alter_theme_logo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="theme",
            name="logo",
            field=models.FileField(
                blank=True,
                help_text="Leave blank to use the default Django logo",
                storage=django.core.files.storage.FileSystemStorage(
                    base_url="/", location="/code/static/"
                ),
                upload_to="admin-interface/logo/",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["gif", "jpg", "jpeg", "png", "svg"]
                    )
                ],
                verbose_name="logo",
            ),
        ),
    ]
