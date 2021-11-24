# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from invenio_drafts_resources.services.records.components import (
    DraftFilesComponent,
    PIDComponent,
)

from invenio_drafts_resources.services.records.config import (
    RecordServiceConfig,
    SearchDraftsOptions,
    SearchOptions,
)

from invenio_records_resources.services import ConditionalLink
from invenio_drafts_resources.services.records.config import is_draft, is_record


from ..permissions import CompendiumRecordPermissionPolicy
from ..components import (
    CompendiumRecordParentServiceComponent,
    CompendiumAccessComponent,
    MetadataComponent,
)
from ..links import CompendiumRecordLink, compendium_pagination_links

from ...records.api import CompendiumDraft, CompendiumRecord
from ..schemas import CompendiumParentSchema, CompendiumRecordSchema


class CompendiumServiceConfig(RecordServiceConfig):
    record_cls = CompendiumRecord
    draft_cls = CompendiumDraft

    # API Response schemas
    schema = CompendiumRecordSchema
    schema_parent = CompendiumParentSchema

    # Security policy
    permission_policy_cls = CompendiumRecordPermissionPolicy

    # Search options
    search = SearchOptions
    search_versions = SearchDraftsOptions

    # Components
    components = [
        MetadataComponent,
        CompendiumAccessComponent,
        DraftFilesComponent,
        PIDComponent,
        CompendiumRecordParentServiceComponent,
    ]

    links_item = {
        "self": ConditionalLink(
            cond=is_record,
            if_=CompendiumRecordLink(
                "{+api}/projects/{project_id}/compendia/{id}{?args*}"
            ),
            else_=CompendiumRecordLink(
                "{+api}/projects/{project_id}/compendia/{id}/draft{?args*}"
            ),
        ),
        "latest": CompendiumRecordLink(
            "{+api}/projects/{project_id}/compendia/{id}/versions/latest{?args*}"
        ),
        "draft": CompendiumRecordLink(
            "{+api}/projects/{project_id}/compendia/{id}/draft{?args*}", when=is_record
        ),
        "compendium": CompendiumRecordLink(
            "{+api}/projects/{project_id}/compendia/{id}{?args*}", when=is_draft
        ),
        "publish": CompendiumRecordLink(
            "{+api}/projects/{project_id}/compendia/{id}/draft/actions/publish{?args*}",
            when=is_draft,
        ),
        "files": ConditionalLink(
            cond=is_record,
            if_=CompendiumRecordLink(
                "{+api}/projects/{project_id}/compendia/{id}/files{?args*}"
            ),
            else_=CompendiumRecordLink(
                "{+api}/projects/{project_id}/compendia/{id}/draft/files{?args*}"
            ),
        ),
        "versions": CompendiumRecordLink(
            "{+api}/projects/{project_id}/compendia/{id}/versions{?args*}"
        ),
    }

    links_search = compendium_pagination_links("{+api}/pipeline/{id}/compendia{?args*}")

    links_search_drafts = compendium_pagination_links(
        "{+api}/user/projects/{project_id}/compendia{?args*}"
    )

    links_search_versions = compendium_pagination_links(
        "{+api}/projects/{project_id}/compendia/{id}/versions{?args*}"
    )


__all__ = "CompendiumServiceConfig"
