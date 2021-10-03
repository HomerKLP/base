from invoke import task


@task
def lint(c):
    c.run(
        "black . --check && "
        "flake8 . && "
        "mypy . && "
        "bandit -r . --exclude tests && "
        "safety check",
        pty=True,
    )


@task
def test(c, t=None):
    if t:
        c.run(
            f"pytest -vsk {t} --no-migrations --reuse-db",
            pty=True,
        )
        return None
    c.run(
        "pytest -v --cov . --cov-report term-missing "
        "--cov-fail-under=100 --flake8 --mypy -n 4 --no-migrations "
        "--reuse-db",
        pty=True,
    )


@task
def black(c):
    c.run("black .", pty=True)


@task
def flake(c):
    c.run("flake8 .", pty=True)


@task
def mypy(c):
    c.run("mypy .", pty=True)


@task
def outdated(c):
    c.run("pip list --outdated --format=columns", pty=True)


@task
def bandit(c):
    c.run("bandit -r . --exclude tests", pty=True)


@task
def safety(c):
    c.run("safety check", pty=True)
