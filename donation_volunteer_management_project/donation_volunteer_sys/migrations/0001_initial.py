# Generated by Django 5.2.1 on 2025-06-06 09:13

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
            name='DonationArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areaname', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=230, null=True)),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=300, null=True)),
                ('address', models.CharField(max_length=120, null=True)),
                ('userpic', models.ImageField(blank=True, null=True, upload_to='donor')),
                ('regdate', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donationname', models.CharField(max_length=200, null=True)),
                ('donationpic', models.ImageField(blank=True, null=True, upload_to='donation')),
                ('collectionloc', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=300, null=True)),
                ('status', models.CharField(max_length=300, null=True)),
                ('donationdate', models.DateField(null=True)),
                ('adminremark', models.CharField(max_length=300, null=True)),
                ('volunteerremark', models.CharField(max_length=300, null=True)),
                ('updateondate', models.DateField(null=True)),
                ('donationarea', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='donation_volunteer_sys.donationarea')),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donation_volunteer_sys.donor')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliverypic', models.FileField(null=True, upload_to='')),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
                ('donation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donation_volunteer_sys.donation')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=110, null=True)),
                ('address', models.CharField(max_length=300, null=True)),
                ('userpic', models.ImageField(blank=True, null=True, upload_to='volunteer')),
                ('idpic', models.ImageField(blank=True, null=True, upload_to='volunteer')),
                ('aboutme', models.CharField(max_length=300, null=True)),
                ('status', models.CharField(max_length=120, null=True)),
                ('regdate', models.DateTimeField(auto_now_add=True)),
                ('adminremark', models.CharField(max_length=300, null=True)),
                ('updateondate', models.DateField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='donation',
            name='volunteer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='donation_volunteer_sys.volunteer'),
        ),
    ]
