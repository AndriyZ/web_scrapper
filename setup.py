from setuptools import setup, find_packages

package_scrapper = {
    'name': 'scrapper',
    'version': '0.1',
    'description': 'Web scrapper application',
    'packages': find_packages(),
    'author': 'Andriy Zadorozhnyi',
    'install_requires': ['newspaper3k'],

    # Always disable support for zip eggs
    'zip_safe': False,
}

setup(**package_scrapper)
