# 🌊 Offshore Intelligence API v2

A lightweight Flask API that provides:
- Offshore wind installation backlog data
- Live offshore wind news headlines (via RSS)

## 📡 Endpoints

### `/`
Check if the API is running.

### `/api/backlog`
Returns example offshore installation projects.

### `/api/news`
Fetches the latest 5 offshore wind news articles from [offshorewind.biz](https://www.offshorewind.biz).

## 🚀 Deployment
This API is hosted on **Render** and automatically redeploys on GitHub commits.
