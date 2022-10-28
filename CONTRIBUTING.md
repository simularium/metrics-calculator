# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

## Developer Installation

If something goes wrong at any point during installing the library please see how
[our CI/CD on GitHub Actions](.github/workflows/build-main.yml) installs and builds the
project as it will always be the most up-to-date.

## Get Started!

Ready to contribute? Here's how to set up `simularium_metrics_calculator` for local development.

1. Fork the `metrics-calculator` repo on GitHub.

2. Clone your fork locally:

    ```bash
    git clone git@github.com:{your_name_here}/metrics-calculator.git
    ```

3. Install Just

    ```bash
    brew install just
    ```

4. Install the project in editable mode. (It is also recommended to work in a virtualenv or anaconda environment):

    ```bash
    cd simularium_metrics_calculator/
    just install
    ```

5. Create a branch for local development:

    ```bash
    git checkout -b {your_development_type}/short-description
    ```

    Ex: feature/read-tiff-files or bugfix/handle-file-not-found<br>
    Now you can make your changes locally.

6. When you're done making changes, check that your changes pass linting and
   tests with [just](https://github.com/casey/just):

    ```bash
    just build
    ```

7. Commit your changes and push your branch to GitHub:

    ```bash
    git add .
    git commit -m "Your detailed description of your changes."
    git push origin {your_development_type}/short-description
    ```

8. Submit a pull request through the GitHub website.

## Just Commands

For development commands we use [just](https://github.com/casey/just).

```bash
just
```
```
Available recipes:
    build                    # run lint and then run tests
    clean                    # clean all build, python, and lint files
    default                  # list all available commands
    generate-docs            # generate Sphinx HTML documentation
    install                  # install with all deps
    lint                     # lint, format, and check all files
    release                  # release a new version
    serve-docs               # generate Sphinx HTML documentation and serve to browser
    tag-for-release version  # tag a new version
    test                     # run tests
    update-from-cookiecutter # update this repo using latest cookiecutter-py-package
```

## Adding a calculator

To add a new metric calculator:
1. In `simularium_metrics_calculator/calculators/`, create a `Calculator` for the metric 
that implements `calculate()` and `units()`. See 
[Number of Agents Calculator](simularium_metrics_calculator/calculators/number_of_agents_calculator.py) as an example.
2. Add it to `simularium_metrics_calculator/calculators/__init__.py`.
3. Add it to the [metrics list](simularium_metrics_calculator/metrics_registry.py).

## Deploying

A reminder for the maintainers on how to deploy.
Make sure the main branch is checked out and all desired changes
are merged. Then run:

```bash
just tag-for-release "vX.Y.Z"
just release
```

The presence of a tag starting with "v" will trigger the `publish` step in the
main github workflow, which will build the package and upload it to PyPI. The
version will be injected into the package metadata by
[`setuptools-scm`](https://github.com/pypa/setuptools_scm)
