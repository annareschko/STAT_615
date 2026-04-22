import streamlit as st

st.set_page_config(page_title="Economics Concept Explorer", page_icon="📈", layout="wide")

# -----------------------------
# Mini Knowledge Base
# -----------------------------
ECON_CONCEPTS = {
    "opportunity cost": {
        "title": "Opportunity Cost",
        "explanation": (
            "Opportunity cost is the value of the next best alternative that is given up "
            "when a choice is made. Every decision involves a trade-off."
        ),
        "key_terms": ["trade-off", "scarcity", "marginal analysis"],
        "examples": [
            "Choosing to study instead of working a paid shift — the opportunity cost is the wages you give up.",
            "A business using land for a store instead of a parking lot — the opportunity cost is the revenue the parking lot could have generated."
        ],
        "fun_fact": "The phrase 'There is no such thing as a free lunch' is a classic way to explain opportunity cost.",
        "related": ["scarcity", "production possibility frontier", "marginal analysis"],
    },

    "inflation": {
        "title": "Inflation",
        "explanation": (
            "Inflation is the sustained increase in the general price level of goods and services. "
            "When inflation rises, purchasing power falls."
        ),
        "key_terms": ["price level", "CPI", "purchasing power"],
        "examples": [
            "If inflation is 6%, a $100 grocery basket now costs $106.",
            "High inflation can erode savings if interest rates are lower than inflation."
        ],
        "fun_fact": "Most central banks target around 2% inflation per year.",
        "related": ["monetary policy", "deflation", "hyperinflation"],
    },

    "quantitative easing": {
        "title": "Quantitative Easing (QE)",
        "explanation": (
            "Quantitative easing is a monetary policy where a central bank buys long-term assets "
            "to lower interest rates and increase money supply when short-term rates are already near zero."
        ),
        "key_terms": ["central bank", "bond purchases", "liquidity"],
        "examples": [
            "After the 2008 crisis, the Federal Reserve bought large amounts of Treasury and mortgage-backed securities.",
            "QE is often used during recessions to stimulate borrowing and investment."
        ],
        "fun_fact": "QE was once considered unconventional, but it is now a standard recession tool.",
        "related": ["monetary policy", "interest rates", "open market operations"],
    },

    "aggregate demand": {
        "title": "Aggregate Demand",
        "explanation": (
            "Aggregate demand is the total demand for all final goods and services in an economy. "
            "It includes consumption, investment, government spending, and net exports."
        ),
        "key_terms": ["GDP", "consumption", "investment", "government spending", "net exports"],
        "examples": [
            "A tax cut increases disposable income, raising consumption and aggregate demand.",
            "A global slowdown reduces demand for exports, lowering aggregate demand."
        ],
        "fun_fact": "Keynesian economics emphasizes managing aggregate demand to stabilize the economy.",
        "related": ["aggregate supply", "fiscal policy", "business cycles"],
    },
}

QUICK_TOPICS = ["opportunity cost", "inflation", "quantitative easing", "aggregate demand"]


# -----------------------------
# Helper Function
# -----------------------------
def find_concept(query: str):
    if not query:
        return None

    q = query.lower().strip()

    # Exact match
    if q in ECON_CONCEPTS:
        return ECON_CONCEPTS[q]

    # Partial match
    for key, data in ECON_CONCEPTS.items():
        if q in key.lower() or q in data["title"].lower():
            return data

    return None


# -----------------------------
# UI Layout
# -----------------------------
st.title("📈 Economics Concept Explorer")
st.write("Search any economics concept to get explanations, examples, key terms, and related ideas.")

col1, col2 = st.columns([2, 1])

with col1:
    query = st.text_input("Search for a concept")

    st.write("### Quick Topics")
    quick_cols = st.columns(len(QUICK_TOPICS))
    for i, topic in enumerate(QUICK_TOPICS):
        if quick_cols[i].button(topic.title()):
            query = topic

    concept = find_concept(query)

    if not query:
        st.info("Type a concept above or click a quick topic to begin.")
    elif concept is None:
        st.warning("Concept not found. Try another economics term.")
    else:
        st.markdown(f"## {concept['title']}")
        st.markdown(f"**Explanation:** {concept['explanation']}")

        st.markdown("### Key Terms")
        for term in concept["key_terms"]:
            st.write(f"- {term}")

        st.markdown("### Real-World Examples")
        for ex in concept["examples"]:
            st.write(f"- {ex}")

        st.markdown("### Fun Fact")
        st.info(concept["fun_fact"])

        st.markdown("### Related Concepts")
        rel_cols = st.columns(len(concept["related"]))
        for i, rel in enumerate(concept["related"]):
            if rel_cols[i].button(rel.title(), key=f"rel_{rel}"):
                st.session_state["query"] = rel
                st.experimental_rerun()

with col2:
    st.markdown("### What This App Can Do")
    st.write("- Explore micro & macro concepts")
    st.write("- Learn key terms and examples")
    st.write("- Jump between related ideas")
    st.write("- Great for studying or teaching")

    st.markdown("### Ideas to Expand")
    st.write("- Add more concepts")
    st.write("- Add quizzes or flashcards")
    st.write("- Add charts or diagrams")
    st.write("- Connect to a real AI API later")
