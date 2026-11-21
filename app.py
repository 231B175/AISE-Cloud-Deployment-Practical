import streamlit as st


st.set_page_config(
    page_title="AISE Cloud Deployment Demo",
    page_icon="AI",
    layout="centered",
)


st.markdown(
    """
    <style>
    .hero {
        padding: 2rem;
        border-radius: 1rem;
        background: linear-gradient(135deg, #eef2ff 0%, #e0f2fe 100%);
        margin-bottom: 1.5rem;
    }
    .hero h1 {
        margin-bottom: 0.35rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <h1>AI-Enabled Software Engineering</h1>
        <p>Cloud Deployment Demonstration</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write(
    "Use this demo to verify that your Streamlit application is deployed "
    "and responding correctly."
)

with st.container(border=True):
    st.subheader("Deployment check")
    name = st.text_input(
        "Your name",
        placeholder="Enter your name",
        max_chars=80,
    )

    col1, col2 = st.columns([1, 4])
    with col1:
        submitted = st.button("Submit", type="primary", use_container_width=True)
    with col2:
        st.caption("The button and form should both respond.")

    if submitted:
        clean_name = name.strip()
        if clean_name:
            st.success(f"Hello, {clean_name}! Your deployment is working.")
        else:
            st.warning("Please enter your name before submitting.")

st.divider()
st.caption("Status: Application is running")