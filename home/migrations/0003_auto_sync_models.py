from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_rename_date_sent_contact_created_at"),
    ]

    operations = [
        # Rename Contact -> ContactMessage (matches current models.py)
        migrations.RenameModel(
            old_name='Contact',
            new_name='ContactMessage',
        ),

        # Rename Project.technologies -> tech_stack
        migrations.RenameField(
            model_name='project',
            old_name='technologies',
            new_name='tech_stack',
        ),

        # Add 'order' field to Project (used for ordering)
        migrations.AddField(
            model_name='project',
            name='order',
            field=models.PositiveIntegerField(default=0, help_text='Lower numbers appear first'),
        ),

        # Create Education model
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('order', models.PositiveIntegerField(default=0, help_text='Lower numbers appear first')),
            ],
            options={'verbose_name_plural': 'Education', 'ordering': ['order']},
        ),

        # Create Experience model
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('partner_label', models.CharField(max_length=200, blank=True, help_text='Optional label shown next to org name, e.g. "Partnered with IBM"')),
                ('github_link', models.URLField(blank=True)),
                ('order', models.PositiveIntegerField(default=0, help_text='Lower numbers appear first')),
            ],
            options={'ordering': ['order']},
        ),

        # Create Blog model
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=True, help_text='Uncheck to save as draft')),
            ],
            options={'ordering': ['-created_at']},
        ),
    ]
