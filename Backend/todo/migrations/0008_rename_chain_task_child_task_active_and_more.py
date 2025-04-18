# Generated by Django 5.2 on 2025-04-18 14:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0007_alter_task_options_remove_task_start_time"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="chain",
            new_name="child",
        ),
        migrations.AddField(
            model_name="task",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="task",
            name="oldestAncestor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="descendants",
                to="todo.task",
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="original_date",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subtask",
                to="todo.task",
            ),
        ),
    ]
