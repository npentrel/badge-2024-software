from app_components.notification import Notification
from system.notification.events import ShowNotificationEvent
from system.eventbus import eventbus



class NotificationService:
    def __init__(self):
        eventbus.on_async(ShowNotificationEvent, self._handle_incoming_notification, self)
        self.notifications = [Notification(message="", port=x, open=False) for x in range(0, 7)]

    async def _handle_incoming_notification(self, event: ShowNotificationEvent):
        self.notifications[event.port].message = event.message
        self.notifications[event.port].open()

    def update(self, delta):
        for notification in self.notifications:
            notification.update(delta)

    def draw(self, ctx):
        for notification in self.notifications:
            notification.draw(ctx)
