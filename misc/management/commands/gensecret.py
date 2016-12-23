import os
import random
import string

from django.conf import settings
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Generate a new secret key'
    requires_system_checks = False
    requires_migrations_checks = False
    can_import_settings = True

    def handle(self, *args, **options):
        secrets_file = os.path.join(settings.BASE_DIR, 'secretkey.txt')
        secret = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(50))

        try:
            open(secrets_file, 'w').write(secret)
        except IOError:
            self.stderr.write("ERROR: Unable to create secrets file (" + secrets_file + ")")
            return

        self.stdout.write("Generated new secrets file")
