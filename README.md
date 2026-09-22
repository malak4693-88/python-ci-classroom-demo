# GitHub Actions Python CI Classroom Demo

[![Python CI](https://github.com/mattival/python-ci-classroom-demo/actions/workflows/tests.yml/badge.svg)](https://github.com/mattival/python-ci-classroom-demo/actions/workflows/tests.yml)

This project demonstrates a small Python continuous-integration pipeline. GitHub Actions installs the test dependencies and runs pytest after every push and pull request.

## Project Structure

```text
github-actions-demo/
|-- .github/
|   `-- workflows/
|       `-- tests.yml
|-- tests/
|   `-- test_price_calculator.py
|-- .gitignore
|-- price_calculator.py
|-- pytest.ini
`-- requirements.txt
```

## Run Locally

Create and activate a virtual environment if desired, then install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

Run the same test command used by CI:

```powershell
python -m pytest --cov=price_calculator --cov-report=term-missing
```

## What the Workflow Does

The workflow in `.github/workflows/tests.yml`:

1. Runs after a push, a pull request, or a manual start.
2. Uses a clean Ubuntu runner.
3. checks out the repository.
4. Installs Python 3.13.
5. Restores the pip download cache when possible.
6. Installs pytest and pytest-cov.
7. Runs the test suite and prints a coverage report.

The workflow token receives read-only access to repository contents. The job also has a ten-minute timeout and cancels an older run when a newer commit arrives on the same branch.

## Suggested Classroom Walkthrough

### 1. Establish the Local Baseline

Run the tests locally and inspect the passing test names and coverage output.

```powershell
python -m pytest -v --cov=price_calculator --cov-report=term-missing
```

### 2. Inspect the Workflow

Open `.github/workflows/tests.yml` and identify:

- The trigger events
- The runner operating system
- The Python version
- The dependency installation command
- The test command

### 3. Trigger a Successful Run

Push the project to a GitHub repository. Open the **Actions** tab and follow the log for the `test` job.

### 4. Demonstrate a Regression

Temporarily change the final line of `calculate_total` to add 1 to the result. Commit and push the change.

The pipeline should fail in the test step. Open the failed test output and compare the expected and actual values.

Restore the correct implementation, commit, and push again. The next run should pass.

### 5. Show a Pull-Request Check

Create a branch, make a harmless change, and open a pull request. The same workflow appears as a check on the pull request.

## Discussion Points

- Why does CI install dependencies from an empty environment?
- Why should the local and CI test commands match?
- Which test protects the discount boundary?
- What would happen if a required package were missing from `requirements.txt`?
- Which checks should block a pull request?
- When would testing several Python versions be useful?

## Extension: Test Multiple Python Versions

Replace the fixed Python version with a job matrix:

```yaml
strategy:
  matrix:
    python-version: ["3.12", "3.13"]

steps:
  - uses: actions/checkout@v7
  - uses: actions/setup-python@v7
    with:
      python-version: ${{ matrix.python-version }}
      cache: pip
```

Each matrix entry creates a separate job and consumes runner time.

## Notes for Production Projects

Major version tags keep this classroom example readable. Higher-security projects can pin actions to reviewed full commit SHAs so the referenced action code cannot change unexpectedly.

Add only the checks the project needs. A short, stable pipeline gives better feedback than a large pipeline that developers learn to ignore.

## References

- [Understanding GitHub Actions](https://docs.github.com/en/actions/get-started/understand-github-actions)
- [Building and testing Python](https://docs.github.com/en/actions/tutorials/build-and-test-code/python)
- [Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
- [Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use)
- [pytest documentation](https://docs.pytest.org/en/stable/)
