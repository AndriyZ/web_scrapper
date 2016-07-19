web_scrapper application was written by Andriy Zadorozhnyi
Python version 3.4
To install all requirements neede of application run pip install -r ../web_scrapper/requirements.txt
To install command web_scrapper to you virtual environment run python setup.py install
After this command web_scrapper will be installed to your python environment
Type web_scrapper -h to see command option
Command web_scrapper cna be run with arguments or without then:
	1 Run with arguments: web_scrapper --ulrs_to_parse http://itukraine.org.ua/en/new https://	news.vice.com/hub/sections  --not_older 3 - all articles for 3 days only form http://itukraine.org.ua/en/new and 
https://news.vice.com/hub/sections will be parsed.
	2  Run without arguments: web_scrapper application will read articles utl and not_older date form config.py

Enjoy!
