import streamlit as st
import requests
import plotly.graph_objects as go

st.set_page_config(page_title="DevTracker Pro", layout="wide", page_icon="🚀")

st.markdown("""
<style>
.metric-card { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 15px; color: white; text-align: center; }
.stTextInput>div>div>input { border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

st.title("🚀 GitHub + LeetCode Tracker - Pro Edition")
st.write("Enter username to get live stats with charts")

col1, col2 = st.columns(2)
with col1:
    github_user = st.text_input("GitHub Username daal", placeholder="e.g. torvalds")
with col2:
    leet_user = st.text_input("LeetCode Username daal", placeholder="e.g. neal")

if st.button("🔥 Show Pro Stats", use_container_width=True):
    if not github_user and not leet_user:
        st.warning("Ek toh username daal bhai!")
    else:
        c1, c2 = st.columns(2)

        # --- GITHUB ---
        if github_user:
            with c1:
                st.subheader(f"GitHub: {github_user}")
                r = requests.get(f"https://api.github.com/users/{github_user}").json()
                if "message" not in r:
                    st.image(r['avatar_url'], width=120)
                    m1, m2, m3 = st.columns(3)
                    m1.metric("Repos", r['public_repos'])
                    m2.metric("Followers", r['followers'])
                    m3.metric("Following", r['following'])

                    # Chart
                    fig = go.Figure(data=[go.Bar(x=['Repos','Followers','Following'], y=[r['public_repos'], r['followers'], r['following']], marker_color=['#667eea','#764ba2','#f093fb'])])
                    fig.update_layout(height=300, margin=dict(l=0,r=0,t=0,b=0))
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.error("GitHub user nahi mila!")

        # --- LEETCODE ---
        if leet_user:
            with c2:
                st.subheader(f"LeetCode: {leet_user}")
                try:
                    q = {"query": "query getUserProfile($username: String!) { matchedUser(username: $username) { submitStats { acSubmissionNum { difficulty count } } profile { ranking } } }", "variables": {"username": leet_user}}
                    res = requests.post("https://leetcode.com/graphql", json=q).json()
                    stats = res['data']['matchedUser']['submitStats']['acSubmissionNum']
                    rank = res['data']['matchedUser']['profile']['ranking']

                    easy = stats[1]['count']
                    med = stats[2]['count']
                    hard = stats[3]['count']
                    total = stats[0]['count']

                    m1, m2, m3, m4 = st.columns(4)
                    m1.metric("Total", total)
                    m2.metric("Easy", easy)
                    m3.metric("Med", med)
                    m4.metric("Hard", hard)
                    st.metric("Global Rank", f"#{rank}")

                    # Pie Chart
                    fig2 = go.Figure(data=[go.Pie(labels=['Easy','Medium','Hard'], values=[easy, med, hard], hole=.5, marker_colors=['#00CC96','#FFA15A','#EF553B'])])
                    fig2.update_layout(height=300, margin=dict(l=0,r=0,t=0,b=0), showlegend=True)
                    st.plotly_chart(fig2, use_container_width=True)
                except:
                    st.error("LeetCode user nahi mila ya API limit!")

st.divider()
st.caption("Built with Streamlit | DevTracker Pro v2.0 | Highly Standard Edition")