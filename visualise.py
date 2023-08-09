import streamlit as st
import pandas as pd
from employee_data import load_employee_data
from department_data import load_department_data


def visualize_data():
    st.title("Visualize Joined Employee and Department Data")

    employee_data = load_employee_data()
    department_data = load_department_data()

    if employee_data.empty or department_data.empty:
        st.warning("No data to visualize.")
    else:
        joined_data = pd.merge(
            employee_data, department_data, on='Deptno', how='inner')
        st.dataframe(joined_data)


if __name__ == "__main__":
    visualize_data()
