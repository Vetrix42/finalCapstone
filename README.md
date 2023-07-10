Project Name: Task Manager System
Description
The Task Manager System is a program designed for a small business to effectively manage tasks assigned to each member of a team. This project extends the functionality of a simple task management system by utilizing lists, dictionaries, and functions. The primary objective is to refactor the existing codebase to improve code readability, reduce complexity, and enhance the overall user experience.

By abstracting the code into modular functions, the Task Manager System becomes easier to understand, maintain, and extend. The project includes features such as user registration, task creation, viewing all tasks, viewing user-specific tasks, task completion, task editing, and generating reports. These enhancements aim to streamline task management processes, increase productivity, and provide valuable insights into task progress and user performance.

Table of Contents
Installation
Usage
Credits
Installation
To use the Task Manager System, follow these steps:

Clone the repository:

bash
Copy code
git clone (https://github.com/Vetrix42/finalCapstone)
Navigate to the project directory:

arduino
Copy code
cd Task-Manager-System
Open the terminal or command prompt and run the program:

Copy code
python task_manager 3.py
Usage
Once you have launched the Task Manager System, follow these instructions to utilize its functionalities:

Main Menu:

The main menu presents different options to choose from.
Select an option by entering the corresponding letter or command.
User Registration:

To register a new user, choose the 'r' option.
Follow the prompts to enter the required information.
If the username already exists, an error message will be displayed, and you can try again.
Add a Task:

Choose the 'a' option to add a new task.
Provide the necessary details for the task, such as the task name, description, assigned user, and due date.
The task will be added to the system for tracking.
View All Tasks:

Select 'va' to view all tasks listed in 'tasks.txt'.
The tasks will be displayed in an easy-to-read format, with each task identified by a corresponding number.
View User's Tasks:

Choose 'vm' to view all tasks assigned to the current user.
The assigned tasks will be displayed with corresponding numbers.
Enter the number of a specific task to choose an action or enter '-1' to return to the main menu.
If editing a task, you can modify the assigned user or due date, provided the task is incomplete.
Generate Reports:

The admin user can select the 'gr' option to generate reports.
Two text files, 'task_overview.txt' and 'user_overview.txt', will be generated.
'task_overview.txt' provides an overview of task statistics and completion percentages.
'user_overview.txt' contains information on user tasks, including completion percentages and overdue tasks.
Note: Ensure that the 'user.txt' and 'tasks.txt' files are present in the same directory as the 'task_manager.py' file.

Credits
The Task Manager System project was created and maintained by Your Name.

Special thanks to the creators of the initial codebase and the accompanying text files for providing the foundation for this project. The refactoring and enhancements were implemented to improve code readability, functionality, and user experience.# finalCapstone
