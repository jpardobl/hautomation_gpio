#!/usr/bin/env python

import os
import sys


def populate_db():
    pwd = os.getcwd()
    sys.path.append(pwd)

    try:
        if "DJANGO_SETTINGS_MODULE" not in os.environ:
            raise ImportError("No DJANGO_SETTINGS_MODULE env variable found")

        from hacore.models import Protocol

        if Protocol.objects.filter(name="GPIO").count() == 0:
            Protocol(
                name="GPIO",
                gobj_name="driver_GPIO",
                module="hautomation_gpio",
                validate_address_module="hautomation_gpio.utils").save()
            sys.stdout.writelines("Protocoll successfully populated into db")
        else:
            sys.stdout.writelines("Protocol is already at the db. No changes made.")
        sys.path.remove(os.getcwd())
        sys.exit(0)
    except Exception as  ex:
        sys.path.remove(os.getcwd())
        sys.stderr.writelines(ex.message)
        sys.exit(1)
