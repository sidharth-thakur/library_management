# Generated by Django 5.0.3 on 2024-03-16 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('book_file', models.FileField(default='', upload_to='books_pdfs')),
                ('book_cover', models.ImageField(default='', upload_to='library_manage/books_image')),
                ('ratings', models.DecimalField(decimal_places=1, default=2, max_digits=3)),
                ('status', models.CharField(choices=[('available', 'Available'), ('borrowed', 'Borrowed')], default='Available', max_length=20)),
            ],
        ),
    ]
