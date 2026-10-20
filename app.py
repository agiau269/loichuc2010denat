Dưới đây là toàn bộ đoạn code đã được bổ sung thêm phần Lá thư gửi lời chúc sức khỏe đến bà ngoại riêng biệt.
Đoạn code đã gom sạch sẽ các thẻ HTML, điều chỉnh tên nút bấm và hiển thị đúng thông tin của bạn (Giàu):
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="20/10 - Chúc Mừng Chị Ba Anh Thư & Bà Ngoại",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Quicksand:wght@400;500;600;700&display=swap');

.stApp {
    background: linear-gradient(145deg, #fff9f5, #fef0eb, #fcece6);
    color: #6b4c42;
    font-family: 'Quicksand', sans-serif;
}
header, footer, #MainMenu {visibility: hidden;}
.block-container {
    max-width: 850px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}
.hero {
    text-align: center;
    padding: 2rem 1rem;
    border: 1px solid #fae1d9;
    border-radius: 28px;
    background: rgba(255,255,255,.8);
    box-shadow: 0 12px 35px rgba(212,143,121,.12);
}
.eyebrow {
    letter-spacing: .15em;
    color: #b87355;
    font-size: .8rem;
    font-weight: 700;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    color: #9e5b40;
    font-size: clamp(2.2rem, 7vw, 3.8rem);
    margin: .6rem 0;
}
.hero-sub {
    line-height: 1.9;
    color: #826053;
}
.card {
    background: rgba(255,255,255,.88);
    border: 1px solid #fae1d9;
    border-radius: 24px;
    padding: 1.5rem;
    margin: 1.2rem 0;
    box-shadow: 0 10px 28px rgba(212,143,121,.09);
}
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    color: #9e5b40;
    text-align: center;
    margin: .4rem 0 1rem;
}
.poem {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1rem, 3.5vw, 1.25rem);
    line-height: 2.05;
    color: #826053;
    text-align: center;
}
.letter {
    white-space: pre-line;
    font-size: 1rem;
    line-height: 2;
    color: #6b4c42;
}
.signature {
    font-family: 'Playfair Display', serif;
    color: #9e5b40;
    text-align: right;
    font-size: 1.3rem;
    margin-top: 1rem;
}
.wish-pill {
    display: inline-block;
    background: #fef0eb;
    color: #b87355;
    border: 1px solid #f7d6cd;
    border-radius: 999px;
    padding: .5rem .8rem;
    margin: .2rem;
    font-weight: 700;
    font-size: .85rem;
}
div.stButton > button {
    background: linear-gradient(100deg, #d98262, #bd6242);
    color: white;
    border: 0;
    border-radius: 999px;
    padding: .75rem 1.2rem;
    font-weight: 700;
}
div.stButton > button:hover {
    color: white;
    border: 0;
}
.footer {
    text-align: center;
    color: #a37c6d;
    line-height: 1.9;
    padding: 1rem;
}
</style>
""", unsafe_allow_html=True)

# Hiệu ứng hoa rơi vàng hồng
components.html("""
<div id="petals"></div>
<style>
#petals {
    position: fixed;
    inset: 0;
    pointer-events: none;
    overflow: hidden;
}
.petal {
    position: absolute;
    top: -30px;
    animation: fall linear infinite;
    opacity: .75;
}
@keyframes fall {
    to { transform: translateY(110vh) rotate(450deg); }
}
</style>
<script>
const root = document.getElementById('petals');
const flowers = ['✨', '🌸', '💫', '💛', '🌷'];
for (let i = 0; i < 18; i++) {
    const p = document.createElement('span');
    p.className = 'petal';
    p.textContent = flowers[Math.floor(Math.random()*flowers.length)];
    p.style.left = Math.random()*100 + '%';
    p.style.fontSize = (14+Math.random()*14) + 'px';
    p.style.animationDuration = (9+Math.random()*12) + 's';
    p.style.animationDelay = (-Math.random()*15) + 's';
    root.appendChild(p);
}
</script>
""", height=0)

# PHẦN ĐẦU TRANG
st.markdown("""
<div class="hero">
    <div style="font-size:2rem">✨ 💛 🌸 💛 ✨</div>
    <div class="eyebrow">
        20 THÁNG 10 · NGÀY PHỤ NỮ VIỆT NAM
    </div>
    <div class="hero-title">Gửi Chị Ba Anh Thư</div>
    <div class="hero-sub">
        Chúc người chị xinh đẹp, giỏi giang của em một ngày 20/10 ngập tràn niềm vui.<br>
        <b>Luôn rạng rỡ, hạnh phúc và thành công trên mọi con đường nhé!</b>
    </div>
</div>
""", unsafe_allow_html=True)

# PHẦN ẢNH
st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
st.image(
    "chiba.JPG", 
    caption="Chúc chị Ba luôn trẻ đẹp và rạng ngời mỗi ngày ✨", 
    use_container_width=True
)

# BÀI THƠ TẶNG CHỊ BA
st.markdown("""
<div class="card">
    <div style="text-align:center;font-size:1.8rem">
        ✨ ✨ ✨
    </div>
    <div class="section-title">Thơ tặng chị Ba Anh Thư</div>
    <div class="poem">
        Tháng mười ngày lễ đến rồi,<br>
        Chúc cho chị Ba nụ cười trên môi.<br>
        Trẻ trung, xinh đẹp, yêu đời,<br>
        Niềm vui hạnh phúc tới nơi ngập tràn.<br><br>
        Mong cho sự nghiệp hanh thông,<br>
        Gia đình gắn kết dài lâu,<br>
        Bình an, tài lộc đến mau mỗi ngày. <span style="color:#d98262">❤</span>
    </div>
    <div style="text-align:center;font-size:1.8rem;margin-top:1rem">
        💛 💛 💛
    </div>
</div>
""", unsafe_allow_html=True)

# NHỮNG ĐIỀU CHÚC MONG
st.markdown("""
<div class="card" style="text-align:center">
    <div style="font-size:3rem">💛</div>
    <div class="section-title">Gửi gắm yêu thương</div>
    <p style="font-family:'Playfair Display',serif;font-size:1.2rem;line-height:1.9;color:#9e5b40">
        Chúc Anh Thư luôn giữ vững năng lượng tích cực, gặp nhiều may mắn<br>
        và lúc nào cũng được yêu thương chiều chuộng nhé!
    </p>
    <span class="wish-pill">✨ Xinh đẹp rạng ngời</span>
    <span class="wish-pill">💛 Luôn vui vẻ</span>
    <span class="wish-pill">🌸 Thành công</span>
    <span class="wish-pill">💫 May mắn</span>
</div>
""", unsafe_allow_html=True)

# LÁ THƯ DÀNH CHO CHỊ BA
st.markdown(
    '<div class="section-title">💌 Món quà tinh thần cho chị Ba</div>',
    unsafe_allow_html=True
)

if "letter_open_chiba" not in st.session_state:
    st.session_state.letter_open_chiba = False

if st.button("💌 Mở lời chúc bí mật từ Giàu gửi chị Ba", use_container_width=True):
    st.session_state.letter_open_chiba = not st.session_state.letter_open_chiba

if st.session_state.letter_open_chiba:
    st.markdown("""
    <div class="card">
        <div class="letter">Gửi chị Ba Anh Thư yêu quý,

Nhân ngày Phụ nữ Việt Nam 20/10, Giàu chúc Anh Thư luôn luôn tươi trẻ, hạnh phúc và gặp thật nhiều may mắn trong cuộc sống và gia đình nhỏ luôn hạnh phúc. Cảm ơn Anh Thư vì luôn là người chị tuyệt vời. 

❤️✨💛</div>
        <div class="signature">Giàu 💛</div>
    </div>
    """, unsafe_allow_html=True)

# LÁ THƯ CON GỬI BÀ NGOẠI
st.markdown(
    '<div class="section-title">👵 Lời chúc sức khỏe gửi Bà Ngoại</div>',
    unsafe_allow_html=True
)

if "letter_open_ngoai" not in st.session_state:
    st.session_state.letter_open_ngoai = False

if st.button("🌸 Mở lời chúc con gửi Bà Ngoại", use_container_width=True):
    st.session_state.letter_open_ngoai = not st.session_state.letter_open_ngoai

if st.session_state.letter_open_ngoai:
    st.markdown("""
    <div class="card">
        <div class="letter">Kính gửi Bà Ngoại yêu thương của con,

Nhân ngày 20/10, con chúc Ngoại luôn dồi dào sức khỏe, sống lâu trăm tuổi, lúc nào cũng thanh thản, vui vẻ và bình an bên con cháu. 

Con mong Ngoại luôn có thật nhiều niềm vui mỗi ngày, ăn ngon ngủ ngon và luôn giữ nụ cười hiền hậu trên môi. Chúc bà Ngoại luôn khoẻ mành và an vui.❤️👵🌸✨</div>
        <div class="signature">Cháu Giàu của Ngoại 💛</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    ✨💛🌸💛✨<br>
    <b>20.10.2026 · ✨</b>
</div>
""", unsafe_allow_html=True)
