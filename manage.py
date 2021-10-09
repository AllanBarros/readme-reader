#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    #VSCODE DEBUGGER PARA AMBIENTE LOCAL
    
    if os.environ.get("VSCODE_DEBUGGER", False):
    
        import ptvsd
        ptvsd_port = 4000

        try:
            ptvsd.enable_attach(address=("0.0.0.0", ptvsd_port), redirect_output=True)
            print("Started ptvsd at port %s." % ptvsd_port)
        except OSError:
            print("ptvsd port %s already in use." % ptvsd_port)
    
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
