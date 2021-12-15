# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from storm_commons.services.components import (
    RecordMetadataComponent,
    VersionedRecordAccessDefinitionComponent,
)


class CompendiumMetadataComponent(RecordMetadataComponent):
    """Service component for metadata definition."""

    new_version_skip_fields = ["publication_date", "version"]


class CompendiumParentAccessDefinitionComponent(
    VersionedRecordAccessDefinitionComponent
):
    """Access component to Research Compendium parent."""

    def _create(self, identity, data=None, record=None, **kwargs):
        """Extra ``create`` method operation."""
        parent = record.parent

        # special case: parent is associated with a project
        # in the future, the project reference will be based as
        # parameter in the method invocation.
        from storm_project import current_project

        parent.access.owners.append({"project": current_project.id})


__all__ = (
    "CompendiumMetadataComponent",
    "CompendiumParentAccessDefinitionComponent",
)
