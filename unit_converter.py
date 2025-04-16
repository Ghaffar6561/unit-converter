# unit_converter.py
import streamlit as st

st.set_page_config(page_title="Google Style Unit Converter", layout="centered")

st.title("🔁 Google-style Unit Converter")

# --- Category options ---
category = st.selectbox("Choose a category", ["Length", "Weight", "Temperature", "Time"])

# --- Unit mappings ---
units = {
    "Length": {
        "meters": 1,
        "kilometers": 1000,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "miles": 1609.34,
        "feet": 0.3048,
        "inches": 0.0254
    },
    "Weight": {
        "kilograms": 1,
        "grams": 0.001,
        "pounds": 0.453592,
        "ounces": 0.0283495
    },
    "Time": {
        "seconds": 1,
        "minutes": 60,
        "hours": 3600,
        "days": 86400
    }
}

# --- Temperature conversion ---
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else ((value - 32) * 5/9 + 273.15)
    elif from_unit == "Kelvin":
        return (value - 273.15) if to_unit == "Celsius" else ((value - 273.15) * 9/5 + 32)