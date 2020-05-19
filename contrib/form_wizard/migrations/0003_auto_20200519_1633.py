# Generated by Django 2.1.13 on 2020-05-19 13:33

from django.db import migrations


def migrate_forwards(apps, schema_editor):
    Clients = apps.get_model('form_wizard', 'Client')
    WritingClients = apps.get_model('form_wizard', 'WritingClient')
    
    for client in Clients.objects.all():
        writing_clients = WritingClients(
            first_name=client.first_name,
            last_name=client.last_name,
            eng=client.eng,
            phone=client.phone,
            email=client.email
            )
        writing_clients.save()
        
class Migration(migrations.Migration):

    dependencies = [
        ('form_wizard', '0002_writingclient'),
    ]

    operations = [
        migrations.RunPython(migrate_forwards, migrations.RunPython.noop)
    ]
