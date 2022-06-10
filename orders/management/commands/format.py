from argparse import ArgumentParser
from glob import glob
from os.path import dirname, join
from pathlib import Path

from black import FileMode, Report, WriteBack, reformat_many
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def agg_arguments(self, parser: ArgumentParser):
        pass

    def handle(self, *args, **options):
        management_dir = dirname(dirname(__file__))
        project_dir = dirname(dirname(management_dir))
        files = glob(join(project_dir, "**", "*.py"), recursive=True)

        reformat_many(
            sources=set([Path(f) for f in files]),
            fast=True,
            write_back=WriteBack.YES,
            mode=FileMode(),
            report=Report(quiet=True),
            workers=None,
        )
