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
	@flake8 geographic_services
	@isort --check geographic_services

isort-fix:
	@isort geographic_services

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
	@py.test geographic_services -m 'not integration' --cov geographic_services --cov-report xml --cov-report term --cov-report html

coverage-all: clean
	@py.test geographic_services --cov geographic_services --cov-report xml --cov-report term --cov-report html


# Publish

release-patch:
	@bump2version patch

release-minor:
	@bump2version minor

release-major:
	@bump2version major
