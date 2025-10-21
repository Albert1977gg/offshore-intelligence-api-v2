from flask import Flask, jsonify
import feedparser  # voor live nieuws ophalen

app = Flask(__name__)

# --- Home route ---
@app.route('/')
def home():
    return "🌊 Offshore Intelligence API v2 is running and ready to serve data."

# --- Backlog route (statische testdata) ---
@app.route('/api/backlog')
def get_backlog():
    data = [
        {
            "project": "Hollandse Kust West",
            "contractor": "Van Oord",
            "foundation_type": "Monopile",
            "status": "planned",
            "region": "North Sea"
        },
        {
            "project": "Dogger Bank D",
            "contractor": "Seaway7",
            "foundation_type": "Jacket",
            "status": "under_construction",
            "region": "North Sea"
        },
        {
            "project": "Empire Wind",
            "contractor": "Subsea 7",
            "foundation_type": "Monopile",
            "status": "operational",
            "region": "US East Coast"
        }
    ]
    return jsonify(data)

# --- Live offshore wind news route ---
@app.route('/api/news')
def get_offshore_news():
    rss_url = "https://www.offshorewind.biz/feed/"
    feed = feedparser.parse(rss_url)

    articles = []
    for entry in feed.entries[:5]:
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published
        })

    return jsonify({
        "source": "offshorewind.biz",
        "articles": articles
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
