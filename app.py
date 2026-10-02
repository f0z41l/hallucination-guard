
import streamlit as st
from pipeline import verify_question


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Hallucination Guard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# --------------------------------------------------
# Custom CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    /* Main container */
    .block-container {
        max-width: 1100px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }


    /* Header */

    .main-title {
        text-align: center;
        font-size: 2.4rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }

    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1rem;
        margin-bottom: 2rem;
    }


    /* Mobile */

    @media (max-width: 768px) {

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;

            /* Extra space below Streamlit mobile toolbar */
            padding-top: 5rem;
        }

        .main-title {
            font-size: 1.8rem;
        }

        .subtitle {
            font-size: 0.9rem;
            margin-bottom: 1.5rem;
        }

        .stButton > button {
            width: 100%;
            min-height: 3rem;
            font-size: 1rem;
        }

        [data-testid="stMetric"] {
            padding: 0.5rem 0;
        }

        p {
            word-wrap: break-word;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="main-title">Hallucination Guard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Evidence-Based Verification System for Large Language Models'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# Question Input
# --------------------------------------------------

st.subheader("Ask a Question")

question = st.text_area(
    "Enter your question",
    placeholder="Example: What is the capital of France?",
    height=100,
    label_visibility="collapsed"
)

verify_button = st.button(
    "Verify Answer",
    use_container_width=True
)


# --------------------------------------------------
# Verification
# --------------------------------------------------

if verify_button:

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner(
            "Generating answer and verifying evidence..."
        ):

            result = verify_question(question)


        # --------------------------------------------------
        # Generated Answer
        # --------------------------------------------------

        st.subheader("Generated Answer")

        st.info(result["answer"])


        # --------------------------------------------------
        # Verification Result
        # --------------------------------------------------

        st.subheader("Verification Result")

        if result["status"] == "Verified":

            st.success("Verified")

        elif result["status"] == "Low Confidence":

            st.warning("Low Confidence")

        else:

            st.error("Possible Hallucination")


        # --------------------------------------------------
        # Metrics
        # --------------------------------------------------

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


        # --------------------------------------------------
        # Confidence Level
        # --------------------------------------------------

        st.write("**Confidence Level**")

        st.progress(
            int(result["confidence"])
        )


        # --------------------------------------------------
        # Best Supporting Evidence
        # --------------------------------------------------

        st.subheader("Best Supporting Evidence")

        st.info(result["best_evidence"])


        # --------------------------------------------------
        # All Retrieved Evidence
        # --------------------------------------------------

        with st.expander("View All Retrieved Evidence"):

            for i, evidence in enumerate(
                result["evidence"], 1
            ):

                st.markdown(
                    f"**Evidence {i}**"
                )

                st.write(evidence)

                if i < len(result["evidence"]):

                    st.divider()


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "Hallucination Guard • Evidence-Based LLM Verification"
)
