# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-compendium is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Module that adds support for Compendium management in the Storm Platform."""

import os

from setuptools import find_packages, setup

readme = open("README.rst").read()
history = open("CHANGES.rst").read()

tests_require = [
    "pytest-invenio>=1.4.0",
]

invenio_db_version = ">=1.0.9,<2.0.0"
invenio_search_version = ">=1.4.2,<2.0.0"

extras_require = {
    "docs": [
        "Sphinx>=3,<4",
    ],
    "tests": tests_require,
    # Elasticsearch
    "elasticsearch7": [
        f"invenio-search[elasticsearch7]{invenio_search_version}",
    ],
    # Databases
    "mysql": [
        f"invenio-db[mysql,versioning]{invenio_db_version}",
    ],
    "postgresql": [
        f"invenio-db[postgresql,versioning]{invenio_db_version}",
    ],
    "sqlite": [
        f"invenio-db[versioning]{invenio_db_version}",
    ],
}

setup_requires = []
install_requires = [
    "invenio-drafts-resources>=0.14.0,<0.15.0",
    "invenio-records-resources>=0.17.0,<0.18",
    "storm-project @ git+https://github.com/storm-platform/storm-project",
]

extras_require["all"] = [req for _, reqs in extras_require.items() for req in reqs]


packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join("storm_compendium", "version.py"), "rt") as fp:
    exec(fp.read(), g)
    version = g["__version__"]

setup(
    name="storm-compendium",
    version=version,
    description=__doc__,
    long_description=readme + "\n\n" + history,
    keywords=["Storm Platform", "Research Compendium", "Invenio module"],
    license="MIT",
    author="Felipe Menino Carlos",
    author_email="felipe.carlos@inpe.br",
    url="https://github.com/storm-platform/storm-compendium",
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    entry_points={
        "invenio_config.module": [
            "storm_compendium = storm_compendium.config",
        ],
        "invenio_base.apps": [
            "storm_compendium = storm_compendium:StormCompendium",
        ],
        "invenio_base.api_apps": [
            "storm_compendium = storm_compendium:StormCompendium",
        ],
        "invenio_base.api_blueprints": [
            "storm_compendium_api_ext = storm_compendium.views:blueprint",
            "storm_compendium_api = storm_compendium.views:init_compendium_blueprint_api",
            "storm_compendium_files_api = storm_compendium.views:init_compendium_files_blueprint_api",
            "storm_compendium_files_draft_api = storm_compendium.views:init_compendium_draft_files_blueprint_api",
        ],
        "invenio_db.models": [
            "compendium_record = storm_compendium.compendium.records.models"
        ],
        "invenio_jsonschemas.schemas": [
            "compendium_record = storm_compendium.compendium.records.jsonschemas"
        ],
        "invenio_search.mappings": [
            "compendium_record = storm_compendium.compendium.records.mappings"
        ],
        # 'invenio_access.actions': [],
        # 'invenio_admin.actions': [],
        # 'invenio_assets.bundles': [],
        # 'invenio_base.api_apps': [],
        # 'invenio_base.api_blueprints': [],
        # 'invenio_base.blueprints': [],
        # 'invenio_celery.tasks': [],
        # 'invenio_db.models': [],
        # 'invenio_pidstore.minters': [],
        # 'invenio_records.jsonresolver': [],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 1 - Planning",
    ],
)
