# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from invenio_records_permissions.generators import (
    Disable,
    SystemProcess,
    AuthenticatedUser,
)

from storm_project.project.services.security.permissions import (
    ResearchProjectOwner,
    ResearchProjectContributor,
)

from storm_project.project.services.security.generators.context import (
    UserInProject,
    VersionedProjectRecordColaborator,
)

from invenio_records_permissions.policies.records import RecordPermissionPolicy


class CompendiumRecordPermissionPolicy(RecordPermissionPolicy):
    """Access control configuration for Node Records.

    See:
        This policy is based on `RDMRecordPermissionPolicy` descriptions (https://github.com/inveniosoftware/invenio-rdm-records/blob/6a2574556392223331048f60d6fe9d190269477c/invenio_rdm_records/services/permissions.py).
    """

    #
    # High-level permissions
    #

    # Content creators and managers
    can_manage = [VersionedProjectRecordColaborator(), SystemProcess()]

    # General users
    can_use = can_manage + [UserInProject()]

    #
    # Records
    #

    # Allow record search
    can_search = can_use

    # Allow reading record metadata
    can_read = can_use

    # Allow submitting new record
    can_create = can_use

    # Allow reading the record files
    can_read_files = can_use

    #
    # Drafts
    #

    # Allow search drafts
    can_search_drafts = can_use

    # Allow reading draft metadata
    can_read_draft = can_use

    # Allow reading draft files
    can_draft_read_files = can_use

    # Allow updating draft metadata
    can_update_draft = can_manage

    # Allow uploading, updating and deleting drafts files
    can_draft_create_files = can_manage
    can_draft_update_files = can_manage
    can_draft_delete_files = can_manage

    #
    # Actions
    #

    # Allow editing published record (via draft)
    can_edit = can_manage

    # Allow deleting/discarding a draft (and associated files)
    can_delete_draft = can_manage

    # Allow creating a new version of an existing published record.
    can_new_version = can_manage

    # Allow publishing a new record or changes to an existing record.
    can_publish = can_manage

    #
    # Disabled actions (these should not be used or changed)
    #
    # - Records/files are updated/deleted via drafts so we don't support
    #   using below actions.
    can_update = [Disable()]
    can_delete = [Disable()]
    can_create_files = [Disable()]
    can_update_files = [Disable()]
    can_delete_files = [Disable()]


__all__ = "CompendiumRecordPermissionPolicy"
