import streamlit as st
from youtube_agent import youtube_agent

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="AI YouTube Analyzer",
    page_icon="🎥",
    layout="centered",
)

# -------------------- CUSTOM DARK UI --------------------
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    .stTextInput input {
        background-color: #1E1E1E;
        color: white;
        border-radius: 8px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        height: 45px;
        width: 100%;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .result-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #1A1A1A;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- TITLE --------------------
st.title("🎥 AI YouTube Video Analyzer")
st.caption("Analyze any YouTube video with AI insights 💻")


# -------------------- LOAD AGENT --------------------
@st.cache_resource
def get_agent():
    return youtube_agent()

agent = get_agent()

# -------------------- INPUT SECTION --------------------
video_url = st.text_input("🔗 Enter YouTube Video URL")

analyze_btn = st.button("🚀 Analyze Video")


# -------------------- VALIDATION --------------------
def is_valid_youtube_url(url):
    return "youtube.com" in url or "youtu.be" in url

# -------------------- MAIN LOGIC --------------------
if analyze_btn:
    if not video_url:
        st.warning("⚠️ Please enter a YouTube URL")
    elif not is_valid_youtube_url(video_url):
        st.error("❌ Invalid YouTube link")
    else:
        with st.spinner("⏳ Analyzing video... Please wait"):
            try:
                response = agent.run(
                    f"Analyze this video: {video_url}"
                )

                st.success("✅ Analysis Complete!")

                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.subheader("📊 Analysis Report")
                st.markdown(response.content)
                st.markdown('</div>', unsafe_allow_html=True)

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")


# -------------------- FOOTER --------------------
st.markdown("---")
st.markdown("💡 Built with Streamlit | AI Powered Project")