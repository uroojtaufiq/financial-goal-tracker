import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Financial Goal Tracker 🎯", page_icon="💰")

st.title("💸 Financial Goal Tracker")

# User Inputs
goal_amount = st.number_input("Enter your savings goal (in $):", min_value=100, step=100)
current_savings = st.number_input("Enter your current savings (in $):", min_value=0, step=50)

# Progress Calculation
if goal_amount > 0:
    progress = (current_savings / goal_amount) * 100
    st.progress(min(progress / 100, 1.0))

    # Show status
    st.write(f"You're {progress:.2f}% towards your goal! 🚀")

    # Celebrate if goal reached
    if current_savings >= goal_amount:
        st.success("Congratulations! You achieved your goal! 🎉")
        st.balloons()
    else:
        st.info("Keep saving! You're getting closer. 💪")

# Plot Savings Progress
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=progress,
    gauge={"axis": {"range": [None, 100]},
           "bar": {"color": "green"}},
    title={'text': "Goal Completion (%)"}
))

st.plotly_chart(fig)

#extra effects 
if st.button('Feeling festive? ❄️'):
    st.snow()
