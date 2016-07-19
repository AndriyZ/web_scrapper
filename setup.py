from setuptools import setup


setup(name='web_scrapper',
      description='Web scrapper application',
      entry_points={
        'console_scripts': [
            'web_scrapper=cli:main']
                    },
      version='0.1',
      author = 'Andriy Zadorozhnyi',
      install_requires =['newspaper3k', 'pytz'],
      )

