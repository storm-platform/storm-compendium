# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from marshmallow import Schema, fields, validate

from marshmallow_utils.fields import SanitizedUnicode
from storm_commons.schemas.validators import marshmallow_not_blank_field


class FileDefinitionSchema(Schema):
    """File definition schema."""

    key = SanitizedUnicode(required=True, validate=marshmallow_not_blank_field())


class ExecutionDescriptorSchema(Schema):
    """Execution descriptor schema."""

    uri = fields.Url(required=True, validate=marshmallow_not_blank_field())
    name = SanitizedUnicode(required=True, validate=marshmallow_not_blank_field(max=16))
    version = SanitizedUnicode(
        required=True, validate=marshmallow_not_blank_field(max=16)
    )


class ExecutionEnvironmentSchema(Schema):
    """Execution environment schema."""

    meta = fields.Dict(required=True)
    descriptor = fields.Nested(ExecutionDescriptorSchema, required=True)


class ExecutionDataSchema(Schema):
    """Execution Data metadata schema."""

    inputs = fields.List(fields.Nested(FileDefinitionSchema), required=True)
    outputs = fields.List(fields.Nested(FileDefinitionSchema), required=True)


class ExecutionMetadataSchema(Schema):
    """Execution metadata schema."""

    data = fields.Nested(ExecutionDataSchema, required=True)
    environment = fields.Nested(ExecutionEnvironmentSchema, required=True)


class CompendiumMetadataSchema(Schema):
    """Compendium metadata schema."""

    title = SanitizedUnicode(
        required=True, validate=marshmallow_not_blank_field(max=64)
    )
    description = SanitizedUnicode(
        required=True, validate=marshmallow_not_blank_field(max=2000)
    )

    execution = fields.Nested(ExecutionMetadataSchema, required=True)
