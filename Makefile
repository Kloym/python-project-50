install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

run:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

report:
	./gradlew jacocoTestReport
