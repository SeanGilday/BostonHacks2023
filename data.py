# data.py
# Author: Sean Gilday (sgilday@bu.edu)
# 
# Organize data within the Creatathon to suggest other projects
# and evaluate winners

# project data type
# name = name of project
# participants = hash table of all participant projects
# type = type of project
class Project:
    def __init__(self, name, file, description, account):
        self.name = name
        self.file = file
        self.description = description
        self.account = account
        self.submissions = {}
        self.type = None
        self.winner = None
        self.top5 = {}
    

# submission data type
# name = name of submission
# upvotes = num of upvotes
# file = file of submission
class Submission:
    def __init__(self, name, file, project, account, description):
        self.name = name
        self.upvotes = 0
        self.file = file
        self.project = project
        self.account = account
        self.description = description
        self.comments = {}

# account data type
# username = username
# email = email
# projects = projects that they've created
# submissions = submissions that they've uploaded
class Account:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.projects = {}
        self.submissions = {}

projectGraph = {}

# Add project to website graph
# Create hashtable for single project
def createProject(account, name, file, description):
    project = Project(name, file, description, account)
    if file.endswith('.mp3'):
        project.type = "Music"
    elif file.endswith('.jpg'):
        project.type = "Art"
    projectGraph.append(project)
    account.projects.append(project)

# upload submission for a project
def uploadSubmission(account, project, submission):
    submission = Submission(account, project, submission)
    project.submissions.append(submission)
    account.submission.append(submission)

# suggest other projects
def suggestProjects(project):
    return project.top5

# submission receives an upvote
def receiveUpvote(S: Submission):
    S.upvote += 1
    if S not in S.project.top5:
        if S.upvote > min(S.project.top5):
            S.project.top5.remove(min(S.project.top5))
            S.project.top5.append(S)
        if S.project.winner == None or S.upvote > S.project.winner.upvote:
            S.project.winner = S
