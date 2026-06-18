import streamlit as st
st.title("📊 Student Exam Score Predictor")
st.write("Enter your academic details ")
st.markdown("---")

# --- Form Inputs ---
# Using a form container to handle data neatly on submit
with st.form("prediction_form"):
    st.subheader("📝 Student Information")
    
    # Name and Age side-by-side
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Student Name:", placeholder="e.g., Urvashi")
    with col2:
        age = st.number_input("Age:", min_value=5, max_value=25, value=15, step=1)

    # Class, Board, and Subject dropdowns
    col3, col4, col5 = st.columns(3)
    with col3:
        student_class = st.selectbox("Class/Year:", ["Class 9", "Class 10", "Class 11", "Class 12"])
    with col4:
        board = st.selectbox("Education Board:", ["CBSE", "State Board"])
    with col5:
        subject = st.selectbox("Subject Focus:", ["Mathematics", "physics", "English","chemistry","biology" ])

    # Study hours input
    hours = st.number_input("Daily Study Hours:", min_value=0.0, max_value=16.0, value=4.0, step=0.5, 
                            help="How many hours do you spend studying this subject every day?")

    # Submit Button inside the form
    submit_button = st.form_submit_button(label="Analyze & Predict Score")

# --- Interactive Logic & Analysis on Click ---
if submit_button:
    if not name.strip():
        st.error("Please enter the student's name before submitting!")
    else:
        # Core Formula Logic
        # Start with a base score of 40 marks
        predicted_score = 40

        # Add points based on hours studied (7.5 marks per hour)
        predicted_score += (hours * 7.5)

        # Board Portion Evaluation Adjustments
        if board == "CBSE":
            predicted_score += 50  # CBSE focus on continuous application questions
        else:
            predicted_score += 1  # State Board direct concept formatting

        # Clamp the score dynamically between 0 and 100
        predicted_score = min(100, max(0, round(predicted_score)))

        # Performance Feedback Analysis strings
        if predicted_score >= 90:
            feedback_type = "success"
            feedback_text = f"🏆 **Outstanding performance pattern, {name}!** Your daily study routine aligns perfectly with top-tier board evaluation standards. Keep maintaining this consistency across your {subject} portions!"
        elif predicted_score >= 75:
            feedback_type = "info"
            feedback_text = f"👍 **Great foundation, {name}!** You have built a solid grasp over the curriculum. Reviewing sample papers and handling complex questions will easily push you past the 90 mark."
        elif predicted_score >= 30:
            feedback_type = "warning"
            feedback_text = f"⚠️ **Good baseline, {name}.** However, the {board} portions for {subject} require slightly more core dedication.."
        else:
            feedback_type = "error"
            feedback_text = f"🛑 **Attention needed, {name}.** Your current hours are falling short for the depth of {student_class} requirements. We highly suggest breaking down the syllabus portions systematically."

        # --- Display Output Metrics & Feedback ---
        st.markdown("---")
        st.subheader("📋 Performance Analysis Report")
        
        # Displaying key metrics cleanly
        m_col1, m_col2, m_col3 = st.columns(3)
        m_col1.metric("Student", name, f"Age {age}")
        m_col2.metric("Curriculum Focus", f"{board}", student_class)
        m_col3.metric("Target Subject", subject)

        # Highlighted Predicted Score Box
        st.markdown(f"### 🎯 Predicted Exam Score: `{predicted_score} / 100`")

        # Dynamic alerting display based on performance bracket
        if feedback_type == "success":
            st.success(feedback_text)
        elif feedback_type == "info":
            st.info(feedback_text)
        elif feedback_type == "warning":
            st.warning(feedback_text)
        else:
            st.error(feedback_text)
