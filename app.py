import streamlit as st
from pipeline import verify_question

st.set_page_config(
    page_title="Hallucination Guard",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Hallucination Guard")
st.write("Evidence-Based Verification System for Large Language Models")

question = st.text_input(
    "Enter your question:",
    placeholder="Example: What is the capital of France?"
)

if st.button("Verify Answer"):

    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating and verifying answer..."):

            result = verify_question(question)

        st.subheader("Generated Answer")
        st.write(result["answer"])

        st.subheader("Verification Result")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Confidence",
                f"{result['confidence']:.2f}%"
            )

        with col2:
            st.metric(
                "Semantic Similarity",
                f"{result['similarity']:.4f}"
            )

        with col3:
            st.metric(
                "NLI",
                result["nli_label"].capitalize()
            )

        if result["status"] == "Verified":
            st.success("✅ Verified")

        elif result["status"] == "Low Confidence":
            st.warning("⚠️ Low Confidence")

        else:
            st.error("❌ Possible Hallucination")

        st.subheader("Best Supporting Evidence")
        st.info(result["best_evidence"])

        with st.expander("View All Retrieved Evidence"):

            for i, evidence in enumerate(
                result["evidence"], 1
            ):
                st.write(f"**Evidence {i}:**")
                st.write(evidence)
                st.divider()