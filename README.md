# django-task-scheduler
<h2>Python Django project to connect workers with each task</h2>

# Main Functions
<h3> Navbar </h3>
Project has basic navbar which changes for logged and anonymous users.
Anonymous user:
<img src="https://user-images.githubusercontent.com/109242797/179841357-903282e4-7181-4659-8c5e-c2c2c02ee5ba.png" alt='not found' title='Anonymous User'>

Loged user:
<img src="https://user-images.githubusercontent.com/109242797/179841337-34bd9efa-833a-4803-a437-7c98c87af74a.png" alt='not found' title='Loged User'>

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
<img src="https://user-images.githubusercontent.com/109242797/179840097-0354ebbc-a1bd-44b8-9ceb-7a7d3bb22081.png" alt='not found' title='Task View'>
Tasks in each view are seperated by status as 'Not Asigned', 'In Progress', 'Done'. Clicking on each tasks trasnfers into detail page of a task.

<h3>Detail Task View</h3>
<img src="https://user-images.githubusercontent.com/109242797/179839621-266fe64b-53a0-41d2-a94e-c2d2fa7ec7f0.png" alt='not found' title='Detail View'>

Detail View shows most important data of the task. On the left it is represented a creator of a task, on the right its executor. It is easy to check all data of the task.

<h3>Gaining a task</h3>
<img src="https://user-images.githubusercontent.com/109242797/179840859-2bf632cb-4c1d-4430-bbc0-42c49a8b0813.png" alt='not found' title='Get Task'>
Each user could gain a task by clicking on it in All Task View or Department Task View. Task which don't have executor on the right of the detail view have special button GET TASK. User could get this task and define the finish date. 

<h3>Finishing a task</h3>
User who has to complete each task has a special funcion in Detail View as a button DONE. The button will appear on the right such as GET TASK button in previous point. Clicking DONE will finish a task and fill the finish date.

<h3>🔷🔷Asigning (Pushing) a task🔷🔷</h3>
<img src="https://user-images.githubusercontent.com/109242797/179842092-72b1e460-7280-467a-8c24-cbecdc62b2d7.png" alt='not found' title='Asign Task'>
Project includes special module for managers. If user grade is a manager it can push each task for any user just by one click. Choosing a due date and a user on page as shown above will asign choosen user as a task executor. Lately any user can check a tasks asigned to him just by clicking 'Your Tasks' on navbar. 

# Additional Functions
<h3> Statistics </h3>
<img src="https://user-images.githubusercontent.com/109242797/179843824-ce5ef8ac-c982-4ef2-af71-db2103ae1ed9.png" alt='not found' title='Statistics'>
Special module for tasks and users statistics.

<h3> User list </h3>
There is implemented a user list which can be checked by clicking Users on navbar

