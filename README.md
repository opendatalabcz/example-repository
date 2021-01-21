# Example GitHub workflow for Python static code analysis

Static checks are made using [GitHub actions](https://docs.github.com/en/actions/quickstart). Our workflow is located at `.github/workflows/checks.yml`.

Each workflow starts after a [specific event](https://docs.github.com/en/actions/reference/events-that-trigger-workflows). You can easily change that if you want.

```
...
# Triggers the workflow on push or pull request events
on: [push, pull_request]
...
```

Checks runs in a [test environment](https://docs.github.com/en/actions/guides/building-and-testing-python). Our workflow runs only on Ubuntu with Python 3.6 but you can change it if you want.

```
...
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.6]
...
```

## Static checks

- Lint - [flake8](https://flake8.pycqa.org/en/latest/index.html)
    - basic [Flake configuration](https://flake8.pycqa.org/en/latest/user/configuration.html) is in `.flake8` file
    - workflow uses [Flake8 with annotations](https://github.com/marketplace/actions/flake8-with-annotations) action 
- Security check - [Bandit](https://bandit.readthedocs.io/en/latest/)
    - workflow uses [py3-bandit](https://github.com/marketplace/actions/py3-bandit) action
    - configuration only works using env variables (there is a [bug](https://github.com/PyCQA/bandit/issues/657) that breaks config file support)