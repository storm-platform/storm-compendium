# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from storm_compendium.compendium.services.links import (
    CompendiumRecordLink,
    CompendiumFileLink,
)

from storm_compendium.compendium.services.security.permissions import (
    CompendiumRecordPermissionPolicy,
)

from storm_compendium.compendium.records.api import CompendiumDraft, CompendiumRecord

from invenio_drafts_resources.services.records.config import is_record
from invenio_records_resources.services import FileServiceConfig, ConditionalLink


def file_record_is_draft(file, ctx):
    """Shortcut for links to determine if record is a record."""
    return file.record.is_draft


class FileServiceCommonConfig(FileServiceConfig):
    permission_policy_cls = CompendiumRecordPermissionPolicy

    file_links_list = {
        "self": ConditionalLink(
            cond=is_record,
            if_=CompendiumRecordLink(
                "{+api}/projects/{project_id}/compendia/{id}/files{?args*}"
            ),
            else_=CompendiumRecordLink(
                "{+api}/projects/{project_id}/compendia/{id}/draft/files{?args*}"
            ),
        ),
    }

    file_links_item = {
        "self": ConditionalLink(
            cond=file_record_is_draft,
            if_=CompendiumFileLink(
                "{+api}/projects/{project_id}/compendia/{id}/draft/files{?args*}"
            ),
            else_=CompendiumFileLink(
                "{+api}/projects/{project_id}/compendia/{id}/files{?args*}"
            ),
        ),
        "content": ConditionalLink(
            cond=file_record_is_draft,
            if_=CompendiumFileLink(
                "{+api}/projects/{project_id}/compendia/{id}/draft/files/{key}/content{?args*}"
            ),
            else_=CompendiumFileLink(
                "{+api}/projects/{project_id}/compendia/{id}/files/{key}/content{?args*}"
            ),
        ),
        "commit": CompendiumFileLink(
            "{+api}/projects/{project_id}/compendia/{id}/draft/files/{key}/commit{?args*}",
            when=file_record_is_draft,
        ),
    }


class FileCompendiumDraftServiceConfig(FileServiceCommonConfig):
    record_cls = CompendiumDraft
    permission_action_prefix = "draft_"


class FileCompendiumRecordServiceConfig(FileServiceCommonConfig):
    record_cls = CompendiumRecord


__all__ = (
    "FileServiceCommonConfig",
    "FileCompendiumDraftServiceConfig",
    "FileCompendiumRecordServiceConfig",
)
