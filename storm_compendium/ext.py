# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Module that adds support for Compendium management in the Storm Platform."""

import storm_compendium.config as config

from storm_compendium.compendium.resources.compendium import (
    CompendiumResource,
    CompendiumResourceConfig,
)
from storm_compendium.compendium.resources.files import (
    CompendiumFileResource,
    FileCompendiumRecordResourceConfig,
    FileCompendiumDraftResourceConfig,
)
from storm_compendium.compendium.services.compendium.config import (
    CompendiumServiceConfig,
)
from storm_compendium.compendium.services.compendium.service import CompendiumService
from storm_compendium.compendium.services.files.config import (
    FileCompendiumDraftServiceConfig,
    FileCompendiumRecordServiceConfig,
)

from storm_compendium.compendium.services.files.service import CompendiumFileService


class StormCompendium(object):
    """storm-compendia extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)

        # Services
        self.init_services(app)

        # Resources
        self.init_resources(app)

        app.extensions["storm-compendium"] = self

    def init_config(self, app):
        """Initialize configuration."""
        for k in dir(config):
            if k.startswith("STORM_COMPENDIUM_"):
                app.config.setdefault(k, getattr(config, k))

    def init_services(self, app):
        """Initialize compendium services."""

        #
        # Files services
        #
        self.files_service = CompendiumFileService(FileCompendiumRecordServiceConfig)
        self.files_draft_service = CompendiumFileService(
            FileCompendiumDraftServiceConfig
        )

        #
        # Compendium service
        #
        self.compendium_service = CompendiumService(
            config=CompendiumServiceConfig,
            files_service=self.files_service,
            draft_files_service=self.files_draft_service,
        )

    def init_resources(self, app):
        """Initialize compendium resources."""

        #
        # Compendium resource
        #
        self.compendium_resource = CompendiumResource(
            CompendiumResourceConfig, self.compendium_service
        )

        #
        # Compendium Files (Record)
        #
        self.compendium_files_resource = CompendiumFileResource(
            FileCompendiumRecordResourceConfig, self.files_service
        )

        #
        # Compendium Files (Draft)
        #
        self.compendium_draft_files_resource = CompendiumFileResource(
            FileCompendiumDraftResourceConfig, self.files_draft_service
        )
