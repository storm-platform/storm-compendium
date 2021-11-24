
install_package:

	pip install -e .

delete_invenio_db:

	invenio db destroy

init_invenio_db:

	invenio db init

create_invenio_db:

	invenio db create

recreate_invenio_db: delete_invenio_db init_invenio_db create_invenio_db

delete_invenio_index:

	invenio index destroy

create_invenio_index:

	invenio index init

create_invenio_files_location:

	invenio files location create test ./data --default

recreate_invenio_index: delete_invenio_index create_invenio_index

recreate_all: install_package recreate_invenio_db recreate_invenio_index create_invenio_files_location

