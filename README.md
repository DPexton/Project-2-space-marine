

# Project: Space Marine Generator

# QA DevOps Core Practical Project

## Contents
- [Brief](#brief)
    - [Requirements](#requirements)
    - [My Objective](#my-objective)
- [Architecture](#architecture)
    - [Project Tracking](#project-tracking)
    - [Risk Assessment](#risk-assessment)
- [Infracstructure](#infrastructure)
    - [Database Structure](#database-structure)
    - [Continuous Integration Pipeline](#continuous-integration-pipeline)
    - [Docker Containers](#docker-containers)
    - [Interaction Diagram](#interaction-diagram)
    - [Refactoring](#refactoring)
- [Development](#development)
    - [Front-end Design](#front-end-design)
    - [Unit Testing](#unit-testing)
- [Footer](#footer)
    - [Future Improvements](#future-improvements)
    - [Acknowledgements](#acknowledgements)


    ## Brief
    To create a service-oriented architecture for the application, this application must be composed of at least 4 services working together.

    ## Requirements
    The requirements of the project are as follows:

- An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
- This could also provide a record of any issues or risks that you faced creating your project.
- An Application fully integrated using the Feature-Branch model into a Version Control - System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
- If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
- The project must follow the Service-oriented architecture that has been asked for.
- The project must be deployed using containerisation and an orchestration tool.
- As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
- The project must make use of a reverse proxy to make your application accessible to the user.

## My Objective

I chose to create an application that will generate a random Space Marine from the Warhammer 40,000 universe. This was achieved by two services that will generate a random Space Marine Chapter(Team essentially) and Role. The outcome of each of these services will then be used in a third service to generate a name for the Marine based on the Role and Chapter generated. The outcome of this will then be pushed to a frontend service which will display on a webpage, also allowing the user to generate a brand new Marine at the click of a button.

## Architecture

### Trello Board - Project Tracking

![trello-board](https://i.imgur.com/5jZaCs6.png)

From here we can see the stages and prioritisation of tasks in this project. This board allowed me to keep track of my progress throughout the project.

[Here](https://trello.com/b/HE060b6h/space-marine-generator) is a link to the trello board.

### Risk Assessment

![risk-assessment](https://i.imgur.com/f0S0QdX.png)

This is the final version of my project risk assessment. As you can see at the bottom of the board the two highlighted risks were added later as these became apparent during the development process.

## Infrastructure

### Database Structure

![DATABASE](https://i.imgur.com/wLdBU5m.png)

Here is a simple diagram showing the database created by my application to handle the Space Marine information. Due to the nature of the application only one database is needed.

### Continuous Integration
Below you can see my CI pipeline, showing my projects beginning from a trello board, into the source code being created through Python and Flask and stored on my version control system (GitHub). From here the code is built through a Jenkins pipeline which implements pytest to complete unit testing. This is then built by docker compose and passed to a swarm manager and workers. Nginx was used as a load balancer and this along with docker swarm was configured using Ansible. Using the Jenkins pipeline also means that whenever anything is pushed to the relevant branch on GitHub. The application will update and apply the changes automatically.

![CI-Pipeline](https://i.imgur.com/fhX13JG.jpg)

### Docker Containers

As you will see below my project utilized four containers each operating a certain aspect of the application as a whole.

![containers](https://i.imgur.com/mT1QLe6.png)

### Interaction Diagram

Below is a diagram showing how Docker Swarm is implemented as an orchestration tool with NGINX serving as a load balancer. Docker Swarm creates a network of virtual machines to provide the same service. In my case, each VM currently operates a seperate container. NGINX is used to improve connection stability by directing the connection to the VM with the least number of connections. NGINX also functions as a proxy server, allowing me to make my application more secure.

![interaction](https://i.imgur.com/Hoi1oKn.png)


### Refactoring

When I initially created my application, the simplest way I could find to test the 'Name' function of my application was to create a seperate function for each name, ensuring that when the select 2 values (role and chapter) were passed through that the correct name was output. This was lengthy, time consuming and also made adding further chapters, roles and names difficult as it dramatically increased the time needed to do so. After some time I decided to create a dictionary, with the key-value pairs being the role and chapter (which would be separated by a comma and split) and the relevant name. This meant the whole section could be tested using one function and adding further content is now much easier. Below is the new testing code:

![Refactoring](https://i.imgur.com/e83ZT2O.png)

## Development

### Design

My front end uses a relatively simple design created using HTML. This is displayed when navigating to the NGINX IP on port 80, this in turn will pass the request to one of the VM's in the swarm. Each time the user clicks the 'Generate' button a new Space Marine will be created and displayed.

![frontend](https://i.imgur.com/idvWCy8.png)

### Unit-Testing

I have tested each part of my application to ensure full robust functionality. Due to the fact that my application requires no user input to generate results, this made testing fairly straight-forward. For both the chapter and role functions the testing was the same, it simply passed the List of values I created through and as long as the output match one of these the test will pass. My testing for the name function is detailed in the Refactoring section of this ReadME. For the front end I simply tested the applications ability to retrieve the values from the three containers and output them in a readable statement as shown below: 

![frontend-test](https://i.imgur.com/YOxDIRD.png)

### Coverage

As you can see below, using pytest and the Cobertura plugin for jenkins I can generate readable coverage reports. With each build the coverage remains above 96%. The gap in this I believe is caused by the create.py file in my front-end, which I will look to cover in a future build 

![coverage](https://i.imgur.com/BUnESpr.png)


## Footer

### Future Improvements

- Going forward I would like to implement a function that would display the Chapter Emblem for whatever chapter the generated Space Marine belongs to. This would result in increased visual feedback for the user.

- I would also like to implement JSON into a future build to serialise and transmit structured data across the application. This would result in less data used and an overall more efficient application

### Acknowledgments

- [Oliver Nichols](https://github.com/OliverNichols)
- [Harry Volker](https://github.com/htr-volker)
