install: # for first gitclone
	poetry install

brain-games: #  for fast start
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

lint:
	poetry run flake8 brain_games
