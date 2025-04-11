import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# App title
st.title(" BMI Calculator")

# User input sliders
height = st.slider("Enter your height (in cm):", 100, 250, 175)
weight = st.slider("Enter your weight (in kg):", 40, 200, 70)

# BMI Calculation
bmi = weight / ((height / 100) ** 2)

# Display result
st.write(f"### Your BMI is *{bmi:.2f}*")

# BMI Categories
st.write("### BMI Categories (WHO)")
bmi_category = ""
if bmi < 18.5:
    bmi_category = "🔵 Underweight"
    advice = "You may need to gain weight. Consider a balanced diet with more calories."
elif 18.5 <= bmi <= 24.9:
    bmi_category = "🟢 Normal weight"
    advice = "Great! Keep maintaining a healthy lifestyle."
elif 25 <= bmi <= 29.9:
    bmi_category = "🟠 Overweight"
    advice = "Try to include more physical activity and a balanced diet in your routine."
else:
    bmi_category = "🔴 Obesity"
    advice = "Consider consulting a healthcare provider for a personalized health plan."

st.write(f"*Category:* {bmi_category}")
st.write(f"*Advice:* {advice}")

# Graphical representation of BMI categories
fig, ax = plt.subplots()
categories = ["Underweight", "Normal", "Overweight", "Obese"]
values = [18.5, 24.9, 29.9, 40]  # Approximate upper limits

ax.bar(categories, values, color=['blue', 'green', 'orange', 'red'])
ax.axhline(bmi, color='black', linestyle='dashed', label=f'Your BMI: {bmi:.2f}')
ax.set_ylabel("BMI Value")
ax.legend()

st.pyplot(fig)

# BMI Category Information
st.write("### 📌 BMI Chart:")
st.write("- *Underweight:* BMI less than 18.5")
st.write("- *Normal weight:* BMI between 18.5 and 24.9")
st.write("- *Overweight:* BMI between 25 and 29.9")
st.write("- *Obesity:* BMI 30 or greater")

# Reset Button (updated)
if st.button("Reset"):
    st.rerun()  # ✅ Updated function

# Footer
st.markdown("---")
st.markdown("####  Developed by *Ashfa Shakeel*")
