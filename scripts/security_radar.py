#!/usr/bin/env python3
"""
security_radar.py – Daily GitHub Security Project Radar
Searches GitHub for recently-updated repos in 4 cybersecurity / AI-safety categories
and writes a Markdown report to LATEST_SECURITY_REPOS.md.

Usage:
    python scripts/security_radar.py

Environment variables (optional):
    GITHUB_TOKEN  – Personal access token to increase the API rate limit
                    (unauthenticated: 10 req/min, authenticated: 30 req/min)
    TOP_N         – How many repos to list per category (default: 30)
"""

import os
import sys
import datetime
import time

try:
    import requests
except ImportError:
    print("ERROR: 'requests' library is not installed. Run: pip install requests")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

TOP_N = int(os.environ.get("TOP_N", "30"))
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUTPUT_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           "LATEST_SECURITY_REPOS.md")

# Rolling 7-day window (calculated at run time)
DAYS_WINDOW = 7
since_date = (datetime.date.today() - datetime.timedelta(days=DAYS_WINDOW)).isoformat()

# GitHub Search API
SEARCH_URL = "https://api.github.com/search/repositories"

# ---------------------------------------------------------------------------
# Category definitions
# Each category contains a list of search queries whose results are merged
# (duplicates are removed by repo full_name).
# ---------------------------------------------------------------------------

CATEGORIES = [
    {
        "title": "🔴 网络安全渗透 / 红队 (Penetration Testing / Red Team)",
        "queries": [
            f"penetration testing pushed:>{since_date} stars:>50 archived:false",
            f"pentest pushed:>{since_date} stars:>50 archived:false",
            f"渗透测试 pushed:>{since_date} stars:>20 archived:false",
            f'"red team" pushed:>{since_date} stars:>50 archived:false',
            f"红队 pushed:>{since_date} stars:>20 archived:false",
        ],
    },
    {
        "title": "🛠️ 网络安全工具 (Security Tools / Scanner / Recon / Exploit)",
        "queries": [
            f'"security tool" pushed:>{since_date} stars:>50 archived:false',
            f"vulnerability scanner pushed:>{since_date} stars:>50 archived:false",
            f"recon tool pushed:>{since_date} stars:>50 archived:false",
            f"信息收集 pushed:>{since_date} stars:>20 archived:false",
            f"exploit framework pushed:>{since_date} stars:>50 archived:false",
            f'"awesome security" pushed:>{since_date} stars:>100 archived:false',
        ],
    },
    {
        "title": "🤖 大模型安全 (LLM Security / Prompt Injection / Guardrails)",
        "queries": [
            f'"LLM security" pushed:>{since_date} stars:>10 archived:false',
            f"大模型安全 pushed:>{since_date} stars:>5 archived:false",
            f'"prompt injection" pushed:>{since_date} stars:>10 archived:false',
            f"提示注入 pushed:>{since_date} stars:>5 archived:false",
            f"guardrails LLM pushed:>{since_date} stars:>10 archived:false",
            f'"AI safety" pushed:>{since_date} stars:>20 archived:false',
            f'"red teaming" LLM pushed:>{since_date} stars:>10 archived:false',
        ],
    },
    {
        "title": "🔓 大模型越狱 (Jailbreak / Prompt Hacking)",
        "queries": [
            f"jailbreak LLM pushed:>{since_date} stars:>10 archived:false",
            f"越狱 LLM pushed:>{since_date} stars:>5 archived:false",
            f'"jailbreak prompts" pushed:>{since_date} stars:>10 archived:false',
            f'"prompt hacking" pushed:>{since_date} stars:>10 archived:false',
            f"提示越狱 pushed:>{since_date} stars:>5 archived:false",
        ],
    },
]

# ---------------------------------------------------------------------------
# GitHub API helpers
# ---------------------------------------------------------------------------

def make_session() -> requests.Session:
    session = requests.Session()
    session.headers.update({
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    })
    if GITHUB_TOKEN:
        session.headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return session


def search_repos(session: requests.Session, query: str, per_page: int = 100):
    """
    Run a GitHub repository search and return a list of repo dicts.
    Handles rate-limit responses gracefully.
    Returns None on unrecoverable errors (network, HTTP error), or a list
    (possibly empty) on success.
    """
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": per_page,
        "page": 1,
    }

    try:
        resp = session.get(SEARCH_URL, params=params, timeout=30)
    except requests.RequestException as exc:
        print(f"  [WARN] Network error for query '{query}': {exc}")
        return None

    if resp.status_code == 403:
        # Rate-limited
        reset_ts = int(resp.headers.get("X-RateLimit-Reset", 0))
        wait = max(reset_ts - int(time.time()), 0) + 2
        print(f"  [WARN] Rate-limited. Waiting {wait}s before retry …")
        time.sleep(wait)
        try:
            resp = session.get(SEARCH_URL, params=params, timeout=30)
        except requests.RequestException as exc:
            print(f"  [WARN] Network error on retry for query '{query}': {exc}")
            return None

    if resp.status_code == 422:
        print(f"  [WARN] Query rejected (422) for: {query}")
        return None

    if not resp.ok:
        print(f"  [WARN] HTTP {resp.status_code} for query '{query}': {resp.text[:200]}")
        return None

    data = resp.json()
    items = data.get("items", [])
    print(f"  [OK] {len(items)} results for: {query}")
    # Small polite delay to stay within secondary rate limits
    time.sleep(1)
    return items


def collect_category(session: requests.Session, category: dict) -> list:
    """Fetch repos for all queries in a category, deduplicate, and return top-N by stars."""
    seen: dict = {}
    errors: list = []

    for query in category["queries"]:
        items = search_repos(session, query)
        if items is None:
            errors.append(query)
            continue
        for item in items:
            full_name = item.get("full_name", "")
            if full_name and full_name not in seen:
                seen[full_name] = item

    repos = sorted(seen.values(), key=lambda r: r.get("stargazers_count", 0), reverse=True)
    return repos[:TOP_N], errors


# ---------------------------------------------------------------------------
# Markdown rendering
# ---------------------------------------------------------------------------

def fmt_date(iso_str: str) -> str:
    if not iso_str:
        return "—"
    # e.g. "2026-04-28T12:34:56Z" → "2026-04-28"
    return iso_str[:10]


def render_repo_table(repos: list) -> str:
    if not repos:
        return "_本周期内暂无符合条件的仓库。_\n"

    lines = [
        "| # | 仓库 | 描述 | ⭐ Stars | 语言 | 最近推送 |",
        "|---|------|------|---------|------|---------|",
    ]
    for i, repo in enumerate(repos, 1):
        name = repo.get("full_name", "")
        url = repo.get("html_url", "#")
        desc = (repo.get("description") or "").replace("|", "\\|").strip()
        if len(desc) > 80:
            desc = desc[:77] + "…"
        stars = repo.get("stargazers_count", 0)
        lang = repo.get("language") or "—"
        pushed = fmt_date(repo.get("pushed_at", ""))
        lines.append(f"| {i} | [{name}]({url}) | {desc} | {stars:,} | {lang} | {pushed} |")
    return "\n".join(lines) + "\n"


def render_report(results: list) -> str:
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    today = datetime.date.today().isoformat()
    window_start = (datetime.date.today() - datetime.timedelta(days=DAYS_WINDOW)).isoformat()

    lines = [
        "# 🛡️ 每日网络安全项目库雷达",
        "",
        f"> **报告生成时间**：{now}  ",
        f"> **数据窗口**：{window_start} ~ {today}（最近 {DAYS_WINDOW} 天有推送的仓库）  ",
        f"> **每类展示**：Top {TOP_N}  ",
        f"> **数据来源**：[GitHub Search API](https://docs.github.com/en/rest/search/search)  ",
        "",
        "---",
        "",
    ]

    for category_title, repos, errors in results:
        lines += [
            f"## {category_title}",
            "",
        ]
        if errors:
            lines += [
                f"> ⚠️ 以下查询未能完成，结果可能不完整：",
                "> " + "、".join(errors),
                "",
            ]
        lines.append(render_repo_table(repos))
        lines.append("")

    lines += [
        "---",
        "",
        "_由 [security_radar.py](scripts/security_radar.py) 自动生成 · "
        "[查看 Workflow](.github/workflows/security-radar.yml)_",
        "",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print(f"Security Radar – collecting repos updated since {since_date}")
    print(f"Output: {OUTPUT_FILE}")
    if GITHUB_TOKEN:
        print("GitHub token: present (higher rate limit)")
    else:
        print("GitHub token: NOT set – unauthenticated (10 req/min limit applies)")

    session = make_session()
    results = []

    for category in CATEGORIES:
        print(f"\n[Category] {category['title']}")
        repos, errors = collect_category(session, category)
        print(f"  → {len(repos)} unique repos collected")
        results.append((category["title"], repos, errors))

    report = render_report(results)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        fh.write(report)

    print(f"\n✅ Report written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
