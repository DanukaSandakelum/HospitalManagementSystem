# Hospital Management System

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A Python-based Hospital Management System for handling patient billing and staff salary calculations.

## Features

- **Patient Management**
  - Calculate hospitalization bills based on days admitted
  - Store patient demographics and medical information
- **Staff Management**
  - Calculate salaries for doctors and nurses
  - Handle different compensation structures
- **User-Friendly Menu**
  - Interactive console interface
  - Simple navigation

## Class Structure

```mermaid
classDiagram
    Person <|-- Patient
    Person <|-- Staff
    Staff <|-- Doctor
    Staff <|-- Nurse
    
    class Person {
        +str name
        +str nic
        +int age
        +__init__(name, nic, age)
    }
    
    class Patient {
        +str disease
        +int days_admitted
        +float daily_charge
        +total_bill() float
    }
    
    class Staff {
        +float basic_salary
        +get_salary()* float
    }
    
    class Doctor {
        +int patients_handled
        +CONSULTATION_FEE = 5000
        +get_salary() float
    }
    
    class Nurse {
        +int overtime_hours
        +OVERTIME_RATE = 200
        +get_salary() float
    }
