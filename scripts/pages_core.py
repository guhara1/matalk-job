# -*- coding: utf-8 -*-
"""핵심 페이지: 메인·About·Contact·Pricing·Reviews·정책·광고상품·업소매매·공지."""

from data import (COMPANY, INDUSTRIES, REGIONS, NATIONALITIES, TEAM, STATS,
                  PRICING_RECRUIT, PRICING_SHOP, MAGAZINE, NOTICES, SHOP_SALES)
from templates import U, page, breadcrumb, faq_node, faq_html
from ads import render_tier
from district_profiles import get_profile
from notice_bodies import NOTICE_BODIES


# ── 메인 ─────────────────────────────────────────────────────
def main_page():
    ind_cards = "".join(
        f'<a class="card cv" href="/jobs/{i["slug"]}/"><span class="tag">{i["name"]}</span>'
        f'<h3 style="margin:10px 0 4px">{i["name"]} 마사지</h3>'
        f'<p style="font-size:13px">평균 일급 {i["wage"]}만원</p></a>' for i in INDUSTRIES)
    reg_cards = "".join(
        f'<a class="card cv" href="/locations/{r["slug"]}/"><h3>{r["name"]}</h3>'
        f'<p style="font-size:13px;margin-top:4px">{len(r["districts"])}개 행정구</p></a>' for r in REGIONS)
    team_cards = "".join(
        f'<div class="card"><b style="color:var(--blue-1)">{t["name"]}</b> · {t["role"]}'
        f'<p style="font-size:14px;margin-top:8px">{t["bio"]}</p></div>' for t in TEAM)
    faqs = [
        ("마톡은 어떤 서비스인가요?", "마톡은 전국 마사지 관리사 구인구직과 로드샵 채용, 업소매매를 연결하는 합법 플랫폼입니다. 직업정보제공사업 신고를 마쳤습니다."),
        ("채용 정보는 믿을 수 있나요?", "마톡은 합법 신고 업체의 공고만 게재하며, 불법 영업이 의심되는 업소는 게재를 거부합니다. 운영팀이 사업자 정보를 검증합니다."),
        ("이용 요금이 있나요?", "구직자는 무료로 이용할 수 있습니다. 채용 공고 광고와 업소매매 등록은 유료 상품으로 운영됩니다."),
        ("어떻게 지원하나요?", "공고 상세 페이지에서 이메일 지원 또는 매칭 신청으로 연결됩니다. 안전을 위해 전화 직접 연결은 제공하지 않습니다."),
        ("어느 지역을 다루나요?", "서울·경기·인천·부산 82개 행정구의 채용 정보를 다루며, 매일 갱신됩니다."),
        ("신입도 일자리를 찾을 수 있나요?", "네. 신입 교육을 운영하는 매장이 많아, 적성과 체력 요건을 확인한 뒤 수습을 거쳐 정착할 수 있습니다."),
    ]
    g = [{"@type": "WebPage", "name": COMPANY["brand"], "url": U + "/"}, faq_node(faqs)]
    extra = ('<meta name="naver-site-verification" content="">'
             '<meta name="google-site-verification" content="">')
    body = f"""<section class="hero"><div class="hero-grid reveal">
<div class="kicker">전국 마사지 구인구직 플랫폼</div>
<h1>마사지 관리사 채용,<br><span class="grad-text">마톡에서 안전하게</span></h1>
<p class="lead" style="margin-top:18px">서울·경기·인천·부산 82개 행정구의 마사지 구인구직·로드샵 채용·업소매매를 한곳에서. 합법 신고 플랫폼이 검증한 공고만 제공합니다.</p>
<div class="chips">
<span class="chip">공고 <b>{STATS['jobs']}여건</b></span>
<span class="chip">평균 매칭 <b>{STATS['avg_match_hours']}시간</b></span>
<span class="chip"><b>{STATS['districts']}</b>개 행정구</span>
<span class="chip">매칭 로그 <b>{STATS['match_logs']}건</b></span></div>
<div class="pill-row" style="margin-top:24px">
<a href="/jobs/" class="btn btn-grad">구인공고 보기</a>
<a href="/seekers/" class="btn btn-ghost">구직 가이드</a></div>
</div></section>

{render_tier('vvip', limit=4)}

<section class="section reveal"><div class="kicker">업종별 채용 현황</div>
<h2 style="margin:6px 0 22px">업종으로 찾기</h2><div class="grid g3">{ind_cards}</div></section>

{render_tier('vip', limit=6)}

<section class="section reveal"><div class="kicker">지역별 채용 현황</div>
<h2 style="margin:6px 0 22px">지역으로 찾기</h2><div class="grid g4">{reg_cards}</div></section>

<section class="section reveal" style="max-width:900px"><div class="kicker">HOW IT WORKS</div>
<h2 style="margin:6px 0 22px">마톡 이용 4단계</h2>
<div class="grid g4">
<div class="card"><span class="ad-rank">01</span><h3 style="margin:6px 0">탐색</h3><p style="font-size:14px">업종·지역으로 공고를 탐색합니다.</p></div>
<div class="card"><span class="ad-rank">02</span><h3 style="margin:6px 0">매칭</h3><p style="font-size:14px">조건에 맞는 공고에 매칭을 신청합니다.</p></div>
<div class="card"><span class="ad-rank">03</span><h3 style="margin:6px 0">확인</h3><p style="font-size:14px">일급·정산·근무 조건을 사전 조율합니다.</p></div>
<div class="card"><span class="ad-rank">04</span><h3 style="margin:6px 0">근무</h3><p style="font-size:14px">계약 후 안전하게 근무를 시작합니다.</p></div>
</div></section>

{render_tier('premium', limit=8)}

<section class="section reveal" style="max-width:900px"><div class="kicker">WHO · HOW · WHY</div>
<h2 style="margin:6px 0 16px">운영팀이 직접 검증합니다</h2>
<div class="note-text" style="max-width:780px;margin-bottom:30px">
<div style="margin-bottom:20px"><span class="kicker">WHO · 누가</span>
<p style="margin-top:8px">마톡의 콘텐츠는 익명의 외주 작성자가 아니라, 실명과 경력을 공개한 운영팀이 직접 만들고 검수합니다. 9년차 채용 데이터 분석가 김세영이 시장 리서치와 매칭 로그 검증을 총괄하고, 이도윤이 로드샵 현장 검증과 안전 게재 정책을 책임집니다. KSPO 생활스포츠지도사 박지연은 관리사 입문 교육과 역량 기준을 자문합니다. 각 담당자는 자신의 전문 영역에 대해 책임을 지며, 모든 페이지 하단에는 사업자 정보와 연락처를 투명하게 공개합니다. 누가 만들었는지 명확히 밝히는 것이 신뢰의 출발점이라고 믿기 때문입니다.</p></div>
<div style="margin-bottom:20px"><span class="kicker">HOW · 어떻게</span>
<p style="margin-top:8px">모든 일급 시세와 지역 수요 정보는 누적 매칭 로그 {STATS['match_logs']}건과 로드샵 현장 인터뷰 {STATS['shop_interviews']}건이라는 1차 데이터에서 출발합니다. 서울·경기·인천·부산 82개 행정구를 직접 조사해 랜드마크·교통·고객층·강세 업종을 구별로 정리했고, 시장 상황이 바뀌면 정기적으로 갱신합니다. 공고를 게재하기 전에는 사업자 등록과 영업 신고 여부를 확인하며, 모든 수치는 추정이 아닌 실제 데이터에 근거합니다. 어디서나 볼 수 있는 일반적인 요약이 아니라, 마톡이 직접 수집하고 검증한 원본 데이터만 제공하는 것이 원칙입니다.</p></div>
<div><span class="kicker">WHY · 왜</span>
<p style="margin-top:8px">마사지 구인구직은 일하는 사람의 안전과 수입에 직결된 민감한 영역입니다. 그래서 마톡은 직업정보제공사업 신고를 갖춘 합법 업체의 공고만 게재하고, 불법 영업이 의심되는 업소는 사업자 정보 확인 단계에서 게재를 거부합니다. 고수익을 미끼로 한 해외 송출이나 정상 시술과 무관한 모집은 일절 취급하지 않습니다. 정확하고 검증된 정보로 관리사와 안전한 일터를 연결하는 것, 그것이 마톡이 존재하는 이유입니다.</p></div>
</div>
<div class="grid g3">{team_cards}</div></section>

<section class="section reveal"><h2 style="font-size:28px">자주 묻는 질문</h2>{faq_html(faqs)}</section>

<section class="section reveal" style="text-align:center;max-width:760px">
<h2>지금 마톡에서 시작하세요</h2>
<p class="lead" style="margin:14px auto 24px">안전하게 검증된 마사지 채용 정보, 마톡이 함께합니다.</p>
<div class="pill-row" style="justify-content:center">
<a href="/jobs/" class="btn btn-grad">구인공고 보기</a>
<a href="/contact-ads/" class="btn cta-gold">광고문의</a></div></section>"""
    title = f"{COMPANY['brand']} | 마사지 구인구직·알바 채용정보"
    desc = f"전국 82개 행정구 마사지 관리사 구인구직. 채용 공고 {STATS['jobs']}여건 매일 갱신·평균 {STATS['avg_match_hours']}시간 매칭. 직업정보제공사업 신고 합법 플랫폼."
    return ("/", page(title, desc, "/", body, g, extra_meta=extra))


# ── About ────────────────────────────────────────────────────
def about_page():
    team_cards = "".join(
        f'<div class="card"><b style="color:var(--blue-1);font-size:17px">{t["name"]}</b> · {t["role"]}'
        f'<p class="dim" style="font-size:13px;margin:4px 0 8px">담당: {t["area"]}</p>'
        f'<p style="font-size:14px">{t["bio"]}</p></div>' for t in TEAM)
    g = [{"@type": "AboutPage", "name": f"{COMPANY['brand']} 소개", "url": U + "/about/"},
         breadcrumb([("홈", "/"), ("회사 소개", "/about/")])]
    body = f"""<section class="hero"><div class="hero-grid reveal">
<div class="kicker">회사 소개</div>
<h1>안전한 마사지 채용<br><span class="grad-text">마톡이 만듭니다</span></h1>
<p class="lead" style="margin-top:18px">{COMPANY['brand']}은 {COMPANY['legal_name']}가 운영하는 직업정보제공사업 신고 플랫폼입니다.</p>
</div></section>
<section class="section reveal" style="max-width:760px">
<h2>우리가 일하는 방식</h2>
<p class="note-text" style="margin-top:12px">마톡은 마사지 관리사와 합법 로드샵을 안전하게 연결하기 위해 만들어졌습니다. 우리는 '누가, 어떻게, 왜' 이 정보를 만드는지를 투명하게 공개합니다. 모든 채용 정보는 운영팀이 사업자 정보를 확인하고, 불법 영업이 의심되는 업소는 게재를 거부합니다.</p>
<h2 style="margin-top:34px">데이터 방법론</h2>
<p class="note-text" style="margin-top:12px">마톡의 시세·수요 콘텐츠는 누적 매칭 로그 {STATS['match_logs']}건과 로드샵 현장 인터뷰 {STATS['shop_interviews']}건을 기반으로 작성됩니다. 82개 행정구 각각의 랜드마크·교통·고객층을 현장 조사해 지역별 고유 데이터로 정리하며, 시장 변화에 맞춰 정기적으로 갱신합니다. 어디서나 볼 수 있는 일반 정보가 아니라, 직접 수집한 1차 데이터를 제공하는 것이 우리의 원칙입니다.</p>
<h2 style="margin-top:34px">운영팀</h2>
<div class="grid g3" style="margin-top:16px">{team_cards}</div>
<h2 style="margin-top:34px">회사 정보</h2>
<div class="card" style="margin-top:14px"><table style="width:100%;font-size:14px;line-height:2.2;color:var(--muted)">
<tr><td class="dim">상호</td><td>{COMPANY['legal_name']} ({COMPANY['brand']})</td></tr>
<tr><td class="dim">대표자</td><td>{COMPANY['ceo']}</td></tr>
<tr><td class="dim">사업자등록번호</td><td>{COMPANY['biz_no']}</td></tr>
<tr><td class="dim">직업정보제공사업 신고</td><td>{COMPANY['job_info_no']}</td></tr>
<tr><td class="dim">주소</td><td>{COMPANY['address']}</td></tr>
<tr><td class="dim">개인정보보호책임자</td><td>{COMPANY['privacy_officer']}</td></tr>
<tr><td class="dim">고객센터</td><td>{COMPANY['tel']} ({COMPANY['tel_hours']})</td></tr>
<tr><td class="dim">이메일</td><td>{COMPANY['email']}</td></tr>
</table></div></section>"""
    return ("/about/", page(f"회사 소개 — {COMPANY['brand']} 운영팀·데이터 방법론 | {COMPANY['brand']}",
            f"{COMPANY['brand']}({COMPANY['legal_name']})는 직업정보제공사업 신고 합법 마사지 구인구직 플랫폼입니다. 운영팀과 1차 데이터 방법론을 공개합니다.",
            "/about/", body, g))


# ── Contact ──────────────────────────────────────────────────
def contact_page():
    g = [{"@type": "ContactPage", "name": "고객센터", "url": U + "/contact/"},
         breadcrumb([("홈", "/"), ("고객센터", "/contact/")])]
    body = f"""<section class="hero"><div class="hero-grid reveal">
<div class="kicker">고객센터</div><h1>무엇을 도와드릴까요?</h1>
<p class="lead" style="margin-top:18px">마톡 이용·광고·제보 관련 문의를 안내합니다.</p>
</div></section>
<section class="section reveal" style="max-width:760px"><div class="grid g2">
<div class="card"><h3>고객센터</h3><p style="margin-top:8px">{COMPANY['tel']}<br>{COMPANY['tel_hours']}</p></div>
<div class="card"><h3>이메일</h3><p style="margin-top:8px">{COMPANY['email']}</p></div>
<div class="card"><h3>광고 문의</h3><p style="margin-top:8px">채용 공고·업소매매 광고는 <a href="/contact-ads/" style="color:var(--blue-1)">광고문의</a>에서 신청하세요.</p></div>
<div class="card"><h3>불법·피해 제보</h3><p style="margin-top:8px">불법 영업·사기 제보는 이메일 또는 <a href="/notices/" style="color:var(--blue-1)">공지사항</a>의 신고 채널을 이용하세요.</p></div>
</div>
<p class="dim" style="margin-top:20px;font-size:13px">전화는 광고·이용 안내용입니다. 채용 지원·매수 문의는 각 공고·매물 페이지를 이용해 주세요.</p>
</section>"""
    return ("/contact/", page(f"고객센터 — 문의 안내 | {COMPANY['brand']}",
            f"{COMPANY['brand']} 고객센터. 이용·광고·제보 문의 안내. 고객센터 {COMPANY['tel']}, 이메일 {COMPANY['email']}.",
            "/contact/", body, g))


# ── Pricing (급여 시세) ──────────────────────────────────────
def pricing_page():
    rows = "".join(
        f'<tr><td>{i["name"]}</td><td style="text-align:right">{i["wage_lo"]}만원</td>'
        f'<td style="text-align:right;color:var(--blue-1);font-weight:700">{i["wage"]}만원</td>'
        f'<td style="text-align:right">{i["wage_hi"]}만원</td>'
        f'<td style="text-align:right">{i["wage"]*26}만원</td></tr>' for i in INDUSTRIES)
    g = [{"@type": "WebPage", "name": "마사지 급여 시세", "url": U + "/pricing/"},
         breadcrumb([("홈", "/"), ("급여 시세", "/pricing/")])]
    body = f"""<section class="hero"><div class="hero-grid reveal">
<div class="kicker">2026 급여 시세</div><h1>마사지 관리사<br><span class="grad-text">급여 시세표</span></h1>
<p class="lead" style="margin-top:18px">업종별 일급 시세와 월 환산 수입을 매칭 데이터 기반으로 정리했습니다.</p>
</div></section>
<section class="section reveal" style="max-width:820px">
<table style="width:100%;border-collapse:collapse;font-size:15px">
<thead><tr style="border-bottom:1px solid var(--line);color:var(--dim);font-size:13px">
<th style="text-align:left;padding:12px 0">업종</th><th style="text-align:right">신입</th>
<th style="text-align:right">평균</th><th style="text-align:right">경력</th><th style="text-align:right">월 환산</th></tr></thead>
<tbody>{rows}</tbody></table>
<p class="dim" style="font-size:13px;margin-top:14px">※ 월 환산은 평균 일급 × 26일 기준 참고치입니다. 상권·경력·근무시간에 따라 달라집니다.</p>
<div class="linkbox" style="margin-top:34px"><h3>급여 관련 더 알아보기</h3>
<a href="/magazine/salary-guide-2026/">2026 급여 시세 완전정리</a>
<a href="/magazine/shop-vs-freelance/">로드샵 vs 프리랜서 수입 비교</a>
<a href="/jobs/">업종별 구인공고 보기</a></div>
</section>"""
    return ("/pricing/", page(f"2026 마사지 관리사 급여 시세표 — 업종별 일급 | {COMPANY['brand']}",
            "2026 마사지 관리사 급여 시세표. 스웨디시·아로마·타이·로미로미·스포츠 업종별 신입·평균·경력 일급과 월 환산 수입을 정리했습니다.",
            "/pricing/", body, g))


# ── Reviews (매칭 사례) ──────────────────────────────────────
def reviews_page():
    cases = [
        ("강남 아로마 이직", "서울 강남구", "프리미엄 스파로 이직 후 단골이 늘어 월 수입이 안정됐어요."),
        ("분당 타이 신입", "경기 성남분당", "신입 교육을 거쳐 3개월 만에 단골을 확보했습니다."),
        ("해운대 스웨디시", "부산 해운대구", "관광 상권이라 주말 회전율이 높아 단기 수입이 좋았어요."),
        ("송도 프리미엄", "인천 연수구", "외국인 고객 응대 경험을 쌓으며 단가를 높였습니다."),
        ("부평 스포츠", "인천 부평구", "산단 근처라 근육 회복 단골이 많아 평일이 안정적이에요."),
        ("서면 아로마", "부산 부산진구", "번화가 유동 수요가 많아 다양한 고객을 경험했습니다."),
    ]
    cards = "".join(
        f'<div class="card cv"><span class="tag">{r}</span><h3 style="margin:10px 0 6px">{t}</h3>'
        f'<p style="font-size:14px">{c}</p></div>' for t, r, c in cases)
    g = [{"@type": "WebPage", "name": "매칭 사례", "url": U + "/reviews/"},
         breadcrumb([("홈", "/"), ("매칭 사례", "/reviews/")])]
    body = f"""<section class="hero"><div class="hero-grid reveal">
<div class="kicker">매칭 사례</div><h1>마톡과 함께한<br><span class="grad-text">매칭 사례</span></h1>
<p class="lead" style="margin-top:18px">실제 관리사들이 마톡으로 일자리를 찾은 사례를 소개합니다.</p>
</div></section>
<section class="section reveal"><div class="grid g3">{cards}</div></section>"""
    return ("/reviews/", page(f"매칭 사례 — 마사지 관리사 취업 후기 | {COMPANY['brand']}",
            "마톡으로 마사지 일자리를 찾은 관리사들의 매칭 사례. 지역·업종별 취업 후기를 확인하세요.",
            "/reviews/", body, g))


# ── 정책 3종 ─────────────────────────────────────────────────
def policy_pages():
    c = COMPANY
    docs = {
     "privacy": ("개인정보처리방침", [
        ("수집하는 개인정보", f"{c['brand']}은 광고문의·매칭 신청 시 성명, 연락처, 이메일, 문의 내용을 수집합니다. 구직자 열람은 별도 회원가입 없이 이용할 수 있습니다."),
        ("이용 목적", "수집된 정보는 문의 응대, 광고·매칭 서비스 제공, 법령상 의무 이행을 위해서만 이용합니다."),
        ("보유 및 파기", "수집 목적 달성 후 관련 법령이 정한 기간이 지나면 지체 없이 파기합니다."),
        ("제3자 제공", "법령에 근거하거나 이용자가 동의한 경우를 제외하고 개인정보를 제3자에게 제공하지 않습니다."),
        ("개인정보보호책임자", f"성명 {c['privacy_officer']} · 이메일 {c['email']}. 개인정보 관련 문의를 처리합니다."),
        ("이용자 권리", "이용자는 본인의 개인정보 열람·정정·삭제를 요청할 수 있으며, 마톡은 지체 없이 조치합니다."),
     ]),
     "terms": ("이용약관", [
        ("목적", f"본 약관은 {c['legal_name']}({c['brand']})가 제공하는 마사지 구인구직·업소매매 정보 서비스의 이용 조건을 규정합니다."),
        ("서비스 내용", "마톡은 직업정보제공사업 신고에 따라 채용 정보 게재·열람, 광고, 업소매매 등록 서비스를 제공합니다."),
        ("게재 기준", "마톡은 합법 신고 업체의 공고만 게재하며, 불법 영업이 의심되는 게재 요청을 거부할 수 있습니다."),
        ("이용자 의무", "이용자는 허위 정보를 게재하거나 타인의 권리를 침해해서는 안 됩니다."),
        ("책임의 한계", "마톡은 정보 제공 플랫폼으로서 채용 당사자 간 계약의 직접 당사자가 아닙니다. 거래는 당사자 책임으로 진행됩니다."),
        ("약관의 변경", "약관 변경 시 사전 공지하며, 변경된 약관은 공지한 시점부터 효력이 발생합니다."),
     ]),
     "youth": ("청소년보호정책", [
        ("기본 방침", f"{c['brand']}은 청소년이 유해 정보에 노출되지 않도록 보호하며, 관련 법령을 준수합니다."),
        ("게재 제한", "마톡은 마사지 관리사 채용 정보를 제공하는 성인 대상 구인구직 서비스로, 청소년 유해 매체물에 해당하는 정보를 게재하지 않습니다."),
        ("불법 정보 차단", "성매매 알선 등 불법·유해 정보의 게재를 전면 거부하며, 발견 즉시 차단하고 관계 기관에 협조합니다."),
        ("청소년보호책임자", f"성명 {c['privacy_officer']} · 이메일 {c['email']}."),
        ("신고 안내", "유해 정보를 발견하면 고객센터로 신고해 주세요. 신속히 확인 후 조치합니다."),
     ]),
    }
    out = []
    for slug, (name, secs) in docs.items():
        notes = "".join(
            f'<div class="note-card"><div class="note-num">{i+1:02d}</div><div class="note-content">'
            f'<h3 class="note-title">{t}</h3><div class="note-text"><p>{b}</p></div></div></div>'
            for i, (t, b) in enumerate(secs))
        g = [{"@type": "WebPage", "name": name, "url": U + f"/policy/{slug}/"},
             breadcrumb([("홈", "/"), (name, f"/policy/{slug}/")])]
        body = f"""<article class="wrap" style="max-width:760px;padding-top:80px">
<div class="breadcrumb"><a href="/">홈</a> › {name}</div>
<h1 style="font-size:clamp(28px,4vw,42px)">{name}</h1>
<p class="dim" style="margin:10px 0 24px">{c['legal_name']} ({c['brand']}) · 시행일 2026-01-01</p>{notes}</article>"""
        out.append((f"/policy/{slug}/", page(f"{name} | {c['brand']}",
                    f"{c['brand']} {name}. {c['legal_name']}가 운영하는 마사지 구인구직 플랫폼의 {name}입니다.",
                    f"/policy/{slug}/", body, g)))
    return out


# ── 광고상품 페이지 ──────────────────────────────────────────
def recruitment_pricing_page():
    cards = ""
    for p in PRICING_RECRUIT:
        perks = "".join(f"<li>{x}</li>" for x in p["perks"])
        cards += f"""<div class="price-card cv">
<span class="ad-badge b-{p['color'] if p['color']!='gray' else 'premium'}">{p['tier']}</span>
<p class="dim" style="margin:8px 0">{p['slot']} · {p['limit']}</p>
<div class="price-num">{p['m1']}만원<span style="font-size:14px;color:var(--dim)">/1개월</span></div>
<p class="dim" style="font-size:13px;margin:6px 0">6개월 {p['m6']}만 · 12개월 {p['m12']}만</p>
<ul style="color:var(--muted);font-size:14px;margin:14px 0 0 18px;line-height:2">{perks}</ul></div>"""
    faqs = [
        ("광고 노출 위치는 어디인가요?", "VVIP는 메인·지역·업종 페이지 최상단, VIP는 콘텐츠 중간, 프리미엄은 하단에 노출됩니다."),
        ("같은 등급 내 순서는 어떻게 정해지나요?", "선등록순으로 정렬되며, 슬롯이 부족하면 인접 지역·업종으로 backfill됩니다."),
        ("광고 신청은 어떻게 하나요?", "광고문의 폼으로 신청하면 담당자가 등급·기간·게재 위치를 안내합니다."),
    ]
    g = [{"@type": "Service", "name": "채용공고 광고", "offers": {"@type": "AggregateOffer",
          "lowPrice": 13, "highPrice": 110, "priceCurrency": "KRW"}},
         faq_node(faqs), breadcrumb([("홈", "/"), ("채용공고 광고", "/recruitment-pricing/")])]
    body = f"""<section class="hero"><div class="hero-grid reveal">
<div class="kicker">채용공고 광고</div><h1>채용공고<br><span class="grad-text">광고 상품 안내</span></h1>
<p class="lead" style="margin-top:18px">VVIP·VIP·프리미엄 3등급으로 채용 공고를 효과적으로 노출하세요.</p>
</div></section>
<section class="section reveal"><div class="grid g3">{cards}</div></section>
<section class="section reveal"><h2 style="font-size:26px">광고 자주 묻는 질문</h2>{faq_html(faqs)}</section>
<section class="section" style="text-align:center"><a href="/contact-ads/" class="btn cta-gold">광고문의 하기</a></section>"""
    return ("/recruitment-pricing/", page(f"채용공고 광고 상품 안내 — VVIP·VIP·프리미엄 | {COMPANY['brand']}",
            "마톡 채용공고 광고 상품. VVIP 월 44만원, VIP 20만원, 프리미엄 13만원부터. 등급별 노출 위치와 혜택을 안내합니다.",
            "/recruitment-pricing/", body, g))


def shop_sale_pricing_page():
    cards = ""
    for p in PRICING_SHOP:
        badge = '<span class="ad-badge b-vvip">BEST</span>' if p["best"] else ""
        cards += f"""<div class="price-card cv">{badge}
<h3 style="margin:8px 0">{p['plan']} 등록</h3>
<div class="price-num">{p['price']}만원</div>
<p class="dim" style="font-size:14px;margin-top:8px">{p['note']}</p></div>"""
    g = [{"@type": "Service", "name": "업소매매 등록", "offers": {"@type": "AggregateOffer",
          "lowPrice": 10, "highPrice": 33, "priceCurrency": "KRW"}},
         breadcrumb([("홈", "/"), ("업소매매 등록", "/shop-sale-pricing/")])]
    body = f"""<section class="hero"><div class="hero-grid reveal">
<div class="kicker">업소매매 등록</div><h1>마사지샵 양도<br><span class="grad-text">매물 등록 안내</span></h1>
<p class="lead" style="margin-top:18px">익명 게재, 매수자 1:1 매칭, 거래 수수료 0원으로 안전하게 매물을 등록하세요.</p>
</div></section>
<section class="section reveal"><div class="grid g3">{cards}</div>
<div class="linkbox" style="margin-top:30px"><h3>업소매매 안내</h3>
<p style="margin-bottom:8px">· 익명 게재 — 동까지만 공개해 매장 노출을 보호합니다.</p>
<p style="margin-bottom:8px">· 매수자 1:1 매칭 — 운영자를 거치지 않고 직접 연결됩니다.</p>
<p>· 거래 수수료 0원 — 등록비 외 별도 수수료가 없습니다.</p></div></section>
<section class="section" style="text-align:center">
<a href="/shop-sale/" class="btn btn-grad">매물 보기</a> <a href="/contact-ads/" class="btn cta-gold">등록 문의</a></section>"""
    return ("/shop-sale-pricing/", page(f"업소매매 등록 안내 — 1개월 10만원 | {COMPANY['brand']}",
            "마사지샵 업소매매 등록 안내. 1개월 10만원, 2개월 15만원(BEST), 12개월 33만원. 익명 게재·매수자 1:1 매칭·수수료 0원.",
            "/shop-sale-pricing/", body, g))


def pricing_ads_page():
    g = [{"@type": "WebPage", "name": "광고상품 종합 안내", "url": U + "/pricing-ads/"},
         breadcrumb([("홈", "/"), ("광고상품", "/pricing-ads/")])]
    body = f"""<section class="hero"><div class="hero-grid reveal">
<div class="kicker">광고상품 종합 안내</div><h1>마톡<br><span class="grad-text">광고상품 안내</span></h1>
<p class="lead" style="margin-top:18px">채용공고 광고와 업소매매 등록, 두 가지 상품을 안내합니다.</p>
</div></section>
<section class="section reveal"><div class="grid g2">
<a class="card cv" href="/recruitment-pricing/"><span class="tag">채용공고</span>
<h3 style="margin:10px 0 6px">채용공고 광고</h3>
<p>VVIP·VIP·프리미엄 3등급. 월 13만원부터 메인·지역·업종 페이지에 노출.</p>
<p style="color:var(--blue-1);font-weight:700;margin-top:10px">자세히 보기 →</p></a>
<a class="card cv" href="/shop-sale-pricing/"><span class="tag">업소매매</span>
<h3 style="margin:10px 0 6px">업소매매 등록</h3>
<p>1개월 10만원부터. 익명 게재·매수자 1:1 매칭·수수료 0원.</p>
<p style="color:var(--blue-1);font-weight:700;margin-top:10px">자세히 보기 →</p></a>
</div></section>
<section class="section" style="text-align:center"><a href="/contact-ads/" class="btn cta-gold">광고문의 하기</a></section>"""
    return ("/pricing-ads/", page(f"광고상품 종합 안내 — 채용공고·업소매매 | {COMPANY['brand']}",
            "마톡 광고상품 종합 안내. 채용공고 광고(VVIP·VIP·프리미엄)와 업소매매 등록 상품을 한눈에 비교하세요.",
            "/pricing-ads/", body, g))


def contact_ads_page():
    g = [{"@type": "ContactPage", "name": "광고문의", "url": U + "/contact-ads/"},
         breadcrumb([("홈", "/"), ("광고문의", "/contact-ads/")])]
    grade_opts = "".join(f'<option>{p["tier"]}</option>' for p in PRICING_RECRUIT) + "<option>업소매매</option>"
    region_opts = "".join(f'<option>{r["name"]}</option>' for r in REGIONS)
    body = f"""<section class="hero"><div class="hero-grid reveal">
<div class="kicker">광고문의</div><h1>광고문의</h1>
<p class="lead" style="margin-top:18px">채용공고 광고·업소매매 등록 문의를 남겨주시면 담당자가 연락드립니다.</p>
</div></section>
<section class="section reveal" style="max-width:620px">
<form id="adForm" class="card" style="display:flex;flex-direction:column;gap:14px">
<label>성명<input name="name" required style="width:100%;margin-top:6px;padding:12px;background:var(--bg);border:1px solid var(--line);border-radius:10px;color:var(--text)"></label>
<label>연락처<input name="phone" required style="width:100%;margin-top:6px;padding:12px;background:var(--bg);border:1px solid var(--line);border-radius:10px;color:var(--text)"></label>
<label>지역<select name="region" style="width:100%;margin-top:6px;padding:12px;background:var(--bg);border:1px solid var(--line);border-radius:10px;color:var(--text)">{region_opts}</select></label>
<label>광고 등급<select name="grade" style="width:100%;margin-top:6px;padding:12px;background:var(--bg);border:1px solid var(--line);border-radius:10px;color:var(--text)">{grade_opts}</select></label>
<label>문의 내용<textarea name="message" rows="4" style="width:100%;margin-top:6px;padding:12px;background:var(--bg);border:1px solid var(--line);border-radius:10px;color:var(--text)"></textarea></label>
<input type="text" name="company_url" style="display:none" tabindex="-1" autocomplete="off">
<button type="submit" class="btn cta-gold" style="justify-content:center">문의 보내기</button>
<p id="adMsg" class="dim" style="font-size:13px"></p>
</form></section>
<script>
document.getElementById('adForm').addEventListener('submit',function(e){{
 e.preventDefault();var f=e.target,d={{}};new FormData(f).forEach(function(v,k){{d[k]=v}});
 var m=document.getElementById('adMsg');m.textContent='전송 중...';
 fetch('/api/contact-ads',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify(d)}})
 .then(function(r){{return r.json()}}).then(function(j){{m.textContent=j.ok?'문의가 접수되었습니다. 곧 연락드리겠습니다.':'전송에 실패했습니다. 잠시 후 다시 시도해 주세요.';if(j.ok)f.reset()}})
 .catch(function(){{m.textContent='전송에 실패했습니다. 이메일({COMPANY['email']})로 문의해 주세요.'}});
}});
</script>"""
    return ("/contact-ads/", page(f"광고문의 — 채용공고·업소매매 광고 신청 | {COMPANY['brand']}",
            "마톡 광고문의. 채용공고 광고(VVIP·VIP·프리미엄)·업소매매 등록 신청을 남겨주시면 담당자가 안내합니다.",
            "/contact-ads/", body, g))


# ── 업소매매 ─────────────────────────────────────────────────
def shop_sale_index():
    cards = "".join(
        f'<a class="card cv" href="/shop-sale/{s["id"]}/">'
        f'<span class="tag">{s["label"]}</span> <span class="ad-badge b-vvip" style="float:right">매매중</span>'
        f'<h3 style="margin:12px 0 6px">{s["title"]}</h3>'
        f'<p style="font-size:13px;color:var(--muted)">{s["region"]} {s["district"]} · {s["industry"]} · {s["area"]}평</p>'
        f'<div style="margin-top:12px;display:flex;flex-wrap:wrap;gap:8px;font-size:13px">'
        f'<span class="chip">권리금 <b>{s["premium"]}만</b></span>'
        f'<span class="chip">월매출 <b>{s["revenue"]}만</b></span>'
        f'<span class="chip">월순익 <b>{s["profit"]}만</b></span></div></a>'
        for s in SHOP_SALES)
    region_opts = "".join(f'<option value="{r["name"]}">{r["name"]}</option>' for r in REGIONS)
    ind_opts = "".join(f'<option value="{i["name"]}">{i["name"]}</option>' for i in INDUSTRIES)
    g = [{"@type": "CollectionPage", "name": "업소매매", "url": U + "/shop-sale/"},
         breadcrumb([("홈", "/"), ("업소매매", "/shop-sale/")])]
    body = f"""<section class="hero"><div class="hero-grid reveal">
<div class="kicker">업소매매</div><h1>마사지샵<br><span class="grad-text">업소매매 매물</span></h1>
<p class="lead" style="margin-top:18px">익명 게재·매수자 1:1 매칭·수수료 0원. 검증된 양도 매물을 확인하세요.</p>
</div></section>
<section class="section reveal">
<div class="pill-row" style="gap:12px;margin-bottom:24px">
<select id="fRegion" style="padding:10px 14px;background:var(--surface);border:1px solid var(--line);border-radius:10px;color:var(--text)"><option value="">전체 지역</option>{region_opts}</select>
<select id="fInd" style="padding:10px 14px;background:var(--surface);border:1px solid var(--line);border-radius:10px;color:var(--text)"><option value="">전체 업종</option>{ind_opts}</select>
</div>
<div class="grid g3" id="shopGrid">{cards}</div></section>
<script>
(function(){{var r=document.getElementById('fRegion'),i=document.getElementById('fInd'),cards=[].slice.call(document.querySelectorAll('#shopGrid>a'));
function flt(){{cards.forEach(function(c){{var t=c.textContent;var ok=(!r.value||t.indexOf(r.value)>-1)&&(!i.value||t.indexOf(i.value)>-1);c.style.display=ok?'':'none'}})}}
r.addEventListener('change',flt);i.addEventListener('change',flt);}})();
</script>"""
    return ("/shop-sale/", page(f"마사지샵 업소매매 — 양도 매물 {len(SHOP_SALES)}건 | {COMPANY['brand']}",
            f"마사지샵 업소매매 매물 {len(SHOP_SALES)}건. 지역·업종별 권리금·월매출·월순익 정보. 익명 게재·매수자 1:1 매칭·수수료 0원.",
            "/shop-sale/", body, g, show_promo=False))


def shop_sale_detail(s):
    pf = get_profile_for_region(s)
    total = s["premium"] + s["deposit"]
    g = [{"@type": "Product", "name": s["title"], "description": f"{s['region']} {s['district']} {s['industry']} 마사지샵 양도 매물. {s['area']}평.",
          "offers": {"@type": "Offer", "priceCurrency": "KRW", "price": s["premium"] * 10000,
                     "availability": "https://schema.org/InStock"},
          "additionalProperty": [
              {"@type": "PropertyValue", "name": "권리금", "value": f"{s['premium']}만원"},
              {"@type": "PropertyValue", "name": "보증금", "value": f"{s['deposit']}만원"},
              {"@type": "PropertyValue", "name": "월세", "value": f"{s['rent']}만원"},
              {"@type": "PropertyValue", "name": "면적", "value": f"{s['area']}평"},
              {"@type": "PropertyValue", "name": "업종", "value": s["industry"]},
              {"@type": "PropertyValue", "name": "월매출", "value": f"{s['revenue']}만원"},
              {"@type": "PropertyValue", "name": "월순익", "value": f"{s['profit']}만원"},
              {"@type": "PropertyValue", "name": "상권", "value": s["label"]}]},
         breadcrumb([("홈", "/"), ("업소매매", "/shop-sale/"), (s["title"], f"/shop-sale/{s['id']}/")])]
    related = "".join(
        f'<a href="/shop-sale/{o["id"]}/">{o["title"]} — 권리금 {o["premium"]}만원</a>'
        for o in SHOP_SALES if o["id"] != s["id"] and o["region"] == s["region"])[:500]
    if not related:
        related = "".join(f'<a href="/shop-sale/{o["id"]}/">{o["title"]} — 권리금 {o["premium"]}만원</a>'
                          for o in SHOP_SALES if o["id"] != s["id"])[:500]
    body = f"""<section class="hero" style="padding-bottom:30px"><div class="hero-grid reveal">
<div class="breadcrumb"><a href="/">홈</a> › <a href="/shop-sale/">업소매매</a> › {s['district']}</div>
<span class="ad-badge b-vvip">매매중</span> <span class="tag">{s['label']}</span>
<h1 style="font-size:clamp(28px,4vw,42px);margin:12px 0 6px">{s['title']}</h1>
<p class="lead">{s['region']} {s['district']} · {s['industry']} · {s['area']}평</p>
<div class="card" style="margin-top:20px;background:linear-gradient(135deg,#2a2210,#1a1608);border-color:rgba(214,178,116,.4)">
<span class="dim">월매출 / 월순익</span>
<div style="font-size:26px;font-weight:800;color:var(--gold-2);margin-top:6px">{s['revenue']}만원 <span style="color:var(--dim);font-size:16px">/ 순익 {s['profit']}만원</span></div></div>
<div class="grid g4" style="margin-top:18px">
<div class="card"><span class="dim" style="font-size:13px">권리금</span><div class="price-num" style="font-size:22px">{s['premium']}만</div></div>
<div class="card"><span class="dim" style="font-size:13px">보증금</span><div class="price-num" style="font-size:22px">{s['deposit']}만</div></div>
<div class="card"><span class="dim" style="font-size:13px">월세</span><div class="price-num" style="font-size:22px">{s['rent']}만</div></div>
<div class="card"><span class="dim" style="font-size:13px">초기비용</span><div class="price-num" style="font-size:22px">{total}만</div></div>
</div>
<p class="dim" style="font-size:13px;margin-top:12px">※ 익명 게재 매물입니다. 정확한 위치·상호는 매수 문의 시 안내됩니다.</p>
</div></section>

<section class="section reveal" style="max-width:760px">
<h2>매물 정보</h2>
<table style="width:100%;font-size:15px;line-height:2.4;color:var(--muted);margin-top:10px">
<tr><td class="dim">지역</td><td style="text-align:right">{s['region']} {s['district']}</td></tr>
<tr><td class="dim">업종</td><td style="text-align:right">{s['industry']}</td></tr>
<tr><td class="dim">면적</td><td style="text-align:right">{s['area']}평</td></tr>
<tr><td class="dim">상권</td><td style="text-align:right">{s['label']}</td></tr>
<tr><td class="dim">권리금</td><td style="text-align:right">{s['premium']}만원</td></tr>
<tr><td class="dim">보증금</td><td style="text-align:right">{s['deposit']}만원</td></tr>
<tr><td class="dim">월세</td><td style="text-align:right">{s['rent']}만원</td></tr>
<tr><td class="dim">월매출</td><td style="text-align:right">{s['revenue']}만원</td></tr>
<tr><td class="dim">월순익</td><td style="text-align:right">{s['profit']}만원</td></tr>
</table>

<h2 style="margin-top:34px">매물 특징</h2>
<p class="note-text" style="margin-top:12px">{pf} 본 매물은 {s['label']} 입지의 {s['area']}평 규모로, {s['industry']} 운영에 적합한 환경을 갖추고 있습니다. 안정적인 월매출({s['revenue']}만원)과 순익({s['profit']}만원)을 유지해 온 매물입니다.</p>

<h2 style="margin-top:34px">매수 전 체크포인트</h2>
<ul style="color:var(--muted);margin:12px 0 0 18px;line-height:2.1">
<li>임대차 계약 조건과 잔여 계약 기간 확인</li>
<li>월매출·순익의 최근 3~6개월 추이 검토</li>
<li>영업 신고·사업자 승계 가능 여부 확인</li>
<li>기존 단골·예약 인계 범위 협의</li>
<li>시설·집기 인수 범위와 상태 점검</li>
</ul>
<div class="linkbox" style="margin-top:30px"><h3>매수 문의</h3>
<p>이 매물에 관심이 있으시면 아래로 문의하세요. 매수자와 1:1로 매칭됩니다.</p>
<a href="mailto:{COMPANY['email']}?subject=[매수문의] {s['title']}">{COMPANY['email']} 로 매수 문의 →</a></div>

<h2 style="margin-top:30px">관련 매물</h2>
<div class="linkbox">{related}</div>
</section>"""
    title = f"{s['title']} — 권리금 {s['premium']}만원·월매출 {s['revenue']}만 | {COMPANY['brand']} 업소매매"
    desc = f"{s['region']} {s['district']} {s['industry']} 마사지샵 양도. 권리금 {s['premium']}만원, 월매출 {s['revenue']}만원, 월순익 {s['profit']}만원, {s['area']}평. 익명 게재·수수료 0원."
    return (f"/shop-sale/{s['id']}/", page(title, desc, f"/shop-sale/{s['id']}/", body, g, "website", show_promo=False))


def get_profile_for_region(s):
    # 매물 지역의 행정구 프로필 시장 설명 주입
    for r in REGIONS:
        for ds, dn in r["districts"]:
            if dn == s["district"]:
                return get_profile(ds, dn)["market"]
    return f"{s['district']}는 마사지 수요가 안정적인 권역입니다."


# ── 공지사항 ─────────────────────────────────────────────────
PRIO_COLOR = {"긴급": "b-vvip", "중요": "b-vip", "일반": "b-premium"}

def notices_index():
    cards = "".join(
        f'<a class="card cv" href="/notices/{n["slug"]}/">'
        f'<span class="ad-badge {PRIO_COLOR[n["priority"]]}">{n["priority"]}</span> <span class="tag">{n["cat"]}</span>'
        f'<h3 style="margin:12px 0 6px">{n["title"]}</h3><p style="font-size:14px">{n["lead"]}</p>'
        f'<p class="dim" style="font-size:13px;margin-top:8px">{n["date"]}</p></a>' for n in NOTICES)
    g = [{"@type": "CollectionPage", "name": "공지사항", "url": U + "/notices/"},
         breadcrumb([("홈", "/"), ("공지사항", "/notices/")])]
    body = f"""<section class="hero"><div class="hero-grid reveal">
<div class="kicker">공지사항</div><h1>마톡<br><span class="grad-text">공지사항</span></h1>
<p class="lead" style="margin-top:18px">안전·정책·신고 채널 안내를 확인하세요.</p>
</div></section>
<section class="section reveal"><div class="grid g2">{cards}</div></section>"""
    return ("/notices/", page(f"공지사항 — 안전·정책 안내 | {COMPANY['brand']}",
            "마톡 공지사항. 해외 취업 사기 주의, 불법 영업 모니터링 정책, 신입 안전 수칙, 피해 신고 채널 안내.",
            "/notices/", body, g))


def notice_article(n):
    secs = NOTICE_BODIES.get(n["slug"], [])
    notes = "".join(
        f'<div class="note-card reveal"><div class="note-num">{i+1:02d}</div><div class="note-content">'
        f'<h3 class="note-title" id="s{i+1}">{t}</h3><div class="note-text"><p>{b}</p></div></div></div>'
        for i, (t, b) in enumerate(secs))
    toc = "".join(f'<a href="#s{i+1}">{t}</a>' for i, (t, _) in enumerate(secs))
    others = "".join(f'<a href="/notices/{o["slug"]}/">{o["title"]}</a>'
                     for o in NOTICES if o["slug"] != n["slug"])[:500]
    g = [{"@type": "Article", "headline": n["title"], "description": n["lead"],
          "author": {"@type": "Organization", "name": COMPANY["brand"] + " 운영팀"},
          "datePublished": n["date"], "dateModified": "2026-05-01", "publisher": {"@id": U + "/#org"}},
         breadcrumb([("홈", "/"), ("공지사항", "/notices/"), (n["title"], f"/notices/{n['slug']}/")])]
    body = f"""<article class="wrap" style="max-width:760px;padding-top:80px">
<div class="breadcrumb"><a href="/">홈</a> › <a href="/notices/">공지사항</a> › {n['cat']}</div>
<span class="ad-badge {PRIO_COLOR[n['priority']]}">{n['priority']}</span> <span class="tag">{n['cat']}</span>
<h1 style="font-size:clamp(28px,4.5vw,44px);margin:14px 0 12px">{n['title']}</h1>
<p class="lead">{n['lead']}</p>
<p class="dim" style="font-size:13px;margin-top:8px">{COMPANY['brand']} 운영팀 · {n['date']}</p>
<div class="toc"><h4>목차</h4>{toc}</div>{notes}
<div class="linkbox"><h3>마사지 일자리 안전하게 시작하기 — 관련 안내</h3>
<a href="/magazine/safe-workplace/">안전한 일터 고르는 법</a>
<a href="/magazine/contract-checklist/">근로계약서 체크리스트</a>
<a href="/jobs/">합법 검증된 구인공고 보기</a></div>
<h2 style="font-size:24px;margin-top:36px">다른 공지</h2><div class="linkbox">{others}</div></article>"""
    title = f"{n['title']} | {COMPANY['brand']} 공지사항"
    desc = n["lead"] + f" {COMPANY['brand']} 공지사항."
    return (f"/notices/{n['slug']}/", page(title, desc, f"/notices/{n['slug']}/", body, g, "article"))


def build_core_pages():
    pages = [main_page(), about_page(), contact_page(), pricing_page(), reviews_page(),
             recruitment_pricing_page(), shop_sale_pricing_page(), pricing_ads_page(),
             contact_ads_page(), shop_sale_index(), notices_index()]
    pages += policy_pages()
    for s in SHOP_SALES:
        pages.append(shop_sale_detail(s))
    for n in NOTICES:
        pages.append(notice_article(n))
    return pages
