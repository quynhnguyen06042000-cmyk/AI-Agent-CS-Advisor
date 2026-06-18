import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Agent Advisor",
    layout="wide"
)

st.title("🤖 AI Agent Advisor for Computer Science")
st.subheader("Phân tích và Khuyến nghị ứng dụng AI Agent trong lĩnh vực Khoa học Máy tính")

# =========================
# DATA
# =========================

data = {
    "Field": [
        "Software Development",
        "Education",
        "Research",
        "Cybersecurity",
        "Project Management"
    ],
    "Potential Score": [
        95,
        90,
        88,
        85,
        80
    ]
}

df = pd.DataFrame(data)

# =========================
# DASHBOARD
# =========================

st.header("📊 Tổng quan")

st.bar_chart(
    df.set_index("Field")
)

st.write(
    """
Biểu đồ thể hiện mức độ tiềm năng ứng dụng AI Agent
trong các lĩnh vực của Khoa học Máy tính.
"""
)

# =========================
# ANALYSIS
# =========================

st.header("🔍 Phân tích lĩnh vực")

field = st.selectbox(
    "Chọn lĩnh vực",
    df["Field"]
)

if st.button("Analyze"):

    if field == "Software Development":

        st.subheader("💻 Software Development")

        st.write("### AI Agent Applications")

        st.write("""
- Code Generation Agent
- Debugging Agent
- Testing Agent
- Code Review Agent
        """)

        st.write("### Benefits")

        st.write("""
- Tăng năng suất lập trình
- Giảm lỗi phần mềm
- Rút ngắn thời gian phát triển
        """)

        st.write("### Recommendation")

        st.success("""
Khuyến nghị triển khai AI Agent
trong quy trình phát triển phần mềm.

Ví dụ:
- GitHub Copilot
- Cursor
- Windsurf
        """)

    elif field == "Education":

        st.subheader("🎓 Computer Science Education")

        st.write("### AI Agent Applications")

        st.write("""
- Virtual Teaching Assistant
- Personalized Learning Agent
- Auto Grading Agent
        """)

        st.write("### Benefits")

        st.write("""
- Hỗ trợ học tập 24/7
- Cá nhân hóa lộ trình học
- Giảm tải cho giảng viên
        """)

        st.write("### Recommendation")

        st.success("""
Khuyến nghị triển khai AI Teaching Assistant
cho các môn lập trình và thuật toán.
        """)

    elif field == "Research":

        st.subheader("🔬 Research")

        st.write("### AI Agent Applications")

        st.write("""
- Research Assistant Agent
- Literature Review Agent
- Paper Summarization Agent
        """)

        st.write("### Benefits")

        st.write("""
- Tiết kiệm thời gian đọc tài liệu
- Tăng hiệu quả nghiên cứu
- Hỗ trợ khám phá tri thức
        """)

        st.write("### Recommendation")

        st.success("""
Khuyến nghị xây dựng AI Research Assistant
cho sinh viên và giảng viên.
        """)

    elif field == "Cybersecurity":

        st.subheader("🔐 Cybersecurity")

        st.write("### AI Agent Applications")

        st.write("""
- Threat Detection Agent
- Security Monitoring Agent
- Incident Response Agent
        """)

        st.write("### Benefits")

        st.write("""
- Phát hiện tấn công nhanh hơn
- Tăng cường bảo mật
- Giảm thời gian phản ứng
        """)

        st.write("### Recommendation")

        st.success("""
Khuyến nghị tích hợp AI Agent
vào hệ thống giám sát an ninh mạng.
        """)

    elif field == "Project Management":

        st.subheader("📈 Project Management")

        st.write("### AI Agent Applications")

        st.write("""
- Risk Prediction Agent
- Resource Allocation Agent
- Progress Monitoring Agent
        """)

        st.write("### Benefits")

        st.write("""
- Tối ưu nguồn lực
- Dự báo rủi ro
- Hỗ trợ ra quyết định
        """)

        st.write("### Recommendation")

        st.success("""
Khuyến nghị tích hợp AI Agent
với Jira, Trello hoặc GitHub Projects.
        """)

# =========================
# FINAL RECOMMENDATION
# =========================

st.header("🏆 Khuyến nghị ưu tiên")

ranking = pd.DataFrame(
    {
        "Rank": [1, 2, 3],
        "Field": [
            "Software Development",
            "Education",
            "Research"
        ]
    }
)

st.table(ranking)

st.info(
    """
Theo phân tích, ba lĩnh vực nên ưu tiên triển khai AI Agent là:

1. Software Development
2. Education
3. Research

Do có tính khả thi cao và mang lại giá trị lớn.
"""
)