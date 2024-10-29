# Import libraries
import streamlit as st

# Add custom CSS for styling
st.markdown("""
    <style>
    .stMain {
        background-color: #fff;
        color: black;
    }
    .st-az {
        background-color: #5995f0;
    }
    .titolone {
        display: flex;
        align-items: center;
        background-color: #5995f0;
    }
    .h1 {
        color: #5995f0;
    }
    .subheader-text {
        color: #5995f0;
    }
    .section-text {
        color: #2C3E50;
        font-size: 18px;
        margin-top: 20px;
    }
    .quiz-section {
        background-color: #fff;
        padding: 20px;
        border-radius: 10px;
    }
    .score-text {
        color: #5995f0;
        font-size: 24px;
        font-weight: bold;
    }
    .divider {
        height: 5px;
        background-color: #5995f0;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# App title
st.image("logo-MEb.png", width=60) 
st.markdown("""
<div class="titolone">
    <h1 style="color: #fff">Ophthalmology Clinical Quiz</h1>
</div>
""", unsafe_allow_html=True)

# Case Presentation
st.subheader("Case Presentation")
st.markdown("""
A 23-year-old man with progressive keratoconus undergoes corneal collagen cross-linking (CXL) using riboflavin and UV-A radiation. 
Postoperatively, he experiences severe photophobia, watering, redness, and a slow re-epithelialization process, leading to corneal melting 
and eventual perforation.
""")

# Quiz Section
st.subheader("Clinical Quiz")
st.write("Test your knowledge")

# Quiz Questions and Answers
questions = [
    {
        "question": "What were the key preoperative indicators for this patient to receive CXL?",
        "options": ["Progressive keratoconus with decreasing visual acuity and thinning cornea",
                    "Stable keratoconus with no signs of progression",
                    "Previous corneal surgery and history of high myopia"],
        "answer": "Progressive keratoconus with decreasing visual acuity and thinning cornea",
        "explanation": "The patient was referred for CXL due to progressive keratoconus with documented deterioration in best-corrected visual acuity (BCVA) and central corneal thickness."
    },
    {
        "question": "Which postoperative symptoms indicated an acute inflammatory response?",
        "options": ["Significant photophobia and watery discharge", 
                    "Blurry vision without other symptoms", 
                    "Complete re-epithelialization with no redness or photophobia"],
        "answer": "Significant photophobia and watery discharge",
        "explanation": "The case report describes the patient experiencing intense photophobia, watering, and discomfort on the first postoperative day."
    },
    {
        "question": "What immediate steps should be considered to manage postoperative corneal melting?",
        "options": ["Increase UV-A radiation dosage to prevent infection", 
                    "Discontinue current medication, initiate antibiotic and steroid therapy, and monitor for infection", 
                    "Continue the same postoperative medications without changes"],
        "answer": "Discontinue current medication, initiate antibiotic and steroid therapy, and monitor for infection",
        "explanation": "The postoperative medication was modified to include antibiotics and steroids to control the inflammation and rule out infection as a possible cause of the inflammatory response."
    },
    {
        "question": "What laboratory tests help rule out secondary causes for the patient’s inflammatory response?",
        "options": ["Keratometric readings", 
                    "Immunological and infection screenings, including PCR for viral DNA", 
                    "Contact lens tolerance testing"],
        "answer": "Immunological and infection screenings, including PCR for viral DNA",
        "explanation": "Tests such as PCR for herpes simplex virus DNA and markers for autoimmune diseases are essential to rule out secondary causes of inflammation that might be contributing to the patient’s reaction."
    },
    {
        "question": "What definitive treatment was required after corneal perforation?",
        "options": ["Continuation of topical steroid therapy", 
                    "Penetrating keratoplasty", 
                    "Repeat cross-linking"],
        "answer": "Penetrating keratoplasty",
        "explanation": "When the cornea continued to deteriorate and perforation occurred, penetrating keratoplasty was performed to restore corneal integrity and vision."
    }
]

# Display Quiz
score = 0
selected_answers = []
for i, q in enumerate(questions):
    st.write(f"**Question {i+1}:** {q['question']}")
    answer = st.radio("", q['options'], key=f"q_{i}")
    selected_answers.append(answer)

# Submit button for Quiz
if st.button("Submit Quiz"):
    for i, q in enumerate(questions):
        st.write(f"**Question {i+1}:** {q['question']}")
        if selected_answers[i] == q['answer']:
            score += 1
            st.markdown(f"<p style='color:green;'>✔️ Correct: {q['answer']}</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p style='color:red;'>❌ Incorrect: {selected_answers[i]}</p>", unsafe_allow_html=True)
        # Explanation for each answer
        st.write(f"**Explanation:** {q['explanation']}")
    
    # Display total score
    st.markdown(f"<div class='score-text'>Your Score: {score}/{len(questions)}</div>", unsafe_allow_html=True)
