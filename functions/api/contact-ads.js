// 광고문의 폼 → Telegram 봇 2개 전송 (Cloudflare Pages Function)
// 봇 토큰·챗 ID는 Cloudflare Pages 환경변수에 등록한다 (코드에 넣지 않음):
//   TELEGRAM_BOT_TOKEN_1 / TELEGRAM_CHAT_ID_1  (봇 1)
//   TELEGRAM_BOT_TOKEN_2 / TELEGRAM_CHAT_ID_2  (봇 2)
//   ALLOWED_ORIGIN (선택, 기본 *)
//
// 진단: 브라우저에서 /api/contact-ads?ping=1 을 열면 환경변수 적재·봇 토큰
// 유효성을 확인할 수 있다 (토큰 값 자체는 노출하지 않음).

function corsHeaders(env) {
  return {
    "Access-Control-Allow-Origin": env.ALLOWED_ORIGIN || "*",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Content-Type": "application/json",
  };
}

export async function onRequestOptions({ env }) {
  return new Response(null, { status: 204, headers: corsHeaders(env) });
}

// 진단용: /api/contact-ads?ping=1
export async function onRequestGet({ request, env }) {
  const url = new URL(request.url);
  if (url.searchParams.get("ping") !== "1") {
    return new Response(JSON.stringify({ ok: false, error: "method" }), {
      status: 405, headers: corsHeaders(env),
    });
  }
  const check = async (token) => {
    if (!token) return { ok: false, reason: "env_missing" };
    try {
      const r = await fetch(`https://api.telegram.org/bot${token}/getMe`);
      const j = await r.json();
      if (j.ok) return { ok: true, bot: "@" + j.result.username };
      return { ok: false, reason: j.description || `http_${r.status}` };
    } catch (_) {
      return { ok: false, reason: "fetch_failed" };
    }
  };
  const result = {
    env_loaded: {
      TELEGRAM_BOT_TOKEN_1: !!env.TELEGRAM_BOT_TOKEN_1,
      TELEGRAM_CHAT_ID_1: !!env.TELEGRAM_CHAT_ID_1,
      TELEGRAM_BOT_TOKEN_2: !!env.TELEGRAM_BOT_TOKEN_2,
      TELEGRAM_CHAT_ID_2: !!env.TELEGRAM_CHAT_ID_2,
      ALLOWED_ORIGIN: env.ALLOWED_ORIGIN || null,
    },
    bot1: await check(env.TELEGRAM_BOT_TOKEN_1),
    bot2: await check(env.TELEGRAM_BOT_TOKEN_2),
  };
  return new Response(JSON.stringify(result, null, 2), {
    headers: corsHeaders(env),
  });
}

export async function onRequestPost({ request, env }) {
  const cors = corsHeaders(env);
  const json = (obj, status = 200) =>
    new Response(JSON.stringify(obj), { status, headers: cors });

  try {
    const data = await request.json();

    // honeypot — 봇이 채우는 숨김 필드면 성공처럼 응답하고 종료
    if (data.company_url) return json({ ok: true });

    const name = (data.name || "").toString().trim().slice(0, 50);
    const phone = (data.phone || "").toString().trim().slice(0, 30);
    const region = (data.region || "").toString().trim().slice(0, 20);
    const grade = (data.grade || "").toString().trim().slice(0, 20);
    const message = (data.message || "").toString().trim().slice(0, 1000);

    if (name.length < 2 || phone.length < 7) {
      return json({ ok: false, error: "invalid" }, 400);
    }

    const now = new Date().toLocaleString("ko-KR", { timeZone: "Asia/Seoul" });
    const text =
      `[마톡 광고문의]\n접수: ${now}\n성명: ${name}\n연락처: ${phone}\n` +
      `지역: ${region}\n등급: ${grade}\n내용: ${message}`;

    const send = async (token, chat) => {
      if (!token || !chat) return { ok: false, reason: "env_missing" };
      try {
        const r = await fetch(`https://api.telegram.org/bot${token}/sendMessage`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            chat_id: chat,
            text,
            disable_web_page_preview: true,
          }),
        });
        const j = await r.json();
        if (j.ok) return { ok: true };
        return { ok: false, reason: j.description || `http_${r.status}` };
      } catch (_) {
        return { ok: false, reason: "fetch_failed" };
      }
    };

    const [r1, r2] = await Promise.all([
      send(env.TELEGRAM_BOT_TOKEN_1, env.TELEGRAM_CHAT_ID_1),
      send(env.TELEGRAM_BOT_TOKEN_2, env.TELEGRAM_CHAT_ID_2),
    ]);

    // 폼은 항상 ok:true 로 처리 (사용자 UX), 진단은 sent 필드에서 확인
    return json({ ok: true, sent: { bot1: r1, bot2: r2 } });
  } catch (_) {
    return json({ ok: false }, 500);
  }
}
