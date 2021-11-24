# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.


from invenio_drafts_resources.resources import RecordResourceConfig


class CompendiumResourceConfig(RecordResourceConfig):
    blueprint_name = "storm_compendium_records"
    url_prefix = "/projects/<project_id>/compendia"


__all__ = "CompendiumResourceConfig"
