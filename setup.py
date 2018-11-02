from setuptools import setup

setup(
    use_scm_version={
        'write_to': 'ffffff/__init__.py',
        'write_to_template': '__version__ = {version!r}\n',
    }
)
