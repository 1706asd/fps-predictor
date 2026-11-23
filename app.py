"""
🎮 내 PC 게임 프레임(FPS) 예측기
- 진로 연계: 반도체 공학 (GPU 칩 미세공정·연산 성능 → 실제 게임 프레임 체감)
"""
import streamlit as st
import pandas as pd

# =============================================
# 1. 시작: 페이지 설정 및 게이밍 벤치마크 UI 스타일
# =============================================
st.set_page_config(page_title="GPU FPS 예측기", page_icon="🎮", layout="centered")

st.markdown(
    """
    <style>
    .hero-banner {
        padding: 1.6rem 1.8rem;
        border-radius: 16px;
        margin-bottom: 1.3rem;
        color: #f8fafc;
        background: linear-gradient(135deg, #090d16 0%, #172554 55%, #4c1d95 100%);
        border: 1px solid rgba(139, 92, 246, 0.4);
        box-shadow: 0 10px 25px rgba(15, 23, 42, 0.35);
    }
    .hero-badge {
        display: inline-block;
        padding: 0.2rem 0.65rem;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        border-radius: 999px;
        background: rgba(56, 189, 248, 0.2);
        color: #38bdf8;
        border: 1px solid rgba(56, 189, 248, 0.4);
        margin-bottom: 0.5rem;
    }
    .hero-banner h1 {
        margin: 0;
        font-size: 1.85rem;
        font-weight: 800;
        letter-spacing: -0.02em;
    }
    .hero-banner p {
        margin: 0.4rem 0 0;
        font-size: 0.95rem;
        color: #cbd5e1;
    }
    div[data-testid="stMetric"] {
        background: linear-gradient(180deg, rgba(30, 41, 59, 0.06) 0%, rgba(99, 102, 241, 0.1) 100%);
        border: 1px solid rgba(99, 102, 241, 0.25);
        border-radius: 14px;
        padding: 0.9rem 1.1rem;
    }
    </style>
    <div class="hero-banner">
        <div class="hero-badge">SEMICONDUCTOR × GPU BENCHMARK</div>
        <h1>🎮 내 PC 게임 프레임(FPS) 예측기</h1>
        <p>GPU 반도체 연산 성능과 그래픽 옵션에 따른 게임별 프레임 및 적합도 분석</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# =============================================
# 2. 리스트 선언: 게임, 기본 FPS, GPU 성능 배율, 옵션
# =============================================
games = ["리그 오브 레전드", "발로란트", "배틀그라운드"]
base_fps = [260, 240, 90]  # RTX 3060 · 옵션 1단계(낮음) 기준 기본 FPS

gpu_list = ["RTX 3060", "RTX 4060", "RTX 4070"]
gpu_rate = [1.0, 1.2, 1.7]  # GPU 반도체 세대·코어 성능 배율
option_names = ["낮음", "보통", "높음", "매우 높음", "울트라"]


# =============================================
# 핵심 함수 (def): 예상 FPS 계산 및 적합도 판별
# =============================================
def predict_fps(gpu_name, option):
    """GPU 이름과 그래픽 옵션을 매개변수로 받아 예상 FPS 리스트와 적합도 텍스트 메시지를 리턴"""
    gpu_power = gpu_rate[gpu_list.index(gpu_name)]
    option_weight = 1 - 0.15 * (option - 1)  # 옵션 1단계 상승 시 프레임 15% 감소

    fps_list = []
    for base in base_fps:
        predicted = int(base * gpu_power * option_weight)
        fps_list.append(predicted)

    # 최저 프레임(fps) 기준 전체 구동 적합도 조건 판단 (120 / 60 프레임 기준)
    fps = min(fps_list)
    if fps >= 120:
        suitability = "적합"
        message = f"[{suitability}] {gpu_name}은(는) 모든 게임에서 120 FPS 이상을 유지하여 매우 적합합니다!"
    elif fps >= 60:
        suitability = "보통"
        message = f"[{suitability}] {gpu_name}은(는) 모든 게임에서 60 FPS 이상으로 무난하게 플레이 가능합니다."
    else:
        suitability = "미달"
        message = f"[{suitability}] {gpu_name}은(는) 고사양 게임에서 60 FPS 미만으로 옵션 타협이나 업그레이드가 필요합니다."

    return fps_list, message


# =============================================
# 3. 입력받기: 그래픽카드(selectbox) & 그래픽 옵션(slider)
# =============================================
col1, col2 = st.columns(2)
with col1:
    selected_gpu = st.selectbox("🖥️ 그래픽카드(GPU) 선택", gpu_list, index=1)
with col2:
    selected_option = st.slider("⚙️ 그래픽 품질 옵션", 1, 5, 2)
    st.caption(f"선택된 그래픽 품질: **{option_names[selected_option - 1]} ({selected_option}단계)**")

# =============================================
# 4. 버튼 클릭 시 함수 실행
# =============================================
if st.button("🚀 FPS 및 적합도 분석하기", type="primary", use_container_width=True):
    fps_list, message = predict_fps(selected_gpu, selected_option)

    # =============================================
    # 5. 조건 판단 (if-elif-else): 게임별 FPS에 따른 적합도 리스트 생성
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

    # 전체 안내 메시지 출력
    if min(fps_list) >= 120:
        st.success(message, icon="🔥")
    elif min(fps_list) >= 60:
        st.info(message, icon="✅")
    else:
        st.warning(message, icon="⚠️")

    # 상단 핵심 지표 (Metric) 요약
    avg_fps = sum(fps_list) // len(fps_list)
    best_game = games[fps_list.index(max(fps_list))]

    m1, m2, m3 = st.columns(3)
    m1.metric("평균 예상 프레임", f"{avg_fps} FPS")
    m2.metric("최고 프레임 게임", best_game, f"{max(fps_list)} FPS")
    m3.metric("적합(120↑) 게임 수", f"{fit_count} / {len(games)}개")

    # =============================================
    # 6. 반복 출력 (for): FPS 리스트와 적합도 리스트를 순회해 테이블 생성
    # =============================================
    table_data = []
    for i in range(len(games)):
        table_data.append(
            {
                "게임명": games[i],
                "예상 FPS": fps_list[i],
                "적합도": suitability_list[i],
            }
        )

    st.subheader("📊 게임별 예상 프레임 및 적합도 분석표")
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
            "적합도": st.column_config.TextColumn("적합도 (기준: 120 / 60 FPS)"),
        },
    )

    with st.expander("🔬 반도체 공학 원리 및 산출 기준 보기"):
        st.markdown(
            f"""
            - **적합도 판정 기준**: `120 FPS 이상` **적합** (고주사율 게이밍) / `60 FPS 이상` **보통** (원활한 구동) / `60 FPS 미만` **미달**
            - **적용 연산식**: `기본 FPS × GPU 성능 배율({gpu_rate[gpu_list.index(selected_gpu)]}배) × 옵션 가중치({int((1 - 0.15 * (selected_option - 1)) * 100)}%)`
            - **반도체 연계 포인트**: 미세공정(4nm 등) 고도화로 동일 면적당 트랜지스터와 CUDA 코어 집적도가 높아질수록 GPU의 병렬 연산 처리량(FPS)이 비약적으로 상승합니다.
            """
        )
else:
    st.info("위에서 그래픽카드와 옵션을 선택한 뒤 **FPS 및 적합도 분석하기** 버튼을 눌러 주세요.", icon="👆")
