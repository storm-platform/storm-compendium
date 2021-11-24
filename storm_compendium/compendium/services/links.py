# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from copy import deepcopy

from flask import request
from invenio_records_resources.services import Link, FileLink
from invenio_records_resources.services.base.links import preprocess_vars

from storm_projects import current_project


class CompendiumRecordLink(Link):
    """Short cut for writing Node Record links."""

    @staticmethod
    def vars(record, vars):
        """Variables for the URI template."""
        vars.update(
            {
                "id": record.pid.pid_value,
                "project_id": current_project.id,
                "args": {
                    "access_token": request.args.get(
                        "access_token",
                    )
                },
            }
        )


class PaginationCompendiumRecordLink(Link):
    """Short cut for writing Node Record links."""

    def expand(self, obj, context):
        """Expand the URI Template."""
        context = {"project_id": current_project.id, **context}

        vars = {}
        vars.update(deepcopy(context))
        self.vars(obj, vars)
        if self._vars_func:
            self._vars_func(obj, vars)
        vars = preprocess_vars(vars)
        return self._uritemplate.expand(**vars)


class CompendiumFileLink(FileLink):
    """Short cut for writing record links."""

    @staticmethod
    def vars(file_record, vars):
        """Variables for the URI template."""
        vars.update(
            {
                "key": file_record.key,
                "project_id": current_project.id,
                "args": {
                    "access_token": request.args.get(
                        "access_token",
                    )
                },
            }
        )


def compendium_pagination_links(tpl):
    """Create pagination links (prev/self/next) from the same template."""
    return {
        "prev": PaginationCompendiumRecordLink(
            tpl,
            when=lambda pagination, ctx: pagination.has_prev,
            vars=lambda pagination, vars: vars["args"].update(
                {"page": pagination.prev_page.page}
            ),
        ),
        "self": PaginationCompendiumRecordLink(tpl),
        "next": PaginationCompendiumRecordLink(
            tpl,
            when=lambda pagination, ctx: pagination.has_next,
            vars=lambda pagination, vars: vars["args"].update(
                {"page": pagination.next_page.page}
            ),
        ),
    }


__all__ = ("CompendiumFileLink", "CompendiumRecordLink", "compendium_pagination_links")
