# django-task-scheduler
<h2>This is a Python Django project to connect workers with each tasks</h2>

# Main Functions
<h3>Registration</h3>

Project include module to register users with special attributes such as:
<ul>
<li>Names</li>
<li>Avatar Images</li>
<li>Emails</li>
<li>Grades (representing role of the user in company)</li>
<li>Deparment (represeting department of the user in company) </li>
</ul>

<h3>Tasks</h3>
Tasks are modeled with attributes as:
<ul>
<li>Name - representing the name of the task</li>
<li>Status - shows actual status of the task</li>
<li>Task creator - shows which user created a task</li>
<li>Task executor - shows which user is responsible for execution of task</li>
<li>Responsible department - shows which department should execute the task</li>
<li>Desciption - shows deeper description of the task</li>
<li>Date of creation - asigned automatically as a date of creation </li>
<li>Due date - managed manually as a date when task should be finnished </li>
<li>Finish date - shows when task was finished </li>
<li>Importance - shows importance of the task. Critical important tasks are highlited</li>
</ul>


<h3>Task views</h3>
There are implemented three main views of tasks. They were divided into:
<ul>
<li>All Tasks - shows all tasks in company</li>
<li>Department Tasks - shows tasks only by user department</li>
<li>Your Tasks - shows user tasks which makes easy for the user to manage their own tasks </li>
</ul>

Tasks in each view are seperated by status as 'Not Asigned', 'In Progress', 'Done'. Clicking on each tasks trasnfers into detail page of a task.

<h3>Detail Task View</h3>
<img src="(https://user-images.githubusercontent.com/109242797/179839621-266fe64b-53a0-41d2-a94e-c2d2fa7ec7f0.png)" alt='not found' title='Detail View'>

