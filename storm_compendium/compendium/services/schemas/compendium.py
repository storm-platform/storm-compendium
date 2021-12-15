# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from marshmallow import fields

from storm_compendium.compendium.services.schemas.access import CompendiumAccessSchema
from storm_compendium.compendium.services.schemas.metadata import (
    CompendiumMetadataSchema,
)

from invenio_drafts_resources.services.records.schema import RecordSchema, ParentSchema


class CompendiumParentSchema(ParentSchema):
    """Compendium (Parent) schema."""

    access = fields.Nested(CompendiumAccessSchema, required=False, dump_only=True)


class CompendiumRecordSchema(RecordSchema):
    """Compendium schema."""

    metadata = fields.Nested(CompendiumMetadataSchema, required=True)
