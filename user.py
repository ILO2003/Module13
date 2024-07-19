class User:
    def __init__(self, email, name, pwd, job_title):
        self.email = email
        self.name = name
        self.pwd = pwd
        self.job_title = job_title

    def change_password(self, new_pwd):
        self.pwd = new_pwd

    def change_job_title(self, new_job_title):
        self.job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently workds as a {self.job_title}. Emails address of their's is {self.email}")