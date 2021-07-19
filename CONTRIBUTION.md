# Contribution Overview

The ongoing contribution from engineers around Shell is vital to assuring the continued maturation of our teams and organization. That means it's also important to be clear on how to contribute and making it as simple as possible, while properly maintainability an expected level of quality. This page gives general guidance on contributions and gives specifics on how to contribute to this repository.

# General Contribution Model

The contribution model with Shell inner source is via branching and pull requests. **Forking of a codebase is not permitted**, as it duplicates Shell code into personal accounts, outside of Shell's GitHub organizations. This means the general process is:

1. Create a branch from the master branch (or development branch, if it exists)
2. Make your changes -> *update code, tests, and documentation*
3. Make your changes and verify the integrity of them with build/test/integrate checks
4. Create a Pull Request from your branch into the origin branch -> *should be reviewed by at least one person*

# Contribution for shell-inner-source repository

## Contribution process

1. Create a branch from the master branch.
2. Make your changes, updating code, tests, and documentation as necessary.
3. Verify the changes with the integrated GitHub Actions workflow (occurs automatically upon commit). Flake8 and PyTest must pass with no warnings or errors.
4. Create a Pull Request from your branch into the master branch. This will need to be reviewed by a repository administrator for inclusion.

## Moderation/quality management

There are two layers of quality management to consider-
1. When any change is submitted, the automated build process should run. This will do a basic check on any submitted code.
2. When a Pull Request is created to bring into the *master* branch, it must be reviewed by an admin, which will look at any code changes, but also review any updated documentation.

If a Pull Request needs further changes before it can be accepted, it can be amended without canceling/re-submitting.
