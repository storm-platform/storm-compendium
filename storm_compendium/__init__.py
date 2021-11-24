# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Module that adds support for Compendium management in the Storm Platform."""

from .ext import StormCompendium
from .version import __version__

__all__ = ("__version__", "StormCompendium")
