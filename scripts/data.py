# -*- coding: utf-8 -*-
"""마톡(matalk.club) — 단일 데이터 소스.

모든 회사정보·업종·국적·지역·가격·매거진·공지·광고·매물 데이터를 여기서 관리한다.
데이터만 바꾸면 전 페이지가 자동 재생성된다.
"""

# ── 회사 정보 ────────────────────────────────────────────────
COMPANY = {
    "brand": "마톡",
    "brand_en": "Matalk",
    "domain": "matalk.club",
    "url": "https://matalk.club",
    "legal_name": "YH LAB",
    "ceo": "김수환",
    "biz_no": "815-26-00585",
    "job_info_no": "J1802020260002",   # 직업정보제공사업 신고번호
    "address": "경기도 파주시 청석로 268",
    "privacy_officer": "김수환",
    "tel": "0508-1234-5678",            # 광고문의·사용법 안내용
    "tel_hours": "평일 10:00~19:00",
    "email": "help@matalk.club",
    "desc": "전국 마사지 관리사 구인구직·로드샵 채용·업소매매 플랫폼",
}

# ── 업종 (마사지 종류) ───────────────────────────────────────
# slug, 이름, 평균 일급(만원), 한 줄 요약
INDUSTRIES = [
    {"slug": "swedish", "name": "스웨디시", "wage": 16,
     "tag": "오일을 이용한 전신 이완 마사지로 가장 수요가 많은 업종",
     "wage_lo": 14, "wage_hi": 22},
    {"slug": "aroma", "name": "아로마", "wage": 17,
     "tag": "에센셜 오일과 향을 결합한 릴렉세이션 중심 관리",
     "wage_lo": 15, "wage_hi": 23},
    {"slug": "thai", "name": "타이", "wage": 18,
     "tag": "스트레칭과 지압을 결합한 전통 태국식 마사지",
     "wage_lo": 15, "wage_hi": 24},
    {"slug": "lomilomi", "name": "로미로미", "wage": 17,
     "tag": "하와이 전통 기법으로 리듬감 있는 손동작이 특징",
     "wage_lo": 15, "wage_hi": 22},
    {"slug": "sports", "name": "스포츠", "wage": 19,
     "tag": "근육 회복과 컨디셔닝에 특화된 딥티슈 중심 관리",
     "wage_lo": 16, "wage_hi": 26},
]

# ── 관리사 국적 ──────────────────────────────────────────────
NATIONALITIES = [
    {"slug": "korean", "name": "한국", "wage": 18,
     "tag": "소통이 자유롭고 단골 응대에 강점", "demand": "매우 높음"},
    {"slug": "chinese", "name": "중국", "wage": 16,
     "tag": "지압·경락 등 강한 압 선호 고객층에 강세", "demand": "높음"},
    {"slug": "thai", "name": "태국", "wage": 17,
     "tag": "정통 타이 기법과 스트레칭의 본고장", "demand": "높음"},
    {"slug": "vietnamese", "name": "베트남", "wage": 15,
     "tag": "섬세한 손기술과 성실한 근무 태도", "demand": "보통"},
    {"slug": "russian", "name": "러시아", "wage": 20,
     "tag": "프리미엄 스웨디시·아로마 고급 수요에 대응", "demand": "보통"},
    {"slug": "japanese", "name": "일본", "wage": 19,
     "tag": "디테일한 응대와 청결 관리로 단골 만족도 높음", "demand": "보통"},
]

# ── 지역 (광역시도 → 행정구) ─────────────────────────────────
REGIONS = [
    {"slug": "seoul", "name": "서울", "full": "서울특별시", "districts": [
        ("gangnam", "강남구"), ("gangdong", "강동구"), ("gangbuk", "강북구"),
        ("gangseo", "강서구"), ("gwanak", "관악구"), ("gwangjin", "광진구"),
        ("guro", "구로구"), ("geumcheon", "금천구"), ("nowon", "노원구"),
        ("dobong", "도봉구"), ("dongdaemun", "동대문구"), ("dongjak", "동작구"),
        ("mapo", "마포구"), ("seodaemun", "서대문구"), ("seocho", "서초구"),
        ("seongdong", "성동구"), ("seongbuk", "성북구"), ("songpa", "송파구"),
        ("yangcheon", "양천구"), ("yeongdeungpo", "영등포구"), ("yongsan", "용산구"),
        ("eunpyeong", "은평구"), ("jongno", "종로구"), ("jung", "중구"),
        ("jungnang", "중랑구"),
    ]},
    {"slug": "gyeonggi", "name": "경기", "full": "경기도", "districts": [
        ("suwon", "수원시"), ("seongnam", "성남시"), ("goyang", "고양시"),
        ("yongin", "용인시"), ("bucheon", "부천시"), ("ansan", "안산시"),
        ("anyang", "안양시"), ("namyangju", "남양주시"), ("hwaseong", "화성시"),
        ("pyeongtaek", "평택시"), ("uijeongbu", "의정부시"), ("siheung", "시흥시"),
        ("paju", "파주시"), ("gimpo", "김포시"), ("gwangmyeong", "광명시"),
        ("gwangju-si", "광주시"), ("gunpo", "군포시"), ("osan", "오산시"),
        ("icheon", "이천시"), ("yangju", "양주시"), ("anseong", "안성시"),
        ("guri", "구리시"), ("pocheon", "포천시"), ("uiwang", "의왕시"),
        ("hanam", "하남시"), ("yeoju", "여주시"), ("dongducheon", "동두천시"),
        ("gwacheon", "과천시"), ("yangpyeong", "양평군"), ("gapyeong", "가평군"),
        ("yeoncheon", "연천군"),
    ]},
    {"slug": "incheon", "name": "인천", "full": "인천광역시", "districts": [
        ("jung-incheon", "중구"), ("dong-incheon", "동구"), ("michuhol", "미추홀구"),
        ("yeonsu", "연수구"), ("namdong", "남동구"), ("bupyeong", "부평구"),
        ("gyeyang", "계양구"), ("seo-incheon", "서구"), ("ganghwa", "강화군"),
        ("ongjin", "옹진군"),
    ]},
    {"slug": "busan", "name": "부산", "full": "부산광역시", "districts": [
        ("jung-busan", "중구"), ("seo-busan", "서구"), ("dong-busan", "동구"),
        ("yeongdo", "영도구"), ("busanjin", "부산진구"), ("dongnae", "동래구"),
        ("nam-busan", "남구"), ("buk-busan", "북구"), ("haeundae", "해운대구"),
        ("saha", "사하구"), ("geumjeong", "금정구"), ("gangseo-busan", "강서구"),
        ("yeonje", "연제구"), ("suyeong", "수영구"), ("sasang", "사상구"),
        ("gijang", "기장군"),
    ]},
]

def all_districts():
    """(region, dist_slug, dist_name) 평탄화."""
    out = []
    for r in REGIONS:
        for ds, dn in r["districts"]:
            out.append((r, ds, dn))
    return out

# ── 가격: 채용공고 광고 ──────────────────────────────────────
PRICING_RECRUIT = [
    {"tier": "VVIP", "slot": "히어로 직하 최상단", "limit": "4업체",
     "m1": 44, "m6": 88, "m12": 110, "color": "gold",
     "perks": ["메인·지역·업종 페이지 최상단 고정", "골드 대형 카드 + 회사 로고",
               "월 4.2~5.8만회 노출 · CTR 3.4%", "전담 매니저 1:1 게재 관리"]},
    {"tier": "VIP", "slot": "First Content Break", "limit": "12업체",
     "m1": 20, "m6": 45, "m12": 55, "color": "blue",
     "perks": ["콘텐츠 사이 우선 노출", "블루 중형 카드 + 핵심 혜택 강조",
               "월 2.2~3.2만회 노출 · CTR 2.6%", "공고 수정 무제한"]},
    {"tier": "프리미엄", "slot": "페이지 하단", "limit": "무제한",
     "m1": 13, "m6": 20, "m12": 25, "color": "gray",
     "perks": ["업종·지역 페이지 하단 노출", "그레이 컴팩트 카드",
               "월 0.8~1.4만회 노출 · CTR 1.1%", "선등록순 정렬"]},
]

# ── 가격: 업소매매 등록 ──────────────────────────────────────
PRICING_SHOP = [
    {"plan": "1개월", "price": 10, "note": "단기 매물 등록", "best": False},
    {"plan": "2개월", "price": 15, "note": "BEST · 1개월 대비 25% 절감", "best": True},
    {"plan": "12개월", "price": 33, "note": "장기 등록 · 월 환산 2.75만원", "best": False},
]

# ── 매거진 ───────────────────────────────────────────────────
MAGAZINE = [
    {"slug": "salary-guide-2026", "title": "2026 마사지 관리사 급여 시세 완전정리",
     "tag": "급여", "read": 8, "date": "2026-01-12",
     "lead": "업종·지역·경력별 일급 시세를 1차 매칭 데이터로 분석했다."},
    {"slug": "interview-tips", "title": "마사지샵 면접, 합격하는 사람들의 7가지 공통점",
     "tag": "취업", "read": 6, "date": "2026-01-20",
     "lead": "실제 채용 담당자 인터뷰로 정리한 면접 합격 포인트."},
    {"slug": "contract-checklist", "title": "근로계약서 체크리스트 — 일급·정산·휴무 꼭 확인",
     "tag": "계약", "read": 7, "date": "2026-02-03",
     "lead": "분쟁을 막는 계약 조항 12가지를 항목별로 점검한다."},
    {"slug": "newbie-roadmap", "title": "초보 관리사 입직 로드맵 — 0개월부터 6개월까지",
     "tag": "입문", "read": 9, "date": "2026-02-18",
     "lead": "교육·수습·정착 단계별로 해야 할 일을 시기별 정리."},
    {"slug": "shop-vs-freelance", "title": "로드샵 vs 프리랜서 — 수입·안정성·자유도 비교",
     "tag": "커리어", "read": 7, "date": "2026-03-05",
     "lead": "두 근무 형태의 실제 수입 구조와 장단점을 비교한다."},
    {"slug": "safe-workplace", "title": "안전한 일터 고르는 법 — 합법 업소 판별 가이드",
     "tag": "안전", "read": 8, "date": "2026-03-19",
     "lead": "불법 업소를 피하고 안전한 로드샵을 가려내는 기준."},
    {"slug": "newcomer-shop-guide", "title": "신규 오픈샵 입사 가이드 — 기회와 리스크",
     "tag": "입문", "read": 6, "date": "2026-04-02",
     "lead": "신규 오픈 매장의 장단점과 입사 전 확인 사항."},
]

# ── 공지사항 ─────────────────────────────────────────────────
NOTICES = [
    {"slug": "southeast-asia-scam", "title": "[긴급] 동남아 해외 취업 사기 주의 안내",
     "priority": "긴급", "cat": "안전", "date": "2026-02-10",
     "lead": "고수익을 미끼로 한 해외 송출 사기 사례와 대처법."},
    {"slug": "prostitution-monitoring", "title": "[중요] 불법 영업 업소 모니터링 및 게재 거부 정책",
     "priority": "중요", "cat": "정책", "date": "2026-01-28",
     "lead": "성매매 알선 등 불법 업소의 광고 게재를 전면 거부합니다."},
    {"slug": "newcomer-safety", "title": "신규 입직자 안전 수칙 안내",
     "priority": "일반", "cat": "안전", "date": "2026-03-11",
     "lead": "첫 출근 전 반드시 확인해야 할 안전 수칙 정리."},
    {"slug": "fraud-report-channel", "title": "피해 신고 채널 안내 — 임금체불·계약위반",
     "priority": "일반", "cat": "안내", "date": "2026-03-25",
     "lead": "임금체불·부당대우 발생 시 이용 가능한 공식 신고 창구."},
]

# ── 광고(채용공고) — 82개 행정구 전역에 분산 자동 생성 ──────────
# 운영자가 실제 공고를 입력하면 이 생성 데이터를 대체한다(샘플/데모 데이터).
# tier: vvip(4) / vip(12) / premium(행정구별 1건)
_SHOP_WORDS = [
    "라온", "오아시스", "더휴", "세레니티", "힐링타임", "바디케어", "더테라피",
    "리프레시", "포레스트", "스파드림", "데일리스파", "굿핸즈", "포근한손",
    "휴식공간", "릴랙스", "바디앤소울", "참살이", "테라스파", "하루케어",
    "온더스파", "쉼표테라피", "느린오후", "솔채", "봄날테라피", "미가스파",
    "헬로스파", "더네스트", "아우라", "블리스", "노블스파", "라플로라", "모먼트",
    "휴랑", "르윈", "코지스파", "마레", "솔티", "청담힐", "온기테라피", "담소",
    "해온", "나린", "여유공간", "스파로", "채움", "정담", "포레", "한결", "별채",
]
_HOURS = ["12:00~24:00", "11:00~23:00", "13:00~25:00", "12:00~22:00",
          "13:00~23:00", "11:00~22:00", "12:00~24:00 (탄력)"]
_CONTRACTS = ["정규직", "정규/파트", "파트타임"]
_SETTLES = ["일정산", "주정산", "월정산+인센티브", "일정산/주정산 택1"]
_PEOPLE = [2, 3, 1, 4, 2, 3]


def _short(dn):
    return dn[:-1] if dn[-1] in "구시군" else dn


def _ind_by_name(name):
    for i in INDUSTRIES:
        if i["name"] == name:
            return i
    return INDUSTRIES[0]


def _title(name, i):
    opts = [f"{name} 관리사 모집", f"{name} 마사지 관리사 채용", f"{name} 신입·경력 모집",
            f"{name} 경력자 우대 채용", f"{name} 관리사 급구", f"{name} 정규·파트 모집"]
    return opts[i % len(opts)]


def generate_ads():
    from district_profiles import get_profile
    # (지역명, 행정구명) → svc  (행정구명은 지역 간 중복되므로 튜플로 구분)
    svc_of = {}
    for r in REGIONS:
        for ds, dn in r["districts"]:
            svc_of[(r["name"], dn)] = get_profile(ds, dn)["svc"]

    ads = []
    # VVIP 4 — 프리미엄 핵심 상권
    vvip = [("서울", "강남구", "아로마", 22), ("부산", "해운대구", "아로마", 23),
            ("경기", "성남시", "타이", 21), ("인천", "연수구", "아로마", 23)]
    for k, (rg, dn, ind, w) in enumerate(vvip):
        ads.append({"id": f"a10{k+1:02d}", "tier": "vvip",
                    "shop": f"{_SHOP_WORDS[k]} {_short(dn)}점", "title": _title(ind, k),
                    "region": rg, "district": dn, "industry": ind, "wage": w,
                    "people": _PEOPLE[k % len(_PEOPLE)], "hours": _HOURS[k % len(_HOURS)],
                    "contract": "정규직", "settle": _SETTLES[k % len(_SETTLES)]})

    # VIP 12 — 주요 상권
    vip = [("서울", "서초구"), ("서울", "송파구"), ("서울", "마포구"), ("서울", "강서구"),
           ("경기", "수원시"), ("경기", "용인시"), ("경기", "고양시"), ("경기", "부천시"),
           ("인천", "부평구"), ("인천", "남동구"), ("부산", "부산진구"), ("부산", "동래구")]
    used = {(rg, dn) for rg, dn, _, _ in vvip} | set(vip)
    for k, (rg, dn) in enumerate(vip):
        ind = svc_of[(rg, dn)]
        idef = _ind_by_name(ind)
        w = min(idef["wage_hi"], idef["wage"] + (k % 3) + 1)
        ads.append({"id": f"a20{k+1:02d}", "tier": "vip",
                    "shop": f"{_SHOP_WORDS[(k+4) % len(_SHOP_WORDS)]} {_short(dn)}점",
                    "title": _title(ind, k + 1), "region": rg, "district": dn,
                    "industry": ind, "wage": w, "people": _PEOPLE[k % len(_PEOPLE)],
                    "hours": _HOURS[(k+1) % len(_HOURS)], "contract": _CONTRACTS[k % 2],
                    "settle": _SETTLES[(k+1) % len(_SETTLES)]})

    # 프리미엄 — 나머지 모든 행정구에 1건씩 (지역 페이지 현지 공고 노출)
    k = 0
    for r in REGIONS:
        for ds, dn in r["districts"]:
            if (r["name"], dn) in used:
                continue
            ind = svc_of[(r["name"], dn)]
            idef = _ind_by_name(ind)
            w = idef["wage_lo"] + (k % 3)
            ads.append({"id": f"p3{k+1:03d}", "tier": "premium",
                        "shop": f"{_SHOP_WORDS[k % len(_SHOP_WORDS)]} {_short(dn)}점",
                        "title": _title(ind, k), "region": r["name"], "district": dn,
                        "industry": ind, "wage": w, "people": _PEOPLE[k % len(_PEOPLE)],
                        "hours": _HOURS[k % len(_HOURS)], "contract": _CONTRACTS[k % 3],
                        "settle": _SETTLES[k % len(_SETTLES)]})
            k += 1
    return ads


ADS = generate_ads()

# ── 업소매매 매물 ────────────────────────────────────────────
SHOP_SALES = [
    {"id": "s5001", "title": "강남 역세권 프리미엄 스파 양도", "region": "서울", "district": "강남구",
     "industry": "아로마", "area": 55, "premium": 8000, "deposit": 5000, "rent": 450,
     "revenue": "4,500~5,500", "profit": "1,800~2,300", "label": "역세권"},
    {"id": "s5002", "title": "해운대 관광상권 스웨디시샵 매매", "region": "부산", "district": "해운대구",
     "industry": "스웨디시", "area": 42, "premium": 5500, "deposit": 3000, "rent": 320,
     "revenue": "3,200~4,000", "profit": "1,300~1,700", "label": "관광상권"},
    {"id": "s5003", "title": "분당 정자동 타이마사지 양도", "region": "경기", "district": "성남시",
     "industry": "타이", "area": 48, "premium": 6000, "deposit": 4000, "rent": 380,
     "revenue": "3,500~4,200", "profit": "1,400~1,800", "label": "오피스권"},
    {"id": "s5004", "title": "송도 신도시 프리미엄 스파", "region": "인천", "district": "연수구",
     "industry": "아로마", "area": 60, "premium": 7000, "deposit": 5000, "rent": 400,
     "revenue": "3,800~4,600", "profit": "1,500~1,900", "label": "신도시"},
    {"id": "s5005", "title": "서면 중심가 스웨디시샵", "region": "부산", "district": "부산진구",
     "industry": "스웨디시", "area": 38, "premium": 4500, "deposit": 2500, "rent": 280,
     "revenue": "2,800~3,400", "profit": "1,100~1,400", "label": "중심상권"},
    {"id": "s5006", "title": "수원 영통 아로마테라피 양도", "region": "경기", "district": "수원시",
     "industry": "아로마", "area": 45, "premium": 5000, "deposit": 3000, "rent": 300,
     "revenue": "3,000~3,600", "profit": "1,200~1,500", "label": "주거밀집"},
    {"id": "s5007", "title": "마포 홍대권 로미로미샵", "region": "서울", "district": "마포구",
     "industry": "로미로미", "area": 40, "premium": 5200, "deposit": 3000, "rent": 350,
     "revenue": "3,100~3,800", "profit": "1,200~1,600", "label": "번화가"},
    {"id": "s5008", "title": "부평 역세권 스포츠마사지", "region": "인천", "district": "부평구",
     "industry": "스포츠", "area": 36, "premium": 3800, "deposit": 2000, "rent": 240,
     "revenue": "2,500~3,000", "profit": "1,000~1,300", "label": "역세권"},
    {"id": "s5009", "title": "송파 잠실 프리미엄 아로마", "region": "서울", "district": "송파구",
     "industry": "아로마", "area": 52, "premium": 6500, "deposit": 4000, "rent": 420,
     "revenue": "3,600~4,300", "profit": "1,400~1,800", "label": "역세권"},
    {"id": "s5010", "title": "일산 라페스타 스웨디시", "region": "경기", "district": "고양시",
     "industry": "스웨디시", "area": 44, "premium": 4800, "deposit": 3000, "rent": 310,
     "revenue": "2,900~3,500", "profit": "1,150~1,500", "label": "번화가"},
    {"id": "s5011", "title": "서초 강남대로 타이마사지", "region": "서울", "district": "서초구",
     "industry": "타이", "area": 50, "premium": 7200, "deposit": 4500, "rent": 480,
     "revenue": "4,000~4,800", "profit": "1,600~2,000", "label": "대로변"},
    {"id": "s5012", "title": "동래 온천장 아로마샵", "region": "부산", "district": "동래구",
     "industry": "아로마", "area": 43, "premium": 4200, "deposit": 2500, "rent": 270,
     "revenue": "2,700~3,300", "profit": "1,050~1,400", "label": "주거밀집"},
]

# ── 운영팀 / E-E-A-T ─────────────────────────────────────────
TEAM = [
    {"name": "김세영", "role": "콘텐츠 총괄", "area": "데이터 분석·매칭 로그 검증",
     "bio": "9년차 채용 데이터 분석가. 마사지 업계 채용 시장 리서치를 총괄한다."},
    {"name": "이도윤", "role": "운영 책임", "area": "업소 검증·안전 정책",
     "bio": "로드샵 현장 인터뷰 400여 건을 진행하며 게재 기준을 관리한다."},
    {"name": "박지연", "role": "자문 트레이너", "area": "관리사 교육·역량 자문",
     "bio": "KSPO 생활스포츠지도사. 마사지 관리사 입문 교육 프로그램을 자문한다."},
]

STATS = {
    "match_logs": "21,400",   # 매칭 로그
    "shop_interviews": "408",  # 샵 인터뷰
    "districts": 82,
    "jobs": "5,200",
    "avg_match_hours": 47,
}
