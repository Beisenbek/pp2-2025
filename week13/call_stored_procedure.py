import psycopg2
from config import load_config


def add_part(part_name, vendor_name):
    """ Add a new part """
    # read database configuration
    params = load_config()

    try:
        # connect to the PostgreSQL database
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # call a stored procedure
                cur.execute('CALL add_new_part(%s,%s)', (part_name, vendor_name))

            # commit the transaction
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == '__main__':
    add_part('OLED', 'LG')