import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Textile Fiber & Process Guide",
    page_icon="🧵",
    layout="wide"
)

st.title("🧵 Textile Fiber & Process Guide")
st.write("Learn about textile fibers and important manufacturing processes.")

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select a section",
    [
        "Home",
        "Fiber Library",
        "Textile Processes",
        "Fiber Comparison",
        "Knowledge Quiz",
        "Glossary"
    ]
)

fibers = {
    "Cotton": {
        "Type": "Natural plant fiber",
        "Properties": "Soft, breathable, absorbent",
        "Uses": "Clothing, towels, bedsheets"
    },
    "Wool": {
        "Type": "Natural animal fiber",
        "Properties": "Warm, resilient, insulating",
        "Uses": "Sweaters, coats, blankets"
    },
    "Silk": {
        "Type": "Natural animal fiber",
        "Properties": "Smooth, lustrous, lightweight",
        "Uses": "Scarves, dresses, luxury fabrics"
    },
    "Polyester": {
        "Type": "Synthetic fiber",
        "Properties": "Strong, quick-drying, wrinkle-resistant",
        "Uses": "Sportswear, curtains, blended fabrics"
    },
    "Nylon": {
        "Type": "Synthetic fiber",
        "Properties": "Strong, lightweight, abrasion-resistant",
        "Uses": "Ropes, bags, sportswear"
    },
    "Viscose": {
        "Type": "Regenerated cellulose fiber",
        "Properties": "Soft, absorbent, comfortable",
        "Uses": "Dresses, shirts, linings"
    },
    "Linen": {
        "Type": "Natural plant fiber",
        "Properties": "Cool, breathable, absorbent",
        "Uses": "Summer clothing, table linen"
    },
    "Acrylic": {
        "Type": "Synthetic fiber",
        "Properties": "Lightweight, warm, wool-like",
        "Uses": "Sweaters, blankets, knitwear"
    }
}

processes = {
    "Fiber Preparation": "Opens, cleans, and blends fibers.",
    "Carding": "Separates fibers and produces card sliver.",
    "Drawing": "Combines and drafts slivers to improve evenness.",
    "Combing": "Removes short fibers and improves fiber alignment.",
    "Roving": "Drafts sliver and adds a small amount of twist.",
    "Spinning": "Converts a fiber strand into yarn.",
    "Winding": "Transfers yarn onto a suitable package.",
    "Warping": "Arranges warp yarns parallel on a beam.",
    "Sizing": "Protects warp yarns from abrasion during weaving.",
    "Weaving": "Interlaces warp and weft yarns to produce fabric.",
    "Knitting": "Forms fabric by interlooping yarns.",
    "Finishing": "Improves the appearance, feel, or performance of textiles."
}

if page == "Home":
    st.header("Welcome to Textile Engineering!")
    st.write("""
    This website is designed for textile engineering students.

    Explore fiber types, their properties, important manufacturing
    processes, and basic textile terminology.
    """)

    col1, col2, col3 = st.columns(3)
    col1.metric("Fiber Types", len(fibers))
    col2.metric("Process Topics", len(processes))
    col3.metric("Learning Sections", 6)

    st.subheader("What will you learn?")
    st.markdown("""
    - Natural and synthetic fibers
    - Fiber properties and applications
    - Spinning and yarn manufacturing
    - Weaving and knitting
    - Textile finishing
    - Important textile engineering terms
    """)

elif page == "Fiber Library":
    st.header("🔬 Fiber Library")

    selected_fiber = st.selectbox(
        "Choose a fiber",
        list(fibers.keys())
    )

    data = fibers[selected_fiber]

    st.subheader(selected_fiber)
    st.write("**Classification:**", data["Type"])
    st.write("**Properties:**", data["Properties"])
    st.write("**Common Uses:**", data["Uses"])

elif page == "Textile Processes":
    st.header("🏭 Important Textile Processes")

    selected_process = st.selectbox(
        "Choose a process",
        list(processes.keys())
    )

    st.subheader(selected_process)
    st.write(processes[selected_process])

    st.info(
        "The exact manufacturing route depends on the fiber, "
        "yarn system, fabric construction, and machinery."
    )

    st.subheader("Simplified manufacturing sequence")
    st.write(
        "Fiber Preparation → Carding → Drawing → "
        "Roving → Spinning → Winding"
    )
    st.write(
        "For woven fabric: Warping → Sizing (if required) "
        "→ Weaving → Finishing"
    )
    st.write(
        "Knitting is an alternative method of fabric formation."
    )

elif page == "Fiber Comparison":
    st.header("📊 Compare Textile Fibers")

    selected = st.multiselect(
        "Select two or more fibers",
        list(fibers.keys()),
        default=["Cotton", "Polyester"]
    )

    if len(selected) >= 2:
        rows = []

        for name in selected:
            rows.append({
                "Fiber": name,
                "Type": fibers[name]["Type"],
                "Properties": fibers[name]["Properties"],
                "Uses": fibers[name]["Uses"]
            })

        df = pd.DataFrame(rows)
        st.dataframe(df, use_container_width=True, hide_index=True)

        st.download_button(
            label="Download Comparison CSV",
            data=df.to_csv(index=False),
            file_name="fiber_comparison.csv",
            mime="text/csv"
        )
    else:
        st.info("Select at least two fibers to compare.")

elif page == "Knowledge Quiz":
    st.header("✅ Textile Knowledge Quiz")

    questions = [
        {
            "question": "Which fiber comes from the cotton plant?",
            "options": ["Nylon", "Cotton", "Polyester", "Acrylic"],
            "answer": "Cotton"
        },
        {
            "question": "Which process produces card sliver?",
            "options": ["Weaving", "Winding", "Carding", "Sizing"],
            "answer": "Carding"
        },
        {
            "question": "Which process interlaces warp and weft?",
            "options": ["Drawing", "Weaving", "Spinning", "Carding"],
            "answer": "Weaving"
        },
        {
            "question": "Polyester is a type of:",
            "options": [
                "Plant fiber",
                "Animal fiber",
                "Synthetic fiber",
                "Mineral fiber"
            ],
            "answer": "Synthetic fiber"
        },
        {
            "question": "What does GSM measure in textiles?",
            "options": [
                "Yarn twist",
                "Fabric mass per square metre",
                "Fiber length",
                "Machine speed"
            ],
            "answer": "Fabric mass per square metre"
        }
    ]

    with st.form("quiz"):
        answers = []

        for i, question in enumerate(questions):
            answer = st.radio(
                f"{i + 1}. {question['question']}",
                question["options"],
                index=None,
                key=f"question_{i}"
            )
            answers.append(answer)

        submitted = st.form_submit_button("Submit Answers")

    if submitted:
        score = 0

        for i, question in enumerate(questions):
            if answers[i] == question["answer"]:
                score += 1

        st.success(
            f"Your score is {score} out of {len(questions)}"
        )

        for i, question in enumerate(questions):
            if answers[i] == question["answer"]:
                st.write(f"Question {i + 1}: Correct!")
            else:
                st.write(
                    f"Question {i + 1}: Correct answer: "
                    f"{question['answer']}"
                )

elif page == "Glossary":
    st.header("📚 Textile Glossary")

    glossary = {
        "Fiber": "A fine material used to make yarn or textile structures.",
        "Yarn": "A continuous strand made from fibers or filaments.",
        "Sliver": "An untwisted strand of fibers produced by carding or drawing.",
        "Roving": "A drafted fiber strand with a small amount of twist.",
        "Warp": "Lengthwise yarns in woven fabric.",
        "Weft": "Crosswise yarns in woven fabric.",
        "GSM": "Grams per square metre, a measure of fabric mass per unit area.",
        "Spinning": "The process of forming yarn from fibers.",
        "Weaving": "The process of interlacing warp and weft yarns.",
        "Knitting": "The process of forming fabric by interlooping yarns.",
        "Sizing": "Applying a protective material to warp yarns before weaving when required.",
        "Finishing": "Processes that improve textile appearance or performance."
    }

    search = st.text_input("Search a textile term")

    for term, definition in glossary.items():
        if search.lower() in term.lower() or search.lower() in definition.lower():
            with st.expander(term):
                st.write(definition)

st.sidebar.divider()
st.sidebar.caption("Textile Engineering Learning Hub")
