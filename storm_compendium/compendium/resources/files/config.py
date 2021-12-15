# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from marshmallow import fields
from invenio_records_resources.resources import (
    FileResourceConfig as BaseFileResourceConfig,
)

from storm_compendium.compendium.records.api import CompendiumDraft, CompendiumRecord


class CompendiumFileCommonResourceConfig(BaseFileResourceConfig):
    allow_upload = True

    request_view_args = {
        "key": fields.Str(),
        "pid_value": fields.Str(),
        "project_id": fields.Str(),
    }


class FileCompendiumDraftResourceConfig(CompendiumFileCommonResourceConfig):
    """Custom file resource configuration."""

    record_cls = CompendiumDraft

    blueprint_name = "storm_compendium_draft_files"
    url_prefix = "/projects/<project_id>/compendia/<pid_value>/draft"


class FileCompendiumRecordResourceConfig(CompendiumFileCommonResourceConfig):
    """Custom file resource configuration."""

    record_cls = CompendiumRecord

    blueprint_name = "storm_compendium_record_files"
    url_prefix = "/projects/<project_id>/compendia/<pid_value>"


__all__ = (
    "CompendiumFileCommonResourceConfig",
    "FileCompendiumDraftResourceConfig",
    "FileCompendiumRecordResourceConfig",
)
