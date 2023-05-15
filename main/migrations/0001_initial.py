# Generated by Django 4.1.3 on 2023-05-15 17:13

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import main.models.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id_comment', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=250)),
                ('main_comment_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id_device', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('premier', models.DateField()),
                ('device_type', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to=main.models.models.filepath)),
                ('accepted', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='OS',
            fields=[
                ('id_os', models.IntegerField(primary_key=True, serialize=False)),
                ('version', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField(null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('accepted', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id_spec', models.IntegerField(primary_key=True, serialize=False)),
                ('processor', models.CharField(max_length=50, null=True)),
                ('ram', models.IntegerField(null=True)),
                ('memory', models.IntegerField(null=True)),
                ('battery', models.IntegerField(null=True)),
                ('size', models.CharField(max_length=10, null=True)),
                ('price', models.FloatField(null=True)),
                ('screen_type', models.CharField(max_length=20, null=True)),
                ('devices_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.devices')),
            ],
        ),
        migrations.CreateModel(
            name='OS_devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devices_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.devices')),
                ('os_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.os')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField()),
                ('dislike', models.BooleanField()),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.comment')),
                ('devices_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.devices')),
                ('os_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.os')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Followed_devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devices_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.devices')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Error_report',
            fields=[
                ('id_error', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=500)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField(null=True)),
                ('devices_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.devices')),
                ('os_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.os')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='devices_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.devices'),
        ),
        migrations.AddField(
            model_name='comment',
            name='os_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.os'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
