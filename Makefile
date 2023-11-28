.PHONY : docs
docs :
	rm -rf docs/build/
	sphinx-autobuild -b html --watch plotstyle/ docs/source/ docs/build/

.PHONY : run-checks
run-checks :
	isort --check .
	black --check .
	ruff check .
	mypy .
	CUDA_VISIBLE_DEVICES='' pytest -v --color=yes --doctest-modules tests/ plotstyle/

.PHONY : format
format :
	isort .
	black .
	ruff format .

.PHONY : build
build :
	rm -rf *.egg-info/
	python -m build

.PHONY : dev
dev :
	pip install -e ".[dev,extra]"