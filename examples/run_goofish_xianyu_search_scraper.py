#!/usr/bin/env python3
"""
Goofish (Xianyu / 闲鱼) Scraper: Fast Search & Deals — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/goofish-xianyu-search-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/goofish-xianyu-search-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/goofish-xianyu-search-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_goofish_xianyu_search_scraper.py
"""

import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "keyword": "iPhone 15",
    "maxItems": 10,
    "detailLevel": "full",
    "sortBy": "newest"
}

run = client.actor("unitbytes/goofish-xianyu-search-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("price"), item.get("url"))
