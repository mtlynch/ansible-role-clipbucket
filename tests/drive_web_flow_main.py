import argparse

import clipbucket_driver

BASE_URL = 'http://localhost'


def main(args):
    driver = clipbucket_driver.ClipBucketDriver(BASE_URL)
    driver.do_login(args.username, args.password)
    driver.do_check_modules()

    driver.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='ClipBucket Web Driver',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--username', required=True)
    parser.add_argument('--password', required=True)
    main(parser.parse_args())
