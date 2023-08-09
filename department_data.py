import os
import streamlit as st
import pandas as pd

DATA_FOLDER = 'data'
EMPLOYEE_CSV_PATH = os.path.join(DATA_FOLDER, 'department_data.csv')


def load_department_data():
    """
    Load department data from the CSV file if it exists, or create a new CSV file if not.
    Returns:
    -------
        pd.DataFrame: Loaded department data
    """
    if not os.path.exists(EMPLOYEE_CSV_PATH):
        data = pd.DataFrame(columns=['Deptno', 'Dname', 'Loc'])
        data.to_csv(EMPLOYEE_CSV_PATH, index=False)  # Create the CSV file

    data = pd.read_csv(EMPLOYEE_CSV_PATH)
    return data


def get_department_data():
    """
    Display the Department Data Entry form and handle data addition.
    """
    st.title("Department Data Entry")

    deptno = st.text_input("Department Number (Deptno):")
    dname = st.text_input("Department Name (Dname):")
    loc = st.text_input("Location (Loc):")

    department_data = load_department_data()

    if st.button("Add Department"):
        department_data.loc[len(department_data)] = [deptno, dname, loc]
        department_data.to_csv(EMPLOYEE_CSV_PATH, index=False)
        st.success("Department added successfully!")

    st.dataframe(department_data)
