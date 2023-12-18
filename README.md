# Final project for 2023's 219114/115 Programming I
* Starting files for part 1
  - database.py
  - project_manage.py
  - persons.csv
* admin.py
-The `admin.py` script is part of the project administration module. It provides 
functionality for administrative tasks related to project management, such as creating projects, 
managing members, and interacting with advisors.

#Features
- Create a new project
- Manage project members
- Interact with potential advisors
- Perform administrative tasks related to project management

* member.py
-The `member.py` script is part of the project's member module. It provides functionality 
* for members to interact with projects and view response requests. Members can view projects
* they are part of and see response requests related to those projects.

#Features
- Show projects a member is part of
- Show response requests for the member's projects

* student
-The student-invitation module allows students to manage project invitations, respond to invitations,
and interact with their assigned projects.

# Features
- View and respond to project invitations from leads
- Accept or deny project invitations
- View and modify project details

* lead_student.py
-The lead student module facilitates project management for lead students. It includes features to create, 
manage, and complete projects effectively.

# Features
- Create a new project
- Find potential members and send invitations
- Form a project group by adding members
- View and modify project details
- Send advisor requests
- Submit the final project report

* faculty.py
The normal faculty module provides functionalities for faculty members who are 
not serving as advisors. It includes features for responding to requests, 
viewing project details, and evaluating projects.

# Features
- View requests to serve as a supervisor
- Send responses to deny serving as an advisor
- View details of all projects
- Evaluate projects (missing step, explained in the proposal)

* advisor.py
-The advising faculty module provides functionalities for faculty members serving as advisors.
It includes features for managing requests, responding to requests, viewing project details, evaluating projects, 
and approving projects.

# Features
- View requests to serve as a supervisor
- Send accept response for projects eventually serving as an advisor
- Send deny response for projects not eventually serving as an advisor
- View details of all projects
- Evaluate projects (missing step, explained in the proposal)
- Approve projects


| Role    | Action                   | Method                | Class   | Completion % |
|---------|--------------------------|-----------------------|---------|--------------|
| admin   | update row in table      | update                | Table   | 100%         |
| admin   | append row               | insert                | Table   | 100%         |
| admin   | show function            | update                | Admin   | 100%         |
| admin   | update function          | new_data              | Admin   | 100%         |
| member  | show choice              | show_choice           | Member  | 100%         |
| member  | show project information | show_project          | Member  | 100%         |
| member  | show response request    | show response request | Member  | 100%         |
| lead    | select choice            | show function         | Lead    | 100%         |
| lead    | create new project       | create_project        | Lead    | 50%          |
| lead    | send invitation          | send_invitation       | Lead    | 50%          |
| lead    | add member               | add_member            | Lead    | 10%          |
| lead    | add advisor              | add_advisor           | Lead    | 10%          |
| lead    | submit project           | submit_project        | Lead    | 0%           |
| advisor | select function          | select_function       | Advisor | 0%           |
| lead    |                          | create_project        | Lead    | 30%          |
| lead    |                          | send_invitation       | Lead    | 10%          |
| faculty |                          | create_project        | Lead    | 30%          |
| lead    |                          | send_invitation       | Lead    | 10%          |






 

