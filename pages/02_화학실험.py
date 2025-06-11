import streamlit as st

st.set_page_config(page_title="산-염기 중화 시뮬레이션", layout="centered")

st.title("🔬 산-염기 중화 시뮬레이션")

st.markdown("""
이 실험은 **강산 (HCl)** 과 **강염기 (NaOH)** 의 반응을 가정한 중화 반응 시뮬레이션입니다.  
**반응식:** `HCl + NaOH → NaCl + H₂O`
""")

st.subheader("🧪 실험값 입력")

# 입력값
acid_conc = st.number_input("산(HCl) 농도 (M)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
acid_vol = st.number_input("산 부피 (mL)", min_value=1, max_value=500, value=50)

base_conc = st.number_input("염기(NaOH) 농도 (M)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
base_vol = st.number_input("염기 부피 (mL)", min_value=1, max_value=500, value=50)

# 계산
acid_moles = acid_conc * (acid_vol / 1000)
base_moles = base_conc * (base_vol / 1000)

st.subheader("🧾 결과")

# 반응 결과 계산
if acid_moles > base_moles:
    excess = acid_moles - base_moles
    result = f"산이 {excess:.3f} mol 만큼 남았습니다. 용액은 **산성**입니다. (pH ≈ 1~3)"
elif base_moles > acid_moles:
    excess = base_moles - acid_moles
    result = f"염기가 {excess:.3f} mol 만큼 남았습니다. 용액은 **염기성**입니다. (pH ≈ 11~13)"
else:
    result = "완전 중화되었습니다. 용액은 **중성**입니다. (pH ≈ 7)"

# 출력
st.markdown(f"""
- 산 몰수: **{acid_moles:.3f} mol**  
- 염기 몰수: **{base_moles:.3f} mol**  
- {result}
""")
