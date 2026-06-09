import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 탐험대",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 MBTI 진로 탐험대")
st.write("나의 MBTI를 선택하면 어울리는 진로를 추천해줄게! 😊")
st.write("---")

career_data = {
    "INTJ": [
        {
            "career": "🔬 연구원",
            "major": "생명과학과, 화학과, 물리학과",
            "personality": "깊이 있게 탐구하고 문제를 해결하는 걸 좋아하는 사람이 잘 맞아!"
        },
        {
            "career": "💻 데이터 분석가",
            "major": "통계학과, 컴퓨터공학과, 산업공학과",
            "personality": "논리적으로 생각하고 체계적으로 계획하는 성향에 딱이야."
        }
    ],

    "INTP": [
        {
            "career": "🧠 AI 개발자",
            "major": "인공지능학과, 컴퓨터공학과",
            "personality": "호기심이 많고 새로운 아이디어를 탐구하는 사람에게 추천!"
        },
        {
            "career": "📚 교수·학자",
            "major": "관심 분야 관련 학과",
            "personality": "깊이 있는 지식을 탐구하고 배우는 걸 좋아한다면 잘 맞아."
        }
    ],

    "ENTJ": [
        {
            "career": "🏢 기업 경영인",
            "major": "경영학과, 경제학과",
            "personality": "리더십이 있고 목표를 향해 추진하는 힘이 강한 사람이 잘해!"
        },
        {
            "career": "⚖️ 변호사",
            "major": "법학 관련 학과",
            "personality": "논리적으로 설득하고 문제를 해결하는 능력이 뛰어난 편이야."
        }
    ],

    "ENTP": [
        {
            "career": "📢 마케팅 기획자",
            "major": "광고홍보학과, 경영학과",
            "personality": "새로운 아이디어를 내고 사람들과 소통하는 걸 즐기는 성향!"
        },
        {
            "career": "🚀 창업가",
            "major": "경영학과, 창업학과",
            "personality": "도전을 두려워하지 않고 혁신적인 생각을 하는 사람에게 추천!"
        }
    ],

    "INFJ": [
        {
            "career": "🩺 상담심리사",
            "major": "심리학과, 상담학과",
            "personality": "공감 능력이 뛰어나고 다른 사람의 성장을 돕는 걸 좋아해."
        },
        {
            "career": "✍️ 작가",
            "major": "국어국문학과, 문예창작과",
            "personality": "깊은 통찰력과 풍부한 상상력을 가진 사람에게 잘 맞아."
        }
    ],

    "INFP": [
        {
            "career": "🎨 디자이너",
            "major": "시각디자인과, 산업디자인과",
            "personality": "창의적이고 자신만의 감성을 표현하는 걸 좋아해."
        },
        {
            "career": "📖 콘텐츠 작가",
            "major": "문예창작과, 언론정보학과",
            "personality": "자신의 생각과 이야기를 전달하는 데 즐거움을 느껴."
        }
    ],

    "ENFJ": [
        {
            "career": "👩‍🏫 교사",
            "major": "교육학과, 사범대",
            "personality": "사람들의 성장을 응원하고 돕는 걸 좋아하는 사람이 잘 맞아."
        },
        {
            "career": "🤝 인사 담당자",
            "major": "경영학과, 심리학과",
            "personality": "사람의 강점을 발견하고 조직을 이끄는 능력이 뛰어나!"
        }
    ],

    "ENFP": [
        {
            "career": "🎤 방송인",
            "major": "미디어커뮤니케이션학과",
            "personality": "에너지가 넘치고 다양한 사람과 소통하는 걸 좋아해."
        },
        {
            "career": "📱 콘텐츠 크리에이터",
            "major": "미디어 관련 학과",
            "personality": "창의적이고 새로운 시도를 즐기는 사람에게 추천!"
        }
    ],

    "ISTJ": [
        {
            "career": "📊 회계사",
            "major": "회계학과, 경영학과",
            "personality": "꼼꼼하고 책임감이 강한 사람이 잘 맞아."
        },
        {
            "career": "🏛️ 공무원",
            "major": "행정학과, 법학 관련 학과",
            "personality": "원칙을 중요하게 여기고 성실한 성향에 잘 어울려."
        }
    ],

    "ISFJ": [
        {
            "career": "💉 간호사",
            "major": "간호학과",
            "personality": "배려심이 깊고 세심하게 사람을 돌볼 수 있어."
        },
        {
            "career": "👶 유치원 교사",
            "major": "유아교육과",
            "personality": "따뜻하고 책임감 있는 사람이 잘 맞는 직업이야."
        }
    ],

    "ESTJ": [
        {
            "career": "📋 행정 관리자",
            "major": "행정학과, 경영학과",
            "personality": "체계적이고 조직을 이끄는 능력이 뛰어나!"
        },
        {
            "career": "👮 경찰관",
            "major": "경찰행정학과",
            "personality": "원칙을 중요하게 여기고 정의감이 강한 편이야."
        }
    ],

    "ESFJ": [
        {
            "career": "🏥 의료 코디네이터",
            "major": "보건행정학과",
            "personality": "친절하고 사람을 돕는 걸 좋아하는 성향!"
        },
        {
            "career": "🎓 학교 상담사",
            "major": "상담학과, 심리학과",
            "personality": "주변 사람들의 고민을 잘 들어주는 사람이 잘 맞아."
        }
    ],

    "ISTP": [
        {
            "career": "🔧 기계 엔지니어",
            "major": "기계공학과",
            "personality": "손으로 직접 만들고 문제를 해결하는 걸 좋아해."
        },
        {
            "career": "🚗 자동차 정비사",
            "major": "자동차공학과",
            "personality": "실용적이고 관찰력이 뛰어난 사람에게 추천!"
        }
    ],

    "ISFP": [
        {
            "career": "📸 사진작가",
            "major": "사진영상학과",
            "personality": "예술적 감각이 뛰어나고 섬세한 표현을 즐겨."
        },
        {
            "career": "🐾 수의사",
            "major": "수의학과",
            "personality": "동물을 사랑하고 따뜻한 마음을 가진 사람에게 잘 맞아."
        }
    ],

    "ESTP": [
        {
            "career": "💼 영업 전문가",
            "major": "경영학과",
            "personality": "활동적이고 사람들과 어울리는 걸 좋아해."
        },
        {
            "career": "🎪 이벤트 기획자",
            "major": "관광경영학과, 이벤트 관련 학과",
            "personality": "순발력이 좋고 현장 분위기를 즐기는 사람에게 추천!"
        }
    ],

    "ESFP": [
        {
            "career": "🎭 배우",
            "major": "연극영화과",
            "personality": "표현력이 풍부하고 사람들에게 즐거움을 주는 걸 좋아해."
        },
        {
            "career": "✈️ 승무원",
            "major": "항공서비스학과",
            "personality": "친절하고 밝은 에너지로 사람을 대하는 데 강점이 있어."
        }
    ]
}

mbti = st.selectbox(
    "📝 나의 MBTI를 선택해봐!",
    list(career_data.keys())
)

if st.button("🔍 진로 추천 받기"):
    st.success(f"✨ {mbti} 유형에게 어울리는 진로를 소개할게!")

    for idx, info in enumerate(career_data[mbti], start=1):
        st.markdown(f"""
### {idx}. {info['career']}

🎓 **추천 학과**  
{info['major']}

💡 **이런 성격이라면 잘 맞아요!**  
{info['personality']}

---
""")

    st.info(
        "📌 MBTI는 참고 자료일 뿐이야!\n\n"
        "진로를 선택할 때는 **내가 좋아하는 것**, "
        "**잘하는 것**, **가치 있게 생각하는 것**을 함께 고려해보자! 🌱"
    )

st.caption("Made with ❤️ using Streamlit")
