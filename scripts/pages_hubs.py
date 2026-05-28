# -*- coding: utf-8 -*-
"""허브 페이지: 구인허브·업종채용·구직허브·업종구직·관리사 국적·매거진."""

from data import INDUSTRIES, NATIONALITIES, COMPANY, MAGAZINE
from templates import U, page, breadcrumb, faq_node, faq_html
from ads import render_tier

# ── 업종 구직 상세 데이터 (전부 고유) ────────────────────────
SEEKER_DETAIL = {
 "swedish": {"apt": "오일 마사지의 흐름과 압 조절을 꾸준히 익히려는 사람에게 맞습니다. 가장 보편적인 업종이라 첫 입직 종목으로 적합합니다.",
   "body": "전신을 다루는 만큼 손목·어깨 지구력이 중요합니다. 하루 5~7타임을 견디는 코어 체력을 갖추면 안정적입니다.",
   "income": "신입 일급 14만원대에서 시작해 경력·단골 확보 시 22만원까지 형성됩니다. 수요가 가장 많아 일감 확보가 쉽습니다.",
   "caution": "정형화된 루틴에 안주하면 차별화가 어렵습니다. 압 조절과 응대로 재방문을 만드는 것이 핵심입니다.",
   "career": "스웨디시로 기본기를 다진 뒤 아로마·딥티슈로 확장하는 경로가 일반적입니다.",
   "intro": "스웨디시는 오일을 이용해 전신을 부드럽게 이완시키는 마사지로, 국내 로드샵에서 가장 수요가 많은 업종입니다. 입직 진입 장벽이 낮아 신입이 첫 종목으로 선택하기 좋고, 일감이 풍부해 안정적으로 경험을 쌓을 수 있습니다. 보편적인 만큼 경쟁도 있어, 압 조절과 응대 디테일로 차별화하는 것이 장기 수입의 관건입니다.",
   "day": "하루 일과는 보통 오후에 출근해 매장 준비와 위생 점검으로 시작합니다. 예약과 워크인을 번갈아 응대하며 타임 사이에 비품을 정리하고 컨디션을 회복합니다. 저녁 피크 시간대에 예약이 몰리므로 체력 안배가 중요하며, 마감 후 시술 베드와 수건을 정리하고 다음 날을 준비합니다.",
   "q": [("스웨디시 신입 교육 기간은?", "보통 2~4주 수습 교육을 거쳐 실무에 투입됩니다."),
         ("체력이 약해도 가능한가요?", "타임 수를 조절하며 시작할 수 있습니다. 코어·손목 관리가 중요합니다."),
         ("자격증이 꼭 필요한가요?", "필수는 아니나 관련 교육 이수가 채용에 유리합니다.")]},
 "aroma": {"apt": "향과 분위기 연출에 관심이 있고 섬세한 응대를 선호하는 사람에게 맞습니다. 프리미엄 객단가가 높습니다.",
   "body": "압은 스웨디시보다 부드럽지만 향·온도 관리 등 디테일이 많아 집중력이 필요합니다.",
   "income": "신입 15만원대, 프리미엄 상권 경력자는 23만원까지 형성됩니다. 고소득 단골 확보 시 안정적입니다.",
   "caution": "에센셜 오일 알레르기·향 민감 고객 응대에 주의가 필요합니다.",
   "career": "아로마 전문성에 스파 매니지먼트 역량을 더하면 관리자로 성장할 수 있습니다.",
   "intro": "아로마는 에센셜 오일의 향과 시술을 결합해 깊은 릴렉세이션을 제공하는 업종으로, 프리미엄 상권에서 특히 객단가가 높게 형성됩니다. 강한 압보다 분위기와 응대 디테일이 만족도를 좌우하기 때문에, 섬세한 서비스에 강점이 있는 사람에게 유리합니다. 고소득 단골을 확보하면 수입의 변동성이 크게 줄어듭니다.",
   "day": "출근 후에는 디퓨저와 오일, 조명·음악 등 매장 분위기를 먼저 세팅합니다. 고객의 컨디션과 향 선호를 확인하며 응대하고, 시술 사이사이 환기와 향 관리에 신경 씁니다. 프리미엄 매장일수록 정시 예약 운영과 청결 관리가 중요해 시간 배분이 핵심입니다.",
   "q": [("아로마와 스웨디시 차이는?", "아로마는 향과 릴렉세이션 중심, 스웨디시는 오일 압 마사지 중심입니다."),
         ("향 지식이 필요한가요?", "기본 에센셜 오일 지식을 갖추면 응대에 큰 도움이 됩니다."),
         ("프리미엄 매장 취업 조건은?", "응대 매너와 청결 관리, 일정 경력을 우대합니다.")]},
 "thai": {"apt": "스트레칭과 지압을 결합한 동적인 시술을 선호하는 사람에게 맞습니다. 본인 체력이 좋아야 합니다.",
   "body": "체중을 실어 압을 주고 스트레칭을 보조하므로 전신 근력과 유연성이 요구됩니다.",
   "income": "신입 15만원대에서 경력자 24만원까지 형성됩니다. 정통 기법 숙련자는 단가가 높습니다.",
   "caution": "잘못된 스트레칭은 부상 위험이 있어 정확한 기법 습득이 필수입니다.",
   "career": "타이 정통 기법 숙련 후 강사·교육자로 발전하는 경로가 있습니다.",
   "intro": "타이 마사지는 지압과 스트레칭을 결합한 전통 태국식 기법으로, 시술자의 체력과 정확한 기법이 무엇보다 중요합니다. 정통 기법을 숙련할수록 단가가 높아지고, 강한 압과 스트레칭을 선호하는 고정 고객층이 두텁다는 점이 강점입니다. 기법 교육에 충분히 투자하면 강사·교육자로 커리어를 확장할 수 있습니다.",
   "day": "타이는 오일 없이 편한 복장으로 진행하는 경우가 많아, 출근 후 시술 매트와 공간을 먼저 정돈합니다. 스트레칭 동작이 많아 본인의 워밍업과 체력 관리가 일과의 일부입니다. 시술 강도가 높은 만큼 타임 간 휴식과 손·관절 관리로 부상을 예방하는 것이 중요합니다.",
   "q": [("타이 마사지는 오일을 쓰나요?", "전통 타이는 오일 없이 옷을 입고 진행하는 경우가 많습니다."),
         ("유연성이 필요한가요?", "스트레칭 보조를 위해 본인의 유연성과 근력이 중요합니다."),
         ("정통 교육은 어디서 받나요?", "전문 교육원이나 매장 자체 교육으로 습득합니다.")]},
 "lomilomi": {"apt": "리듬감 있는 손동작과 흐르는 듯한 시술을 선호하는 사람에게 맞습니다. 예술적 감각이 도움이 됩니다.",
   "body": "팔뚝 전체를 사용하는 긴 스트로크가 많아 어깨·팔 지구력이 필요합니다.",
   "income": "신입 15만원대, 경력자 22만원까지 형성됩니다. 차별화 종목이라 전문성이 단가를 좌우합니다.",
   "caution": "기법 숙련도가 만족도를 크게 좌우하므로 충분한 연습이 필요합니다.",
   "career": "로미로미 전문가로 차별화하면 프리미엄 스파에서 강점이 됩니다.",
   "intro": "로미로미는 하와이 전통 기법으로, 팔뚝 전체를 사용한 길고 리듬감 있는 스트로크가 특징입니다. 흔하지 않은 차별화 종목이라 전문성을 갖추면 프리미엄 스파에서 강력한 경쟁력이 됩니다. 손동작의 리듬과 흐름을 익히는 데 시간이 필요하지만, 숙련될수록 단가와 만족도가 함께 올라갑니다.",
   "day": "시술 전 오일과 매장 분위기를 세팅하고, 긴 스트로크를 안정적으로 구사하기 위해 어깨·팔 워밍업을 합니다. 리듬감이 핵심이라 시술 중 호흡과 동작의 일관성을 유지하는 데 집중합니다. 타임 사이에는 팔·어깨 피로를 풀어 다음 시술의 완성도를 지킵니다.",
   "q": [("로미로미는 어떤 마사지인가요?", "하와이 전통 기법으로 리듬감 있는 긴 스트로크가 특징입니다."),
         ("배우기 어렵나요?", "기본 손동작 습득 후 리듬감을 익히는 데 시간이 필요합니다."),
         ("수요가 많은가요?", "차별화 종목으로 프리미엄 상권에서 수요가 있습니다.")]},
 "sports": {"apt": "근육 구조에 관심이 있고 강한 압을 다루는 시술을 선호하는 사람에게 맞습니다.",
   "body": "딥티슈 위주라 강한 압을 지속할 수 있는 상체 근력이 핵심입니다.",
   "income": "신입 16만원대, 경력자 26만원까지로 일급 상한이 가장 높은 편입니다. 산단·운동 인구 수요가 강합니다.",
   "caution": "과한 압은 고객 부상 위험이 있어 근육 해부학 이해가 필요합니다.",
   "career": "스포츠 마사지에 재활·트레이닝 지식을 더하면 전문가로 성장합니다.",
   "intro": "스포츠 마사지는 근육 회복과 컨디셔닝에 특화된 딥티슈 중심 업종으로, 일급 상한이 가장 높은 편에 속합니다. 운동 인구와 산업단지 종사자 등 근육 피로 회복 수요가 두터워 평일 매출이 안정적입니다. 근육 해부학에 대한 이해를 갖추면 정확한 시술로 신뢰를 얻고 단가를 높일 수 있습니다.",
   "day": "출근 후 시술 베드와 보조 도구를 점검하고, 강한 압을 안정적으로 주기 위해 본인의 상체 컨디션을 확인합니다. 고객의 통증 부위와 운동 이력을 문진한 뒤 시술 강도를 조절합니다. 딥티슈는 체력 소모가 커 타임 간 충분한 회복과 손목·팔 관리가 필수입니다.",
   "q": [("스포츠 마사지 자격이 필요한가요?", "관련 교육이나 자격이 채용에 유리합니다."),
         ("힘이 많이 드나요?", "딥티슈 위주라 상체 근력과 지구력이 중요합니다."),
         ("주 고객층은?", "운동 인구, 산단 종사자 등 근육 피로 회복 수요가 많습니다.")]},
}

# ── 관리사 국적 상세 데이터 ──────────────────────────────────
THERAPIST_DETAIL = {
 "korean": {"strength": "한국어 소통이 자유로워 단골 응대와 세밀한 요구 반영에 강점이 있습니다.",
   "pref": "스웨디시·아로마 등 응대 비중이 큰 업종에서 선호됩니다.",
   "visa": "체류 자격 제약이 없어 근무 형태 선택이 자유롭습니다.",
   "strategy": "응대력을 무기로 프리미엄 상권 단골을 확보하면 일급 상한이 높습니다.",
   "trend": "한국 국적 관리사는 언어 장벽이 없어 고객의 세밀한 요구를 정확히 반영할 수 있다는 점이 가장 큰 경쟁력입니다. 최근에는 프리미엄 상권을 중심으로 응대력 좋은 한국 관리사에 대한 선호가 뚜렷하게 높아지고 있습니다. 단골 관리와 정기 예약 운영에 강해 수입의 안정성이 높은 편입니다."},
 "chinese": {"strength": "지압·경락 등 강한 압을 선호하는 고객층에 강세를 보입니다.",
   "pref": "타이·지압 계열, 강한 압 수요 매장에서 선호됩니다.",
   "visa": "체류 자격에 따라 근무 가능 범위가 달라 사전 확인이 필요합니다.",
   "strategy": "강한 압 전문성을 살려 근육 회복 수요 상권을 공략하는 전략이 유효합니다.",
   "trend": "중국 국적 관리사는 지압과 경락 등 강한 압 기법에 익숙해, 묵직한 압을 선호하는 고객층에서 꾸준한 수요가 있습니다. 산업단지나 운동 인구가 많은 상권에서 근육 회복 목적의 예약과 잘 맞습니다. 체류 자격에 따라 근무 가능 범위가 달라지므로 합법 절차 확인이 전제입니다."},
 "thai": {"strength": "정통 타이 기법과 스트레칭의 본고장 출신으로 전문성이 높습니다.",
   "pref": "타이 마사지 전문 매장에서 가장 선호됩니다.",
   "visa": "취업 비자·체류 자격 확인이 채용의 전제 조건입니다.",
   "strategy": "정통 타이 전문성을 차별화 포인트로 삼으면 단가 협상에 유리합니다.",
   "trend": "태국 국적 관리사는 정통 타이 기법과 스트레칭의 본고장 출신이라는 전문성으로 타이 전문 매장에서 가장 선호됩니다. 정통성을 강조하는 매장이 늘면서 숙련 관리사에 대한 수요가 안정적으로 유지되고 있습니다. 취업·체류 자격을 갖춘 합법 채용이 무엇보다 중요합니다."},
 "vietnamese": {"strength": "섬세한 손기술과 성실한 근무 태도로 평가가 좋습니다.",
   "pref": "스웨디시·아로마 등 폭넓은 업종에서 수요가 있습니다.",
   "visa": "체류 자격에 따른 근무 제약을 반드시 확인해야 합니다.",
   "strategy": "성실함과 손기술로 단골 신뢰를 쌓는 장기 근속 전략이 적합합니다.",
   "trend": "베트남 국적 관리사는 섬세한 손기술과 성실한 근무 태도로 현장 평가가 좋아, 스웨디시·아로마 등 폭넓은 업종에서 수요가 형성됩니다. 장기 근속하며 단골 신뢰를 쌓는 사례가 많아 매장 입장에서도 선호도가 높습니다. 체류 자격에 따른 근무 제약은 반드시 사전에 확인해야 합니다."},
 "russian": {"strength": "프리미엄 스웨디시·아로마 고급 수요에 대응하는 강점이 있습니다.",
   "pref": "프리미엄 스파, 외국인 고객 상권에서 선호됩니다.",
   "visa": "취업·체류 자격 확인이 필수이며 합법 절차가 중요합니다.",
   "strategy": "프리미엄 상권의 고급 수요를 공략하면 높은 객단가를 기대할 수 있습니다.",
   "trend": "러시아 국적 관리사는 프리미엄 스웨디시·아로마의 고급 수요에 대응하는 강점으로, 외국인 고객이 많은 상권과 프리미엄 스파에서 선호됩니다. 고급 서비스 수요가 꾸준히 성장하면서 객단가가 높게 형성되는 편입니다. 취업·체류 자격 확인과 합법 절차가 채용의 필수 전제입니다."},
 "japanese": {"strength": "디테일한 응대와 청결 관리로 단골 만족도가 높습니다.",
   "pref": "프리미엄 아로마·스파 매장에서 선호됩니다.",
   "visa": "체류 자격 확인 후 근무 형태를 결정합니다.",
   "strategy": "섬세한 응대와 청결 관리를 강점으로 단골 충성도를 높이는 전략이 효과적입니다.",
   "trend": "일본 국적 관리사는 디테일한 응대와 철저한 청결 관리로 단골 만족도가 높아, 프리미엄 아로마·스파 매장에서 선호됩니다. 세심한 서비스를 중시하는 고객층에서 재방문율이 높게 나타납니다. 체류 자격을 확인한 뒤 근무 형태를 결정하는 것이 일반적입니다."},
}


def jobs_index():
    cards = "".join(
        f'<a class="card cv" href="/jobs/{i["slug"]}/"><span class="tag">{i["name"]}</span>'
        f'<h3 style="margin:12px 0 6px">{i["name"]} 마사지 구인공고</h3>'
        f'<p style="font-size:14px">{i["tag"]}</p>'
        f'<p style="color:var(--blue-1);font-weight:700;margin-top:10px">평균 일급 {i["wage"]}만원 →</p></a>'
        for i in INDUSTRIES)
    body = f"""<section class="hero"><div class="hero-grid reveal">
<div class="kicker">마사지 구인공고</div>
<h1>업종별 마사지<br><span class="grad-text">관리사 채용</span></h1>
<p class="lead" style="margin-top:18px">스웨디시·아로마·타이·로미로미·스포츠 5개 업종의 구인공고를 업종별로 확인하세요.</p>
</div></section>
{render_tier('vvip', limit=4)}
<section class="section"><div class="grid g3">{cards}</div></section>
{render_tier('vip', limit=6)}"""
    g = [{"@type": "CollectionPage", "name": "마사지 구인공고", "url": U + "/jobs/"},
         breadcrumb([("홈", "/"), ("구인공고", "/jobs/")])]
    return ("/jobs/", page("마사지 구인공고 — 업종별 관리사 채용 | " + COMPANY["brand"],
            "스웨디시·아로마·타이·로미로미·스포츠 마사지 관리사 구인공고. 업종별 평균 일급과 채용 정보를 확인하세요. 마톡 합법 채용 플랫폼.",
            "/jobs/", body, g))


def industry_job_page(ind):
    s, n = ind["slug"], ind["name"]
    faqs = [
        (f"{n} 마사지 관리사 평균 일급은?", f"{n}의 평균 일급은 {ind['wage_lo']}만~{ind['wage_hi']}만원 선입니다. 경력과 상권에 따라 상한이 달라집니다."),
        (f"{n} 신입도 지원할 수 있나요?", f"네. {n} 신입 교육을 운영하는 매장이 많아 수습을 거쳐 정착할 수 있습니다."),
        (f"{n} 근무 시간은 어떻게 되나요?", "매장별로 다르나 보통 오후~심야 영업이 일반적이며, 파트·풀타임 선택이 가능합니다."),
        (f"{n} 마사지의 특징은?", f"{ind['tag']}입니다. 해당 업종 특유의 기법 숙련도가 단가를 좌우합니다."),
        (f"{n} 자격증이 필요한가요?", "필수는 아니나 관련 교육 이수가 채용과 단가에 유리합니다."),
    ]
    monthly = ind["wage"] * 26
    g = [{"@type": "Service", "name": f"{n} 마사지 관리사 채용", "serviceType": "구인구직",
          "provider": {"@id": U + "/#org"}},
         faq_node(faqs),
         breadcrumb([("홈", "/"), ("구인공고", "/jobs/"), (f"{n} 마사지", f"/jobs/{s}/")])]
    body = f"""<section class="hero"><div class="hero-grid reveal">
<div class="breadcrumb"><a href="/">홈</a> › <a href="/jobs/">구인공고</a> › {n} 마사지</div>
<div class="kicker">{n} 마사지 구인공고</div>
<h1>{n} 마사지<br><span class="grad-text">관리사 모집</span></h1>
<p class="lead" style="margin-top:18px">{ind['tag']}.</p>
<div class="chips"><span class="chip">평균 일급 <b>{ind['wage']}만원</b></span>
<span class="chip">월 환산 <b>약 {monthly}만원</b></span><span class="chip">일급 <b>{ind['wage_lo']}~{ind['wage_hi']}만원</b></span></div>
</div></section>

{render_tier('vvip', industry=n, limit=4)}

<section class="section reveal" style="max-width:760px">
<div class="kicker">업종 특성</div><h2 style="margin:6px 0 16px">{n} 마사지 4가지 핵심</h2>
<div class="note-card"><div class="note-num">01</div><div class="note-content"><h3 class="note-title">시장 개요</h3>
<div class="note-text"><p>{n}는 {ind['tag']}로, 수요가 꾸준한 업종입니다. 전국 로드샵에서 폭넓게 채용이 이루어지며 신입과 경력 모두 기회가 있습니다.</p></div></div></div>
<div class="note-card"><div class="note-num">02</div><div class="note-content"><h3 class="note-title">필요 역량</h3>
<div class="note-text"><p>{SEEKER_DETAIL[s]['body']}</p></div></div></div>
<div class="note-card"><div class="note-num">03</div><div class="note-content"><h3 class="note-title">근무 패턴</h3>
<div class="note-text"><p>주로 오후부터 심야까지 영업하며, 파트·풀타임 선택이 가능합니다. 상권에 따라 주간·야간 예약 비중이 다릅니다.</p></div></div></div>
<div class="note-card"><div class="note-num">04</div><div class="note-content"><h3 class="note-title">수입 구조</h3>
<div class="note-text"><p>{SEEKER_DETAIL[s]['income']}</p></div></div></div>
</section>

{render_tier('vip', industry=n, limit=6)}

<section class="section reveal"><h2 style="font-size:26px">{n} 채용 자주 묻는 질문</h2>{faq_html(faqs)}</section>

{render_tier('premium', limit=8)}

<div class="linkbox" style="max-width:1100px;margin:0 auto 40px"><h3>{n} 함께 보면 좋은 정보</h3>
<a href="/seekers/{s}/">{n} 구직 가이드 — 적성·수입·면접</a>
<a href="/pricing/">전국 마사지 급여 시세표</a>
<a href="/locations/seoul/">서울 {n} 채용 지역으로 보기</a></div>"""
    title = f"{n} 마사지 관리사 구인공고 — 평균 일급 {ind['wage']}만원 | {COMPANY['brand']}"
    desc = f"{n} 마사지 관리사 구인공고. 평균 일급 {ind['wage']}만원(월 약 {monthly}만원), {ind['tag']}. 신입·경력 채용 정보를 마톡에서 확인하세요."
    return (f"/jobs/{s}/", page(title, desc, f"/jobs/{s}/", body, g))


def seekers_index():
    cards = "".join(
        f'<a class="card cv" href="/seekers/{i["slug"]}/"><span class="tag">{i["name"]}</span>'
        f'<h3 style="margin:12px 0 6px">{i["name"]} 마사지 구직 가이드</h3>'
        f'<p style="font-size:14px">{SEEKER_DETAIL[i["slug"]]["apt"][:50]}…</p></a>'
        for i in INDUSTRIES)
    body = f"""<section class="hero"><div class="hero-grid reveal">
<div class="kicker">마사지 구직 가이드</div>
<h1>마사지 관리사<br><span class="grad-text">구직 가이드</span></h1>
<p class="lead" style="margin-top:18px">업종별 적성·체력·수입·면접 정보를 정리했습니다. 나에게 맞는 업종을 찾아보세요.</p>
</div></section>
<section class="section"><div class="grid g3">{cards}</div></section>"""
    g = [{"@type": "CollectionPage", "name": "마사지 구직 가이드", "url": U + "/seekers/"},
         breadcrumb([("홈", "/"), ("구직 가이드", "/seekers/")])]
    return ("/seekers/", page("마사지 구직 가이드 — 업종별 적성·수입·면접 | " + COMPANY["brand"],
            "스웨디시·아로마·타이·로미로미·스포츠 마사지 구직 가이드. 업종별 적성·체력·수입·면접 정보를 한눈에 정리했습니다.",
            "/seekers/", body, g))


def seeker_page(ind):
    s, n = ind["slug"], ind["name"]
    d = SEEKER_DETAIL[s]
    faqs = d["q"]
    g = [{"@type": "Article", "headline": f"{n} 마사지 구직 가이드",
          "author": {"@type": "Organization", "name": COMPANY["brand"]},
          "datePublished": "2026-01-10", "dateModified": "2026-05-01"},
         faq_node(faqs),
         breadcrumb([("홈", "/"), ("구직 가이드", "/seekers/"), (f"{n}", f"/seekers/{s}/")])]
    body = f"""<section class="hero"><div class="hero-grid reveal">
<div class="breadcrumb"><a href="/">홈</a> › <a href="/seekers/">구직 가이드</a> › {n}</div>
<div class="kicker">{n} 마사지 구직 가이드</div>
<h1>{n} 마사지<br><span class="grad-text">구직 완벽 가이드</span></h1>
<p class="lead" style="margin-top:18px">{n} 마사지가 나에게 맞는지, 수입과 면접은 어떤지 한눈에 정리했습니다.</p>
</div></section>
<section class="section reveal" style="max-width:760px">
<div class="kicker">업종 개요</div><h2 style="margin:6px 0 14px">{n} 마사지란</h2>
<p class="note-text">{d['intro']}</p>
<h3 style="margin-top:26px">{n} 관리사의 하루</h3>
<p class="note-text" style="margin-top:8px">{d['day']}</p>
</section>
<section class="section reveal"><div class="grid g2">
<div class="card"><span class="tag">적성</span><h3 style="margin:10px 0 6px">이런 사람에게 맞아요</h3><p>{d['apt']}</p></div>
<div class="card"><span class="tag">체력</span><h3 style="margin:10px 0 6px">필요한 체력</h3><p>{d['body']}</p></div>
<div class="card"><span class="tag">수입</span><h3 style="margin:10px 0 6px">수입 구조</h3><p>{d['income']}</p></div>
<div class="card"><span class="tag">주의점</span><h3 style="margin:10px 0 6px">알아둘 단점</h3><p>{d['caution']}</p></div>
<div class="card" style="grid-column:1/-1"><span class="tag">커리어</span><h3 style="margin:10px 0 6px">성장 경로</h3><p>{d['career']}</p></div>
</div></section>
<section class="section reveal"><h2 style="font-size:26px">{n} 구직 자주 묻는 질문</h2>{faq_html(faqs)}</section>
<div class="linkbox" style="max-width:1100px;margin:0 auto 40px"><h3>{n} 다음 단계</h3>
<a href="/jobs/{s}/">{n} 마사지 구인공고 보기</a>
<a href="/magazine/interview-tips/">면접 합격 7가지 공통점</a>
<a href="/pricing/">전국 급여 시세표 확인</a></div>"""
    title = f"{n} 마사지 구직 가이드 — 적성·체력·수입·면접 완벽 정리 | {COMPANY['brand']}"
    desc = f"{n} 마사지 구직 가이드. {d['apt'][:60]} 수입·면접·커리어까지 마톡이 정리했습니다."
    if len(desc) > 155:
        desc = desc[:152] + "…"
    return (f"/seekers/{s}/", page(title, desc, f"/seekers/{s}/", body, g, "article"))


def therapist_page(nat):
    s, n = nat["slug"], nat["name"]
    d = THERAPIST_DETAIL[s]
    faqs = [
        (f"{n} 관리사는 어떤 업종에 강한가요?", d["pref"]),
        (f"{n} 관리사 평균 단가는?", f"{n} 관리사의 평균 일급은 약 {nat['wage']}만원 선입니다. 전문성과 상권에 따라 달라집니다."),
        (f"{n} 관리사 채용 시 체류 자격은?", d["visa"]),
    ]
    g = [{"@type": "Article", "headline": f"{n} 마사지 관리사 채용 가이드",
          "author": {"@type": "Organization", "name": COMPANY["brand"]},
          "datePublished": "2026-01-15", "dateModified": "2026-05-01"},
         faq_node(faqs),
         breadcrumb([("홈", "/"), ("관리사", "/therapists/"), (n, f"/therapists/{s}/")])]
    body = f"""<section class="hero"><div class="hero-grid reveal">
<div class="breadcrumb"><a href="/">홈</a> › 관리사 › {n}</div>
<div class="kicker">{n} 마사지 관리사</div>
<h1>{n} 관리사<br><span class="grad-text">채용 가이드</span></h1>
<p class="lead" style="margin-top:18px">{nat['tag']}.</p>
<div class="chips"><span class="chip">평균 단가 <b>{nat['wage']}만원</b></span><span class="chip">수요 <b>{nat['demand']}</b></span></div>
</div></section>
<section class="section reveal" style="max-width:760px">
<div class="kicker">시장 트렌드</div><h2 style="margin:6px 0 14px">{n} 관리사 채용 시장</h2>
<p class="note-text">{d['trend']}</p>
</section>
<section class="section reveal"><div class="grid g2">
<div class="card"><span class="tag">강점</span><h3 style="margin:10px 0 6px">{n} 관리사의 강점</h3><p>{d['strength']}</p></div>
<div class="card"><span class="tag">선호 업종</span><h3 style="margin:10px 0 6px">선호 업종</h3><p>{d['pref']}</p></div>
<div class="card"><span class="tag">체류 자격</span><h3 style="margin:10px 0 6px">체류·근무 조건</h3><p>{d['visa']}</p></div>
<div class="card"><span class="tag">단가 전략</span><h3 style="margin:10px 0 6px">단가 전략</h3><p>{d['strategy']}</p></div>
</div></section>
<section class="section reveal" style="max-width:760px">
<div class="kicker">매칭 전략</div><h2 style="margin:6px 0 14px">{n} 관리사 취업·정착 가이드</h2>
<p class="note-text">{n} 관리사로 일자리를 찾을 때는 본인의 강점({d['strength']})을 살릴 수 있는 매장을 우선 고려하는 것이 좋습니다. {d['strategy']} 마톡은 합법 신고 업체의 공고만 게재하므로, 체류 자격과 근로계약 조건을 명확히 확인한 뒤 안전하게 입직할 수 있습니다. 평균 단가 {nat['wage']}만원을 기준으로 경력과 상권에 따라 협상하면 합리적인 조건을 찾을 수 있습니다.</p>
</section>
<section class="section reveal"><h2 style="font-size:26px">{n} 관리사 자주 묻는 질문</h2>{faq_html(faqs)}</section>
<div class="linkbox" style="max-width:1100px;margin:0 auto 40px"><h3>함께 보면 좋은 정보</h3>
<a href="/jobs/">업종별 마사지 구인공고</a><a href="/pricing/">급여 시세표</a><a href="/about/">마톡 운영 방식</a></div>"""
    title = f"{n} 마사지 관리사 채용 — 선호 업종·평균 단가·체류 조건 | {COMPANY['brand']}"
    desc = f"{n} 마사지 관리사 채용 가이드. {d['strength'][:50]} 선호 업종·평균 단가 {nat['wage']}만원·체류 조건까지 정리."
    if len(desc) > 155:
        desc = desc[:152] + "…"
    return (f"/therapists/{s}/", page(title, desc, f"/therapists/{s}/", body, g, "article"))


def therapists_index():
    cards = "".join(
        f'<a class="card cv" href="/therapists/{n["slug"]}/"><span class="tag">{n["name"]}</span>'
        f'<h3 style="margin:12px 0 6px">{n["name"]} 관리사 채용</h3>'
        f'<p style="font-size:14px">{n["tag"]}</p>'
        f'<p style="color:var(--blue-1);font-weight:700;margin-top:10px">평균 {n["wage"]}만원 · 수요 {n["demand"]} →</p></a>'
        for n in NATIONALITIES)
    body = f"""<section class="hero"><div class="hero-grid reveal">
<div class="kicker">관리사 국적별 안내</div>
<h1>국적별 마사지<br><span class="grad-text">관리사 채용</span></h1>
<p class="lead" style="margin-top:18px">국적별 선호 업종·평균 단가·체류 조건을 확인하세요.</p>
</div></section>
<section class="section"><div class="grid g3">{cards}</div></section>"""
    g = [{"@type": "CollectionPage", "name": "국적별 관리사 채용", "url": U + "/therapists/"},
         breadcrumb([("홈", "/"), ("관리사", "/therapists/")])]
    return ("/therapists/", page("국적별 마사지 관리사 채용 — 선호 업종·단가 | " + COMPANY["brand"],
            "한국·중국·태국·베트남·러시아·일본 마사지 관리사 채용 가이드. 국적별 선호 업종과 평균 단가, 체류 조건을 정리했습니다.",
            "/therapists/", body, g))


# ── 매거진 ───────────────────────────────────────────────────
def magazine_index():
    cards = "".join(
        f'<a class="card cv" href="/magazine/{m["slug"]}/"><span class="tag">{m["tag"]}</span>'
        f'<h3 style="margin:12px 0 8px">{m["title"]}</h3><p style="font-size:14px">{m["lead"]}</p>'
        f'<p class="dim" style="font-size:13px;margin-top:10px">{m["date"]} · {m["read"]}분</p></a>'
        for m in MAGAZINE)
    body = f"""<section class="hero"><div class="hero-grid reveal">
<div class="kicker">마톡 매거진</div>
<h1>마사지 관리사<br><span class="grad-text">커리어 매거진</span></h1>
<p class="lead" style="margin-top:18px">급여·취업·계약·안전까지, 현장 데이터 기반 가이드를 제공합니다.</p>
</div></section>
<section class="section"><div class="grid g3">{cards}</div></section>"""
    g = [{"@type": "CollectionPage", "name": "마톡 매거진", "url": U + "/magazine/"},
         breadcrumb([("홈", "/"), ("매거진", "/magazine/")])]
    return ("/magazine/", page("마톡 매거진 — 마사지 관리사 커리어 가이드 | " + COMPANY["brand"],
            "마사지 관리사 급여·취업·계약·안전 가이드. 현장 데이터 기반 매거진을 마톡에서 만나보세요.",
            "/magazine/", body, g))


def magazine_article(m):
    # 본문 7편 — 각 글마다 고유 노트카드 생성
    from magazine_bodies import MAGAZINE_BODIES
    sections = MAGAZINE_BODIES.get(m["slug"], [])
    notes = "".join(
        f'<div class="note-card reveal"><div class="note-num">{i+1:02d}</div><div class="note-content">'
        f'<h3 class="note-title" id="s{i+1}">{t}</h3><div class="note-text"><p>{b}</p></div></div></div>'
        for i, (t, b) in enumerate(sections))
    toc = "".join(f'<a href="#s{i+1}">{t}</a>' for i, (t, _) in enumerate(sections))
    others = "".join(
        f'<a href="/magazine/{o["slug"]}/">{o["title"]}</a>'
        for o in MAGAZINE if o["slug"] != m["slug"])[:600]
    g = [{"@type": "Article", "headline": m["title"], "description": m["lead"],
          "author": {"@type": "Organization", "name": COMPANY["brand"] + " 운영팀"},
          "datePublished": m["date"], "dateModified": "2026-05-01",
          "publisher": {"@id": U + "/#org"}, "image": U + "/assets/og.png"},
         breadcrumb([("홈", "/"), ("매거진", "/magazine/"), (m["title"], f"/magazine/{m['slug']}/")])]
    body = f"""<article class="wrap" style="max-width:760px;padding-top:80px">
<div class="breadcrumb"><a href="/">홈</a> › <a href="/magazine/">매거진</a> › {m['tag']}</div>
<span class="tag">{m['tag']}</span>
<h1 style="font-size:clamp(30px,5vw,46px);margin:14px 0 12px">{m['title']}</h1>
<p class="lead">{m['lead']}</p>
<p class="dim" style="font-size:13px;margin-top:8px">{COMPANY['brand']} 운영팀 · {m['date']} · 읽는 시간 {m['read']}분</p>
<div class="toc"><h4>목차</h4>{toc}</div>
{notes}
<div class="linkbox"><h3>마사지 관리사 급여·취업·지역 정보 더 알아보기</h3>
<a href="/pricing/">2026 전국 마사지 급여 시세표</a>
<a href="/jobs/">업종별 마사지 구인공고 전체 보기</a>
<a href="/seekers/">업종별 구직 가이드</a>
<a href="/notices/">안전·법령 공지사항</a></div>
<h2 style="font-size:24px;margin-top:40px">매거진 더 보기</h2>
<div class="linkbox">{others}</div>
</article>"""
    title = f"{m['title']} | {COMPANY['brand']} 매거진"
    desc = (f"{m['lead']} {COMPANY['brand']} 매거진이 매칭 로그·현장 인터뷰 기반으로 "
            f"{m['tag']} 가이드를 정리했습니다. 읽는 시간 약 {m['read']}분.")
    if len(desc) > 155:
        desc = desc[:152] + "…"
    return (f"/magazine/{m['slug']}/", page(title, desc, f"/magazine/{m['slug']}/", body, g, "article"))


def build_hub_pages():
    pages = [jobs_index(), seekers_index(), therapists_index(), magazine_index()]
    for i in INDUSTRIES:
        pages.append(industry_job_page(i))
        pages.append(seeker_page(i))
    for n in NATIONALITIES:
        pages.append(therapist_page(n))
    for m in MAGAZINE:
        pages.append(magazine_article(m))
    return pages
