# Python CLI Task Manager

A console-based task management system designed for small teams. This application allows users to log in, view their assigned tasks, and lets administrators manage users and view system statistics.

## Features

* **User Authentication:** Secure login system verifying credentials against a local database.
* **Role-Based Access:**
    * **Admin:** Can register new users and view system statistics (total users/tasks).
    * **Standard User:** Can view all tasks or filter for their own assigned tasks.
* **Task Management:** Add new tasks with titles, descriptions, due dates, and assignment tracking.
* **Data Persistence:** All users and tasks are stored in local text files (`user.txt` and `tasks.txt`), ensuring data remains available between sessions.

## Prerequisites

* Python 3.x

## Installation

1.  **Download:**
    * Click the green **<> Code** button at the top of this page.
    * Select **Download ZIP**.
    * Extract the ZIP file to a folder on your computer.

2.  **Verify Data Files:**
    * Ensure `user.txt` and `tasks.txt` are in the same folder as the script.
    * *If they are missing, create them manually:*
        * Create `user.txt` and add: `admin, adm1n`
        * Create `tasks.txt` (can be empty initially).

## Usage

1.  **Run the Application:**
    Open your terminal/command prompt in the project folder and run:

        python task_manager.py

2.  **Log In:**
    Use the default admin credentials to start:
    * **Username:** `admin`
    * **Password:** `adm1n`

3.  **Menu Options:**
    Once logged in, choose from the following commands:
    * `r` - **Register User:** Add a new user (Admin only).
    * `a` - **Add Task:** Create a new task and assign it to a user.
    * `va` - **View All:** Display every task in the system.
    * `vm` - **View My Tasks:** Show only tasks assigned to you.
    * `s` - **Statistics:** View total counts of users and tasks (Admin only).
    * `e` - **Exit:** Close the program.

## Data Structure

* **`user.txt`:** Stores credentials in the format `username, password`.
* **`tasks.txt`:** Stores task details in the format:
  `assigned_to, task_title, description, due_date, date_assigned, completion_status`
