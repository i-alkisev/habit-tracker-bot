def task_run_db():
    """Run production database."""
    return {
        'actions': [
            'docker-compose -f db/docker-compose.yml up -d'
        ],
    }


def task_run_test_db():
    """Run test database."""
    return {
        'actions': ['docker-compose -f db/test-docker-compose.yml up -d'],
    }


def task_localization():
    """Generage localization."""
    return {
        'actions': [
            'pybabel compile -D all -l en_US.UTF-8 -d po \
            -i po/en_US.UTF-8/LC_MESSAGES/all.po',
        ]
    }


def task_style():
    """Check codestyle."""
    return {
        'actions': [
            'pre-commit install',
            'pre-commit run --all-files',
        ],
        'verbosity': 2,
    }


def task_html():
    """Generate documentation."""
    return {
        'actions': [
            'cd docs && make html',
        ],
    }


def task_test():
    """Do test."""
    return {
        'actions': [
            'python run_tests.py',
            'docker-compose -f db/test-docker-compose.yml down'
        ],
        'task_dep': [
            'style',
            'localization',
            'html',
            'run_test_db',
        ],
        'verbosity': 2,
    }


def task_run_bot():
    """Run bot."""
    return {
        'actions': [
            'python main.py',
        ],
        'task_dep': [
            'localization',
            'run_db',
        ],
        'verbosity': 2,
    }


def task_erase():
    """Clean all generates."""
    return {
        'actions': [
            'git clean -fdx',
        ],
    }
