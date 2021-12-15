# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from invenio_pidstore.models import PIDStatus
from invenio_records.dumpers import ElasticsearchDumper

from invenio_drafts_resources.records import Draft, Record
from invenio_records_resources.records.api import FileRecord

from invenio_records.systemfields import ModelField, DictField, ConstantField
from invenio_drafts_resources.records.api import ParentRecord as ParentRecordBase

from invenio_records_resources.records.systemfields import (
    PIDStatusCheckField,
    FilesField,
    IndexField,
)

import storm_compendium.compendium.records.models as models
from storm_commons.records.systemfields.fields.access import RecordAccessField

from storm_compendium.compendium.records.systemfields.access import CompendiumAccess
from storm_compendium.compendium.records.systemfields.has_draftcheck import (
    HasDraftCheckField,
)


class CompendiumParent(ParentRecordBase):
    """Node Parent record."""

    model_cls = models.CompendiumParentMetadata

    access = RecordAccessField(access_obj_class=CompendiumAccess)

    dumper = ElasticsearchDumper()
    schema = ConstantField("$schema", "local://records/compendiumparent-v1.0.0.json")


class CommonFieldsMixin:
    """Common system fields between compendium records and drafts."""

    parent_record_cls = CompendiumParent
    versions_model_cls = models.CompendiumVersionsState

    bucket_id = ModelField(dump=False)
    bucket = ModelField(dump=False)

    #
    # Compendium data reference (input and output)
    #
    inputs = DictField("metadata.execution.data.inputs")
    outputs = DictField("metadata.execution.data.outputs")

    #
    # Compendium execution metadata
    #
    execution = DictField("metadata.execution")

    #
    # Compendium general metadata
    #
    metadata = DictField("metadata")

    pids = DictField("pids")
    is_published = PIDStatusCheckField(status=PIDStatus.REGISTERED, dump=True)

    dumper = ElasticsearchDumper()
    schema = ConstantField("$schema", "local://records/compendiumrecord-v1.0.0.json")


class CompendiumFileDraft(FileRecord):
    model_cls = models.CompendiumFileDraftMetadata
    record_cls = None


class CompendiumDraft(CommonFieldsMixin, Draft):
    model_cls = models.CompendiumDraftMetadata

    index = IndexField(
        "compendium_record-drafts-compendiumdraft-v1.0.0",
        search_alias="compendium_record",
    )

    files = FilesField(store=False, file_cls=CompendiumFileDraft, delete=False)

    has_draft = HasDraftCheckField()


class CompendiumFileRecord(FileRecord):
    model_cls = models.CompendiumFileRecordMetadata
    record_cls = None


class CompendiumRecord(CommonFieldsMixin, Record):
    model_cls = models.CompendiumRecordMetadata

    index = IndexField(
        "compendium_record-records-compendiumrecord-v1.0.0",
        search_alias="compendium_record-records",
    )

    files = FilesField(
        store=False, file_cls=CompendiumFileRecord, create=False, delete=False
    )

    has_draft = HasDraftCheckField(CompendiumDraft)


CompendiumFileDraft.record_cls = CompendiumDraft
CompendiumFileRecord.record_cls = CompendiumRecord

__all__ = (
    "CompendiumParent",
    "CompendiumDraft",
    "CompendiumFileDraft",
    "CompendiumRecord",
    "CompendiumFileRecord",
)
