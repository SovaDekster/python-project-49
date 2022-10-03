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

reinstallation:
	pip install --user --force-reinstall dist/*.whl

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

lint:
	poetry run flake8 brain_games
