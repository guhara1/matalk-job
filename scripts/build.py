# -*- coding: utf-8 -*-
"""통합 빌더 — 루트에 전 페이지 + sitemap/rss/robots/manifest/favicon/og 생성·미니파이."""

import os
import re
import sys
import zlib
import struct
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data import COMPANY, MAGAZINE, NOTICES, ADS
from templates import page
from ads import ad_detail
from pages_core import build_core_pages
from pages_hubs import build_hub_pages
from pages_locations import build_location_pages

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U = COMPANY["url"]

# ── 미니파이 ─────────────────────────────────────────────────
_PROTECT = re.compile(r"(<(script|style|textarea|pre)[^>]*>.*?</\2>)", re.S | re.I)

def minify_html(html):
    blocks = []
    def stash(m):
        blocks.append(m.group(1))
        return f"\x00{len(blocks)-1}\x00"
    tmp = _PROTECT.sub(stash, html)
    tmp = re.sub(r">\s+<", "><", tmp)          # 태그 사이 공백 제거
    tmp = re.sub(r"\s{2,}", " ", tmp)           # 연속 공백 축소
    tmp = re.sub(r"\n", "", tmp)
    def restore(m):
        b = blocks[int(m.group(1))]
        # script/style 내부 줄바꿈·들여쓰기 경량 압축
        if b[:7].lower().startswith("<script") or b[:6].lower().startswith("<style"):
            b = re.sub(r"\n\s*", "", b)
        return b
    return re.sub(r"\x00(\d+)\x00", restore, tmp)


# ── 파일 쓰기 ────────────────────────────────────────────────
def write_page(path, html):
    if path == "/":
        out = os.path.join(ROOT, "index.html")
    else:
        out = os.path.join(ROOT, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(minify_html(html))
    return path


# ── 정적 파일 ────────────────────────────────────────────────
def write_robots():
    body = f"""User-agent: *
Allow: /
Disallow: /api/
Disallow: /admin/

User-agent: Googlebot
Allow: /
User-agent: Googlebot-Image
Allow: /
User-agent: Googlebot-News
Allow: /
User-agent: Storebot-Google
Allow: /
User-agent: Google-Extended
Allow: /

User-agent: Yeti
Allow: /
Crawl-delay: 1
User-agent: NaverBot
Allow: /
Crawl-delay: 1

User-agent: Daum
Allow: /
User-agent: Daumoa
Allow: /
User-agent: Bingbot
Allow: /
User-agent: msnbot
Allow: /

User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Applebot
Allow: /

Sitemap: {U}/sitemap.xml
Sitemap: {U}/sitemap1.xml
Host: {COMPANY['domain']}
"""
    _w("robots.txt", body)


def _priority(path):
    if path == "/":
        return "1.0"
    if path.startswith("/locations/") and path.count("/") == 3:  # /locations/region/
        return "0.95"
    if path.startswith("/jobs/") and path != "/jobs/":
        return "0.9"
    if path.startswith("/seekers/") or path.startswith("/therapists/"):
        return "0.85"
    if path.startswith("/locations/"):
        return "0.8"
    if path.startswith("/ad/"):
        return "0.75"
    if path.startswith("/magazine/") or path.startswith("/notices/"):
        return "0.8"
    if path.startswith("/shop-sale/"):
        return "0.7"
    if path.startswith("/policy/"):
        return "0.3"
    return "0.7"


def write_sitemap(paths):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    urls = "".join(
        f"<url><loc>{U}{p}</loc><lastmod>{today}</lastmod>"
        f"<changefreq>weekly</changefreq><priority>{_priority(p)}</priority></url>"
        for p in paths)
    xml = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>'
    _w("sitemap.xml", xml)
    _w("sitemap1.xml", xml)   # 미러 백업


def write_rss():
    items = []
    def rfc822(d):
        return datetime.strptime(d, "%Y-%m-%d").replace(tzinfo=timezone.utc).strftime("%a, %d %b %Y 09:00:00 +0000")
    for m in MAGAZINE:
        items.append(f"<item><title>{_esc(m['title'])}</title><link>{U}/magazine/{m['slug']}/</link>"
                     f"<guid>{U}/magazine/{m['slug']}/</guid><pubDate>{rfc822(m['date'])}</pubDate>"
                     f"<description>{_esc(m['lead'])}</description></item>")
    for n in NOTICES:
        items.append(f"<item><title>{_esc(n['title'])}</title><link>{U}/notices/{n['slug']}/</link>"
                     f"<guid>{U}/notices/{n['slug']}/</guid><pubDate>{rfc822(n['date'])}</pubDate>"
                     f"<description>{_esc(n['lead'])}</description></item>")
    xml = (f'<?xml version="1.0" encoding="UTF-8"?>\n'
           f'<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel>'
           f'<title>{COMPANY["brand"]} 매거진·공지</title><link>{U}/</link>'
           f'<description>{COMPANY["desc"]}</description><language>ko-KR</language>'
           f'<atom:link href="{U}/rss.xml" rel="self" type="application/rss+xml"/>'
           f'{"".join(items)}</channel></rss>')
    _w("rss.xml", xml)


def write_manifest():
    body = ('{"name":"%s","short_name":"%s","start_url":"/","display":"standalone",'
            '"background_color":"#0a0e1a","theme_color":"#0a0e1a",'
            '"icons":[{"src":"/favicon.svg","sizes":"any","type":"image/svg+xml"}]}'
            % (COMPANY["brand"], COMPANY["brand"]))
    _w("site.webmanifest", body)


def write_favicon():
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
           '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
           '<stop offset="0" stop-color="#7bb0ff"/><stop offset="1" stop-color="#2c54a8"/></linearGradient></defs>'
           '<rect width="64" height="64" rx="16" fill="url(#g)"/>'
           '<text x="32" y="44" font-size="38" font-weight="900" text-anchor="middle" fill="#06122e" font-family="sans-serif">M</text></svg>')
    _w("favicon.svg", svg)


def write_og():
    """순수 파이썬 PNG 1200×630 (다크 블루) — 의존성 0."""
    W, H = 1200, 630
    bg = (10, 14, 26)
    raw = bytearray()
    for y in range(H):
        raw.append(0)  # filter type 0
        # 상단→하단 미세 그라데이션
        t = y / H
        r = int(bg[0] + (27 - bg[0]) * t * 0.4)
        g = int(bg[1] + (58 - bg[1]) * t * 0.4)
        b = int(bg[2] + (120 - bg[2]) * t * 0.4)
        raw.extend([r, g, b] * W)
    def chunk(typ, data):
        c = struct.pack(">I", len(data)) + typ + data
        return c + struct.pack(">I", zlib.crc32(typ + data) & 0xffffffff)
    ihdr = struct.pack(">IIBBBBB", W, H, 8, 2, 0, 0, 0)
    png = (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) +
           chunk(b"IDAT", zlib.compress(bytes(raw), 9)) + chunk(b"IEND", b""))
    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    with open(os.path.join(ROOT, "assets", "og.png"), "wb") as f:
        f.write(png)


def write_cf_function():
    """Cloudflare Pages Function — 광고문의 → Telegram."""
    js = r"""export async function onRequestPost({ request, env }) {
  const cors = {
    "Access-Control-Allow-Origin": env.ALLOWED_ORIGIN || "*",
    "Content-Type": "application/json",
  };
  try {
    const data = await request.json();
    // honeypot
    if (data.company_url) return new Response(JSON.stringify({ ok: true }), { headers: cors });
    const name = (data.name || "").toString().slice(0, 50);
    const phone = (data.phone || "").toString().slice(0, 30);
    const region = (data.region || "").toString().slice(0, 20);
    const grade = (data.grade || "").toString().slice(0, 20);
    const message = (data.message || "").toString().slice(0, 1000);
    if (name.length < 2 || phone.length < 7) {
      return new Response(JSON.stringify({ ok: false, error: "invalid" }), { status: 400, headers: cors });
    }
    const text = `[마톡 광고문의]\n성명: ${name}\n연락처: ${phone}\n지역: ${region}\n등급: ${grade}\n내용: ${message}`;
    const send = async (token, chat) => {
      if (!token || !chat) return;
      await fetch(`https://api.telegram.org/bot${token}/sendMessage`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ chat_id: chat, text }),
      });
    };
    await send(env.TELEGRAM_BOT_TOKEN_1, env.TELEGRAM_CHAT_ID_1);
    await send(env.TELEGRAM_BOT_TOKEN_2, env.TELEGRAM_CHAT_ID_2);
    return new Response(JSON.stringify({ ok: true }), { headers: cors });
  } catch (e) {
    return new Response(JSON.stringify({ ok: false }), { status: 500, headers: cors });
  }
}
"""
    out = os.path.join(ROOT, "functions", "api", "contact-ads.js")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(js)


def _w(name, body):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(body)

def _esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ── 메인 ─────────────────────────────────────────────────────
def main():
    all_pages = []
    all_pages += build_core_pages()
    all_pages += build_hub_pages()
    all_pages += build_location_pages()
    # 광고 상세
    for ad in ADS:
        title, desc, g, body = ad_detail(ad)
        all_pages.append((f"/ad/{ad['id']}/", page(title, desc, f"/ad/{ad['id']}/", body, g, "website")))

    paths = []
    for path, html in all_pages:
        paths.append(write_page(path, html))

    # 중복 경로 검증
    dup = {p for p in paths if paths.count(p) > 1}
    if dup:
        print("⚠️  중복 경로:", dup)

    write_robots()
    write_sitemap(sorted(set(paths)))
    write_rss()
    write_manifest()
    write_favicon()
    write_og()
    write_cf_function()

    print(f"✅ 빌드 완료: {len(paths)} HTML 페이지")
    print(f"   + robots.txt · sitemap.xml · sitemap1.xml · rss.xml · site.webmanifest · favicon.svg · assets/og.png")
    print(f"   + functions/api/contact-ads.js")


if __name__ == "__main__":
    main()
