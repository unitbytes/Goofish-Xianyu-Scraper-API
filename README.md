# 🐟 Goofish & Xianyu (闲鱼) Scraper + Real-Time Standby REST API Suite (`$1 / 1K`)

<div align="center">

[![Available on Apify](https://img.shields.io/badge/Available_on-Apify-28B52A?style=for-the-badge&logo=apify&logoColor=white)](https://apify.com/unitbytes/goofish-xianyu-search-scraper?fpr=939u3w&fp_sid=gh_goofish_api)
[![Open in Colab](https://img.shields.io/badge/Open_in-Google_Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/unitbytes/Goofish-Xianyu-Scraper-API/blob/main/notebooks/quickstart.ipynb)
[![n8n Creator Hub](https://img.shields.io/badge/n8n_Creator_Hub-@unitbytes-EA4B71?style=for-the-badge&logo=n8n&logoColor=white)](https://n8n.io/creators/unitbytes/)
[![Release](https://img.shields.io/github/v/release/unitbytes/Goofish-Xianyu-Scraper-API?style=for-the-badge&logo=github&color=10b981)](https://github.com/unitbytes/Goofish-Xianyu-Scraper-API/releases)
[![Pricing](https://img.shields.io/badge/Pricing-Pay_Per_Result-orange?style=for-the-badge)](https://apify.com/unitbytes/goofish-xianyu-search-scraper?fpr=939u3w&fp_sid=gh_goofish_api)

**The fastest cookieless Goofish / Xianyu (闲鱼) China secondhand marketplace scraper and sub-second Multi-Tenant Standby REST API suite on Apify (`$1.00–$2.00 / 1,000 items`). Extract live secondhand deals, seller storefronts, Zhima Credit (芝麻信用) trust badges, seller inventory catalogs, and verified buyer reviews.**

[**🚀 Try Live on Apify**](https://apify.com/unitbytes/goofish-xianyu-search-scraper?fpr=939u3w&fp_sid=gh_goofish_api) • [**📓 Open in Google Colab**](https://colab.research.google.com/github/unitbytes/Goofish-Xianyu-Scraper-API/blob/main/notebooks/quickstart.ipynb) • [**⚡ Official n8n Creator Hub**](https://n8n.io/creators/unitbytes/) • [**🔧 39 Free n8n Templates**](https://unitbytes.com/n8n/) • [**📖 Documentation & Schemas**](https://unitbytes.com/actors/) • [**📚 Engineering Playbooks**](https://unitbytes.com/blog/)

</div>

---

<p align="center">
  <a href="https://apify.com/unitbytes/goofish-xianyu-search-scraper?fpr=939u3w&fp_sid=gh_goofish_api" target="_blank">
    <img src="https://raw.githubusercontent.com/unitbytes/.github/main/assets/banners/unitbytes-goofish-xianyu-search-deals-scraper-banner.jpg" alt="🐟 Goofish & Xianyu (闲鱼) Scraper + Real-Time Standby REST API Suite (`$1 / 1K`)" width="100%" />
  </a>
</p>

<p align="center">
  <a href="https://apify.com/unitbytes/goofish-xianyu-search-scraper?fpr=939u3w&fp_sid=gh_goofish_api" target="_blank">
    <img src="https://raw.githubusercontent.com/unitbytes/.github/main/assets/try-it-for-free.svg" width="240" height="48" alt="Try it for Free">
  </a>
  <br>
  <sub>⚡ <b>1-Click Free Trial:</b> Test live queries using Apify's `$5` free monthly credit • Zero login or cookies required</sub>
</p>

---

<!-- UNITBYTES_REPO_KIT_START -->
## 📦 Included in This Repository (Python Quickstarts, Google Colab, n8n Workflows, MCP & Sample Data)

This repository contains ready-to-run **Python SDK scripts**, an **interactive 1-Click Google Colab notebook (`notebooks/quickstart.ipynb`)**, **9-node n8n automation workflow `.json` templates**, **AI Agent MCP configuration (`.cursor/mcp.json`)**, and **sample output datasets (JSON & CSV)**:

| Extraction Engine | 🐍 Python SDK Quickstart | ⚡ n8n Workflow Template | 📊 Sample Output | 🚀 Cloud Console |
| :--- | :--- | :--- | :---: | :---: |
| **Goofish (Xianyu / 闲鱼) Scraper: Fast Search & Deals**<br><sub>[`unitbytes/goofish-xianyu-search-scraper`](https://apify.com/unitbytes/goofish-xianyu-search-scraper?fpr=939u3w&fp_sid=gh_goofish_api) • [Full Schema](https://unitbytes.com/actors/goofish-xianyu-search-scraper/) • [Engineering Playbook](https://unitbytes.com/blog/how-to-scrape-goofish-xianyu-secondhand-arbitrage-guide/)</sub> | [`examples/run_goofish_xianyu_search_scraper.py`](examples/run_goofish_xianyu_search_scraper.py) | [`n8n/goofish-xianyu-search-scraper-n8n-workflow.json`](n8n/goofish-xianyu-search-scraper-n8n-workflow.json) | [`JSON`](samples/goofish-xianyu-search-scraper-sample.json) · [`CSV`](samples/goofish-xianyu-search-scraper-sample.csv) | [⚡ **Run on Apify**](https://apify.com/unitbytes/goofish-xianyu-search-scraper?fpr=939u3w&fp_sid=gh_goofish_api) |
| **Goofish (闲鱼) All-in-One: Search, Sellers & Reviews**<br><sub>[`unitbytes/goofish-scraper`](https://apify.com/unitbytes/goofish-scraper?fpr=939u3w&fp_sid=gh_goofish_api) • [Full Schema](https://unitbytes.com/actors/goofish-xianyu-seller-scraper/) • [Engineering Playbook](https://unitbytes.com/blog/how-to-scrape-goofish-xianyu-secondhand-arbitrage-guide/)</sub> | [`examples/run_goofish_xianyu_seller_scraper.py`](examples/run_goofish_xianyu_seller_scraper.py) | [`n8n/goofish-xianyu-seller-scraper-n8n-workflow.json`](n8n/goofish-xianyu-seller-scraper-n8n-workflow.json) | [`JSON`](samples/goofish-xianyu-seller-scraper-sample.json) · [`CSV`](samples/goofish-xianyu-seller-scraper-sample.csv) | [⚡ **Run on Apify**](https://apify.com/unitbytes/goofish-scraper?fpr=939u3w&fp_sid=gh_goofish_api) |
| **Goofish (闲鱼) Synchronous Standby REST APIs (`<500ms` GET)**<br><sub>[`unitbytes--goofish-scraper.apify.actor`](https://apify.com/unitbytes/goofish-scraper?fpr=939u3w&fp_sid=gh_goofish_api) • [`unitbytes--goofish-xianyu-search-scraper.apify.actor`](https://apify.com/unitbytes/goofish-xianyu-search-scraper?fpr=939u3w&fp_sid=gh_goofish_api)</sub> | [`examples/run_goofish_standby_api.py`](examples/run_goofish_standby_api.py) | [`n8n/goofish-xianyu-seller-scraper-n8n-workflow.json`](n8n/goofish-xianyu-seller-scraper-n8n-workflow.json) | [`JSON`](samples/goofish-xianyu-seller-scraper-sample.json) · [`CSV`](samples/goofish-xianyu-seller-scraper-sample.csv) | [⚡ **Standby Docs**](https://apify.com/unitbytes/goofish-scraper?fpr=939u3w&fp_sid=gh_goofish_api) |

- 📓 **1-Click Interactive Google Colab Notebook:** Open [`notebooks/quickstart.ipynb`](notebooks/quickstart.ipynb) directly in your browser via [**Google Colab ↗**](https://colab.research.google.com/github/unitbytes/Goofish-Xianyu-Scraper-API/blob/main/notebooks/quickstart.ipynb) to inspect sample DataFrames and test live API queries with zero local setup.
- 🤖 **Cursor, Windsurf & Claude Code MCP Ready:** Includes [`.cursor/mcp.json`](.cursor/mcp.json) pre-configured with `https://mcp.apify.com` so AI coding agents can invoke these UnitBytes scrapers natively.
- 💡 **Using n8n?** Explore our official creator profile at **[n8n.io/creators/unitbytes](https://n8n.io/creators/unitbytes/)** or copy all 39 pre-built 9-node scraping workflows (`Ctrl+V`) at **[unitbytes.com/n8n](https://unitbytes.com/n8n/)**.
- 📚 **Engineering Playbook:** Read **[How to Search & Scrape Goofish (Xianyu / 闲鱼) Without a +86 Phone Login in 2026 (API Guide)](https://unitbytes.com/blog/how-to-scrape-goofish-xianyu-secondhand-arbitrage-guide/)** or browse all scraping & automation guides at **[unitbytes.com/blog](https://unitbytes.com/blog/)**.
<!-- UNITBYTES_REPO_KIT_END -->

---

## ⚡ Pre-Configured 1-Click Task Presets

Launch pre-configured extraction templates directly in the Apify Cloud Console with zero parameter setup:

| Task Preset | Target Extraction Use Case | Direct Launch |
| :--- | :--- | :---: |
| **Find Used iPhones & Refurbished Apple Deals on Goofish (闲鱼)** | Extract iPhone 15, 14, and 13 listings on Goofish. Filter by price, seller Zhima credit, battery health specs, and clean plain-text descriptions. | [⚡ Run Task Preset](https://apify.com/unitbytes/goofish-xianyu-search-scraper/examples/goofish-iphone-used-phones?fpr=939u3w&fp_sid=gh_goofish_api) |
| **Track Nintendo Switch OLED & Japanese Console Deals on Goofish** | Monitor Nintendo Switch OLED, PS5, and retro handhelds on Goofish. Extract Japanese import editions, bundled games, condition, and seller ratings. | [⚡ Run Task Preset](https://apify.com/unitbytes/goofish-xianyu-search-scraper/examples/goofish-nintendo-switch-consoles?fpr=939u3w&fp_sid=gh_goofish_api) |
| **Source Anime Figures, Bandai & Pop Mart Collectibles on Goofish** | Search rare anime figures, garage kits, Pop Mart blind boxes, and authentic Japanese collectibles on Goofish. Get HD photo galleries and seller feedback. | [⚡ Run Task Preset](https://apify.com/unitbytes/goofish-xianyu-search-scraper/examples/goofish-anime-figures-collectibles?fpr=939u3w&fp_sid=gh_goofish_api) |
| **Monitor RTX 4090, 4080 & Used Graphics Cards on Goofish** | Track secondary market prices for NVIDIA GeForce RTX 4090, 4080, and 3080 GPUs on Goofish. Detect price drops and vet seller transaction history. | [⚡ Run Task Preset](https://apify.com/unitbytes/goofish-xianyu-search-scraper/examples/goofish-graphics-cards-gpu?fpr=939u3w&fp_sid=gh_goofish_api) |
| **Discover Vintage Leica, Canon & Sony Cameras on Goofish** | Find vintage 35mm film cameras, medium format bodies, Leica rangefinders, and vintage lenses on Goofish with high-resolution inspection photos. | [⚡ Run Task Preset](https://apify.com/unitbytes/goofish-xianyu-search-scraper/examples/goofish-vintage-film-cameras?fpr=939u3w&fp_sid=gh_goofish_api) |
| **Track Second-Hand Luxury Bags, Streetwear & Sneakers on Goofish** | Monitor designer fashion, luxury handbags, and limited-edition sneakers on Goofish. Filter by appraisal service guarantee (`filterAppraise`) and condition. | [⚡ Run Task Preset](https://apify.com/unitbytes/goofish-xianyu-search-scraper/examples/goofish-designer-luxury-fashion?fpr=939u3w&fp_sid=gh_goofish_api) |
| **Audit Seller Sold History & Clearing Prices on Goofish (闲鱼)** | Extract complete historical sold listings from any Goofish 闲鱼 (Xianyu / Idlefish) seller to analyze sales velocity, real clearing prices, turnover rate, and historical discount margins. | [⚡ Run Task Preset](https://apify.com/unitbytes/goofish-scraper/examples/audit-seller-sold-history-pricing?fpr=939u3w&fp_sid=gh_goofish_api) |
| **Export Active Seller Product Catalog from Goofish (闲鱼)** | Scrape all currently active, on-sale product listings from any Goofish 闲鱼 (Xianyu / Idlefish) seller profile with prices, high-res photos, tags, and direct item links. | [⚡ Run Task Preset](https://apify.com/unitbytes/goofish-scraper/examples/export-active-seller-catalog?fpr=939u3w&fp_sid=gh_goofish_api) |
| **Deep Goofish Seller Catalog & Spec Enrichment** | Deeply enrich Goofish seller listings with full plain-text descriptions, condition ratings, view/want statistics, seller location, and structured specifications dictionaries. | [⚡ Run Task Preset](https://apify.com/unitbytes/goofish-scraper/examples/deep-seller-catalog-specs-enrichment?fpr=939u3w&fp_sid=gh_goofish_api) |
| **Seller Credibility, Trust & Zhima Credit Background Check** | Perform instant seller credibility background checks on Goofish (闲鱼 / Idlefish). Extract Zhima credit ratings, real-name verification badges, follower counts, and account age. | [⚡ Run Task Preset](https://apify.com/unitbytes/goofish-scraper/examples/seller-trust-and-zhima-credit-check?fpr=939u3w&fp_sid=gh_goofish_api) |
| **Audit Goofish Seller Buyer Reviews & Rating Reputation** | Scrape comprehensive buyer feedback and rating reviews for any Goofish (闲鱼 / Xianyu) seller store. Extract buyer nicknames, review text, ratings, and purchase timestamps. | [⚡ Run Task Preset](https://apify.com/unitbytes/goofish-scraper/examples/audit-seller-buyer-reviews-reputation?fpr=939u3w&fp_sid=gh_goofish_api) |

---

## 🧭 Which Goofish / Xianyu (闲鱼) Engine Should You Use?

| Engine | Apify Actor & Standby URL | Best For | Key Extracted Data | Starting Price |
| :--- | :--- | :--- | :--- | :---: |
| **🛡️ Goofish All-in-One: Search, Sellers & Reviews** | [`unitbytes/goofish-scraper`](https://apify.com/unitbytes/goofish-scraper?fpr=939u3w&fp_sid=gh_goofish_api)<br><sub>Standby: `unitbytes--goofish-scraper.apify.actor`</sub> | Deep seller due diligence, Zhima Credit (`芝麻信用`) verification, storefront inventory (`selling`/`sold`), and buyer review auditing | Seller profile, credit grade, active/sold item catalogs, historical buyer reviews, and keyword search | `$0.001 / review` (`$1.00 / 1K`) |
| **🐟 Goofish Search & Deals Scraper** | [`unitbytes/goofish-xianyu-search-scraper`](https://apify.com/unitbytes/goofish-xianyu-search-scraper?fpr=939u3w&fp_sid=gh_goofish_api)<br><sub>Standby: `unitbytes--goofish-xianyu-search-scraper.apify.actor`</sub> | High-speed secondhand deal discovery, luxury/electronics arbitrage, and price monitoring | Keyword search feeds, CNY prices, `wantCount` heat, item details, and seller trust badges | `$0.002 / item` (`$2.00 / 1K`) |

---

## 🛠️ Extraction Engines in This Suite

### 🚀 Goofish (Xianyu / 闲鱼) Scraper: Fast Search & Deals (`unitbytes/goofish-xianyu-search-scraper`)

The fastest and most affordable Goofish 闲鱼 (Xianyu / Idlefish) scraper. Dual modes: ultra-fast summary and 150+ field full details with zero compute fees. MCP & AI Agent ready.

- **Pricing:** `$0.002 / item` (Pay-Per-Event — `$0.002` search item (summary), `$0.0049` enriched detail item (volume tiers from `$0.0016`))
- **Cloud Console:** [https://apify.com/unitbytes/goofish-xianyu-search-scraper?fpr=939u3w&fp_sid=gh_goofish_api](https://apify.com/unitbytes/goofish-xianyu-search-scraper?fpr=939u3w&fp_sid=gh_goofish_api)
- **Full Documentation & Schema:** [https://unitbytes.com/actors/goofish-xianyu-search-scraper/](https://unitbytes.com/actors/goofish-xianyu-search-scraper/)
- **n8n Workflow File:** [`n8n/goofish-xianyu-search-scraper-n8n-workflow.json`](n8n/goofish-xianyu-search-scraper-n8n-workflow.json)
- **Engineering Playbook:** [How to Search & Scrape Goofish (Xianyu / 闲鱼) Without a +86 Phone Login in 2026 (API Guide)](https://unitbytes.com/blog/how-to-scrape-goofish-xianyu-secondhand-arbitrage-guide/)

#### Key Capabilities
- **150+ Normalized Attributes:** Extracts title, price, original purchase price, bargain status, seller location, wants counter, and high-res media.
- **Authentic Zhima Credit Auditing:** Identifies seller credit tiers (Excellent, Great, Medium) to filter out fraudulent vendors and prioritize authentic deals.
- **Price & Category Boundaries:** Apply precise price filters, shipping inclusion flags, and sorting criteria (newest, price ascending, popularity).
- **Sub-Second Response Pipeline:** Built with high-throughput cloud infrastructure and automated request orchestration for enterprise streaming speed.

#### ⚙️ Input Parameters (Schema)

| Parameter | Type | Default / Prefill | Description |
| :--- | :---: | :--- | :--- |
| `keyword` | `string` | `iPhone 15` | Keyword in Chinese or English (e.g. 'iPhone 15', '手机', '显卡', 'Switch', '乐高'). Ignored if startUrls or searchUrls is provided. |
| `startUrls` | `array` | — | Direct Goofish item URLs (e.g. 'https://www.goofish.com/item?id=1084132717206') or numeric item IDs to enrich directly with 150+ fields using ultra-fast session warm-up without searching. |
| `searchUrls` | `array` | — | One or more Goofish search URLs (e.g. 'https://www.goofish.com/search?q=iPhone+15'). Search keywords and parameters are automatically extracted and scraped. |
| `maxItems` | `integer` | `10` | Maximum number of items to scrape (1 to 1,500). |
| `detailLevel` | `string` | `full` | 'summary' (ultra-fast card extraction) or 'full' (enriches each item with 150+ fields including multi-image gallery, full specs, and seller intelligence). |
| `sortBy` | `string` | `newest` | Sorting order of the listings. |
| `priceMin` | `integer` | — | Minimum price in Chinese Yuan (CNY ¥). |
| `priceMax` | `integer` | — | Maximum price in Chinese Yuan (CNY ¥). |
| `quickFilters` | `array` | — | One-click filters provided by Goofish. |
| `regionIds` | `array` | — | Chinese administrative region/city codes (e.g., '440100' for Guangzhou, '310100' for Shanghai). |
| `proxyConfiguration` | `object` | `{"useApifyProxy": true, "apifyProxyGroups": ["RE` | Apify Residential Proxy is strictly required. Goofish (Alibaba) aggressively blocks all datacenter IPs and non-sticky proxies. |

#### ⚡ Real-Time Synchronous Multi-Tenant Standby REST API (`<500ms` GET)

Both Goofish / Xianyu (闲鱼) engines support **instant synchronous HTTP `GET` requests** via Apify Multi-Tenant Standby Mode (`Authorization: Bearer <APIFY_API_TOKEN>`):

- ⚡ **All-in-One Standby Server:** `https://unitbytes--goofish-scraper.apify.actor` ([Console & Docs](https://apify.com/unitbytes/goofish-scraper?fpr=939u3w&fp_sid=gh_goofish_api))
- ⚡ **Search & Deals Standby Server:** `https://unitbytes--goofish-xianyu-search-scraper.apify.actor` ([Console & Docs](https://apify.com/unitbytes/goofish-xianyu-search-scraper?fpr=939u3w&fp_sid=gh_goofish_api))
- 🐍 **Runnable Python Script:** [`examples/run_goofish_standby_api.py`](examples/run_goofish_standby_api.py)

| Endpoint | Method | Query Parameters | Description |
| :--- | :---: | :--- | :--- |
| `/v1/search` | `GET` | `keyword`, `page`, `sort_by`, `min_price`, `max_price`, `detail_level` (`summary`/`full`) | Real-time Xianyu keyword search with server-side price range, condition, and sorting filters. |
| `/v1/item` | `GET` | `item_id` (or `url`) | Full secondhand listing detail, high-res image gallery, CNY price, seller card, and location. |
| `/v1/seller` | `GET` | `seller_id` (or `url`) | Seller profile, Zhima Credit (芝麻信用) grade, verification badges, sales volume, and rating summary. |
| `/v1/seller/items` | `GET` | `seller_id`, `status` (`selling`/`sold`), `page`, `detail_level` | Paginate a seller's active (`selling`) or historical (`sold`) storefront inventory. |
| `/v1/seller/reviews` | `GET` | `seller_id`, `rate_type`, `page` | Paginate verified buyer reviews, ratings, transaction timestamps, and buyer feedback tags. |

#### Python SDK Quickstart (`examples/run_goofish_xianyu_search_scraper.py`)
```python
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
```

#### Sample Output Schema (`samples/goofish-xianyu-search-scraper-sample.json`)
```json
{
  "id": "800000000002",
  "title": "Switch OLED 喷射战士3限定港版",
  "price": 1340,
  "currency": "CNY",
  "url": "https://www.goofish.com/item?id=800000000002",
  "pictureUrl": "https://img.alicdn.com/bao/uploaded/i2/2200000000002/O1CN01Dd3gwqAchoG3thAe_!!4611686018427384045-0-xy_item.jpg",
  "imageUrls": [
    "https://img.alicdn.com/bao/uploaded/i2/2200000000002/O1CN01Dd3gwqAchoG3thAe_!!4611686018427384045-0-xy_item.jpg"
  ],
  "city": "九江",
  "freeShipping": true,
  "tags": [
    "6小时前发布",
    "卖家信用极好",
    "freeShippingIcon"
  ],
  "postedAt": "2026-09-16T14:34:20+00:00",
  "description": "Switch OLED 喷射战士3限定港版\n原装配件齐全，箱说全，五码合一，机身有轻微使用痕迹，按键灵敏，屏幕已贴钢化膜，功能一切正常。\n支持顺丰包邮，支持验货宝验机！",
  "status": "onsale",
  "condition": "轻微划痕磨损",
  "specs": {
    "品牌": "Nintendo/任天堂",
    "型号": "Switch OLED",
    "成色": "轻微划痕磨损",
    "游戏机版本": "港版",
    "内存容量": "64GB",
    "包装": "有原包装盒"
  },
  "seller": {
    "id": "2200000000002",
    "name": "闲鱼数码达人_02",
    "url": "https://www.goofish.com/personal?userId=2200000000002",
    "city": "九江",
    "lastActive": "6小时前来过",
    "averageReplyTime": "2小时",
    "registrationDays": 1811,
    "zhimaAuth": true,
    "zhimaCredit": "卖家信用极好",
    "totalSold": 9,
    "goodReviewRate": "100%",
    "replyRate24h": "66%"
  },
  "tradeGuarantee": true,
  "stats": {
    "views": 41,
    "wants": 12,
    "favorites": 18
  },
  "detailLevel": "full"
}
```

#### Frequently Asked Questions
**Q: Do I need a Chinese phone number (+86) or Goofish account?**
No. The scraper operates entirely in Zero-Cookie Guest Mode using automated device emulation. You do not need a Chinese phone number, Alipay account, or session cookies.

**Q: Can I search using English keywords?**
Yes. Global brand names, models, and numbers (e.g. iPhone 15, Switch OLED, RTX 4090, Sony A7M4, Leica) work natively. For specialized domestic Chinese goods, searching with Chinese terms returns the highest volume of listings.

**Q: What is the advantage of filterPersonal?**
Goofish hosts both individual sellers and commercial vendors. Enabling filterPersonal filters out commercial dropshippers and shows only genuine individual users selling their personal secondhand items, which is where the best arbitrage deals are found.

**Q: What does Zhima Credit tell me about a seller?**
Zhima Credit (芝麻信用) is Alibaba's official credit rating system. Sellers with 信用极好 (Excellent Credit) have verified government identities, linked banking credentials, and an exemplary transaction track record.

---

### 🚀 Goofish (闲鱼) All-in-One: Search, Sellers & Reviews (`unitbytes/goofish-scraper`)

<p align="center">
  <a href="https://apify.com/unitbytes/goofish-scraper?fpr=939u3w&fp_sid=gh_goofish_api" target="_blank">
    <img src="https://raw.githubusercontent.com/unitbytes/.github/main/assets/banners/unitbytes-goofish-xianyu-seller-inventory-reviews-scraper-banner.jpg" alt="Goofish (闲鱼) All-in-One: Search, Sellers & Reviews" width="100%" />
  </a>
</p>

Extract Goofish & Idlefish 闲鱼 (Xianyu) product search results, seller store profiles, active & sold inventory catalogs, buyer reviews, Zhima Credit ratings, unboxing photos, and shop stats. 55% lower cost with zero compute fees and risk-free start.

- **Pricing:** `$0.001 / item` (Pay-Per-Event — `$0.001` seller review, `$0.002` search item, `$0.003` detail item, `$0.0035` seller item, `$0.004` seller profile (Gold+ tiers from `$0.00085`))
- **Cloud Console:** [https://apify.com/unitbytes/goofish-scraper?fpr=939u3w&fp_sid=gh_goofish_api](https://apify.com/unitbytes/goofish-scraper?fpr=939u3w&fp_sid=gh_goofish_api)
- **Full Documentation & Schema:** [https://unitbytes.com/actors/goofish-xianyu-seller-scraper/](https://unitbytes.com/actors/goofish-xianyu-seller-scraper/)
- **n8n Workflow File:** [`n8n/goofish-xianyu-seller-scraper-n8n-workflow.json`](n8n/goofish-xianyu-seller-scraper-n8n-workflow.json)
- **Engineering Playbook:** [How to Search & Scrape Goofish (Xianyu / 闲鱼) Without a +86 Phone Login in 2026 (API Guide)](https://unitbytes.com/blog/how-to-scrape-goofish-xianyu-secondhand-arbitrage-guide/)

#### Key Capabilities
- **Complete Active Listing Catalogs:** Extract every active item a seller has listed, including tiered pricing, descriptions, and uploaded photos.
- **Historical Sales Velocity:** Analyze sold item counts and transaction velocity to identify top-performing secondary market categories.
- **Response Rate & Engagement:** Collect seller average response times, active hours, and follower counts to gauge merchant professionalism.
- **Risk & Fraud Scoring:** Audit merchant account creation date, dispute ratios, and Zhima credit rating to identify dependable suppliers.

#### ⚙️ Input Parameters (Schema)

| Parameter | Type | Default / Prefill | Description |
| :--- | :---: | :--- | :--- |
| `mode` | `string` | `search` | Select your scraping objective: 'Product Search' to find items and pricing by keyword, 'Seller Store & Reviews' to audit merchant trust, catalogs, and buyer feedback, or 'Search + Deep Seller Audit' to search products and automatically audit top sellers. |
| `keyword` | `string` | `iPhone 15` | Enter product keyword to search on Goofish (e.g., 'iPhone 15', 'vintage camera', '羽绒服'). |
| `maxItems` | `integer` | `20` | Maximum number of search results to extract (1 to 5000). |
| `sortBy` | `string` | `newest` | Sort order for search results. |
| `priceMin` | `integer` | — | Filter search results with price greater than or equal to this amount in CNY. |
| `priceMax` | `integer` | — | Filter search results with price less than or equal to this amount in CNY. |
| `quickFilters` | `array` | — | One-click search filters provided by Goofish. |
| `regionIds` | `array` | — | Chinese administrative region/city codes (e.g., '440100' for Guangzhou, '310100' for Shanghai). |
| `startUrls` | `array` | — | Direct Goofish item URLs (e.g. 'https://www.goofish.com/item?id=1084132717206') or numeric item IDs to enrich directly. |
| `searchUrls` | `array` | — | Direct Goofish search result URLs (e.g. https://www.goofish.com/search?q=iPhone). |
| `sellerInputs` | `array` | — | Enter Goofish (闲鱼 / Xianyu) seller profile URLs (e.g. https://www.goofish.com/personal?userId=2216555697343), item listing URLs (seller is resolved automatically), fleamarket:// mobile deeplinks, or numeric seller IDs. Supports up to 100 targets per run. |
| `includeListings` | `boolean` | `True` | Extract the seller's active and historical store catalog. |
| `includeReviews` | `boolean` | `True` | Extract buyer transaction reviews, ratings, traded item context, and unboxing photos. |
| `maxListings` | `integer` | `20` | Maximum number of product listings to scrape per seller (0 to 5000). Set 0 to disable listings extraction. |
| `maxReviews` | `integer` | `30` | Maximum number of buyer reviews to scrape per seller (0 to 1000). Set 0 to disable reviews extraction. |
| `statusFilter` | `string` | `all` | Filter extracted seller items by status: 'all' (complete catalog), 'onsale' (active items), or 'sold' (historical sold items). |
| `reviewFilter` | `string` | `all` | Filter buyer reviews: 'all' (all reviews), 'with_photos' (only reviews with buyer unboxing photos), 'negative_only' (1-star complaints and disputes), or 'positive_only' (5-star praises). |
| `outputFormat` | `string` | `tabular` | Choose 'tabular' for clean, flat individual rows per product/review (best for 1-click Excel, CSV & Google Sheets exports) or 'nested' for consolidated records per seller (best for API & developer JSON pipelines). |

#### ⚡ Real-Time Synchronous Multi-Tenant Standby REST API (`<500ms` GET)

Both Goofish / Xianyu (闲鱼) engines support **instant synchronous HTTP `GET` requests** via Apify Multi-Tenant Standby Mode (`Authorization: Bearer <APIFY_API_TOKEN>`):

- ⚡ **All-in-One Standby Server:** `https://unitbytes--goofish-scraper.apify.actor` ([Console & Docs](https://apify.com/unitbytes/goofish-scraper?fpr=939u3w&fp_sid=gh_goofish_api))
- ⚡ **Search & Deals Standby Server:** `https://unitbytes--goofish-xianyu-search-scraper.apify.actor` ([Console & Docs](https://apify.com/unitbytes/goofish-xianyu-search-scraper?fpr=939u3w&fp_sid=gh_goofish_api))
- 🐍 **Runnable Python Script:** [`examples/run_goofish_standby_api.py`](examples/run_goofish_standby_api.py)

| Endpoint | Method | Query Parameters | Description |
| :--- | :---: | :--- | :--- |
| `/v1/search` | `GET` | `keyword`, `page`, `sort_by`, `min_price`, `max_price`, `detail_level` (`summary`/`full`) | Real-time Xianyu keyword search with server-side price range, condition, and sorting filters. |
| `/v1/item` | `GET` | `item_id` (or `url`) | Full secondhand listing detail, high-res image gallery, CNY price, seller card, and location. |
| `/v1/seller` | `GET` | `seller_id` (or `url`) | Seller profile, Zhima Credit (芝麻信用) grade, verification badges, sales volume, and rating summary. |
| `/v1/seller/items` | `GET` | `seller_id`, `status` (`selling`/`sold`), `page`, `detail_level` | Paginate a seller's active (`selling`) or historical (`sold`) storefront inventory. |
| `/v1/seller/reviews` | `GET` | `seller_id`, `rate_type`, `page` | Paginate verified buyer reviews, ratings, transaction timestamps, and buyer feedback tags. |

#### Python SDK Quickstart (`examples/run_goofish_xianyu_seller_scraper.py`)
```python
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "mode": "search",
    "keyword": "iPhone 15",
    "maxItems": 20,
    "sortBy": "newest",
    "includeListings": True,
    "includeReviews": True
}

run = client.actor("unitbytes/goofish-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("price"), item.get("originalPrice"))
```

#### Sample Output Schema (`samples/goofish-xianyu-seller-scraper-sample.json`)
```json
{
  "rowStatus": "ok",
  "recordType": "item",
  "id": "800000000001",
  "sellerId": "2200000000001",
  "sellerNick": "闲鱼优质卖家_01",
  "sellerCredit": "卖家信用极好",
  "city": "广东深圳",
  "title": "任天堂 Switch OLED 日版 续航增强版 白色 99新",
  "price": 1450.0,
  "originalPrice": 2199.0,
  "status": "onsale",
  "freeShipping": true,
  "url": "https://www.goofish.com/item?id=800000000001"
}
```

#### Frequently Asked Questions
**Q: Do I need a Chinese mobile number (+86) or Goofish account?**
No. The scraper operates entirely autonomously in guest mode with automated session harvesting. No login, SMS codes, or personal account credentials are required.

**Q: Can I paste an item link instead of a seller profile?**
Yes. The scraper features automatic item resolution. Paste any Goofish item link (e.g. https://www.goofish.com/item?id=...), and the actor will identify the seller and scrape their complete profile, inventory, and reviews.

**Q: What is the difference between summary and full detail level?**
Summary: Extremely fast and cost-efficient. Fetches product titles, prices, primary images, locations, and status tags.

**Q: How do I export to Excel or Google Sheets without broken columns?**
Set "outputFormat": "tabular". This produces flat, spreadsheet-ready rows where each listing or review is its own record with seller metadata attached.


---

## ⚡ Quick Installation & Local Usage

### 1. Run Interactively in Google Colab (Zero Local Setup)
Click **[Open in Google Colab ↗](https://colab.research.google.com/github/unitbytes/Goofish-Xianyu-Scraper-API/blob/main/notebooks/quickstart.ipynb)** ([`notebooks/quickstart.ipynb`](notebooks/quickstart.ipynb)) to inspect the sample output DataFrame immediately and run live extractions in your browser without installing Python locally.

### 2. Run Locally with Python (`apify-client`)
```bash
git clone https://github.com/unitbytes/Goofish-Xianyu-Scraper-API.git
cd Goofish-Xianyu-Scraper-API
pip install -r requirements.txt
export APIFY_API_TOKEN="your_apify_api_token"
python examples/run_goofish_xianyu_search_scraper.py
```

### 3. Import into n8n (Self-Hosted or Cloud)
1. Open any `.json` file inside the [`n8n/`](n8n/) folder (or copy in 1 click from **[unitbytes.com/n8n](https://unitbytes.com/n8n/)** / **[n8n.io/creators/unitbytes](https://n8n.io/creators/unitbytes/)**).
2. Press **`Ctrl+V` / `Cmd+V`** directly onto your n8n workflow canvas.
3. Configure your Apify API Token in the `HTTP Header Auth` credential on Node `2. Run UnitBytes (...)` (and customize your search inputs in Node `1. Configure Search & Rules`), then click **Test Workflow**.

### 4. Use with AI Coding Agents (Cursor, Windsurf & Claude Code MCP)
This repository includes a ready-to-use Model Context Protocol configuration at [`.cursor/mcp.json`](.cursor/mcp.json) pointing to `https://mcp.apify.com` with this suite's UnitBytes actors pre-registered. Open this folder in **Cursor** or **Windsurf** to let your AI agent run live extractions and inspect schemas automatically.

---

## 💼 Need Done-For-You Datasets or Custom Pipelines?

Don't want to manage API tokens or scripts? **UnitBytes Data Delivery** provides ready-to-use **CSV, Excel (.xlsx), Google Sheets, or Webhook feeds** tailored to your exact target keywords, cities, or categories.

- 🌐 **Request a Sample Dataset:** [https://unitbytes.com/#enterprise-intake](https://unitbytes.com/#enterprise-intake)
- 📧 **Direct Engineering Contact:** [contact@unitbytes.com](mailto:contact@unitbytes.com)
- ⚡ **Explore All 39 Scrapers:** [https://unitbytes.com/actors/](https://unitbytes.com/actors/)
- 📚 **Engineering Playbooks & Guides:** [https://unitbytes.com/blog/](https://unitbytes.com/blog/)
- 🔗 **Official n8n Creator Profile:** [https://n8n.io/creators/unitbytes/](https://n8n.io/creators/unitbytes/)
