"""Une application pour la gestion des employés """
import streamlit as st
from typing import List

# Les classes Employee et Department
class Employee:
    """Employee Class
    """    
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f"{self.name} - {self.position} - ${self.salary}"

class Department:
    """Department Class
    """    
    def __init__(self, name):
        self.name = name
        self.employees: List[Employee] = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def average_salary(self):
        if not self.employees:
            return 0
        total_salary = sum(employee.salary for employee in self.employees)
        return total_salary / len(self.employees)

# Initialisation d'un département
department = Department("Finance")

# Titre de l'application
st.title("Système de Gestion d'Employés")

# Formulaire pour ajouter un employé
st.header("Ajouter un Employé")
name = st.text_input("Nom de l'employé")
position = st.text_input("Poste")
salary = st.number_input("Salaire", min_value=0)

if st.button("Ajouter Employé"):
    if name and position and salary:
        emp = Employee(name, position, salary)
        department.add_employee(emp)
        st.success(f"Employé {name} ajouté au département {department.name}.")
    else:
        st.error("Veuillez remplir tous les champs pour ajouter un employé.")

# Affichage des employés du département
st.header(f"Liste des Employés dans le Département {department.name}")
if department.employees:
    for emp in department.employees:
        st.write(emp)
else:
    st.write("Aucun employé dans ce département.")

# Calcul du salaire moyen
st.header("Calcul du Salaire Moyen")
if st.button("Calculer Salaire Moyen"):
    avg_salary = department.average_salary()
    st.write(f"Le salaire moyen dans le département {department.name} est : ${avg_salary:.2f}")
