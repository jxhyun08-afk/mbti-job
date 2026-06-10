import streamlit as st

st.set_page_config(
    page_title="MBTI 포켓몬 테스트",
    page_icon="⚡",
    layout="centered"
)

pokemon_data = {
    "INTJ": {
        "name": "뮤츠",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
        "description": "전략적이고 독립적인 성향을 가진 포켓몬이야.",
        "mbti": "INTJ는 미래를 계획하고 문제를 논리적으로 해결하는 능력이 뛰어나. 🧠✨"
    },
    "INTP": {
        "name": "후딘",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png",
        "description": "뛰어난 지능과 분석력을 가진 포켓몬!",
        "mbti": "INTP는 호기심이 많고 새로운 아이디어를 탐구하는 걸 좋아해. 📚💡"
    },
    "ENTJ": {
        "name": "리자몽",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
        "description": "강한 리더십과 추진력을 가진 포켓몬이야.",
        "mbti": "ENTJ는 목표를 향해 팀을 이끌어가는 타고난 리더야. 🔥👑"
    },
    "ENTP": {
        "name": "팬텀",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png",
        "description": "장난기 많고 창의적인 아이디어 뱅크!",
        "mbti": "ENTP는 새로운 도전을 즐기고 재치 있는 해결책을 찾아내는 유형이야. 🎭⚡"
    },
    "INFJ": {
        "name": "루기아",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png",
        "description": "차분하면서도 깊은 통찰력을 지닌 전설의 포켓몬.",
        "mbti": "INFJ는 다른 사람을 이해하고 도와주는 따뜻한 이상주의자야. 🌊💙"
    },
    "INFP": {
        "name": "이브이",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
        "description": "무한한 가능성을 품은 포켓몬!",
        "mbti": "INFP는 상상력이 풍부하고 자신만의 가치관을 중요하게 생각해. 🌈✨"
    },
    "ENFJ": {
        "name": "피카츄",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
        "description": "주변 사람들에게 긍정적인 에너지를 전해줘!",
        "mbti": "ENFJ는 사람들을 응원하고 함께 성장하는 걸 좋아해. ⚡😊"
    },
    "ENFP": {
        "name": "토게키스",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/468.png",
        "description": "행복을 전하는 자유로운 포켓몬!",
        "mbti": "ENFP는 밝고 창의적이며 새로운 경험을 즐기는 모험가야. 🎈🌟"
    },
    "ISTJ": {
        "name": "거북왕",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
        "description": "든든하고 책임감이 강한 포켓몬.",
        "mbti": "ISTJ는 맡은 일을 끝까지 해내는 믿음직한 사람이야. 🛡️📋"
    },
    "ISFJ": {
        "name": "해피너스",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png",
        "description": "다른 사람을 보살피는 따뜻한 포켓몬.",
        "mbti": "ISFJ는 배려심이 깊고 주변 사람들을 챙기는 데 강점이 있어. 💕🥚"
    },
    "ESTJ": {
        "name": "괴력몬",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/68.png",
        "description": "강한 책임감과 실행력을 가진 포켓몬.",
        "mbti": "ESTJ는 체계적이고 현실적인 리더 유형이야. 💪📊"
    },
    "ESFJ": {
        "name": "픽시",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/36.png",
        "description": "친절하고 다정한 매력을 가진 포켓몬.",
        "mbti": "ESFJ는 사람들과 조화를 이루며 돕는 걸 좋아해. 🌷🤗"
    },
    "ISTP": {
        "name": "루카리오",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/448.png",
        "description": "침착하고 뛰어난 문제 해결 능력을 지닌 포켓몬.",
        "mbti": "ISTP는 위기 상황에서도 차분하게 해결책을 찾아내는 유형이야. 🥋⚙️"
    },
    "ISFP": {
        "name": "뮤",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/151.png",
        "description": "순수하고 자유로운 영혼을 가진 포켓몬.",
        "mbti": "ISFP는 감수성이 풍부하고 자신만의 개성을 중요하게 생각해. 🎨🌸"
    },
    "ESTP": {
        "name": "인페르노",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/392.png",
        "description": "에너지 넘치고 행동력이 뛰어난 포켓몬.",
        "mbti": "ESTP는 새로운 경험을 즐기고 즉흥적인 상황에도 강해. 🔥🏃"
    },
    "ESFP": {
        "name": "푸린",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png",
        "description": "밝고 사랑스러운 분위기 메이커!",
        "mbti": "ESFP는 사람들과 어울리는 걸 좋아하고 긍정적인 에너지가 넘쳐. 🎤🎉"
    }
}

st.title("⚡ MBTI 포켓몬 매칭 테스트")
st.write("나의 MBTI와 닮은 포켓몬은 누구일까? 🤔")
st.write("MBTI를 선택하면 포켓몬 친구를 소개해줄게! 🎮")

mbti = st.selectbox(
    "🌟 MBTI를 선택하세요",
    list(pokemon_data.keys())
)

if st.button("🔍 포켓몬 만나기"):
    pokemon = pokemon_data[mbti]

    st.balloons()

    st.header(f"🎉 {mbti} 유형의 포켓몬은...")
    st.subheader(f"✨ {pokemon['name']} ✨")

    st.image(
        pokemon["image"],
        width=250,
        caption=pokemon["name"]
    )

    st.markdown("### 🐾 포켓몬 특징")
    st.info(pokemon["description"])

    st.markdown("### 💭 MBTI 성격 설명")
    st.success(pokemon["mbti"])

    st.markdown(
        """
        ---
        🌈 **기억해!**
        
        MBTI는 나를 이해하는 하나의 도구일 뿐이야.  
        어떤 MBTI든 각자의 멋진 강점이 있다는 사실! 💖
        """
    )
