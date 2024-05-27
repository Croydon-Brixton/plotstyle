.PHONY : docs
docs :
	rm -rf docs/build/
	sphinx-autobuild -b html --watch plotstyle/ docs/source/ docs/build/

.PHONY : run-checks
run-checks :
	ruff check .
	mypy .
	CUDA_VISIBLE_DEVICES='' pytest -v --color=yes --doctest-modules tests/ plotstyle/

.PHONY : format
format :
	ruff format .
	ruff check --fix .

.PHONY : build
build :
	rm -rf *.egg-info/
	python -m build

.PHONY : dev
dev :
	pip install -e ".[dev,extra]"