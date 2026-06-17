import snowflake.connector

def get_connection():
    conn = snowflake.connector.connect(
        user="ROMANNTR",
        password="6y2fQRcg7vGzEve",
        account="DNOPFSB-EJ71380",
        warehouse="COMPUTE_WH",
        database="AI_ANALYST_DB",
        schema="PROJECT"
    )
    return conn