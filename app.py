import streamlit as st

st.set_page_config(
    page_title="Near-Duplicate Image Detection",
    page_icon="🖼️",
    layout="wide"
)

st.markdown("""
<style>
.typewriter {
    font-size: 42px;
    font-weight: 800;
    color: #4f46e5;   /* light + dark safe */
    overflow: hidden;
    white-space: nowrap;
    border-right: 3px solid rgba(79,70,229,0.8);
    width: 0;
    animation:
        typing 3s steps(35, end) forwards,
        blink 0.8s step-end infinite;
}

/* typing animation */
@keyframes typing {
    from { width: 0 }
    to { width: 100% }
}

/* cursor blink */
@keyframes blink {
    50% { border-color: transparent }
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="typewriter">🖼️ Near-Duplicate Image Detection</div>',
    unsafe_allow_html=True
)

st.write("Colab me Streamlit chal raha hai 😎")
