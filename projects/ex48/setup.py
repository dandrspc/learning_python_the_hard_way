try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ex48',
    'author': 'Daniel Andrés Palacios @dandrspc',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it',
    'author_email': 'dapalca@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
