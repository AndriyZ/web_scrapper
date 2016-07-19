'''
Command line module to handle user input
'''
import argparse
import logger
import config
import api

logger = logger.get_logger()


def create_argument_parser():
    '''
    This method creates argument parser for run_sever command
    
    returns: parser - instance of ArgumentParser
    '''

    parser = argparse.ArgumentParser(prog='web_scrapper',
                                     description='text',
                                     formatter_class=\
                                        argparse.RawDescriptionHelpFormatter
                                         )
    parser.add_argument('-ulrs_to_parse', '--urls_to_parse',
                            help="space separated urls for parse",
                            dest="urls",
                            nargs='+',
                            type=str)
    parser.add_argument('-not_older', '--not_older',
                            help='Specify number of days to compare',
                            dest="not_older",type=int
                            )
    return parser


def main():
    print('aa')
    logger.info('Start application')
    parser = create_argument_parser()
    args = parser.parse_args()
    if args:
        logger.info('command_line')
        if args.urls is None:
            urls = config.SITE_URLS
        else:
            urls = args.urls
            print(type(args.urls))
            print(args.urls)
        
        if args.not_older is None:
            not_older = config.DAYS_TO_COMPARE
        else:
            not_older = args.not_older
    logger.debug('Using urls to parse - {0}'.format(' '.join(urls)))
    logger.debug('Application will collect articles not older then {0} days'.format(not_older))
    logger.info('Start parsing of articles')
    print(api.parse(urls, not_older))

    