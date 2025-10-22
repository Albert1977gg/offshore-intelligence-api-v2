from flask import Flask, jsonify, Response

app = Flask(__name__)

@app.route("/")
def home():
    return "🌊 Offshore Intelligence API v2 is running and ready to serve data."

@app.route("/api/backlog")
def backlog():
    data = [
        {
            "project": "Hollandse Kust West",
            "contractor": "Van Oord",
            "foundation_type": "Monopile",
            "status": "planned",
            "region": "North Sea"
        },
        {
            "project": "Dogger Bank",
            "contractor": "SSE Renewables",
            "foundation_type": "Jacket",
            "status": "under construction",
            "region": "UK North Sea"
        }
    ]
    return jsonify(data)

@app.route("/api/news")
def news():
    data = {
        "source": "offshorewind.biz",
        "articles": [
            {
                "title": "Van Oord wins new offshore wind contract",
                "link": "https://www.offshorewind.biz/article1",
                "published": "2025-10-22T10:00:00Z"
            },
            {
                "title": "Siemens Gamesa expands offshore turbine capacity",
                "link": "https://www.offshorewind.biz/article2",
                "published": "2025-10-21T08:00:00Z"
            }
        ]
    }
    return jsonify(data)

@app.route("/openapi.yaml")
def openapi_yaml():
    yaml_text = """openapi: 3.0.1
info:
  title: Offshore Intelligence API v2
  description: >
    Provides offshore wind project backlog data and live offshore wind news headlines.
    The API delivers JSON-formatted results for use in ChatGPT, dashboards, or internal systems.
  version: "1.0.0"
servers:
  - url: https://offshore-intelligence-api-v2.onrender.com
paths:
  /api/backlog:
    get:
      summary: Get offshore installation backlog data
      operationId: getBacklog
      responses:
        '200':
          description: List of offshore installation projects
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    project:
                      type: string
                      example: Hollandse Kust West
                    contractor:
                      type: string
                      example: Van Oord
                    foundation_type:
                      type: string
                      example: Monopile
                    status:
                      type: string
                      example: planned
                    region:
                      type: string
                      example: North Sea
  /api/news:
    get:
      summary: Get live offshore wind news headlines
      operationId: getOffshoreNews
      responses:
        '200':
          description: Latest 5 offshore wind news articles
          content:
            application/json:
              schema:
                type: object
                properties:
                  source:
                    type: string
                    example: offshorewind.biz
                  articles:
                    type: array
                    items:
                      type: object
                      properties:
                        title:
                          type: string
                          example: Van Oord wins new offshore wind contract
                        link:
                          type: string
                          example: https://www.offshorewind.biz/article
                        published:
                          type: string
                          example: 2025-10-22T10:00:00Z
"""
    return Response(yaml_text, mimetype="text/yaml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
