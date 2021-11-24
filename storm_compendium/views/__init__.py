# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from flask import Blueprint

from .api import (
    init_compendium_blueprint_api,
    init_compendium_files_blueprint_api,
    init_compendium_draft_files_blueprint_api,
)


blueprint = Blueprint("storm_compendium_ext", __name__)


@blueprint.record_once
def registry(state):
    """Register services."""
    app = state.app

    ext = app.extensions["storm-compendium"]
    registry = app.extensions["invenio-records-resources"].registry

    registry.register(ext.compendium_service, service_id="storm-compendium-service")
    registry.register(ext.files_service, service_id="storm-compendium-files-service")
    registry.register(
        ext.files_draft_service, service_id="storm-compendium-draft-files-service"
    )


__all__ = (
    "blueprint",
    "init_compendium_blueprint_api",
    "init_compendium_files_blueprint_api",
    "init_compendium_draft_files_blueprint_api",
)
