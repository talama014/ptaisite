# Generated by Django 4.0 on 2021-12-17 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.RenameField(
            model_name='message',
            old_name='create',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='update',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='create',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='update',
            new_name='updated',
        ),
    ]