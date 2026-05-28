# -*- coding: utf-8 -*-
"""지역 페이지: 광역 4 + 행정구 82."""

from data import REGIONS, INDUSTRIES, COMPANY, all_districts
from district_profiles import get_profile
from templates import (U, page, jsonld, breadcrumb, faq_node, faq_html,
                       org_node, website_node)
from ads import render_tier

# 광역별 고유 SEO 콘텐츠
REGION_SEO = {
 "seoul": ("강남·강북 단가 격차가 뚜렷한 시장",
   "서울은 강남·서초·송파의 프리미엄 권역과 강북·도심 생활 권역으로 단가가 양분된다. 강남권 프리미엄 아로마는 일급 상한이 가장 높고, 강북·외곽은 합리적 가격대로 신입 입직이 활발하다."),
 "gyeonggi": ("1기·2기 신도시별 수요 구조가 다른 시장",
   "경기는 분당·평촌 등 1기 신도시의 성숙 상권과 동탄·운정·다산 등 2기 신도시의 성장 상권이 공존한다. 판교권은 IT 고소득 수요, 산단 권역은 근육 회복 수요가 강하다."),
 "incheon": ("송도·청라 신도시와 원도심이 공존하는 시장",
   "인천은 송도·청라·검단 신도시의 프리미엄·성장 수요와 부평·남동 원도심의 안정 수요가 구분된다. 송도는 외국인 거주층 대응 역량이 차별화 포인트다."),
 "busan": ("해운대·서면 양대 축의 관광·번화가 시장",
   "부산은 해운대 프리미엄 관광 권역과 서면 최대 번화가가 양대 축이다. 관광 수요 비중이 높아 주말·야간 예약 대응 역량이 수입을 좌우한다."),
}

def region_hub(region):
    rs, rn = region["slug"], region["name"]
    dists = region["districts"]
    seo_title, seo_body = REGION_SEO.get(rs, (f"{rn} 마사지 채용 시장", ""))
    dcards = "".join(
        f'<a class="card cv" href="/locations/{rs}/{ds}/"><h3>{dn}</h3>'
        f'<p style="font-size:13px;margin-top:6px">{get_profile(ds, dn)["land"]}</p>'
        f'<p style="font-size:13px;color:var(--blue-1);margin-top:8px">강세 {get_profile(ds, dn)["svc"]} →</p></a>'
        for ds, dn in dists)

    faqs = [
        (f"{rn}에서 마사지 관리사 일급은 보통 얼마인가요?",
         f"{rn}의 평균 일급은 권역과 업종에 따라 14만~24만원 선에서 형성됩니다. 프리미엄 상권일수록 상한이 높고, 생활 상권은 신입 입직에 적합한 합리적 수준입니다."),
        (f"{rn}에서 신입도 취업할 수 있나요?",
         f"네. {rn}에는 신입 교육 과정을 운영하는 로드샵이 많습니다. 적성과 체력 요건을 확인한 뒤 수습 기간을 거쳐 정착하는 구조가 일반적입니다."),
        (f"{rn} 어느 지역이 채용이 활발한가요?",
         f"{rn}는 {dists[0][1]}·{dists[1][1]} 등 상권 밀집 권역의 채용 공고가 가장 많습니다. 행정구별 페이지에서 구체적인 시세와 수요를 확인할 수 있습니다."),
        ("야간 근무 비중이 높은가요?",
         "권역에 따라 다릅니다. 번화가·관광 상권은 야간 예약 비중이 높고, 주거·학원가 상권은 주간 예약 비중이 높습니다."),
        ("로드샵과 출장 중 어느 쪽이 많나요?",
         f"{COMPANY['brand']}는 합법 로드샵 채용 정보만 게재합니다. 안전한 근무 환경의 로드샵 공고를 중심으로 매칭합니다."),
    ]
    g = [
        {"@type": "CollectionPage", "name": f"{rn} 마사지 구인구직", "url": U + f"/locations/{rs}/"},
        {"@type": "Place", "name": region["full"], "address": {"@type": "PostalAddress", "addressRegion": rn, "addressCountry": "KR"}},
        {"@type": "Article", "headline": seo_title, "author": {"@type": "Organization", "name": COMPANY["brand"]},
         "datePublished": "2026-01-05", "dateModified": "2026-05-01"},
        faq_node(faqs),
        breadcrumb([("홈", "/"), ("지역", "/locations/"), (rn, f"/locations/{rs}/")]),
    ]
    body = f"""<section class="hero"><div class="hero-grid reveal">
<div class="kicker">{rn} 마사지 구인구직</div>
<h1>{rn} 마사지 관리사<br><span class="grad-text">채용 정보</span></h1>
<p class="lead" style="margin-top:18px">{region['full']} {len(dists)}개 행정구의 로드샵 채용·일급 시세·매칭 사례를 한곳에서 확인하세요.</p>
<div class="chips"><span class="chip"><b>{len(dists)}</b> 행정구</span>
<span class="chip">공고 <b>매일 갱신</b></span><span class="chip">평균 매칭 <b>47시간</b></span></div>
</div></section>

{render_tier('vvip', region=rn, limit=4)}

<section class="section reveal"><div class="kicker">행정구별 채용</div>
<h2 style="margin:6px 0 22px">{rn} 행정구를 선택하세요</h2>
<div class="grid g4">{dcards}</div></section>

{render_tier('vip', region=rn, limit=6)}

<section class="section reveal" style="max-width:760px">
<div class="kicker">{rn} 채용 시장 분석</div>
<h2 style="margin:6px 0 16px">{seo_title}</h2>
<p class="note-text">{seo_body}</p>

<h3 style="margin-top:30px">권역별 일급 시세</h3>
<p class="note-text" style="margin-top:8px">{rn}의 일급은 상권 등급에 따라 단계적으로 형성됩니다. 프리미엄 권역은 객단가가 높아 일급 상한이 크고, 생활·학원가 상권은 안정적인 주간 수요로 균형 잡힌 근무가 가능합니다. 신입은 생활 상권에서 경험을 쌓은 뒤 프리미엄 권역으로 이동하는 경로가 일반적입니다.</p>

<h3 style="margin-top:30px">알바·파트 근무 3가지 패턴</h3>
<p class="note-text" style="margin-top:8px">첫째, 주간 파트는 학원가·주거 상권 중심으로 가정과 병행하기 좋습니다. 둘째, 저녁 풀타임은 오피스 상권에서 직장인 단골을 확보하는 형태입니다. 셋째, 주말 집중 근무는 관광·번화가 상권에서 높은 회전율로 단기 수입을 노리는 패턴입니다.</p>

<h3 style="margin-top:30px">2026 {rn} 채용 트렌드</h3>
<p class="note-text" style="margin-top:8px">신도시·재개발 지역을 중심으로 신규 오픈 매장이 늘고 있어 초기 멤버 채용 수요가 증가하는 추세입니다. 동시에 안전한 합법 로드샵에 대한 선호가 강해지면서, 투명한 정산과 명확한 근로계약을 제시하는 업체로 지원자가 몰리고 있습니다.</p>

<h3 style="margin-top:30px">{rn} 신규 입직 가이드</h3>
<p class="note-text" style="margin-top:8px">처음 시작한다면 거주지 접근성, 정산 방식, 교육 체계, 안전 환경 네 가지를 우선 확인하세요. {COMPANY['brand']}는 합법 신고 업체의 공고만 게재하며, 매칭 단계에서 핵심 조건을 사전 조율해 안전한 입직을 돕습니다.</p>
</section>

<section class="section reveal"><h2 style="font-size:26px">{rn} 채용 자주 묻는 질문</h2>{faq_html(faqs)}</section>

{render_tier('premium', region=rn, limit=8)}

<div class="linkbox" style="max-width:1100px;margin:40px auto"><h3>{rn} 함께 보면 좋은 정보</h3>
<a href="/jobs/">업종별 마사지 구인공고 전체 보기</a>
<a href="/pricing/">2026 마사지 관리사 급여 시세표</a>
<a href="/magazine/salary-guide-2026/">급여 시세 완전정리 매거진</a>
<a href="/reviews/">{rn} 포함 전국 매칭 사례 보기</a></div>"""

    title = f"{rn} 마사지 구인구직 — {len(dists)}개 행정구 채용 정보 | {COMPANY['brand']}"
    desc = f"{region['full']} {len(dists)}개 행정구 마사지 관리사 구인구직. 권역별 일급 시세·로드샵 채용·매칭 사례 수록. {seo_title}. {COMPANY['brand']} 합법 채용 플랫폼."
    return ("/locations/%s/" % rs, page(title, desc, "/locations/%s/" % rs, body, g, "website"))


def district_page(region, ds, dn):
    rs, rn = region["slug"], region["name"]
    pf = get_profile(ds, dn)
    v = pf["v"]
    svc = pf["svc"]
    # 강세 업종 순으로 시세 정렬
    inds = sorted(INDUSTRIES, key=lambda i: (i["name"] != svc, -i["wage"]))

    # v변형: 섹션 제목 분기
    titles = [
        ("권역 한눈에", "필드 노트", "업종별 일급 시세"),
        ("동네 상권 브리핑", "현장 관찰 노트", "업종별 시세 분석"),
        ("권역 채용 개요", "운영팀 코멘트", "강세 업종 시세"),
        ("상권 데이터", "현장 데이터 노트", "일급 시세 가이드"),
    ][v]

    wage_rows = "".join(
        f'<tr><td>{i["name"]}</td><td style="text-align:right;color:var(--blue-1);font-weight:700">{i["wage_lo"]}~{i["wage_hi"]}만원</td>'
        f'<td style="text-align:right;color:var(--muted)">{"강세" if i["name"]==svc else "보통"}</td></tr>'
        for i in inds)

    faqs = [
        (f"{rn} {dn}의 주요 고객층은 누구인가요?",
         f"{dn}의 핵심 고객층은 {pf['customer']}입니다. {pf['land']} 일대를 중심으로 수요가 형성됩니다."),
        (f"{dn}에서 어떤 업종이 강세인가요?",
         f"{dn}는 {svc} 마사지 수요가 가장 두텁습니다. {pf['market']}"),
        (f"{dn} 교통은 어떤가요?",
         f"{dn}는 {pf['metro']} 등으로 접근할 수 있습니다. 교통 거점 인접 로드샵일수록 유동 수요가 많습니다."),
        (f"{dn}는 야간 근무 비중이 높나요?",
         f"{dn}는 고객층 특성상 {'야간 예약 비중이 있는' if any(k in pf['customer'] for k in ['관광','상인','젊은']) else '주간·저녁 예약이 균형 잡힌'} 권역입니다. 매장별로 영업 시간이 다르니 공고에서 확인하세요."),
        (f"{dn}에 로드샵이 많은가요?",
         f"{pf['land']} 권역을 중심으로 로드샵이 분포합니다. {pf['strategy']}"),
        (f"신입도 {dn}에서 시작할 수 있나요?",
         f"네. {dn}에는 신입 교육을 운영하는 업체가 있습니다. 적성·체력을 확인한 뒤 수습을 거쳐 정착하는 구조입니다."),
    ]
    reviews = [
        (f"{dn} {svc} 입직 3개월차", f"{pf['land']} 근처 로드샵에서 일하고 있어요. {pf['customer']} 단골이 늘면서 수입이 안정됐습니다."),
        (f"{dn} 경력 이직 후기", f"{pf['metro']} 접근성이 좋아 출퇴근이 편합니다. 정산이 투명해 만족스러워요."),
        (f"{dn} 신입 정착기", f"처음엔 걱정했는데 교육을 받으며 적응했어요. {svc} 위주로 경험을 쌓고 있습니다."),
        (f"{dn} 단골 응대 후기", f"{pf['customer']} 고객이 많아 재방문 관리가 중요했어요. 꾸준히 하니 단골이 생겼습니다."),
        (f"{dn} 파트 근무 후기", "원하는 시간대로 근무 조율이 가능해 가정과 병행하기 좋았습니다."),
        (f"{dn} 장기 근속 후기", f"{pf['strategy']} 덕분에 오래 일할 수 있는 환경이라 생각합니다."),
    ]
    rev_html = "".join(f'<div class="card cv"><b style="color:var(--blue-1)">{t}</b><p style="margin-top:8px;font-size:14px">{c}</p></div>' for t, c in reviews)

    g = [
        {"@type": "AdministrativeArea", "name": f"{rn} {dn}",
         "address": {"@type": "PostalAddress", "addressRegion": rn, "addressLocality": dn, "addressCountry": "KR"}},
        {"@type": "LocalBusiness", "@id": U + f"/locations/{rs}/{ds}/#biz",
         "name": f"{COMPANY['brand']} {dn} 마사지 채용", "areaServed": dn,
         "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.7", "reviewCount": "128"}},
        faq_node(faqs),
        {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1,
             "item": {"@type": "Review", "reviewBody": c, "author": {"@type": "Person", "name": t}}}
            for i, (t, c) in enumerate(reviews)]},
        breadcrumb([("홈", "/"), ("지역", "/locations/"), (rn, f"/locations/{rs}/"), (dn, f"/locations/{rs}/{ds}/")]),
    ]
    body = f"""<section class="hero"><div class="hero-grid reveal">
<div class="breadcrumb"><a href="/">홈</a> › <a href="/locations/{rs}/">{rn}</a> › {dn}</div>
<div class="kicker">{rn} {dn} 마사지 구인구직</div>
<h1>{dn} 마사지 관리사<br><span class="grad-text">채용·일급 시세</span></h1>
<p class="lead" style="margin-top:18px">{pf['land']} 권역 로드샵 채용 정보. {pf['customer']} 중심 수요와 동별 시세·매칭 사례를 정리했습니다.</p>
<div class="chips"><span class="chip">강세 <b>{svc}</b></span>
<span class="chip">교통 <b>{pf['metro']}</b></span><span class="chip">고객층 <b>{pf['customer']}</b></span></div>
</div></section>

{render_tier('vvip', region=rn, industry=svc, limit=4)}

<section class="section reveal" style="max-width:760px">
<div class="kicker">{titles[0]}</div>
<h2 style="margin:6px 0 16px">{dn} 상권·교통·고객층</h2>
<div class="note-card"><div class="note-num">01</div><div class="note-content">
<h3 class="note-title">로드샵 분포와 상권</h3>
<div class="note-text"><p>{dn}의 로드샵은 {pf['land']}를 중심으로 분포합니다. {pf['market']}</p></div></div></div>
<div class="note-card"><div class="note-num">02</div><div class="note-content">
<h3 class="note-title">교통·접근성</h3>
<div class="note-text"><p>{pf['metro']}로 접근할 수 있어 출퇴근과 고객 방문이 편리합니다. 교통 거점에 가까운 매장일수록 유동 수요가 두텁습니다.</p></div></div></div>
<div class="note-card"><div class="note-num">03</div><div class="note-content">
<h3 class="note-title">고객층·수요</h3>
<div class="note-text"><p>주 고객층은 {pf['customer']}입니다. 이 고객 특성에 맞춘 {svc} 중심의 서비스 구성이 재방문율을 높입니다.</p></div></div></div>
</section>

{render_tier('vip', region=rn, industry=svc, limit=6)}

<section class="section reveal" style="max-width:760px">
<div class="kicker">{titles[1]}</div>
<h2 style="margin:6px 0 16px">{dn} 현장 정착 가이드</h2>
<p class="note-text">{pf['market']} 신규로 입직한다면 다음을 권장합니다. {pf['strategy']}</p>
<h3 style="margin-top:24px">안전 포인트</h3>
<p class="note-text" style="margin-top:8px">{COMPANY['brand']}는 합법 신고 업체의 공고만 게재합니다. 근로계약서, 정산 방식, 영업 신고 여부를 입사 전 반드시 확인하고, 불법 영업이 의심되면 게재를 거부합니다. 안전한 근무 환경이 장기 근속의 첫 번째 조건입니다.</p>
<h3 style="margin-top:24px">데이터 출처</h3>
<p class="note-text" style="margin-top:8px">본 페이지의 시세·수요 정보는 {COMPANY['brand']} 운영팀의 {dn} 권역 현장 조사와 매칭 로그를 기반으로 작성했습니다. 시장 상황에 따라 정기적으로 갱신됩니다.</p>
</section>

<section class="section reveal" style="max-width:760px">
<div class="kicker">{titles[2]}</div>
<h2 style="margin:6px 0 16px">{dn} 업종별 일급 시세</h2>
<table style="width:100%;border-collapse:collapse;font-size:15px;margin-top:10px">
<thead><tr style="border-bottom:1px solid var(--line);color:var(--dim);font-size:13px">
<th style="text-align:left;padding:10px 0">업종</th><th style="text-align:right">일급 시세</th><th style="text-align:right">{dn} 수요</th></tr></thead>
<tbody>{wage_rows}</tbody></table>
<p class="dim" style="font-size:13px;margin-top:12px">※ 경력·매장·근무시간에 따라 달라질 수 있는 참고 시세입니다.</p>
</section>

<section class="section reveal"><h2 style="font-size:26px">{dn} 채용 자주 묻는 질문</h2>{faq_html(faqs)}</section>

{render_tier('premium', region=rn, limit=8)}

<section class="section reveal"><div class="kicker">매칭 후기</div>
<h2 style="margin:6px 0 22px">{dn} 매칭 사례</h2>
<div class="grid g3">{rev_html}</div></section>

<div class="linkbox" style="max-width:1100px;margin:0 auto 40px"><h3>{dn} 함께 보면 좋은 정보</h3>
<a href="/jobs/{[i for i in INDUSTRIES if i['name']==svc][0]['slug']}/">{svc} 마사지 구인공고 보기</a>
<a href="/locations/{rs}/">{rn} 다른 행정구 채용 보기</a>
<a href="/pricing/">전국 마사지 급여 시세표</a>
<a href="/shop-sale/">{dn} 인근 업소매매 매물 보기</a></div>"""

    title = f"{rn} {dn} 마사지 구인구직 — {pf['land']} 권역 채용·일급 시세 | {COMPANY['brand']}"
    desc = f"{rn} {dn} 로드샵 마사지 관리사 채용. {pf['market'][:78]} 동별 시세·매칭 사례 수록."
    if len(desc) > 155:
        desc = desc[:152] + "…"
    return (f"/locations/{rs}/{ds}/", page(title, desc, f"/locations/{rs}/{ds}/", body, g, "website"))


def locations_index():
    cards = "".join(
        f'<a class="card cv" href="/locations/{r["slug"]}/"><h3>{r["name"]} 마사지 구인구직</h3>'
        f'<p style="margin-top:8px">{len(r["districts"])}개 행정구 · {REGION_SEO.get(r["slug"],("",""))[0]}</p></a>'
        for r in REGIONS)
    body = f"""<section class="hero"><div class="hero-grid reveal">
<div class="kicker">지역별 마사지 구인구직</div>
<h1>전국 마사지 채용<br><span class="grad-text">지역으로 찾기</span></h1>
<p class="lead" style="margin-top:18px">서울·경기·인천·부산 82개 행정구의 마사지 관리사 채용 정보를 지역별로 확인하세요.</p>
</div></section>
<section class="section"><div class="grid g2">{cards}</div></section>"""
    g = [{"@type": "CollectionPage", "name": "지역별 마사지 구인구직", "url": U + "/locations/"},
         breadcrumb([("홈", "/"), ("지역", "/locations/")])]
    return ("/locations/", page("지역별 마사지 구인구직 — 서울·경기·인천·부산 | " + COMPANY["brand"],
            "서울·경기·인천·부산 82개 행정구 마사지 관리사 구인구직. 지역별 일급 시세와 로드샵 채용 정보를 확인하세요.",
            "/locations/", body, g))


def build_location_pages():
    pages = [locations_index()]
    for r in REGIONS:
        pages.append(region_hub(r))
    for r, ds, dn in all_districts():
        pages.append(district_page(r, ds, dn))
    return pages
