#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from make_request import mn
from threading import Thread
ex=0
 
# task that runs at a fixed interval
def background_task(interval_sec):
    # run forever
    while True:
        # block for the interval
        mn()


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    if (ex==0):
        print('Starting background task...')
        daemon = Thread(target=background_task, args=(3,), daemon=True, name='Background')
        daemon.start()
        ex+=1
    print("Staring Server")
    main()
