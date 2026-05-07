import streamlit as st
import requests

st.set_page_config(page_title="Trend Content Generator", layout="wide", page_icon="🔥")

st.title("🔥 Trend Content Generator")
st.caption("Powered by live RSS trends + Groq AI")

N8N_URL = "https://databeats123.app.n8n.cloud/webhook/generate-content"

if st.button("🔄 Fetch Latest Trends & Generate Content", type="primary", use_container_width=True):
    with st.spinner("Fetching live trends and generating content... (~45 seconds)"):
        try:
            response = requests.post(N8N_URL, json={}, timeout=120)

            if response.status_code == 200:
                try:
                    result = response.json()
                except Exception:
                    st.error("n8n returned 200 but body is not valid JSON.")
                    st.code(response.text)
                    st.stop()

                # Handle both {success: true, data: {...}} and flat {...}
                data = result.get("data") if "data" in result else result

                if not data or "title" not in data:
                    st.error("Unexpected response structure from n8n.")
                    st.json(result)
                    st.stop()

                # ---- Display Content ----
                st.success("✅ Trending Content Ready!")
                st.divider()

                st.header(data["title"])
                st.info(data["summary"])

                hashtags = data.get("hashtags", [])
                if isinstance(hashtags, list):
                    st.markdown("**🏷️ Hashtags:** " + " ".join(hashtags))
                else:
                    st.markdown(f"**🏷️ Hashtags:** {hashtags}")

                st.divider()

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.subheader("💼 LinkedIn")
                    st.text_area("", data.get("linkedin", ""), height=280, key="li")
                with col2:
                    st.subheader("📸 Instagram")
                    st.text_area("", data.get("instagram", ""), height=280, key="ig")
                with col3:
                    st.subheader("🐦 Twitter / X")
                    st.text_area("", data.get("twitter", ""), height=280, key="tw")

            else:
                st.error(f"n8n returned status {response.status_code}")
                st.code(response.text)

        except requests.exceptions.Timeout:
            st.error("⏱️ Request timed out. n8n took longer than 2 minutes. Check the Executions tab.")
        except requests.exceptions.ConnectionError:
            st.error("🔌 Cannot connect to n8n. Make sure the workflow is Published.")
        except Exception as e:
            st.error(f"Unexpected error: {e}")