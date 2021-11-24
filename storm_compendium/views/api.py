# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.


def init_compendium_blueprint_api(app):
    """Create Compendium API Blueprint."""
    ext = app.extensions["storm-compendium"]

    return ext.compendium_resource.as_blueprint()


def init_compendium_files_blueprint_api(app):
    """Create Compendium Files API Blueprint."""
    ext = app.extensions["storm-compendium"]

    return ext.compendium_files_resource.as_blueprint()


def init_compendium_draft_files_blueprint_api(app):
    """Create Compendium Draft Files API Blueprint."""
    ext = app.extensions["storm-compendium"]

    return ext.compendium_draft_files_resource.as_blueprint()


__all__ = (
    "init_compendium_blueprint_api",
    "init_compendium_files_blueprint_api",
    "init_compendium_draft_files_blueprint_api",
)
