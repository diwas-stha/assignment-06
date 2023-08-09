import streamlit as st
from employee_data import get_employee_data
from department_data import get_department_data
from visualise import visualize_data


def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Select Page", ("Employee Data Entry", "Department Data Entry", "Visualize Data"))

    if page == "Employee Data Entry":
        get_employee_data()
    elif page == "Department Data Entry":
        get_department_data()
    elif page == "Visualize Data":
        visualize_data()


if __name__ == "__main__":
    main()
