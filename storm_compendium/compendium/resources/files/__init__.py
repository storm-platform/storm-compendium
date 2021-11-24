# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from .config import (
    FileCompendiumDraftResourceConfig,
    FileCompendiumRecordResourceConfig,
    CompendiumFileCommonResourceConfig,
)

from .resource import CompendiumFileResource

__all__ = (
    # Resource
    "CompendiumFileResource",
    # Config
    "CompendiumFileCommonResourceConfig",
    "FileCompendiumDraftResourceConfig",
    "FileCompendiumRecordResourceConfig",
)
