# Generated by Django 5.0 on 2024-09-28 06:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_category_occasion_tag_grooming_clothes_accessories'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='donated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='clothes',
            name='in_laundry',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='clothes',
            name='recycled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='clothes',
            name='worn_today',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='accessories',
            name='occasion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='accessories', to='users.occasion'),
        ),
        migrations.AlterField(
            model_name='accessories',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='accessories', to='users.tag'),
        ),
        migrations.AlterField(
            model_name='accessories',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accessories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clothes', to='users.category'),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='occasion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clothes', to='users.occasion'),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='clothes', to='users.tag'),
        ),
        migrations.AlterField(
            model_name='clothes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grooming',
            name='occasion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grooming', to='users.occasion'),
        ),
        migrations.AlterField(
            model_name='grooming',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='grooming', to='users.tag'),
        ),
        migrations.AlterField(
            model_name='grooming',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grooming', to=settings.AUTH_USER_MODEL),
        ),
    ]
