<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ShaheenChat | Global AI Platform</title>
    <link rel="stylesheet" href="style.css">
    <!-- Font Awesome للأيقونات -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>

    <!-- القائمة الجانبية -->
    <aside class="sidebar">
        <div class="logo-container">
            <img src="logo.jpg" alt="Shaheen Logo" class="main-logo">
            <h2>شاهين شات</h2>
        </div>
        <nav>
            <ul>
                <li class="active"><i class="fas fa-home"></i> الرئيسية</li>
                <li><i class="fas fa-comments"></i> المحادثات</li>
                <li class="coming-soon"><i class="fas fa-handshake"></i> التوافق <span>قريباً</span></li>
                <li><i class="fas fa-cog"></i> الإعدادات</li>
            </ul>
        </nav>
        <div class="social-icons">
            <a href="#"><i class="fab fa-whatsapp"></i></a>
            <a href="#"><i class="fab fa-telegram"></i></a>
            <a href="#"><i class="fab fa-instagram"></i></a>
            <a href="mailto:tawafuq.app2026@gmail.com"><i class="fas fa-envelope"></i></a>
        </div>
    </aside>

    <!-- واجهة المحادثة -->
    <main class="chat-container">
        <header class="chat-header">
            <img src="logo.jpg" alt="Hawk" class="header-logo">
            <h1>كيف يمكنني مساعدتك اليوم؟</h1>
        </header>

        <div id="chat-box" class="chat-box">
            <!-- الرسائل ستظهر هنا -->
        </div>

        <div class="input-area">
            <input type="text" id="user-input" placeholder="اكتب رسالتك هنا...">
            <button id="send-btn"><i class="fas fa-paper-plane"></i></button>
        </div>

        <footer>
            <p>ShaheenChat.com © 2026 | <a href="#">سياسة الخصوصية</a></p>
        </footer>
    </main>

    <script src="script.js"></script>
</body>
</html>
