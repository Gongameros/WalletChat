import sqlite3

def create_table():
    conn = sqlite3.connect('WalletChat.db')
    cursor = conn.cursor()

    # SQL command to create the table
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS person (
    ID INTEGER PRIMARY KEY,
    TIERS INTEGER DEFAULT 0 CHECK (TIERS IN (0, 1, 2, 3)),
    transaction_time DATETIME
    );
    '''

    cursor.execute(create_table_sql)
    conn.commit()
    conn.close()

def insert_person(id):
    conn = sqlite3.connect('WalletChat.db')
    cursor = conn.cursor()

    select_sql = '''
    SELECT ID FROM person WHERE ID = ?
    '''
    cursor.execute(select_sql, id)
    existing_id = cursor.fetchone()

    if existing_id is not None:
        print(f"ID {id} already exists in the table.")
    else:
        insert_sql = '''
        INSERT INTO person (ID) VALUES (?)
        '''
        cursor.execute(insert_sql, id)
        conn.commit()

    conn.close()


def get_tier_status(id):
    conn = sqlite3.connect('WalletChat.db')
    cursor = conn.cursor()

    select_sql = '''
    SELECT TIERS FROM person WHERE ID = ?
    '''

    cursor.execute(select_sql, id)
    result = cursor.fetchone()

    if result is not None:
        status = result[0]
        conn.close()
        return status
    else:
        conn.close()
        return None
    