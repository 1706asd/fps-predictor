"""
🎮 내 PC 게임 프레임(FPS) 예측기
- 그래픽카드(GPU)와 그래픽 옵션에 따른 게임별 예상 FPS 및 플레이 적합도 분석 웹앱
"""
import streamlit as st
import pandas as pd

# =============================================
# 1. 시작: 페이지 설정 및 게이밍 대시보드 디자인
# =============================================
st.set_page_config(page_title="내 PC 게임 FPS 예측기", page_icon="🎮", layout="centered")

st.markdown(
    """
    <style>
    /* 메인 타이틀 배너 */
    .gaming-hero {
        position: relative;
        padding: 1.8rem 2rem;
        border-radius: 20px;
        margin-bottom: 1.5rem;
        color: #ffffff;
        background: linear-gradient(135deg, #0b0f19 0%, #1e1b4b 50%, #312e81 100%);
        border: 1px solid rgba(129, 140, 248, 0.35);
        box-shadow: 0 12px 32px rgba(15, 23, 42, 0.3);
        overflow: hidden;
    }
    .gaming-hero::after {
        content: "";
        position: absolute;
        top: -40%;
        right: -10%;
        width: 240px;
        height: 240px;
        background: radial-gradient(circle, rgba(56, 189, 248, 0.25) 0%, transparent 70%);
        pointer-events: none;
    }
    .hero-tag {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        border-radius: 999px;
        background: rgba(56, 189, 248, 0.18);
        color: #38bdf8;
        border: 1px solid rgba(56, 189, 248, 0.45);
        margin-bottom: 0.65rem;
    }
    .gaming-hero h1 {
        margin: 0;
        font-size: 1.95rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        background: linear-gradient(90deg, #ffffff 0%, #c7d2fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .gaming-hero p {
        margin: 0.45rem 0 0;
        font-size: 0.96rem;
        color: #cbd5e1;
    }

    /* 분석하기 버튼 커스텀 */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(90deg, #4f46e5 0%, #7c3aed 100%);
        border: none;
        border-radius: 12px;
        padding: 0.65rem 1.2rem;
        font-weight: 700;
        font-size: 1.02rem;
        box-shadow: 0 6px 18px rgba(99, 102, 241, 0.35);
        transition: all 0.2s ease;
    }
    div.stButton > button[kind="primary"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 24px rgba(124, 58, 237, 0.45);
    }

    /* 강조 수치(Metric) 카드 디자인 */
    div[data-testid="stMetric"] {
        background: linear-gradient(145deg, rgba(30, 41, 59, 0.05) 0%, rgba(99, 102, 241, 0.09) 100%);
        border: 1px solid rgba(99, 102, 241, 0.28);
        border-radius: 16px;
        padding: 1rem 1.2rem;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.06);
    }
    div[data-testid="stMetricLabel"] {
        font-weight: 600;
        opacity: 0.85;
    }
    div[data-testid="stMetricValue"] {
        font-weight: 800;
        color: #4f46e5;
    }
    </style>
    <div class="gaming-hero">
        <div class="hero-tag">PC GAMING PERFORMANCE ANALYZER</div>
        <h1>🎮 내 PC 게임 프레임(FPS) 예측기</h1>
        <p>그래픽카드와 그래픽 품질 옵션을 선택해 게임별 예상 프레임과 플레이 적합도를 확인하세요</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# =============================================
# 2. 리스트 선언: 게임 목록, 기본 FPS, GPU 배율, 옵션명
# =============================================
games = ["리그 오브 레전드", "발로란트", "배틀그라운드"]
base_fps = [260, 240, 90]  # RTX 3060 · 옵션 1단계(낮음) 기준 기본 FPS

gpu_list = ["RTX 3060", "RTX 4060", "RTX 4070"]
gpu_rate = [1.0, 1.2, 1.7]  # 그래픽카드별 성능 배율
option_names = ["낮음", "보통", "높음", "매우 높음", "울트라"]


# =============================================
# 함수 정의 (def): GPU와 옵션을 받아 예상 FPS와 적합도 메시지 리턴
# =============================================
def predict_fps(gpu_name, option):
    """GPU 이름과 그래픽 옵션을 매개변수로 받아 예상 FPS 리스트와 적합도에 따른 텍스트 메시지를 리턴"""
    gpu_power = gpu_rate[gpu_list.index(gpu_name)]
    option_weight = 1 - 0.15 * (option - 1)  # 옵션 1단계 상승 시 프레임 15% 감소

    fps_list = []
    for base in base_fps:
        fps_list.append(int(base * gpu_power * option_weight))

    # 최저 프레임(fps) 기준 적합도 조건 판별 (120 / 60 프레임 기준)
    fps = min(fps_list)
    if fps >= 120:
        suitability = "적합"
        message = f"[{suitability}] {gpu_name} 환경에서는 모든 게임이 120 FPS 이상으로 매우 쾌적하게 구동됩니다!"
    elif fps >= 60:
        suitability = "보통"
        message = f"[{suitability}] {gpu_name} 환경에서는 모든 게임이 60 FPS 이상으로 무난하게 플레이 가능합니다."
    else:
        suitability = "미달"
        message = f"[{suitability}] {gpu_name} 환경에서는 일부 고사양 게임이 60 FPS 미만으로 옵션 조정이 필요합니다."

    return fps_list, message


# =============================================
# 3. 입력받기: 그래픽카드(selectbox) & 그래픽 옵션(slider)
# =============================================
col1, col2 = st.columns(2)
with col1:
    selected_gpu = st.selectbox("🖥️ 그래픽카드(GPU) 선택", gpu_list, index=1)
with col2:
    selected_option = st.slider("⚙️ 그래픽 품질 옵션", 1, 5, 2)
    st.caption(f"현재 선택된 옵션: **{option_names[selected_option - 1]} ({selected_option}단계)**")

# =============================================
# 4. 버튼 클릭 시 함수 실행
# =============================================
if st.button("🚀 프레임 및 적합도 분석하기", type="primary", use_container_width=True):
    fps_list, message = predict_fps(selected_gpu, selected_option)

    # =============================================
    # 5. 조건 판단 (if-elif-else): 게임별 FPS에 따른 적합도 판정
    # =============================================
    suitability_list = []
    fit_count = 0

    for fps in fps_list:
        if fps >= 120:
            suitability = "🟢 적합"
            fit_count += 1
        elif fps >= 60:
            suitability = "🟡 보통"
        else:
            suitability = "🔴 미달"
        suitability_list.append(suitability)

    # =============================================
    # 6. 반복 출력 & 결과 화면 (1. 텍스트 메시지 -> 2. 테이블 -> 3. 강조 수치)
    # =============================================

    # [출력 1] 텍스트 메시지
    if min(fps_list) >= 120:
        st.success(message, icon="🔥")
    elif min(fps_list) >= 60:
        st.info(message, icon="✅")
    else:
        st.warning(message, icon="⚠️")

    # [출력 2] 테이블 (for문으로 게임별 FPS 및 적합도 리스트 순회하여 표 생성)
    table_data = []
    for i in range(len(games)):
        table_data.append(
            {
                "게임명": games[i],
                "예상 FPS": fps_list[i],
                "적합도": suitability_list[i],
            }
        )

    st.subheader("📊 게임별 예상 프레임 및 적합도")
    st.dataframe(
        pd.DataFrame(table_data),
        hide_index=True,
        use_container_width=True,
        column_config={
            "게임명": st.column_config.TextColumn("게임명", width="medium"),
            "예상 FPS": st.column_config.ProgressColumn(
                "예상 FPS",
                format="%d FPS",
                min_value=0,
                max_value=450,
            ),
            "적합도": st.column_config.TextColumn("적합도 (120 / 60 FPS 기준)"),
        },
    )

    # [출력 3] 강조 수치 (Metric)
    avg_fps = sum(fps_list) // len(fps_list)
    best_game = games[fps_list.index(max(fps_list))]

    st.subheader("🏆 핵심 성능 요약")
    m1, m2, m3 = st.columns(3)
    m1.metric("평균 예상 프레임", f"{avg_fps} FPS")
    m2.metric("최고 프레임 게임", best_game, f"{max(fps_list)} FPS")
    m3.metric("적합(120↑) 게임 수", f"{fit_count} / {len(games)}개")

    with st.expander("ℹ️ 프레임 계산 및 적합도 기준 보기"):
        st.markdown(
            f"""
            - **적합도 기준**: `120 FPS 이상` **적합** / `60 FPS 이상` **보통** / `60 FPS 미만` **미달**
            - **계산 공식**: `게임 기본 FPS × 그래픽카드 배율({gpu_rate[gpu_list.index(selected_gpu)]}배) × 옵션 가중치({int((1 - 0.15 * (selected_option - 1)) * 100)}%)`
            """
        )
else:
    st.info("그래픽카드와 옵션을 선택한 뒤 **프레임 및 적합도 분석하기** 버튼을 눌러 주세요.", icon="👆")
