import argparse
import logging

import clipbucket_driver

logger = logging.getLogger(__name__)


def _configure_logging():
    """Configure the root logger for log output."""
    root_logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)


def main(args):
    _configure_logging()
    driver = clipbucket_driver.ClipBucketDriver(args.url)
    driver.do_login(args.username, args.password)
    driver.do_check_modules()

    driver.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='ClipBucket Web Driver',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--url', required=True)
    parser.add_argument('--username', required=True)
    parser.add_argument('--password', required=True)
    main(parser.parse_args())
