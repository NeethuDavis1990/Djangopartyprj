# Generated by Django 3.2 on 2021-04-15 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partyapp', '0006_alter_partymastermodel_invitees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partymastermodel',
            name='Invitees',
            field=models.ManyToManyField(related_name='Partymastermodel', through='partyapp.Partyinviteesbridgemodel', to='partyapp.Inviteesmastermodel'),
        ),
    ]
