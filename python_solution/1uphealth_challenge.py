import argparse
import configparser
import traceback

from pyhive import presto

CONFIG = configparser.ConfigParser()
CONFIG.read('config.ini')
HOST = CONFIG['DEFAULT']['HOST']
CATALOG = CONFIG['DEFAULT']['CATALOG']
SCHEMA = CONFIG['DEFAULT']['SCHEMA']

CURSOR = presto.connect(HOST, username='presto',
                        catalog=CATALOG, schema=SCHEMA).cursor()
ALLERGY_SQL_FILE = "sql/allergyinfo.sql"


def get_allergy_info(first_name, last_name):
    sql = open(ALLERGY_SQL_FILE, 'r').read()
    CURSOR.execute(sql, (first_name, last_name))
    result = CURSOR.fetchall()

    return result


def print_result(result):
    print('%s\t\t%s' % ('Code', 'Description'))

    for code, description in result:
        print('%s\t%s' % (code, description))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('first_name',
                        metavar='firstName',
                        type=str,
                        help='First Name.'
                        )
    parser.add_argument('last_name',
                        metavar='lastName',
                        type=str,
                        help='Last Name.'
                        )
    args = parser.parse_args()
    first_name = args.first_name
    last_name = args.last_name

    result = get_allergy_info(first_name, last_name)
    print_result(result)
