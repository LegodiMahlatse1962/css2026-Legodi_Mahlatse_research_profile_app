"""
Streamlit CV for Lesiba Simon Mahlatse Legodi
Updated: 2026 – Graduation and CSS 2026 Completion
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Lesiba Legodi | CV",
    page_icon="📄",
    layout="wide"
)

# ======================
# SIDEBAR
# ======================
st.sidebar.title("📄 Curriculum Vitae")
#st.sidebar.subheader("Lesiba Simon Mahlatse Legodi")

st.sidebar.write("📍 Polokwane, 31A Thabo Mbeki street")
st.sidebar.write("📧 legodilesiba1962@gmail.com")
st.sidebar.write("📞 060 738 6106")

st.sidebar.markdown("---")
st.sidebar.write("**Date of Birth:** 23 July 2000")
st.sidebar.write("**Place of Birth:** Mokopane")
st.sidebar.write("**Marital Status:** Single")

st.sidebar.markdown("---")
st.sidebar.subheader("🌍 Languages")
st.sidebar.write("- Sepedi (Native)")
st.sidebar.write("- English (Fluent)")

# ======================
# MAIN CONTENT
# ======================
st.title("Lesiba Simon Mahlatse, Legodi")
st.subheader("BSc Information Technology Graduate")

st.markdown("""
**Profile Summary**

BSc Information Technology graduate from North-West University with strong foundations in database systems, cybersecurity, networking, and artificial intelligence. 
Completed the **Coding Summer School (CSS 2026)** organized by CHPC (CSIR) and NITheCS, gaining hands-on experience in workflow management, ETL, exploratory data analysis, data visualization, computational thinking, statistics, and machine learning fundamentals.  
Enthusiastic about applying programming and system design to solve complex, real-world problems. Strong communicator with experience in media support and content creation.
""")

# ======================
# EDUCATION
# ======================
st.header("🎓 Education")

st.markdown("""
**North-West University – Vanderbijlpark Campus**  
BSc in Information Technology (Full Time) | *Graduated: 2025*  

**Relevant Modules**
- Database Design  
- Information Security  
- Decision Support Systems  
- Computer Networks  
- Artificial Intelligence  
- Programming (Java, C#, Python, C++)  
- Systems Analysis and Design  
""")

st.markdown("""
**Makgoka High School – Polokwane**  
NQF Level 4 Certificate | *Graduated: 2019*
""")

# ======================
# PROFESSIONAL DEVELOPMENT
# ======================
st.header("🚀 Professional Development")

with st.expander("Coding Summer School (CSS 2026) – CHPC & NITheCS"):
    st.write("""
    - Completed a two-week intensive programme covering:
      - Workflow management and ETL pipelines
      - Exploratory Data Analysis (EDA) and data visualization
      - Terminal skills and leveraging AI tools
      - Computational thinking, probability & statistics
      - Machine learning and AI fundamentals
    - Hands-on exercises and collaborative learning with 800+ students and professionals from 30+ research institutes and universities
    - **Certificate of Completion awarded**
    """)

# ======================
# TECHNICAL SKILLS
# ======================
st.header("🛠 Technical Skills")

col1, col2 = st.columns(2)

with col1:
    st.write("""
    **Programming**
    - Java
    - C#
    - Python
    - C++

    **Databases**
    - Database Design
    - SQL
    """)

with col2:
    st.write("""
    **Other Skills**
    - Cybersecurity Principles
    - Artificial Intelligence & Decision Support
    - Systems Analysis & Software Design
    - Networking & TCP/IP Concepts
    - IT Literacy (MS Office, Troubleshooting)
    - Public Speaking & Communication
    """)

# ======================
# EXPERIENCE
# ======================
st.header("💼 Experience")

with st.expander("Media Support Assistant | FNAS, North-West University"):
    st.write("""
    - Assisted faculty and staff with photography and media content creation  
    - Captured and edited event photographs  
    - Contributed to academic presentations and digital materials  
    """)

# ======================
# CERTIFICATIONS
# ======================
st.header("📜 Certifications")

st.markdown("""
- **Coding Summer School (CSS 2026)** – CHPC & NITheCS | Certificate of Completion  
- **Cybersecurity Incident Response Planning & Management** – Alison | 21 July 2025  
  🔗 https://alison.com/certification/check/2e76c8298f
""")

# ======================
# HOBBIES & INTERESTS
# ======================
st.header("⚽ Hobbies & Interests")

st.write("""
- Photography  
- Reading  
- Gardening  
- Soccer  
""")

st.markdown("---")
st.write("© 2026 Lesiba Simon Mahlatse Legodi")