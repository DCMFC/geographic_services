clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "*.DS_Store" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@find . -name "*.cache" -type d | xargs rm -rf
	@find . -name "*htmlcov" -type d | xargs rm -rf
	@rm -rf build
	@rm -rf dist


# Development

requirements:
	@pip install -U pip
	@pip install -r requirements.txt

lint:
	@flake8 service_area
	@isort --check service_area

isort-fix:
	@isort service_area

check-vulnerabilities:
	@safety check -r requirements.txt

start-deps: clean
	@sudo docker-compose up -d

run:
	@python manage.py runserver

test: clean
	@pytest -m "not integration"
	@make clean

test-all: clean
	@pytest -x
	@make clean

test-matching: clean
	@pytest --pdb -k$(Q)
	@make clean

coverage: clean
	@py.test service_area -m 'not integration' --cov service_area --cov-report xml --cov-report term --cov-report html

coverage-all: clean
	@py.test service_area --cov service_area --cov-report xml --cov-report term --cov-report html


# Publish

release-patch:
	@bump2version patch

release-minor:
	@bump2version minor

release-major:
	@bump2version major
