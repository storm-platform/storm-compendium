# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from invenio_db import db

from invenio_drafts_resources.records import (
    DraftMetadataBase,
    ParentRecordMixin,
    ParentRecordStateMixin,
)

from invenio_files_rest.models import Bucket
from invenio_records.models import RecordMetadataBase
from invenio_records_resources.records import FileRecordModelMixin

from sqlalchemy_utils.types import UUIDType


class CompendiumParentMetadata(db.Model, RecordMetadataBase):
    """Metadata store for the parent record."""

    __tablename__ = "compendium_parents_metadata"

    project_id = db.Column(
        db.ForeignKey(
            "project_research_projects.id",
            onupdate="CASCADE",
            ondelete="CASCADE",
        )
    )

    project = db.relationship("ResearchProjectMetadata", lazy="joined")


class CompendiumRecordMetadata(db.Model, RecordMetadataBase, ParentRecordMixin):
    """Represent a bibliographic record metadata."""

    __tablename__ = "compendium_records_metadata"
    __parent_record_model__ = CompendiumParentMetadata

    # Enable versioning
    __versioned__ = {}

    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)


class CompendiumFileRecordMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """File associated with a record."""

    __tablename__ = "compendium_records_files"
    __record_model_cls__ = CompendiumRecordMetadata


class CompendiumDraftMetadata(db.Model, DraftMetadataBase, ParentRecordMixin):
    """Draft metadata for a record."""

    __tablename__ = "compendium_drafts_metadata"
    __parent_record_model__ = CompendiumParentMetadata

    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)


class CompendiumFileDraftMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """File associated with a draft."""

    __tablename__ = "compendium_drafts_files"
    __record_model_cls__ = CompendiumDraftMetadata


class CompendiumVersionsState(db.Model, ParentRecordStateMixin):
    """Store for the version state of the parent record."""

    __tablename__ = "compendium_versions_state"

    __parent_record_model__ = CompendiumParentMetadata
    __record_model__ = CompendiumRecordMetadata
    __draft_model__ = CompendiumDraftMetadata


__all__ = (
    "CompendiumParentMetadata",
    "CompendiumRecordMetadata",
    "CompendiumFileRecordMetadata",
    "CompendiumDraftMetadata",
    "CompendiumFileDraftMetadata",
    "CompendiumVersionsState",
)
