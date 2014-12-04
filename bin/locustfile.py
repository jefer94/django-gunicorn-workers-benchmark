# -*- coding: utf-8 -*-

from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    @task
    def index(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior

    min_wait = 5000
    max_wait = 9000
