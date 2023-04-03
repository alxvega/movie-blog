import traceback

from celery import Task
from celery.exceptions import Ignore


class AbortedTaskException(Exception):
    pass


class BaseScraperTask(Task):
    def __call__(self, *args, **kwargs):
        try:
            return super().__call__(*args, **kwargs)
        except AbortedTaskException as e:
            exc = traceback.format_exc()
            self.update_state(state="ABORTED", meta={"exception": repr(e)})
            self.send_event(type_="task-aborted", exception=repr(e), traceback=exc)
            raise Ignore()
