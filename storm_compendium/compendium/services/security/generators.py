# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.


from storm_project.project.services.security.generators import ProjectRecordAgent


class ProjectCompendiumCollaborator(ProjectRecordAgent):
    """Generator to define a user collaborator based on the record parent (versioned)
    informations."""

    def _select_record_agent(self, record, **kwargs):
        # checking if the user is a ``contributor`` or ``owner`` of the requested record.
        # note: Is assumed that the `parent` attribute use the ``RecordAccessField``.
        parent_owners = record.parent.access.owners
        parent_contributors = record.parent.access.contributors

        return parent_owners, parent_contributors
