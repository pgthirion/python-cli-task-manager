# Advanced Task Manager CLI

A robust Python-based application for managing team tasks. This version builds upon basic task management by adding comprehensive reporting features, allowing administrators to generate text-based overviews of user performance and task statuses.

## Features

* **Authentication:** Secure login system using `user.txt`.
* **Task Management:** Create, view, and edit tasks.
* **Progress Tracking:** Mark tasks as complete or edit details of incomplete tasks.
* **Reporting Engine:**
    * **Task Overview:** Generates metrics on completed, incomplete, and overdue tasks.
    * **User Overview:** Detailed breakdown of task completion rates per user.
* **Admin Dashboard:** View total user/task counts and read generated reports directly from the console.

## Prerequisites

* Python 3.x

## Installation

1.  **Download:**
    * Click the green **<> Code** button.
    * Select **Download ZIP**.
    * Extract to a folder.

2.  **Verify Data Files:**
    Ensure the following text files exist in the directory:
    * `user.txt` (Credentials)
    * `tasks.txt` (Task Database)
    * *Note: `task_overview.txt` and `user_overview.txt` will be generated automatically by the program.*

## Usage

Run the application:

    python task_manager.py

### Login
* **Default Admin:** Username: `admin`, Password: `adm1n`

### Main Menu Options

* `r` - **Register User:** Add a new user (Admin only).
* `a` - **Add Task:** Assign a new task to a specific user.
* `va` - **View All:** List every task in the database.
* `vm` - **View My Tasks:**
    * View tasks assigned to you.
    * Select a task by number to **Edit** or **Mark as Complete**.
* `gr` - **Generate Reports:**
    * Calculates statistics (overdue %, completion rates).
    * Writes results to `task_overview.txt` and `user_overview.txt`.
* `s` - **Statistics:** Displays the data from the generated reports on screen (Admin only).
* `e` - **Exit:** Close the application.

## File Structure

* **`task_manager.py`**: Main application logic.
* **`user.txt`**: Stores `username, password`.
* **`tasks.txt`**: Stores task data including assignment dates and completion status.
* **`task_overview.txt`**: Generated report summarizing global task statistics.
* **`user_overview.txt`**: Generated report detailing individual user performance.
