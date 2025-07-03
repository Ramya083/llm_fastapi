import psycopg

# Set your connection parameters
conn = psycopg.connect(
    host="early-regular-bulldog.a1.pgedge.io",
    dbname="pg",
    user="admin",
    password="8O08Hpa9K843XZRsTm0M69IJ",
    sslmode="require"  # Change if needed
)

def insert_interaction(prompt, response):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO llm_interactions (prompt, response) VALUES (%s, %s)",
            (prompt, response)
        )
        conn.commit()

def fetch_all_interactions():
    with conn.cursor() as cur:
        cur.execute("SELECT id, prompt, response, created_at FROM llm_interactions")
        return cur.fetchall()

if __name__ == "__main__":
    # Example usage
    insert_interaction("Hello, LLM!", "Hi there!")
    rows = fetch_all_interactions()
    for row in rows:
        print(row)

    conn.close()