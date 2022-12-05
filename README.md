# Geographic Services APIs

## Installation

<br/>

   * Create a new environment to install the requirements. Here is a example using [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/):

        > mkvirtualenv -p python3 geo_services

<br/>

   * Install the requirements using the `Makefile` command:

        > make requirements

<br/>

   * To start the project dependencies, run:

        > make start-deps

<br/>

   * Use the command below to run the application. The app will start in `http://0.0.0.0:8000` by default:

        > make run

<br/>

   * You can use the Openapi to test the application: `http://0.0.0.0:8000/docs/`

<br/>

## Tests

<br/>

   * To run the unit tests use the command:

        > make test

<br/>

   * To run a specific test or group of test use:

        > make test-matching Q=test_name

<br/>

   * To check the coverage use the command:

        > make coverage

<br/>

## Quality

<br/>

   * Checking python development pattern:

        > make lint

<br/>

   * Fix import's order:

        > make isort-fix

<br/>

   * Checking security issues:

        > make check-vulnerabilities

<br/>

## Publish

<br/>

   * To generate the next release tag, run one of these commands:

      > make release-patch

      > make release-minor

      > make release-major

<br/>

## Documentation

   * The APIs documentation is described here: `http://0.0.0.0:8000/docs/`

<br/>
