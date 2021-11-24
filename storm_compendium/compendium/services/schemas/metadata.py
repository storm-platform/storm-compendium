# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from marshmallow import Schema, fields, validate

from marshmallow_utils.fields import SanitizedUnicode


def _not_blank(**kwargs):
    """Returns a non-blank validation rule.

    See:
        This code was extracted from: https://github.com/inveniosoftware/invenio-communities/blob/1a80d7312719507c4ebe504f00c1a2894f2161d8/invenio_communities/communities/schema.py#L21
    """
    max_ = kwargs.get("max", "")
    return validate.Length(
        error=f"Not empty string and less than {max_} characters allowed.",
        min=1,
        **kwargs,
    )


class FileDefinitionSchema(Schema):
    """File definition schema."""

    key = SanitizedUnicode(required=True, validate=_not_blank())


class ExecutionDescriptorSchema(Schema):
    """Execution descriptor schema."""

    uri = fields.Url(required=True, validate=_not_blank())
    name = SanitizedUnicode(required=True, validate=_not_blank(max=16))
    version = SanitizedUnicode(required=True, validate=_not_blank(max=16))


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

    title = SanitizedUnicode(required=True, validate=_not_blank(max=64))
    description = SanitizedUnicode(required=True, validate=_not_blank(max=2000))

    execution = fields.Nested(ExecutionMetadataSchema, required=True)
