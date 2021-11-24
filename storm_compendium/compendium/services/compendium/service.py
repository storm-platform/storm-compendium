# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from invenio_drafts_resources.services import RecordService


class CompendiumService(RecordService):
    def __init__(self, config, files_service=None, draft_files_service=None):
        """CompendiumService initializer."""
        super().__init__(config, files_service, draft_files_service)


__all__ = "CompendiumService"
