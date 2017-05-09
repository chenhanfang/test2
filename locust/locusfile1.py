from locust import HttpLocust,TaskSet,task
class UserBehavior(TaskSet):
    def on_start(self):
        self.login()
    def login(self):
        self.client.get('/login/login_action',params={'username':'han','password':'chz970916'})

    @task(2)
    def event_manage(self):
        self.client.get('/login/event_manage/')
    @task(2)
    def guest_manage(self):
        self.client.get('/login/guest_manage/')
    @task(1)
    def search_name(self):
        self.client.get('/login/search_name/',params={'phone':'17600000001'})

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000