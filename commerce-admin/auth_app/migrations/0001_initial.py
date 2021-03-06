# Generated by Django 3.0.6 on 2020-06-29 16:43

import auth_app.managers
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('tenant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupTenant',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='name')),
                ('permissions', models.ManyToManyField(related_name='group_tenants', to='auth.Permission', verbose_name='permissions')),
                ('tenant', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='grouptenant_tenants', to='tenant.Tenant', verbose_name='tenant')),
            ],
            options={
                'verbose_name': 'grupo personalizado',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
            ],
            options={
                'verbose_name': 'grupo',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', auth_app.managers.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'usuário admin',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserTenant',
            fields=[
            ],
            options={
                'verbose_name': 'usuário',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth_app.user',),
            managers=[
                ('objects', auth_app.managers.UserTenantManager()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('group_tenants', models.ManyToManyField(blank=True, related_name='group_tenant_members', to='auth_app.GroupTenant')),
                ('groups', models.ManyToManyField(blank=True, related_name='group_members', to='auth.Group')),
                ('permissions', models.ManyToManyField(blank=True, related_name='permission_members', to='auth.Permission')),
                ('tenant', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='member_tenants', to='tenant.Tenant', verbose_name='tenant')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='user_member', to='auth_app.UserTenant')),
            ],
            options={
                'verbose_name': 'membro',
            },
        ),
    ]
