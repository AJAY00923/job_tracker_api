from abc import ABC, abstractmethod

class BaseNotifier(ABC):

    @abstractmethod
    def send_notification(self, message: str):
        pass


class EmailNotifier(BaseNotifier):

    def send_notification(self, message: str):
        print(f"Sending email notification: {message}")

class SlackNotifier(BaseNotifier):

    def send_notification(self, message: str):
        print(f"Sending Slack notification: {message}")

notifiers = [EmailNotifier(), SlackNotifier()]
for notifier in notifiers:
    notifier.send_notification("You have a new job application update!")