import streamlit as st
import streamlit.components.v1 as components
from urllib.parse import quote
import os
import base64

# ============================================================
# MA TRAVELS & TOURS
# Travel Agency Website
# Colors Matched to Logo (Deep Navy Blue, Teal, Metallic Gold)
# ============================================================

st.set_page_config(
    page_title="MA Travels & Tours | Karachi",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# BUSINESS INFORMATION
# ============================================================

COMPANY_NAME = "MA Travels & Tours"

MOBILE_1 = "03424575757"
MOBILE_2 = "03001107792"

LANDLINES = [
    "+92 21 35396754",
    "+92 21 35396756",
    "+92 21 35396778",
    "+92 21 35396797"
]

EMAIL = "mashallahtravels@hotmail.com"

ADDRESS = (
    "Suite #502, Block 39, Defence Garden, "
    "D.H.A Phase I, Karachi, Pakistan"
)

WHATSAPP = "923424575757"

FACEBOOK = "https://www.facebook.com/share/18zYTyEoQB/"
TIKTOK = "https://www.tiktok.com/@mashaallah_travels"
GOOGLE_MAPS = "https://maps.app.goo.gl/tj2PZXmjHrYmitMU6"

# ============================================================
# HELPERS
# ============================================================

def get_image_base64(image_path):
    """Converts image file to Base64 string for safe HTML rendering"""
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            ext = image_path.split('.')[-1].lower()
            mime_type = "image/png" if ext == "png" else "image/jpeg"
            return f"data:{mime_type};base64,{base64.b64encode(img_file.read()).decode()}"
    return None

def whatsapp_url(message):
    return f"https://wa.me/{WHATSAPP}?text={quote(message)}"


def copy_number(number, height=52):
    safe_number = number.replace("\\", "\\\\").replace("'", "\\'")

    html = f"""
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: transparent;
            font-family: 'DM Sans', sans-serif;
        }}

        .copy-phone {{
            width: 100%;
            height: 48px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
            padding: 0 13px;
            border-radius: 12px;
            background: #ffffff;
            border: 1px solid rgba(30, 96, 131, 0.18);
            box-sizing: border-box;
            box-shadow: 0 2px 8px rgba(0,0,0,0.02);
            transition: border-color 0.2s ease;
        }}

        .copy-phone:hover {{
            border-color: #c89d52;
        }}

        .phone-number {{
            color: #0f2537;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            flex: 1;
            user-select: none;
            line-height: 48px;
        }}

        .copy-button {{
            border: 1px solid #c89d52;
            background: #fbf7f0;
            color: #0f2537;
            border-radius: 8px;
            padding: 7px 14px;
            font-size: 12px;
            font-weight: 700;
            cursor: pointer;
            transition: all .2s ease;
        }}

        .copy-button:hover {{
            background: #c89d52;
            color: white;
        }}

        .copy-button.copied {{
            background: #0f2537;
            color: white;
            border-color: #0f2537;
        }}
    </style>

    <div class="copy-phone">
        <div class="phone-number" onclick="copyPhone()" title="Click to copy">
            {number}
        </div>
        <button id="copyBtn" class="copy-button" onclick="copyPhone()">
            Copy
        </button>
    </div>

    <script>
        function copyPhone() {{
            const number = '{safe_number}';
            const button = document.getElementById("copyBtn");

            if (navigator.clipboard && window.isSecureContext) {{
                navigator.clipboard.writeText(number).then(function() {{
                    button.innerHTML = "Copied ✓";
                    button.classList.add("copied");
                    setTimeout(function() {{
                        button.innerHTML = "Copy";
                        button.classList.remove("copied");
                    }}, 1500);
                }});
            }} else {{
                const textarea = document.createElement("textarea");
                textarea.value = number;
                textarea.style.position = "fixed";
                textarea.style.opacity = "0";
                document.body.appendChild(textarea);
                textarea.focus();
                textarea.select();

                try {{
                    document.execCommand("copy");
                    button.innerHTML = "Copied ✓";
                    button.classList.add("copied");
                    setTimeout(function() {{
                        button.innerHTML = "Copy";
                        button.classList.remove("copied");
                    }}, 1500);
                }} catch (err) {{
                    button.innerHTML = "Copy";
                }}
                document.body.removeChild(textarea);
            }}
        }}
    </script>
    """

    components.html(
        html,
        height=height,
        scrolling=False
    )

# ============================================================
# CUSTOM CSS (MATCHED TO LOGO PALETTE)
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700;800&family=Noto+Naskh+Arabic:wght@400;500;600;700&display=swap');

:root {
    --navy: #0f2537;
    --teal: #1e6083;
    --gold: #c89d52;
    --gold-light: #e5c278;
    --cream: #f7f9fb;
    --white: #ffffff;
    --text: #112838;
    --muted: #5e7383;
}

html {
    scroll-behavior: smooth;
}

.stApp {
    font-family: 'DM Sans', sans-serif;
    background:
        radial-gradient(circle at 10% 10%, rgba(200,157,82,.12), transparent 30%),
        radial-gradient(circle at 90% 20%, rgba(30,96,131,.08), transparent 35%),
        #f8fafd;
}

.block-container {
    max-width: 1350px !important;
    padding-top: 1rem !important;
    padding-bottom: 3rem !important;
}

#MainMenu, footer, header {
    visibility: hidden;
}

.topbar {
    background: var(--navy);
    color: white;
    padding: 10px 22px;
    border-radius: 0 0 14px 14px;
    font-size: 13px;
    text-align: center;
    letter-spacing: .3px;
    box-shadow: 0 4px 15px rgba(15,37,55,.15);
}

.topbar span {
    margin: 0 12px;
}

.topbar .top-number {
    color: var(--gold-light);
    font-weight: 600;
}

/* BRAND HEADER */
.brand-header {
    background: rgba(255,255,255,.94);
    backdrop-filter: blur(18px);
    border: 1px solid rgba(30,96,131,.12);
    border-radius: 20px;
    padding: 16px 28px;
    margin-top: 15px;
    box-shadow: 0 10px 35px rgba(0,0,0,.04);
}

.brand-wrapper {
    display: flex;
    align-items: center;
    gap: 22px;
}

.brand-logo-img {
    height: 75px;
    width: auto;
    object-fit: contain;
    border-radius: 10px;
}

.brand-name {
    color: var(--navy);
    font-family: 'Playfair Display', serif;
    font-size: 42px;
    font-weight: 800;
    letter-spacing: -0.5px;
    line-height: 1;
}

.brand-tagline {
    color: var(--teal);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 4px;
    margin-top: 6px;
}

.nav-link {
    display: block;
    text-align: center;
    padding: 10px 4px;
    color: var(--navy) !important;
    font-size: 13px;
    font-weight: 700;
    text-decoration: none !important;
    border-radius: 8px;
    transition: all .25s ease;
}

.nav-link:hover {
    color: var(--gold) !important;
    background: rgba(200,157,82,.1);
    transform: translateY(-2px);
}

.hero {
    position: relative;
    overflow: hidden;
    margin-top: 20px;
    min-height: 540px;
    padding: 80px 7%;
    border-radius: 32px;
    background:
        radial-gradient(circle at 80% 20%, rgba(229,194,120,.22), transparent 25%),
        radial-gradient(circle at 75% 80%, rgba(30,96,131,.25), transparent 30%),
        linear-gradient(135deg, #0a1b29 0%, #0f2537 50%, #1e6083 100%);
    box-shadow: 0 30px 70px rgba(15,37,55,.25);
}

.hero-content {
    position: relative;
    z-index: 5;
    max-width: 760px;
}

.hero-kicker {
    color: var(--gold-light);
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 4px;
    margin-bottom: 20px;
}

.hero h1 {
    margin: 0;
    color: white;
    font-family: 'Playfair Display', serif;
    font-size: clamp(44px, 5.5vw, 76px);
    line-height: 1.05;
}

.hero h1 span {
    color: var(--gold-light);
}

.hero-description {
    color: rgba(255,255,255,.88);
    max-width: 680px;
    font-size: 18px;
    line-height: 1.8;
    margin-top: 25px;
}

.hero-urdu {
    color: rgba(255,255,255,.78);
    font-family: 'Noto Naskh Arabic', serif;
    direction: rtl;
    font-size: 19px;
    line-height: 2;
    max-width: 700px;
    margin-top: 12px;
}

.hero-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 30px;
}

.hero-badge {
    color: white;
    background: rgba(255,255,255,.12);
    border: 1px solid rgba(255,255,255,.2);
    backdrop-filter: blur(10px);
    border-radius: 50px;
    padding: 10px 18px;
    font-size: 13px;
    font-weight: 500;
}

.section {
    padding: 65px 0 25px;
}

.section-label {
    color: var(--gold);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 4px;
    text-transform: uppercase;
}

.section-title {
    color: var(--navy);
    font-family: 'Playfair Display', serif;
    font-size: 42px;
    font-weight: 700;
    margin-top: 5px;
}

.section-description {
    color: var(--muted);
    max-width: 700px;
    line-height: 1.8;
    font-size: 16px;
}

.card {
    height: 100%;
    padding: 30px;
    background: rgba(255,255,255,.95);
    border: 1px solid rgba(30,96,131,.12);
    border-radius: 22px;
    box-shadow: 0 10px 30px rgba(0,0,0,.03);
    transition: all .3s ease;
}

.card:hover {
    transform: translateY(-6px);
    border-color: rgba(200,157,82,.45);
    box-shadow: 0 20px 40px rgba(15,37,55,.1);
}

.card-icon {
    width: 58px;
    height: 58px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #f1f6f9;
    border-radius: 16px;
    font-size: 26px;
    margin-bottom: 20px;
}

.card h3 {
    color: var(--navy);
    font-family: 'Playfair Display', serif;
    font-size: 24px;
    margin-bottom: 10px;
}

.card p {
    color: var(--muted);
    font-size: 14px;
    line-height: 1.7;
    margin: 0;
}

.destination {
    min-height: 230px;
    padding: 30px;
    border-radius: 24px;
    color: white;
    position: relative;
    overflow: hidden;
    background:
        radial-gradient(circle at 85% 20%, rgba(200,157,82,.3), transparent 30%),
        linear-gradient(145deg, #0f2537, #1e6083);
    box-shadow: 0 15px 35px rgba(15,37,55,.15);
}

.destination h3 {
    font-family: 'Playfair Display', serif;
    font-size: 28px;
    margin-top: 15px;
    margin-bottom: 8px;
}

.destination p {
    color: rgba(255,255,255,.82);
    line-height: 1.6;
    font-size: 14px;
    margin: 0;
}

.package {
    background: white;
    padding: 32px;
    border-radius: 24px;
    border: 1px solid rgba(30,96,131,.12);
    height: 100%;
    box-shadow: 0 10px 30px rgba(0,0,0,.03);
}

.package-tag {
    display: inline-block;
    background: #f8f3e8;
    color: #926f31;
    border-radius: 30px;
    padding: 6px 14px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 12px;
}

.package h3 {
    color: var(--navy);
    font-family: 'Playfair Display', serif;
    font-size: 28px;
    margin-bottom: 15px;
}

.package ul {
    padding-left: 0;
    list-style: none;
    margin-bottom: 0;
}

.package li {
    color: var(--muted);
    margin: 12px 0;
    font-size: 15px;
}

.about-box {
    padding: 55px;
    border-radius: 30px;
    color: white;
    background:
        radial-gradient(circle at 90% 20%, rgba(200,157,82,.25), transparent 30%),
        var(--navy);
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 50px rgba(15,37,55,.18);
}

.about-box h2 {
    font-family: 'Playfair Display', serif;
    font-size: 42px;
    margin-bottom: 20px;
}

.about-box p {
    color: rgba(255,255,255,.85);
    line-height: 1.8;
    font-size: 16px;
}

.iata-box {
    background: linear-gradient(135deg, #f4f8fb, #ffffff);
    border: 1px solid #c8d8e4;
    border-radius: 24px;
    padding: 40px;
    text-align: center;
}

div[data-testid="stColumn"] > div[data-testid="stVerticalBlock"] > div.stContainer {
    background: #ffffff;
    border: 1px solid rgba(30, 96, 131, 0.2);
    border-radius: 18px;
    padding: 20px !important;
    box-shadow: 0 8px 25px rgba(15, 37, 55, 0.05);
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.iata-caption {
    color: #0f2537;
    font-size: 13px;
    font-weight: 600;
    margin-top: 12px;
    letter-spacing: 0.3px;
    text-align: center;
}

.contact-box {
    background: white;
    border-radius: 24px;
    padding: 32px;
    border: 1px solid rgba(30,96,131,.12);
    box-shadow: 0 12px 35px rgba(0,0,0,.03);
}

.contact-item {
    padding: 16px 0;
    border-bottom: 1px solid #f0f4f7;
}

.contact-item:last-child {
    border-bottom: none;
}

.contact-label {
    color: var(--navy);
    font-weight: 700;
    margin-bottom: 6px;
}

.contact-value {
    color: var(--muted);
    line-height: 1.7;
    font-size: 14px;
}

.contact-copy-title {
    color: var(--navy);
    font-weight: 700;
    font-size: 14px;
    margin-bottom: 8px;
}

.social-box {
    background: var(--navy);
    padding: 35px;
    border-radius: 24px;
    color: white;
    margin-bottom: 15px;
}

.social-box h3 {
    font-family: 'Playfair Display', serif;
    font-size: 28px;
    margin-bottom: 10px;
}

.social-box p {
    color: rgba(255,255,255,.78);
    font-size: 14px;
    margin: 0;
}

.footer {
    margin-top: 80px;
    padding: 60px 40px 30px;
    border-radius: 32px 32px 0 0;
    background: #07131d;
    color: white;
}

.footer h3 {
    font-family: 'Playfair Display', serif;
    font-size: 24px;
    color: white;
    margin-bottom: 15px;
}

.footer h4 {
    color: var(--gold-light);
    font-size: 16px;
    margin-bottom: 15px;
}

.footer p {
    color: rgba(255,255,255,.68);
    line-height: 1.8;
    font-size: 14px;
}

.footer-bottom {
    border-top: 1px solid rgba(255,255,255,.1);
    margin-top: 40px;
    padding-top: 25px;
    text-align: center;
    color: rgba(255,255,255,.4);
    font-size: 13px;
}

div.stButton > button, div.stDownloadButton > button {
    border-radius: 12px !important;
    font-weight: 700 !important;
    padding: 12px 24px !important;
    border: none !important;
    transition: all .25s ease !important;
}

div.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 20px rgba(15,37,55,.18) !important;
}

.stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
    border-radius: 12px !important;
    border: 1px solid #d3e0ea !important;
    padding: 10px 14px !important;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# TOP BAR
# ============================================================

st.markdown(f"""
<div class="topbar">
    <span>✈️ MA TRAVELS & TOURS</span>
    <span class="top-number">📞 {MOBILE_1}</span>
    <span class="top-number">📱 {MOBILE_2}</span>
    <span>🌍 Karachi, Pakistan</span>
</div>
""", unsafe_allow_html=True)

# ============================================================
# BRAND HEADER
# ============================================================

logo_base64 = None
for path in ["assets/logo.jpg", "assets/logo.png", "assets/logo.jpeg", "logo.jpg", "logo.png"]:
    logo_base64 = get_image_base64(path)
    if logo_base64:
        break

if logo_base64:
    st.markdown(f"""
    <div class="brand-header">
        <div class="brand-wrapper">
            <img src="{logo_base64}" class="brand-logo-img" alt="Logo">
            <div>
                <div class="brand-name">MA TRAVELS & TOURS</div>
                <div class="brand-tagline">TRAVEL • EXPLORE • EXPERIENCE</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="brand-header">
        <div class="brand-wrapper">
            <div style="font-size: 50px; line-height: 1;">✈️</div>
            <div>
                <div class="brand-name">MA TRAVELS & TOURS</div>
                <div class="brand-tagline">TRAVEL • EXPLORE • EXPERIENCE</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# NAVIGATION
# ============================================================

nav_cols = st.columns(8)
navigation = [
    ("Home", "home"),
    ("Services", "services"),
    ("Umrah", "umrah"),
    ("Tours", "tours"),
    ("About", "about"),
    ("IATA", "iata"),
    ("Contact", "contact"),
    ("Booking", "booking")
]

for col, (name, section) in zip(nav_cols, navigation):
    with col:
        st.markdown(
            f'<a class="nav-link" href="#{section}">{name}</a>',
            unsafe_allow_html=True
        )

# ============================================================
# HERO
# ============================================================

st.markdown('<div id="home"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-content">
        <div class="hero-kicker">WELCOME TO MA TRAVELS & TOURS</div>
        <h1>Your Journey.<br><span>Our Responsibility.</span></h1>
        <p class="hero-description">
            Your trusted travel partner for air ticketing, visa services, Umrah packages, 
            hotel booking, international tours and journeys across Pakistan.
        </p>
        <p class="hero-urdu">
            آپ کے سفر کو آسان، آرام دہ اور یادگار بنانا ہماری ترجیح ہے۔
        </p>
        <div class="hero-badges">
            <div class="hero-badge">✈️ Air Ticketing</div>
            <div class="hero-badge">🕋 Umrah</div>
            <div class="hero-badge">🛂 Visa Services</div>
            <div class="hero-badge">🏨 Hotels</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")
hero1, hero2, hero3 = st.columns([1,1,2])

with hero1:
    st.link_button(
        "💬 WhatsApp Us",
        whatsapp_url("Assalamualaikum MA Travels & Tours, I would like information about your travel services."),
        use_container_width=True
    )

with hero2:
    st.link_button(
        "📋 Copy Contact Number",
        "#contact",
        use_container_width=True
    )

# ============================================================
# SERVICES
# ============================================================

st.markdown('<div id="services"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-label">OUR SERVICES</div>
    <div class="section-title">Everything You Need to Travel</div>
    <p class="section-description">
        Complete travel solutions designed to make your journey simple, comfortable and memorable.
    </p>
</div>
""", unsafe_allow_html=True)

services = [
    ("✈️", "Air Ticketing", "Domestic and international flight booking assistance."),
    ("🛂", "Visa Services", "Assistance with travel visa requirements and applications."),
    ("🕋", "Umrah Packages", "Travel assistance for your spiritual journey to Saudi Arabia."),
    ("🏨", "Hotel Booking", "Comfortable accommodation arrangements for your travels."),
    ("🌍", "International Tours", "Explore amazing destinations around the world."),
    ("🇵🇰", "Pakistan Tours", "Discover beautiful destinations across Pakistan."),
    ("🚐", "Airport Transfers", "Convenient airport transfer arrangements."),
    ("🎫", "Travel Insurance", "Travel insurance assistance for greater peace of mind.")
]

for start in range(0, len(services), 4):
    cols = st.columns(4)
    for col, service in zip(cols, services[start:start + 4]):
        icon, title, description = service
        with col:
            st.markdown(
                f"""
                <div class="card">
                    <div class="card-icon">{icon}</div>
                    <h3>{title}</h3>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
    st.write("")

# ============================================================
# UMRAH
# ============================================================

st.markdown('<div id="umrah"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-label">SACRED JOURNEY</div>
    <div class="section-title">Umrah Packages</div>
    <p class="section-description">
        We offer tailored Umrah packages and dedicated assistance for your sacred journey.
    </p>
</div>
""", unsafe_allow_html=True)

umrah_packages = [
    ("ESSENTIAL", "Essential Umrah", ["✈️ Air Ticket Assistance", "🛂 Visa Assistance", "🏨 Hotel Arrangement", "🚐 Transport Assistance"]),
    ("COMFORT", "Comfort Umrah", ["✈️ Air Ticket Assistance", "🛂 Visa Assistance", "🏨 Comfortable Hotel", "🚐 Transport Arrangement"]),
    ("PREMIUM", "Premium Umrah", ["✈️ Flight Arrangement", "🛂 Visa Assistance", "🏨 Premium Hotel Options", "🚐 Transport Assistance"])
]

cols = st.columns(3)
for col, package in zip(cols, umrah_packages):
    tag, title, features = package
    with col:
        st.markdown(
            f"""
            <div class="package">
                <div class="package-tag">{tag}</div>
                <h3>{title}</h3>
                <ul>
                    {''.join(f'<li>{feature}</li>' for feature in features)}
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.link_button(
            "💬 Request Details",
            whatsapp_url(f"Assalamualaikum, I would like details about the {title}."),
            use_container_width=True
        )

# ============================================================
# TOURS
# ============================================================

st.markdown('<div id="tours"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-label">DESTINATIONS</div>
    <div class="section-title">Explore the World</div>
    <p class="section-description">
        Discover exciting international destinations and breathtaking locations across Pakistan.
    </p>
</div>
""", unsafe_allow_html=True)

destinations = [
    ("🇦🇪", "Dubai", "Luxury, shopping, adventure and unforgettable experiences."),
    ("🇹🇷", "Turkey", "Culture, history, beautiful landscapes and historic cities."),
    ("🇸🇦", "Saudi Arabia", "A meaningful destination for your spiritual journey."),
    ("🇵🇰", "Pakistan", "Mountains, valleys, culture and natural beauty.")
]

cols = st.columns(4)
for col, destination in zip(cols, destinations):
    icon, title, description = destination
    with col:
        st.markdown(
            f"""
            <div class="destination">
                <div style="font-size:40px;">{icon}</div>
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.link_button(
            f"Explore {title}",
            whatsapp_url(f"Assalamualaikum, I would like information about travelling to {title}."),
            use_container_width=True
        )

# ============================================================
# ABOUT
# ============================================================

st.markdown('<div id="about"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-label">ABOUT US</div>
</div>

<div class="about-box">
    <h2>Travel With Confidence</h2>
    <p>
        MA Travels & Tours is committed to helping customers plan and arrange their journeys 
        with convenience and care. From flights and visas to Umrah, hotels and custom tours, 
        we provide complete travel assistance crafted to meet your specific needs.
    </p>
    <p style="font-family:'Noto Naskh Arabic',serif; direction:rtl; font-size:18px; margin-top:20px;">
        ہمارا مقصد آپ کے سفر کو آسان، آرام دہ اور یادگار بنانا ہے۔ 
        ہم ٹکٹنگ، ویزا، عمرہ، ہوٹل اور ٹورز سمیت مختلف سفری خدمات میں آپ کی رہنمائی اور معاونت کرتے ہیں۔
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# IATA & PAYMENTS
# ============================================================

st.markdown('<div id="iata"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-label">TRUST & CREDIBILITY</div>
    <div class="section-title">Professional Travel Services</div>
</div>

<div class="iata-box">
""", unsafe_allow_html=True)

iata_col1, iata_col2 = st.columns([2, 1], gap="large")

with iata_col1:
    with st.container():
        cert_path = "assets/image_c483e4.jpg"
        if os.path.exists(cert_path):
            st.image(cert_path, use_container_width=True)
        else:
            st.info("📜 Certificate Image Missing")
        st.markdown('<div class="iata-caption">📜 IATA Certificate of Accreditation — Mashallah Travels</div>', unsafe_allow_html=True)

with iata_col2:
    with st.container():
        iata_logo_path = "assets/image_c483ac.jpg"
        if os.path.exists(iata_logo_path):
            st.image(iata_logo_path, width=180)
        else:
            st.info("✈️ Logo Image Missing")
        st.markdown('<div class="iata-caption">Authorized Agent</div>', unsafe_allow_html=True)

st.markdown("""
    <h2 style="color:#0f2537; font-family:'Playfair Display',serif; margin-top:28px; margin-bottom:6px;">
        IATA Accredited Agency
    </h2>
    <p style="color:#5e7383; margin:0; font-size:15px;">
        Certified, reliable, and professional travel services for all your global journeys.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-label">EASY PAYMENT</div>
    <div class="section-title">Payment Options</div>
    <p class="section-description">
        We support multiple convenient payment methods for your booking arrangements.
    </p>
</div>
""", unsafe_allow_html=True)

payment_cols = st.columns(3)
payments = [
    ("💵", "Cash Payment", "In-office cash payments accepted"),
    ("🏦", "Bank Transfer", "Direct bank transfers & online banking"),
    ("💳", "Online Payment", "Secure digital payments")
]

for col, payment in zip(payment_cols, payments):
    icon, title, text = payment
    with col:
        st.markdown(
            f"""
            <div class="card" style="text-align:center;">
                <div class="card-icon" style="margin:0 auto 18px;">{icon}</div>
                <h3>{title}</h3>
                <p>{text}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# ============================================================
# BOOKING FORM
# ============================================================

st.markdown('<div id="booking"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-label">PLAN YOUR JOURNEY</div>
    <div class="section-title">Request a Travel Quote</div>
    <p class="section-description">
        Fill in your travel details and submit your inquiry to connect directly via WhatsApp.
    </p>
</div>
""", unsafe_allow_html=True)

with st.form("travel_inquiry"):
    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input("Full Name *", placeholder="Enter your full name")
        phone = st.text_input("Phone Number *", placeholder="03XX XXXXXXX")
        email = st.text_input("Email Address", placeholder="your@email.com")
    with c2:
        service = st.selectbox(
            "Service Required",
            [
                "Air Ticketing", "Visa Services", "Umrah Packages", 
                "Hotel Booking", "International Tours", "Pakistan Tours", 
                "Airport Transfers", "Travel Insurance"
            ]
        )
        destination = st.text_input("Destination", placeholder="Where do you want to travel?")
        date = st.date_input("Preferred Travel Date")

    message = st.text_area("Additional Requirements", placeholder="Tell us more about your travel plans...")
    submit = st.form_submit_button("✈️ Prepare Travel Inquiry", use_container_width=True)

if submit:
    if not name or not phone:
        st.error("Please provide both your Name and Phone Number.")
    else:
        inquiry_text = (
            f"Assalamualaikum MA Travels & Tours,\n\n"
            f"New Travel Inquiry:\n"
            f"• Name: {name}\n"
            f"• Phone: {phone}\n"
            f"• Email: {email if email else 'N/A'}\n"
            f"• Service: {service}\n"
            f"• Destination: {destination if destination else 'N/A'}\n"
            f"• Preferred Date: {date}\n"
            f"• Message: {message if message else 'N/A'}"
        )
        st.success("Inquiry prefilled! Click below to send directly via WhatsApp.")
        st.link_button(
            "💬 Send Inquiry via WhatsApp",
            whatsapp_url(inquiry_text),
            use_container_width=True
        )

# ============================================================
# CONTACT & LOCATION
# ============================================================

st.markdown('<div id="contact"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="section-label">GET IN TOUCH</div>
    <div class="section-title">Contact Information</div>
    <p class="section-description">
        Reach out via phone, email, or visit our office in DHA Karachi for direct consultation.
    </p>
</div>
""", unsafe_allow_html=True)

contact_col1, contact_col2 = st.columns(2)

with contact_col1:
    st.markdown(f"""
    <div class="contact-box">
        <div class="contact-item">
            <div class="contact-label">📍 Office Address</div>
            <div class="contact-value">{ADDRESS}</div>
        </div>
        <div class="contact-item">
            <div class="contact-label">✉️ Email Address</div>
            <div class="contact-value">{EMAIL}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.markdown('<div class="contact-copy-title">📱 Mobile Numbers (Click to Copy)</div>', unsafe_allow_html=True)
    copy_number(MOBILE_1)
    st.write("")
    copy_number(MOBILE_2)

with contact_col2:
    st.markdown('<div class="contact-copy-title">☎️ Landline Numbers (Click to Copy)</div>', unsafe_allow_html=True)
    for landline in LANDLINES:
        copy_number(landline)
        st.write("")

st.write("")
social_col1, social_col2 = st.columns(2)

with social_col1:
    st.markdown("""
    <div class="social-box">
        <h3>Connect With Us</h3>
        <p>Follow our official social channels for updates and travel offers.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("🌐 Facebook Page", FACEBOOK, use_container_width=True)
    st.link_button("🎵 TikTok Account", TIKTOK, use_container_width=True)

with social_col2:
    st.markdown("""
    <div class="social-box">
        <h3>Visit Our Office</h3>
        <p>Find our exact location using Google Maps for in-person consultation.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("📍 Open in Google Maps", GOOGLE_MAPS, use_container_width=True)

# ============================================================
# FOOTER
# ============================================================

st.markdown(f"""
<div class="footer">
    <div style="display: flex; flex-wrap: wrap; justify-content: space-between; gap: 30px;">
        <div style="flex: 1; min-width: 250px;">
            <h3>MA TRAVELS & TOURS</h3>
            <p>
                Your trusted travel agency in Karachi for air tickets, visas, 
                Umrah packages, hotels, and custom tour packages.
            </p>
        </div>
        <div style="flex: 1; min-width: 200px;">
            <h4>Quick Links</h4>
            <p>
                <a href="#home" style="color: rgba(255,255,255,.68); text-decoration: none;">Home</a> • 
                <a href="#services" style="color: rgba(255,255,255,.68); text-decoration: none;">Services</a> • 
                <a href="#umrah" style="color: rgba(255,255,255,.68); text-decoration: none;">Umrah</a> • 
                <a href="#tours" style="color: rgba(255,255,255,.68); text-decoration: none;">Tours</a>
            </p>
        </div>
        <div style="flex: 1; min-width: 250px;">
            <h4>Contact Info</h4>
            <p>
                📍 DHA Phase I, Karachi<br>
                ✉️ {EMAIL}<br>
                📱 {MOBILE_1} / {MOBILE_2}
            </p>
        </div>
    </div>
    <div class="footer-bottom">
        © {COMPANY_NAME}. All Rights Reserved. Built with Streamlit.
    </div>
</div>
""", unsafe_allow_html=True)