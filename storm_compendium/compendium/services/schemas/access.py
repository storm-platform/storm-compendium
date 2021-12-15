# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from marshmallow import Schema, fields


class AgentSchema(Schema):
    """Agent schema."""

    user = fields.Integer(required=False)

    project = fields.String(required=False)


class CompendiumAccessSchema(Schema):
    """Access Schema."""

    owned_by = fields.List(fields.Nested(AgentSchema), required=False)

    contributed_by = fields.List(fields.Nested(AgentSchema), required=False)
