// شاهين شات - يعمل بدون سيرفر خارجي (جاهز فوراً)

async function handleSend() {
    // تحديد مكان كتابة الرسالة
    const input = document.getElementById('userInput');
    const chatBox = document.getElementById('chat-box');
    const query = input.value.trim();

    if (!query) return; // لا ترسل رسالة فارغة

    // 1. عرض رسالة المستخدم
    chatBox.innerHTML += `<div class="user">👤 ${query}</div>`;
    input.value = ""; // تفريغ حقل الكتابة
    chatBox.scrollTop = chatBox.scrollHeight;

    // 2. عرض علامة "جاري الكتابة..."
    const loadingId = "bot-" + Date.now();
    chatBox.innerHTML += `<div id="${loadingId}" class="bot">🦅 شاهين شات: <i class="fas fa-spinner fa-spin"></i> جاري التفكير...</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;

    // 3. محاكاة الرد بعد ثانية (بدون الحاجة لأي سيرفر خارجي)
    setTimeout(() => {
        const botMessageDiv = document.getElementById(loadingId);
        if (botMessageDiv) {
            // ردود ذكية وسريعة
            let reply = "شكراً لرسالتك! 🤍 أنا شاهين شات في نسخته التجريبية. قريباً سأصبح أكثر ذكاءً.";
            if (query.includes("مرحب") || query.includes("السلام")) {
                reply = "وعليكم السلام ورحمة الله! 🌸 أهلاً بك في شاهين شات. كيف أقدر أساعدك اليوم؟";
            } else if (query.includes("شكر")) {
                reply = "العفو! شكراً جزيلاً لتواصلك معنا 🤍";
            } else if (query.includes("من انت")) {
                reply = "أنا شاهين شات 🦅، مساعدك الرقمي الذكي. تم تطويري لخدمتك والإجابة على استفساراتك.";
            }
            botMessageDiv.innerHTML = `🦅 شاهين شات: ${reply}`;
        }
        chatBox.scrollTop = chatBox.scrollHeight;
    }, 1000); // يرد بعد 1 ثانية
}

// إرسال الرسالة بالضغط على زر "Enter"
document.addEventListener('DOMContentLoaded', function() {
    const input = document.getElementById('userInput');
    if (input) {
        input.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                handleSend();
            }
        });
    }
});
