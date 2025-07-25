# Generated by Django 5.2.1 on 2025-06-10 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation_volunteer_sys', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='updateondate',
            new_name='updationdate',
        ),
        migrations.RenameField(
            model_name='volunteer',
            old_name='updateondate',
            new_name='updationdate',
        ),
        migrations.AlterField(
            model_name='donation',
            name='donationname',
            field=models.CharField(choices=[('Food Donation', 'Food Donation'), ('Cloth Donation', 'Cloth Donation'), ('Footwear Donation', 'Footwear Donation'), ('Books Donation', 'Books Donation'), ('Furniture Donation', 'Furniture Donation'), ('Vessel Donation', 'Vessel Donation'), ('Other Donation', 'Other Donation')], max_length=200, null=True),
        ),
    ]
