from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0018_remove_productosacademicos_nombrerecurso'),
    ]

    operations = [
        migrations.AddField(
            model_name='datospersonales',
            name='estadocivil',
            field=models.CharField(
                max_length=50,
                blank=True,
                null=True,
                choices=[
                    ("SOLTERO", "Soltero/a"),
                    ("CASADO", "Casado/a"),
                    ("DIVORCIADO", "Divorciado/a"),
                    ("VIUDO", "Viudo/a"),
                    ("UNION_LIBRE", "Unión libre"),
                ],
            ),
        ),
    ]
