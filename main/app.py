import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="Trend Content Generator", layout="wide", page_icon="🔥")

# Display title and caption
st.title("🔥 Trend Content Generator")
st.caption("Powered by live RSS trends + Groq AI")

# Your n8n Production Webhook URL
N8N_URL = "https://databeats123.app.n8n.cloud/webhook/generate-content"

if st.button("🔄 Fetch Latest Trends & Generate Content", type="primary", use_container_width=True):
    with st.spinner("Fetching live trends and generating content... (~45 seconds)"):
        try:
            # We use a 150-second timeout to allow the n8n workflow to complete its steps
            response = requests.post(N8N_URL, json={}, timeout=150)

            if response.status_code == 200:
                try:
                    result = response.json()
                except Exception:
                    st.error("Backend error: n8n returned success but the response was not valid JSON.")
                    st.code(response.text)
                    st.stop()

                # Extract the data from the response (handling both nested and flat JSON)
                data = result.get("data") if "data" in result else result

                # Check for the required 'title' key to ensure the AI worked
                if not data or "title" not in data:
                    st.error("Unexpected response structure from n8n. Check your workflow nodes.")
                    st.json(result)
                    st.stop()

                # ---- Display Content ----
                st.success("✅ Trending Content Ready!")
                st.divider()

                # Headline and Summary
                st.header(data.get("title", "No Title Found"))
                st.info(data.get("summary", "No summary available."))

                # Hashtags
                hashtags = data.get("hashtags", [])
                if isinstance(hashtags, list):
                    st.markdown("**🏷️ Hashtags:** " + " ".join(hashtags))
                else:
                    st.markdown(f"**🏷️ Hashtags:** {hashtags}")

                st.divider()

                # Social Media Columns
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.subheader("💼 LinkedIn")
                    st.text_area("", data.get("linkedin", ""), height=300, key="li")
                with col2:
                    st.subheader("📸 Instagram")
                    st.text_area("", data.get("instagram", ""), height=300, key="ig")
                with col3:
                    st.subheader("🐦 Twitter / X")
                    st.text_area("", data.get("twitter", ""), height=300, key="tw")

            # Handling API Rate Limits (429) specifically
            elif response.status_code == 429:
                st.warning("🛑 API Rate Limit reached. Please wait 60 seconds before trying again.")
            else:
                st.error(f"n8n returned status {response.status_code}")
                st.code(response.text)

        except requests.exceptions.Timeout:
            st.error("⏱️ Request timed out. The backend processing took longer than 2.5 minutes.")
        except Exception as e:
            st.error(f"Unexpected error: {e}")

# CLEAN FOOTER: No personal name included
st.divider()
st.caption("🚀 Live AI Content")