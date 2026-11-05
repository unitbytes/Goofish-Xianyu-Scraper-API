#!/usr/bin/env python3
"""
Goofish & Xianyu (闲鱼) — Real-Time Synchronous Standby REST API Quickstart
Standby Endpoints:
  - https://unitbytes--goofish-scraper.apify.actor (All-in-One: Search, Items, Sellers, Inventory & Reviews)
  - https://unitbytes--goofish-xianyu-search-scraper.apify.actor (Real-Time Search & Seller Standby)
Docs & Schema: https://unitbytes.com/actors/goofish-xianyu-seller-scraper/

Usage:
    pip install requests
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_goofish_standby_api.py
"""

import os
import requests

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

BASE_URL = "https://unitbytes--goofish-scraper.apify.actor"
HEADERS = {"Authorization": f"Bearer {APIFY_TOKEN}"}

# 1. Real-Time Secondhand Product Search (GET /v1/search)
resp = requests.get(
    f"{BASE_URL}/v1/search",
    headers=HEADERS,
    params={"keyword": "ccd相机", "page": 1, "sort_by": "default"},
    timeout=30,
)
resp.raise_for_status()
search_res = resp.json()

items = search_res.get("data", {}).get("items", [])
print(f"Found {len(items)} live Goofish listings:")
for item in items[:3]:
    print(f" - [{item.get('itemId')}] {item.get('title')} | ¥{item.get('price')} CNY | Location: {item.get('location')}")
