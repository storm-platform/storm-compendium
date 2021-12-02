# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Module that adds support for Compendium management in the Storm Platform."""

from .ext import StormCompendium
from .version import __version__

from .proxies import current_compendium_extension, current_compendium_service


__all__ = (
    # Extension constructor
    "StormCompendium",
    # Proxies
    "current_compendium_service",
    "current_compendium_extension",
    # Library metadata
    "__version__",
)
