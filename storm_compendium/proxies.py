# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from flask import current_app
from werkzeug.local import LocalProxy


current_compendium_extension = LocalProxy(
    lambda: current_app.extensions["storm-compendium"]
)
"""Helper proxy to get the current StormCompendium extension."""


current_compendium_service = LocalProxy(
    lambda: current_app.extensions["storm-compendium"].compendium_service
)
"""Helper proxy to get the current StormCompendium service extension."""
