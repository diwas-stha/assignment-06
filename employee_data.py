import os
import streamlit as st
import pandas as pd

DATA_FOLDER = 'data'
EMPLOYEE_CSV_PATH = os.path.join(DATA_FOLDER, 'employee_data.csv')


def load_employee_data():
    """
    Load employee data from the CSV file if it exists, or create a new CSV file if not.
    Returns:
    -------
        pd.DataFrame: Loaded employee data
    """
    if not os.path.exists(EMPLOYEE_CSV_PATH):
        data = pd.DataFrame(columns=['Empno', 'Ename', 'Job', 'Deptno'])
        data.to_csv(EMPLOYEE_CSV_PATH, index=False)  # Create the CSV file

    data = pd.read_csv(EMPLOYEE_CSV_PATH)
    return data


def get_employee_data():
    """
    Display the Employee Data Entry form and handle data addition.
    """
    st.title("Employee Data Entry")

    empno = st.text_input("Employee Number (Empno):")
    ename = st.text_input("Employee Name (Ename):")
    job = st.text_input("Job:")
    deptno = st.text_input("Department Number (Deptno):")

    employee_data = load_employee_data()

    if st.button("Add Employee"):
        employee_data.loc[len(employee_data)] = [empno, ename, job, deptno]
        employee_data.to_csv(EMPLOYEE_CSV_PATH, index=False)
        st.success("Employee added successfully!")

    st.dataframe(employee_data)
