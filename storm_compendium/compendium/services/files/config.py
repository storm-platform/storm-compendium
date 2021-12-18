# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from invenio_drafts_resources.services.records.config import is_record
from invenio_records_resources.services import FileServiceConfig, ConditionalLink
from storm_project.project.services.links import (
    ProjectContextFileLink,
    ProjectContextLink,
)

from storm_compendium.compendium.records.api import CompendiumDraft, CompendiumRecord
from storm_compendium.compendium.services.security.permissions import (
    CompendiumRecordPermissionPolicy,
)


def file_record_is_draft(file, ctx):
    """Shortcut for links to determine if record is a record."""
    return file.record.is_draft


class FileServiceCommonConfig(FileServiceConfig):
    permission_policy_cls = CompendiumRecordPermissionPolicy

    file_links_list = {
        "self": ConditionalLink(
            cond=is_record,
            if_=ProjectContextLink(
                "{+api}/projects/{project_id}/compendia/{id}/files{?args*}"
            ),
            else_=ProjectContextLink(
                "{+api}/projects/{project_id}/compendia/{id}/draft/files{?args*}"
            ),
        ),
    }

    file_links_item = {
        "self": ConditionalLink(
            cond=file_record_is_draft,
            if_=ProjectContextFileLink(
                "{+api}/projects/{project_id}/compendia/{id}/draft/files{?args*}"
            ),
            else_=ProjectContextFileLink(
                "{+api}/projects/{project_id}/compendia/{id}/files{?args*}"
            ),
        ),
        "content": ConditionalLink(
            cond=file_record_is_draft,
            if_=ProjectContextFileLink(
                "{+api}/projects/{project_id}/compendia/{id}/draft/files/{key}/content{?args*}"
            ),
            else_=ProjectContextFileLink(
                "{+api}/projects/{project_id}/compendia/{id}/files/{key}/content{?args*}"
            ),
        ),
        "commit": ProjectContextFileLink(
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
