install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pipx install --force dist/*.whl

run:
	poetry run gendiff gendiff/scripts/file1.json gendiff/scripts/file2.json

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest