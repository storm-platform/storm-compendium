# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.


from marshmallow import fields


from invenio_drafts_resources.services.records.schema import RecordSchema, ParentSchema

from .access import CompendiumAccessSchema
from .metadata import CompendiumMetadataSchema


class CompendiumParentSchema(ParentSchema):
    """Compendium (Parent) schema."""


class CompendiumRecordSchema(RecordSchema):
    """Compendium schema."""

    access = fields.Nested(CompendiumAccessSchema, required=False, dump_only=True)

    metadata = fields.Nested(CompendiumMetadataSchema, required=True)
