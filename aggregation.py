import psycopg2
from metaphor_python import Metaphor


METAPHOR_API_KEY = ""
metaphor = Metaphor(METAPHOR_API_KEY)


DB_NAME = ""
DB_USER = ""
DB_PASS = ""
DB_HOST = ""
DB_PORT = ""

conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        id SERIAL PRIMARY KEY,
        title TEXT,
        url TEXT UNIQUE,
        content TEXT,
        publication_date DATE,
        source TEXT
    )
""")
conn.commit()


KEY_TERMS = [
    "stock market updates",
    "forex news",
    "commodity market trends",
    "central bank policy changes",
    "cryptocurrency trends",
    "mergers and acquisitions",
    "global economic forecasts",
    "interest rate predictions",
    "emerging markets overview",
    "technology stocks insights",
    "real estate market outlook",
    "venture capital investments",
    "private equity deals",
    "hedge fund strategies",
    "banking sector news",
    "fintech innovations",
    "financial regulations updates",
    "bond market movements",
    "Economic indicators reports",
    "IPO news and insights",
    "dividend announcements",
    "credit market trends",
    "asset management strategies",
    "sustainability and finance",
    "green bonds and investments",
    "financial technology partnerships",
    "derivatives market analysis",
    "financial market disruptions",
    "tax policy changes",
    "global trade agreements",
    "financial market innovations",
    "retirement and pension fund news",
    "insurance industry trends",
    "financial literacy and education"
]

def fetch_and_store_articles(query):
    search_response = metaphor.search(query, use_autoprompt=True)
    contents_response = search_response.get_contents()

    for content in contents_response.contents:
        try:
            cursor.execute("""
                INSERT INTO articles (title, url, content, publication_date, source)
                VALUES (%s, %s, %s, NOW(), %s)
            """, (content.title, content.url, content.extract, "Metaphor API"))
            conn.commit()
        except psycopg2.IntegrityError:  
            conn.rollback()

def main():
    for term in KEY_TERMS:
        fetch_and_store_articles(f"Here is an article about {term}")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
