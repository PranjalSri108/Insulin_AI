import streamlit as st

# 🌟 App title and intro
st.set_page_config(page_title="AI for Insulin Mutations", layout="centered")
st.title("🧠 AI-Powered Insulin Mutation Impact Explorer")
st.markdown("""
This demo interface simulates how artificial intelligence can help predict the **impact of genetic mutations on human insulin** stability using pretrained protein models like ESM.

🔬 Enter an insulin sequence and a mutation to see a sample prediction and visualization.
""")

# 🧬 Input section
with st.form("mutation_form"):
    wt_seq = st.text_area("Wild-Type Insulin Sequence", 
        "MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKA", height=150)

    col1, col2 = st.columns(2)
    with col1:
        pos = st.number_input("Mutation Position", min_value=1, max_value=len(wt_seq), value=28)
    with col2:
        mut_aa = st.text_input("Mutant Amino Acid (1-letter code)", max_chars=1).upper()

    submitted = st.form_submit_button("Predict Mutation Impact")

# 🎯 Simulated Prediction Output
if submitted:
    if len(wt_seq) < pos or not mut_aa.isalpha() or len(mut_aa) != 1:
        st.error("⚠️ Please enter a valid position and a single-letter amino acid.")
    else:
        # Create mutated sequence
        mut_seq = wt_seq[:pos - 1] + mut_aa + wt_seq[pos:]

        st.subheader("🔍 Mutant Sequence Preview")
        highlighted_seq = (
            wt_seq[:pos - 1] + f"**:{mut_aa}:**" + wt_seq[pos:]
        )
        st.markdown(f"**Mutated Sequence:** {highlighted_seq}", unsafe_allow_html=True)

        # Simulated prediction
        ddg_fake = 0.75 if mut_aa in ['D', 'E'] else -0.55

        st.subheader("📊 Simulated Prediction")
        st.metric("ΔΔG (Simulated)", f"{ddg_fake:.2f} kcal/mol", delta="↑" if ddg_fake > 0 else "↓")

        if ddg_fake > 0:
            st.error("⚠️ Prediction indicates a destabilizing mutation.")
        else:
            st.success("✅ Prediction indicates a stabilizing mutation.")




