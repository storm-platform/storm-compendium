# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from invenio_records_resources.services import FileService


class CompendiumFileService(FileService):
    """Compendium file service."""


__all__ = "CompendiumFileService"
