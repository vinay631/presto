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


def get_query_result(query_filename, query_params):
    """
    Query the LEAP analytics engine.

    :param query_filename: Filename of the file with sql query.
    :type query_filename: str

    :param query_params: The parameters for the sql query.
    :type query_params: Tuple

    :return: List[List[str]]
    """

    sql = open(query_filename, 'r').read()
    CURSOR.execute(sql, query_params)
    result = CURSOR.fetchall()

    return result


def print_result(headers, result):
    """
    Print result of sql query

    :param headers: Column names of the sql query result.
    :type headers: List[str]

    :param result: Result of sql query.
    :type result: List[List[str]]

    :return: None
    """

    print('\t\t'.join(headers))

    for row in result:
        print('\t'.join(row))


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

    try:
        # Get Allergy info.
        result = get_query_result(ALLERGY_SQL_FILE, (first_name, last_name))

        # Print result.
        headers = ['Code', 'Description']
        if result:
            print_result(headers, result)
        else:
            print("No result found for %s %s" % (first_name, last_name))
    except Exception as excpt:
        print(excpt)
        traceback.print_exc()
