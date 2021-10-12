# Generated by Django 3.2 on 2021-04-12 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partyapp', '0003_auto_20210412_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='partymastermodel',
            name='Invitees',
            field=models.ManyToManyField(related_name='Partymastermodel', through='partyapp.Partyinviteesbridgemodel', to='partyapp.Inviteesmastermodel'),
        ),
        migrations.AddField(
            model_name='partymastermodel',
            name='Menu',
            field=models.ManyToManyField(related_name='Partymastermodel', through='partyapp.Partymenubridgemodel', to='partyapp.Menumastermodel'),
        ),
        migrations.AlterField(
            model_name='partyinviteesbridgemodel',
            name='Invitees',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='party_invitees_bridge_model', to='partyapp.inviteesmastermodel'),
        ),
        migrations.AlterField(
            model_name='partyinviteesbridgemodel',
            name='Party',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='party_invitees_bridge_model', to='partyapp.partymastermodel'),
        ),
        migrations.AlterField(
            model_name='partymenubridgemodel',
            name='Menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='party_menu_bridge_model', to='partyapp.menumastermodel'),
        ),
        migrations.AlterField(
            model_name='partymenubridgemodel',
            name='Party',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='party_menu_bridge_model', to='partyapp.partymastermodel'),
        ),
    ]
