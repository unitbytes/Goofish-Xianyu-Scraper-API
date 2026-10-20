#!/usr/bin/env python3
"""
Goofish (闲鱼) All-in-One: Search, Sellers & Reviews — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/goofish-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/goofish-xianyu-seller-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/goofish-xianyu-seller-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_goofish_xianyu_seller_scraper.py
"""

import os
from apify_client import ApifyClient

client = ApifyClient(os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN"))

run_input = {
    "mode": "search",
    "keyword": "iPhone 15",
    "maxItems": 20,
    "sortBy": "newest",
    "includeListings": True,
    "includeReviews": True,
    "maxListings": 20,
    "maxReviews": 30
}

run = client.actor("unitbytes/goofish-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("price"), item.get("originalPrice"))
