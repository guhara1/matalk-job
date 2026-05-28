export async function onRequestPost({ request, env }) {
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
