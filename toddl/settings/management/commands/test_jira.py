from django.core.management import BaseCommand
from jira import JIRA

BASE_URI = "https://thorgatedigital.atlassian.net/rest/api/3/"


class Command(BaseCommand):
    def handle(self, *args, **options):
        jira = JIRA(basic_auth=('yuriy@thorgate.eu', API_TOKEN), options={
            'server': "https://thorgatedigital.atlassian.net/",
        })


