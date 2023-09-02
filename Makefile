install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

build:
	poetry build

lint:
	poetry run flake8 brain_games

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl
