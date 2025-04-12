import psycopg2
from config import load_config


def get_parts(vendor_id):
    """ Get parts provided by a vendor specified by the vendor_id """
    parts = []
    # read database configuration
    params = load_config()
    try:
        # connect to the PostgreSQL database
        with  psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # create a cursor object for execution
                cur = conn.cursor()
                cur.callproc('get_parts_by_vendor', (vendor_id,))

                # process the result set
                row = cur.fetchone()
                while row is not None:
                    parts.append(row)
                    row = cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return parts

if __name__ == '__main__':
    parts = get_parts(1)
    print(parts)