def get_transactions_list(cursor):
    command = """
    select * from transactions;
    """
    result = cursor.execute(command)
    transactions = result.fetchall()
    print(transactions)