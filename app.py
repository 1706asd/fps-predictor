"""

"""
import streamlit as st
import pandas as pd

# =============================================
# 1. 데이터 구조 (list) — 같은 칸 번호끼리 짝
# =============================================
games = ["리그 오브 레전드", "발로란트", "배틀그라운드"]
game_fps = [260, 240, 90]          # 게임별 기본 FPS (RTX 3060 · 옵션 1단계 기준)

gpu_list = ["RTX 3060", "RTX 4060", "RTX 4070"]
gpu_rate = [1.0, 1.2, 1.7]         # 성능 배율 (3060 = 1.0, 4060 약 +20%, 4070 약 +70%)

option_names = ["낮음", "보통", "높음", "매우 높음", "울트라"]

SMOOTH_FPS = 144                   # 이 이상이면 "쾌적"
MIN_FPS = 60                       # 이 미만이면 "업그레이드 필요"


# =============================================
# 2. 함수 (def)
# =============================================
def option_rate(option):
    """옵션 1단계 올릴 때마다 15%씩 감소 (1단계 = 100%)"""
    return 1 - 0.15 * (option - 1)


def predict_fps(gpu_name, option):
    """그래픽카드와 옵션을 받아 게임별 예상 FPS 리스트와 안내 문구를 돌려준다."""
    gpu_power = gpu_rate[gpu_list.index(gpu_name)]   # 고른 카드와 같은 칸의 배율

    fps_list = []
    for fps in game_fps:
        fps_list.append(int(fps * gpu_power * option_rate(option)))

    if min(fps_list) < MIN_FPS:
        message = f"{gpu_name}은(는) 일부 게임에서 업그레이드가 필요합니다."
    else:
        message = f"{gpu_name}은(는) 대부분의 게임을 쾌적하게 실행할 수 있습니다."
    return fps_list, message


# =============================================
# 3. 조건문 (if-elif-else)
# =============================================
def judge(fps):
    """FPS에 따라 판정 문구를 돌려준다."""
    if fps >= SMOOTH_FPS:
        return "🟢 쾌적"
    elif fps >= MIN_FPS:
        return "🟡 보통"
    else:
        return "🔴 업그레이드 필요"


# =============================================
# 화면: 제목
# =============================================
st.set_page_config(page_title="FPS 예측기", page_icon="🎮")

st.markdown(
    """
    <style>
    .hero {
        padding: 1.4rem 1.6rem; border-radius: 16px; margin-bottom: 1.2rem; color: white;
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 60%, #7c3aed 100%);
    }
    .hero h1 { margin: 0; font-size: 1.9rem; }
    .hero p  { margin: .3rem 0 0; opacity: .85; }
    div[data-testid="stMetric"] {
        background: rgba(124, 58, 237, .08); border-radius: 12px; padding: .8rem 1rem;
    }
    </style>
    <div class="hero">
        <h1>🎮 내 PC 게임 프레임 예측기</h1>
        <p>그래픽카드(GPU) 반도체 성능에 따라 게임이 얼마나 부드럽게 돌아갈까?</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# =============================================
# 화면: 입력 (selectbox, slider, button)
# =============================================
col1, col2 = st.columns(2)
with col1:
    gpu = st.selectbox("🖥️ 그래픽카드 선택", gpu_list, index=1)
with col2:
    option = st.slider("⚙️ 그래픽 옵션", 1, 5, 3)
    st.caption(f"현재 옵션: **{option_names[option - 1]}**")

# =============================================
# 화면: 결과 출력
# =============================================
if st.button("🚀 분석하기", type="primary"):
    fps_list, message = predict_fps(gpu, option)

    if min(fps_list) < MIN_FPS:
        st.warning(message, icon="⚠️")
    else:
        st.success(message, icon="✅")

    # 4. 반복문 (for): 게임 리스트를 돌며 표 데이터 만들기 + 쾌적한 게임 세기
    rows = []
    smooth_count = 0
    for i in range(len(games)):
        rows.append({"게임명": games[i], "예상 FPS": fps_list[i], "판정": judge(fps_list[i])})
        if fps_list[i] >= SMOOTH_FPS:
            smooth_count += 1

    # 강조 수치 (metric)
    average = sum(fps_list) // len(fps_list)
    best_game = games[fps_list.index(max(fps_list))]

    m1, m2, m3 = st.columns(3)
    m1.metric("평균 예상 프레임", f"{average} FPS", delta=judge(average), delta_color="off")
    m2.metric("가장 잘 돌아가는 게임", best_game)
    m3.metric("쾌적한 게임 수", f"{smooth_count} / {len(games)}")

    # 표 (dataframe)
    st.subheader("📊 게임별 예상 프레임")
    st.dataframe(
        pd.DataFrame(rows),
        hide_index=True,
        column_config={
            "예상 FPS": st.column_config.ProgressColumn(
                "예상 FPS", format="%d FPS", min_value=0, max_value=450
            ),
        },
    )

    with st.expander("ℹ️ 계산 방법 보기"):
        gpu_power = gpu_rate[gpu_list.index(gpu)]
        st.markdown(
            f"- 예상 FPS = 게임 기본 FPS × 그래픽카드 배율(**{gpu_power}배**)"
            f" × 옵션 배율(**{int(option_rate(option) * 100)}%**)\n"
            f"- 판정: {SMOOTH_FPS} FPS 이상 쾌적 · {MIN_FPS} FPS 이상 보통 · 그 아래는 업그레이드 필요\n"
            "- 게임 기본 FPS는 수업용 추정치, 그래픽카드 배율은 1080p 벤치마크 평균 참고"
        )
else:
    st.info("그래픽카드와 옵션을 고른 뒤 **분석하기** 버튼을 눌러 주세요.", icon="👆")


이거 streamlit에 올라면 됨?
