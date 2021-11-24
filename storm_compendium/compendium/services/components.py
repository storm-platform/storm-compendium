# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from copy import copy


from storm_project import current_project

from invenio_records.dictutils import dict_set
from invenio_access.permissions import system_process

from invenio_records_resources.services.files import FileServiceComponent
from invenio_records_resources.services.records.components import ServiceComponent

from invenio_drafts_resources.services.records.components import (
    ServiceComponent as DraftServiceComponent,
)


class CompendiumRecordParentServiceComponent(DraftServiceComponent):
    """Component for CompendiumParent project control."""

    def _define_project_id(self, record):
        """Define Project ID in the Record Parent."""
        record.parent.project_id = current_project._record.id

    def create(self, identity, data=None, record=None, errors=None):
        self._define_project_id(record)


class CompendiumDraftFileDefinitionValidatorComponent(FileServiceComponent):
    """Component to control the Compendium Record attributes definitions."""

    def init_files(self, id_, identity, record, data):
        """Init files handler."""
        files = [f["key"] for f in [*record.inputs, *record.outputs]]

        for file_key in data:
            if file_key["key"] not in files:
                raise RuntimeError("File is not defined for this Compendium.")


class CompendiumAccessComponent(ServiceComponent):
    """Access component to Research Project.

    See:
        This code is adapted from: https://github.com/inveniosoftware/invenio-communities/blob/837f33f1c0013a69fcec0ef188200a99fafddc47/invenio_communities/communities/services/components.py#L126

    Todo:
        * This class is also defined in storm-projects. This should be generalized into a common
        Storm platform generators package.
    """

    def _populate_access_and_validate(self, identity, data, record, **kwargs):
        if record is not None and "access" in data:
            record.setdefault("access", {})
            record["access"].update(data.get("access", {}))

    def _init_owners(self, identity, record, **kwargs):
        """Create a owner field into the record metadata."""
        is_system_process = system_process in identity.provides

        owners = []
        if not is_system_process:
            owners = [{"user": identity.id}]

        dict_set(record, "access.owned_by", owners)

    def _init_contributors(self, identity, record, **kwargs):
        """Create a contributor field into the record metadata."""
        is_system_process = system_process in identity.provides

        contributors = []
        if not is_system_process:
            contributors = [{"user": identity.id}]

        dict_set(record, "access.contributed_by", contributors)

    def create(self, identity, data=None, record=None, **kwargs):
        """Add basic ownership fields to the record."""
        self._populate_access_and_validate(identity, data, record, **kwargs)
        self._init_owners(identity, record, **kwargs)
        self._init_contributors(identity, record, **kwargs)

    def update(self, identity, data=None, record=None, **kwargs):
        """Update handler."""
        self._populate_access_and_validate(identity, data, record, **kwargs)

    def update_draft(self, identity, data=None, record=None, **kwargs):
        """Update handler."""
        self._populate_access_and_validate(identity, data, record, **kwargs)

    def publish(self, identity, draft=None, record=None, **kwargs):
        """Update draft metadata."""
        self._populate_access_and_validate(identity, draft, record, **kwargs)

    def edit(self, identity, draft=None, record=None, **kwargs):
        """Update draft metadata."""
        self._populate_access_and_validate(identity, record, draft, **kwargs)

    def new_version(self, identity, draft=None, record=None, **kwargs):
        """Update draft metadata."""
        self._populate_access_and_validate(identity, record, draft, **kwargs)


class MetadataComponent(ServiceComponent):
    """Service component for metadata.

    Note:
        (class-vendoring) Imported class from Invenio RDM Records to reduce dependencies in the system.
        (https://github.com/inveniosoftware/invenio-rdm-records/blob/d7e7c7a2a44986de88e2d7941722bc72fd7dc345/invenio_rdm_records/services/components/metadata.py#L18)
    """

    new_version_skip_fields = ["publication_date", "version"]

    def create(self, identity, data=None, record=None, **kwargs):
        """Inject parsed metadata to the record."""
        record.metadata = data.get("metadata", {})

    def update_draft(self, identity, data=None, record=None, **kwargs):
        """Inject parsed metadata to the record."""
        record.metadata = data.get("metadata", {})

    def publish(self, identity, draft=None, record=None, **kwargs):
        """Update draft metadata."""
        record.metadata = draft.get("metadata", {})

    def edit(self, identity, draft=None, record=None, **kwargs):
        """Update draft metadata."""
        draft.metadata = record.get("metadata", {})

    def new_version(self, identity, draft=None, record=None, **kwargs):
        """Update draft metadata."""
        draft.metadata = copy(record.get("metadata", {}))
        # Remove fields that should not be copied to the new version
        # (publication date and version)
        for f in self.new_version_skip_fields:
            draft.metadata.pop(f, None)


__all__ = (
    "MetadataComponent",
    "CompendiumAccessComponent",
    "CompendiumRecordParentServiceComponent",
    "CompendiumDraftFileDefinitionValidatorComponent",
)
