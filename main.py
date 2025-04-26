import streamlit as st
import pint

# Create a UnitRegistry instance
ureg = pint.UnitRegistry()

def convert_units(value, from_unit, to_unit):
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        return result.magnitude
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("Unit Converter")
st.subheader("By A.Salam IT")
st.write("Convert the between different units possibilities!")

# Dropdown categories
categories = {
    "Length": [ "kilometer", "meter", "centimeter", "mile", "inch", "foot"],
    "Weight": ["kilogram", "gram", "pound", "ounce", "ton"],
    "Temperature": ["fahrenheit", "celsius", "kelvin"],
    "Time": ["day", "hour", "minute", "second",], 
    "Area": ["square kilometer", "square meter", "square foot", "square inch", "acre"],
    "Volume": ["liter", "milliliter", "cubic meter", "gallon", "pint"],
    "Speed": ["kilometer per hour", "mile per hour", "meter per second"],
    "Energy": ["kilojoule", "joule", "kilocalorie", "calorie","watt hour"],
    "Pressure": ["atmosphere", "torr", "pascal", "bar",],
    "Data Storage": ["kilobyte", "bit", "byte", "megabyte", "terabyte"]
}

category = st.selectbox("Select a category", list(categories.keys()))
from_unit = st.selectbox("From Unit", categories[category])
to_unit = st.selectbox("To Unit", categories[category])
value = st.number_input("Enter value", min_value=0.0, step=0.1)

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result} {to_unit}")