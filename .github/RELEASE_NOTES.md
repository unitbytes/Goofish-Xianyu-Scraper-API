### 🚀 v1.1.0 Release Notes — 🐟 Goofish & Xianyu (闲鱼) Scraper + Real-Time Standby REST API Suite (`$1 / 1K`)

The fastest cookieless Goofish / Xianyu (闲鱼) China secondhand marketplace scraper and sub-second Multi-Tenant Standby REST API suite on Apify (`$1.00–$2.00 / 1,000 items`). Extract live secondhand deals, seller storefronts, Zhima Credit (芝麻信用) trust badges, seller inventory catalogs, and verified buyer reviews.

- 📓 **1-Click Interactive Google Colab Notebook:** [**Open `notebooks/quickstart.ipynb` in Colab**](https://colab.research.google.com/github/unitbytes/Goofish-Xianyu-Scraper-API/blob/main/notebooks/quickstart.ipynb)
- 🤖 **AI Coding Agent MCP Ready:** Includes `.cursor/mcp.json` for Cursor, Windsurf, and Claude Code.
- 🔧 **9-Node n8n Automation Workflows:** Ready-to-import `.json` templates under `n8n/` and at **[unitbytes.com/n8n](https://unitbytes.com/n8n/)**.

## 🛠️ Included Extraction Engines & SDK Quickstarts

| Extraction Engine | Pricing (PPE) | Python SDK & n8n Template | Cloud Console & Docs |
| :--- | :---: | :--- | :---: |
| **Goofish (Xianyu / 闲鱼) Scraper: Fast Search & Deals** | `$0.002 / item` | [`examples/run_goofish_xianyu_search_scraper.py`](https://github.com/unitbytes/Goofish-Xianyu-Scraper-API/blob/main/examples/run_goofish_xianyu_search_scraper.py) · [`n8n/goofish-xianyu-search-scraper-n8n-workflow.json`](https://github.com/unitbytes/Goofish-Xianyu-Scraper-API/blob/main/n8n/goofish-xianyu-search-scraper-n8n-workflow.json) | [⚡ **Run on Apify**](https://apify.com/unitbytes/goofish-xianyu-search-scraper?fpr=939u3w&fp_sid=gh_goofish_api_rel) · [Schema](https://unitbytes.com/actors/goofish-xianyu-search-scraper/) |
| **Goofish (闲鱼) All-in-One: Search, Sellers & Reviews** | `$0.001 / item` | [`examples/run_goofish_xianyu_seller_scraper.py`](https://github.com/unitbytes/Goofish-Xianyu-Scraper-API/blob/main/examples/run_goofish_xianyu_seller_scraper.py) · [`n8n/goofish-xianyu-seller-scraper-n8n-workflow.json`](https://github.com/unitbytes/Goofish-Xianyu-Scraper-API/blob/main/n8n/goofish-xianyu-seller-scraper-n8n-workflow.json) | [⚡ **Run on Apify**](https://apify.com/unitbytes/goofish-scraper?fpr=939u3w&fp_sid=gh_goofish_api_rel) · [Schema](https://unitbytes.com/actors/goofish-xianyu-seller-scraper/) |

## ⚡ Pre-Configured 1-Click Task Presets

| Task Preset | Target Use Case | Direct Cloud Launch |
| :--- | :--- | :---: |
| **Find Used iPhones & Refurbished Apple Deals on Goofish (闲鱼)** | Extract iPhone 15, 14, and 13 listings on Goofish. Filter by price, seller Zhima credit, battery health specs, and clean plain-text descriptions. | [⚡ Run Task Preset](https://apify.com/unitbytes/goofish-xianyu-search-scraper/examples/goofish-iphone-used-phones?fpr=939u3w&fp_sid=gh_goofish_api_rel) |
| **Track Nintendo Switch OLED & Japanese Console Deals on Goofish** | Monitor Nintendo Switch OLED, PS5, and retro handhelds on Goofish. Extract Japanese import editions, bundled games, condition, and seller ratings. | [⚡ Run Task Preset](https://apify.com/unitbytes/goofish-xianyu-search-scraper/examples/goofish-nintendo-switch-consoles?fpr=939u3w&fp_sid=gh_goofish_api_rel) |
| **Source Anime Figures, Bandai & Pop Mart Collectibles on Goofish** | Search rare anime figures, garage kits, Pop Mart blind boxes, and authentic Japanese collectibles on Goofish. Get HD photo galleries and seller feedback. | [⚡ Run Task Preset](https://apify.com/unitbytes/goofish-xianyu-search-scraper/examples/goofish-anime-figures-collectibles?fpr=939u3w&fp_sid=gh_goofish_api_rel) |
| **Monitor RTX 4090, 4080 & Used Graphics Cards on Goofish** | Track secondary market prices for NVIDIA GeForce RTX 4090, 4080, and 3080 GPUs on Goofish. Detect price drops and vet seller transaction history. | [⚡ Run Task Preset](https://apify.com/unitbytes/goofish-xianyu-search-scraper/examples/goofish-graphics-cards-gpu?fpr=939u3w&fp_sid=gh_goofish_api_rel) |
| **Audit Seller Sold History & Clearing Prices on Goofish (闲鱼)** | Extract complete historical sold listings from any Goofish 闲鱼 (Xianyu / Idlefish) seller to analyze sales velocity, real clearing prices, turnover rate, and historical discount margins. | [⚡ Run Task Preset](https://apify.com/unitbytes/goofish-scraper/examples/audit-seller-sold-history-pricing?fpr=939u3w&fp_sid=gh_goofish_api_rel) |
| **Export Active Seller Product Catalog from Goofish (闲鱼)** | Scrape all currently active, on-sale product listings from any Goofish 闲鱼 (Xianyu / Idlefish) seller profile with prices, high-res photos, tags, and direct item links. | [⚡ Run Task Preset](https://apify.com/unitbytes/goofish-scraper/examples/export-active-seller-catalog?fpr=939u3w&fp_sid=gh_goofish_api_rel) |
| **Deep Goofish Seller Catalog & Spec Enrichment** | Deeply enrich Goofish seller listings with full plain-text descriptions, condition ratings, view/want statistics, seller location, and structured specifications dictionaries. | [⚡ Run Task Preset](https://apify.com/unitbytes/goofish-scraper/examples/deep-seller-catalog-specs-enrichment?fpr=939u3w&fp_sid=gh_goofish_api_rel) |
| **Seller Credibility, Trust & Zhima Credit Background Check** | Perform instant seller credibility background checks on Goofish (闲鱼 / Idlefish). Extract Zhima credit ratings, real-name verification badges, follower counts, and account age. | [⚡ Run Task Preset](https://apify.com/unitbytes/goofish-scraper/examples/seller-trust-and-zhima-credit-check?fpr=939u3w&fp_sid=gh_goofish_api_rel) |

---

### 🛡️ Core Engineering Guarantees
- **Zero Login or Cookies Required:** Operates 100% anonymously without personal accounts or session tokens.
- **Clean Flat Schemas:** Export directly to Excel, CSV, Google Sheets, Pandas, or AI agents with zero `[object Object]` nesting errors.
- **Permanent Media CDNs:** High-resolution image and video links that never expire or return 403 Forbidden.
- **Enterprise Support & Custom Feeds:** [contact@unitbytes.com](mailto:contact@unitbytes.com) • [https://unitbytes.com](https://unitbytes.com)
