@app.route("/openapi.yaml")
def openapi_yaml():
    yaml_text = """openapi: 3.1.0
info:
  title: Offshore Intelligence API v2
  version: "1.0.0"
  description: |
    Provides offshore wind project backlog data and live offshore wind news headlines.
    The API delivers JSON-formatted results for use in ChatGPT, dashboards, or internal systems.
servers:
  - url: https://offshore-intelligence-api-v2.onrender.com
paths:
  /api/backlog:
    get:
      summary: Get offshore installation backlog data
      operationId: getBacklog
      responses:
        "200":
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
        "200":
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
    return Response(yaml_text, mimetype="application/yaml")
