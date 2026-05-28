# -*- coding: utf-8 -*-
"""광고 시스템: 등급별 카드 렌더 · 필터 · 상세페이지."""

from data import ADS, COMPANY
from templates import U, jsonld, breadcrumb, faq_node, faq_html

TIER_LABEL = {"vvip": "VVIP", "vip": "VIP", "premium": "프리미엄"}

_GLYPH = {"vvip": "★ ", "vip": "◆ ", "premium": ""}

def _card(ad, rank=None):
    t = ad["tier"]
    badge = f'<span class="ad-badge b-{t}">{_GLYPH[t]}{TIER_LABEL[t]}</span>'
    ranknum = f'<span class="ad-rank">{rank:02d}</span>' if (rank and t == "vvip") else ""
    verify = '<div class="ad-verify">인증 업체</div>' if t in ("vvip", "vip") else ""
    return f"""<a class="ad-card ad-{t} cv" href="/ad/{ad['id']}/">
<span class="ad-shine"></span><span class="ad-disclosure">AD</span>
<div class="ad-top">{badge}{ranknum}</div>{verify}
<h3 class="ad-shop">{ad['shop']}</h3>
<p class="ad-title">{ad['title']}</p>
<div class="ad-wage">일급 {ad['wage']}만원~</div>
<div class="ad-meta">{ad['region']} {ad['district']} · {ad['industry']} · {ad['contract']}</div>
<div class="ad-cta">지원하기 <i>→</i></div>
</a>"""

def render_tier(tier, region=None, industry=None, limit=None, heading=True):
    items = [a for a in ADS if a["tier"] == tier]
    if region:
        pref = [a for a in items if a["region"] == region]
        items = pref + [a for a in items if a not in pref]   # backfill
    if industry:
        pref = [a for a in items if a["industry"] == industry]
        items = pref + [a for a in items if a not in pref]
    if limit:
        items = items[:limit]
    if not items:
        return ""
    cards = "".join(_card(a, i + 1) for i, a in enumerate(items))
    head = {"vvip": ("VVIP 추천 채용", "프리미엄 인증 업체 우선 노출"),
            "vip": ("VIP 채용공고", "검증된 추천 업체"),
            "premium": ("프리미엄 채용공고", "선등록순 노출")}[tier]
    h = (f'<div class="ad-zone"><div><div class="kicker">{head[1]}</div>'
         f'<h2 style="margin:6px 0 0">{head[0]}</h2></div>'
         f'<span class="ad-zone-label">광고</span></div>'
         if heading else "")
    return f'<section class="section reveal">{h}<div class="ad-grid-{tier}">{cards}</div></section>'

def jobposting_node(ad):
    return {"@type": "JobPosting", "title": ad["title"],
            "description": f"{ad['region']} {ad['district']} {ad['shop']}에서 {ad['industry']} 마사지 관리사를 모집합니다. 일급 {ad['wage']}만원, 근무시간 {ad['hours']}, {ad['contract']}.",
            "datePosted": "2026-05-01", "validThrough": "2026-12-31",
            "employmentType": "FULL_TIME" if "정규" in ad["contract"] else "PART_TIME",
            "hiringOrganization": {"@type": "Organization", "name": ad["shop"]},
            "jobLocation": {"@type": "Place", "address": {"@type": "PostalAddress",
                "addressRegion": ad["region"], "addressLocality": ad["district"], "addressCountry": "KR"}},
            "baseSalary": {"@type": "MonetaryAmount", "currency": "KRW",
                "value": {"@type": "QuantitativeValue", "value": ad["wage"] * 10000, "unitText": "DAY"}},
            "industry": "마사지·테라피"}

def ad_detail(ad):
    faqs = [
        ("지원은 어떻게 하나요?", f"본 페이지 하단 지원 안내의 이메일({COMPANY['email']})로 이력을 보내시거나, {COMPANY['brand']} 매칭 신청을 통해 연결됩니다. 전화 직접 연결은 제공하지 않습니다."),
        ("경력이 없어도 지원할 수 있나요?", f"{ad['shop']}은 신입 교육 과정을 운영하는 경우가 많습니다. 적성·체력 요건을 확인 후 수습 기간을 거쳐 정착할 수 있습니다."),
        ("일급 정산은 어떻게 되나요?", f"{ad['settle']} 방식입니다. 계약 시 정산 주기와 공제 항목을 근로계약서로 확인하시기 바랍니다."),
        ("근무 시간을 조정할 수 있나요?", f"공고상 근무시간은 {ad['hours']}이며, 파트타임·시간 협의가 가능한지는 채용 담당자와 상담으로 확정합니다."),
        ("숙소나 식대가 제공되나요?", "지역·업체에 따라 숙소·식대·교통비 지원이 다릅니다. 상세 조건은 지원 후 안내됩니다."),
    ]
    g = [{"@type": "WebPage", "name": ad["title"], "url": U + f"/ad/{ad['id']}/"},
         jobposting_node(ad), faq_node(faqs),
         breadcrumb([("홈", "/"), ("구인공고", "/jobs/"),
                     (f"{ad['industry']} 마사지", f"/jobs/{_ind_slug(ad['industry'])}/"),
                     (ad["shop"], f"/ad/{ad['id']}/")])]
    body = f"""<div class="wrap" style="padding-top:60px;display:grid;grid-template-columns:1.6fr 1fr;gap:40px;max-width:1100px">
<div>
<div class="breadcrumb"><a href="/">홈</a> › <a href="/jobs/">구인공고</a> › {ad['shop']}</div>
<span class="ad-badge b-{ad['tier']}">{TIER_LABEL[ad['tier']]}</span>
<h1 style="font-size:clamp(28px,4vw,40px);margin:10px 0 6px">{ad['title']}</h1>
<p class="lead">{ad['region']} {ad['district']} · {ad['shop']}</p>

<h2 style="font-size:24px;margin-top:40px">모집 안내</h2>
<p class="note-text" style="margin-top:10px">{ad['shop']}은 {ad['region']} {ad['district']} 권역에서 운영 중인 {ad['industry']} 전문 로드샵입니다. 안정적인 단골 고객층을 기반으로 함께 성장할 {ad['industry']} 마사지 관리사 {ad['people']}명을 모집합니다. 신입과 경력 모두 지원 가능하며, 검증된 교육 체계와 투명한 정산으로 장기 근속을 지향합니다.</p>

<h2 style="font-size:24px;margin-top:36px">근무 혜택</h2>
<ul style="color:var(--muted);margin:12px 0 0 18px;line-height:2">
<li>업계 상위 수준의 일급({ad['wage']}만원~)과 {ad['settle']}</li>
<li>신입 대상 단계별 실무 교육 및 멘토링</li>
<li>휴게 공간·청결한 근무 환경 제공</li>
<li>장기 근속자 인센티브 및 휴무 협의</li>
</ul>

<h2 style="font-size:24px;margin-top:36px">우대 사항</h2>
<ul style="color:var(--muted);margin:12px 0 0 18px;line-height:2">
<li>{ad['industry']} 또는 유사 업종 경력자</li>
<li>장기 근무가 가능한 분, 단골 응대에 강점이 있는 분</li>
<li>성실한 출퇴근과 책임감 있는 근무 태도</li>
</ul>

<h2 style="font-size:24px;margin-top:36px">지원 절차</h2>
<div class="grid g2" style="margin-top:14px">
<div class="card"><b>01 매칭 신청</b><p style="margin-top:6px">아래 이메일로 희망 조건을 보내거나 매칭을 신청합니다.</p></div>
<div class="card"><b>02 조건 확인</b><p style="margin-top:6px">일급·정산·근무시간 등 핵심 조건을 사전 조율합니다.</p></div>
<div class="card"><b>03 면접·체험</b><p style="margin-top:6px">샵 방문 면접과 필요 시 체험 근무를 진행합니다.</p></div>
<div class="card"><b>04 계약·출근</b><p style="margin-top:6px">근로계약서 작성 후 정식 근무를 시작합니다.</p></div>
</div>

<h2 id="apply" style="font-size:24px;margin-top:40px">지원하기</h2>
<div class="linkbox"><p>지원 문의는 이메일로 받습니다. 전화 직접 연결은 제공하지 않습니다.</p>
<a href="mailto:{COMPANY['email']}?subject=[지원] {ad['shop']} {ad['title']}">{COMPANY['email']} 로 지원 →</a></div>

<h2 style="font-size:24px;margin-top:30px">자주 묻는 질문</h2>
{faq_html(faqs)}
</div>

<aside><div class="card" style="position:sticky;top:90px">
<div class="kicker">채용 요약</div>
<div class="ad-wage" style="font-size:30px;margin:8px 0 16px">일급 {ad['wage']}만원~</div>
<table style="width:100%;font-size:14px;color:var(--muted);line-height:2.2">
<tr><td class="dim">샵</td><td style="text-align:right">{ad['shop']}</td></tr>
<tr><td class="dim">지역</td><td style="text-align:right">{ad['region']} {ad['district']}</td></tr>
<tr><td class="dim">업종</td><td style="text-align:right">{ad['industry']}</td></tr>
<tr><td class="dim">근무시간</td><td style="text-align:right">{ad['hours']}</td></tr>
<tr><td class="dim">모집인원</td><td style="text-align:right">{ad['people']}명</td></tr>
<tr><td class="dim">계약형태</td><td style="text-align:right">{ad['contract']}</td></tr>
<tr><td class="dim">정산</td><td style="text-align:right">{ad['settle']}</td></tr>
</table>
<a href="#apply" class="btn btn-grad" style="width:100%;justify-content:center;margin-top:18px">지원하기</a>
</div></aside>
</div>
<section class="section reveal"><h2 style="font-size:24px">같은 업종 채용공고</h2>
{render_tier(ad['tier'], industry=ad['industry'], limit=4, heading=False)}</section>"""
    title = f"[{ad['shop']}] {ad['title']} · {ad['region']} {ad['district']} | {COMPANY['brand']}"
    desc = f"{ad['region']} {ad['district']} {ad['shop']} {ad['industry']} 마사지 관리사 모집. 일급 {ad['wage']}만원, {ad['hours']}, {ad['contract']}. 모집 {ad['people']}명. {COMPANY['brand']}에서 안전하게 지원하세요."
    return title, desc, g, body

def _ind_slug(name):
    from data import INDUSTRIES
    for i in INDUSTRIES:
        if i["name"] == name:
            return i["slug"]
    return "swedish"
