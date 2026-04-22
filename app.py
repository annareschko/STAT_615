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

    "aggregate supply": {
        "title": "Aggregate Supply",
        "explanation": (
            "Aggregate supply represents the total output firms are willing to produce at different price levels. "
            "In the long run, it depends on productivity, labor, and capital."
        ),
        "key_terms": ["LRAS", "SRAS", "productivity", "input costs"],
        "examples": [
            "A rise in oil prices shifts short-run aggregate supply left.",
            "Technological improvements shift long-run aggregate supply right."
        ],
        "fun_fact": "In the long run, aggregate supply is vertical because output depends on real factors, not prices.",
        "related": ["aggregate demand", "inflation", "economic growth"],
    },

    "fiscal policy": {
        "title": "Fiscal Policy",
        "explanation": (
            "Fiscal policy refers to government decisions about spending and taxation to influence the economy."
        ),
        "key_terms": ["government spending", "taxation", "budget deficit"],
        "examples": [
            "A government increases infrastructure spending to stimulate the economy.",
            "Tax cuts raise household disposable income and boost consumption."
        ],
        "fun_fact": "John Maynard Keynes popularized the idea of using fiscal policy to fight recessions.",
        "related": ["aggregate demand", "monetary policy", "business cycles"],
    },

    "monetary policy": {
        "title": "Monetary Policy",
        "explanation": (
            "Monetary policy involves central bank actions that influence interest rates, money supply, and credit conditions."
        ),
        "key_terms": ["interest rates", "money supply", "central bank"],
        "examples": [
            "The Federal Reserve raises interest rates to reduce inflation.",
            "Lowering interest rates encourages borrowing and investment."
        ],
        "fun_fact": "Most central banks target inflation around 2%.",
        "related": ["inflation", "quantitative easing", "interest rates"],
    },

    "elasticity": {
        "title": "Elasticity",
        "explanation": (
            "Elasticity measures how responsive quantity demanded or supplied is to changes in price, income, or other factors."
        ),
        "key_terms": ["price elasticity", "inelastic", "elastic"],
        "examples": [
            "Gasoline demand is inelastic because people still need to drive.",
            "Restaurant meals are elastic because people can cut back easily."
        ],
        "fun_fact": "Elasticity helps businesses decide how much to raise prices without losing customers.",
        "related": ["demand", "supply", "consumer behavior"],
    },

    "comparative advantage": {
        "title": "Comparative Advantage",
        "explanation": (
            "Comparative advantage occurs when a country can produce a good at a lower opportunity cost than another country."
        ),
        "key_terms": ["opportunity cost", "trade", "specialization"],
        "examples": [
            "Country A produces wine more efficiently, while Country B produces cloth more efficiently — both benefit by trading.",
            "Even if one country is better at producing everything, trade can still benefit both sides."
        ],
        "fun_fact": "David Ricardo introduced comparative advantage in 1817.",
        "related": ["international trade", "opportunity cost", "specialization"],
    },

    "unemployment": {
        "title": "Unemployment",
        "explanation": (
            "Unemployment measures the share of the labor force that is actively seeking work but unable to find a job."
        ),
        "key_terms": ["cyclical", "structural", "frictional"],
        "examples": [
            "During recessions, cyclical unemployment rises.",
            "Automation can increase structural unemployment."
        ],
        "fun_fact": "The unemployment rate never reaches zero — some frictional unemployment is normal.",
        "related": ["business cycles", "labor market", "inflation"],
    },

    "gdp": {
        "title": "Gross Domestic Product (GDP)",
        "explanation": (
            "GDP is the total value of all final goods and services produced within a country in a given period."
        ),
        "key_terms": ["output", "income", "expenditure"],
        "examples": [
            "GDP rises when consumption, investment, or government spending increases.",
            "Exports increase GDP; imports reduce it."
        ],
        "fun_fact": "GDP was first developed in the 1930s to measure the Great Depression.",
        "related": ["economic growth", "aggregate demand", "productivity"],
    },

    "supply and demand": {
        "title": "Supply and Demand",
        "explanation": (
            "Supply and demand describe how prices and quantities are determined in markets. "
            "Prices adjust until quantity supplied equals quantity demanded."
        ),
        "key_terms": ["equilibrium", "shortage", "surplus"],
        "examples": [
            "A heatwave increases demand for ice cream, raising prices.",
            "A bumper crop increases supply of corn, lowering prices."
        ],
        "fun_fact": "The supply–demand model is the foundation of microeconomics.",
        "related": ["elasticity", "market equilibrium", "consumer behavior"],
    },

    "market equilibrium": {
        "title": "Market Equilibrium",
        "explanation": (
            "Market equilibrium occurs when quantity supplied equals quantity demanded at a certain price."
        ),
        "key_terms": ["equilibrium price", "shortage", "surplus"],
        "examples": [
            "If the price is too low, shortages occur as demand exceeds supply.",
            "If the price is too high, surpluses occur as supply exceeds demand."
        ],
        "fun_fact": "Equilibrium is sometimes called the 'market-clearing price.'",
        "related": ["supply and demand", "elasticity"],
    },

    "interest rates": {
        "title": "Interest Rates",
        "explanation": (
            "Interest rates represent the cost of borrowing money or the return on saving money."
        ),
        "key_terms": ["federal funds rate", "APR", "yield"],
        "examples": [
            "Higher interest rates make borrowing more expensive, reducing investment.",
            "Lower interest rates encourage consumers to finance cars and homes."
        ],
        "fun_fact": "Central banks adjust interest rates to control inflation.",
        "related": ["monetary policy", "inflation", "credit markets"],
    },

    "business cycles": {
        "title": "Business Cycles",
        "explanation": (
            "Business cycles are fluctuations in economic activity, typically measured by changes in GDP."
        ),
        "key_terms": ["expansion", "recession", "peak", "trough"],
        "examples": [
            "During expansions, unemployment falls and output rises.",
            "During recessions, spending declines and unemployment rises."
        ],
        "fun_fact": "The average U.S. business cycle lasts about 5–7 years.",
        "related": ["GDP", "unemployment", "fiscal policy"],
    },

    "scarcity": {
        "title": "Scarcity",
        "explanation": (
            "Scarcity means resources are limited relative to wants, forcing individuals and societies to make choices."
        ),
        "key_terms": ["limited resources", "trade-offs", "choices"],
        "examples": [
            "A city must choose between building a new school or repairing roads.",
            "Consumers choose how to spend limited income."
        ],
        "fun_fact": "Scarcity is the fundamental problem that drives all of economics.",
        "related": ["opportunity cost", "supply and demand"],
    },

    "productivity": {
        "title": "Productivity",
        "explanation": (
            "Productivity measures how efficiently inputs like labor and capital produce output."
        ),
        "key_terms": ["output per worker", "technology", "efficiency"],
        "examples": [
            "Automation increases productivity by allowing workers to produce more.",
            "Education and training improve worker productivity."
        ],
        "fun_fact": "Long-run economic growth depends heavily on productivity gains.",
        "related": ["economic growth", "GDP"],
    },

    "economic growth": {
        "title": "Economic Growth",
        "explanation": (
            "Economic growth is the increase in a country's production of goods and services over time."
        ),
        "key_terms": ["GDP growth", "capital", "technology"],
        "examples": [
            "Investment in infrastructure boosts long-term growth.",
            "Innovation increases productivity and drives growth."
        ],
        "fun_fact": "Small differences in growth rates compound dramatically over decades.",
        "related": ["productivity", "GDP", "aggregate supply"],
    },

    "international trade": {
        "title": "International Trade",
        "explanation": (
            "International trade involves the exchange of goods and services across borders, allowing countries to specialize."
        ),
        "key_terms": ["exports", "imports", "trade balance"],
        "examples": [
            "The U.S. imports electronics from Asia and exports aircraft and agricultural goods.",
            "Trade agreements reduce tariffs and increase global commerce."
        ],
        "fun_fact": "Global trade has grown more than 40× since 1950.",
        "related": ["comparative advantage", "exchange rates"],
    },

    "exchange rates": {
        "title": "Exchange Rates",
        "explanation": (
            "Exchange rates determine how much one currency is worth relative to another."
        ),
        "key_terms": ["appreciation", "depreciation", "forex"],
        "examples": [
            "If the dollar strengthens, U.S. imports become cheaper.",
            "If the euro weakens, European exports become more competitive."
        ],
        "fun_fact": "Exchange rates can change minute-by-minute in global markets.",
        "related": ["international trade", "inflation"],
    },
}



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
