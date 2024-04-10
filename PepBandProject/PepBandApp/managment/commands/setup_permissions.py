from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group
from PepBandApp import CustomUser

class Command(BaseCommand):
    help = 'Setup custom permissions for your application'

    def handle(self, *args, **kwargs):
        # Create or get content type
        content_type = ContentType.objects.get_for_model(CustomUser)

        # Create or get permission
        permission, created = Permission.objects.get_or_create(
            codename='can_do_something',
            name='Can do something',
            content_type=content_type,
        )

        # Create or get group
        group, created = Group.objects.get_or_create(name='Custom Group')

        # Assign permission to group
        group.permissions.add(permission)

        self.stdout.write(self.style.SUCCESS('Permissions setup successful'))
