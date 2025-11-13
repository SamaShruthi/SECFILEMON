# watcher/cross_platform_watcher.py

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from alerts.notifier import log_event  # ✅ Use central logging + email alerts

class WatcherHandler(FileSystemEventHandler):
    def on_modified(self, event):
        log_event("MODIFIED", f"Modified: {event.src_path}")

    def on_created(self, event):
        log_event("CREATED", f"Created: {event.src_path}")

    def on_deleted(self, event):
        log_event("DELETED", f"Deleted: {event.src_path}")

def start_watch(path="."):
    event_handler = WatcherHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print(f"👁️  Watching {path}... Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


# import time
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# from alerts.notifier import log_event  # ✅ Import the logging and email alert function


# class WatcherHandler(FileSystemEventHandler):
#     def on_modified(self, event):
#         log_event("MODIFIED", f"Modified: {event.src_path}")  # ✅ Log and optionally email

#     def on_created(self, event):
#         log_event("CREATED", f"Created: {event.src_path}")  # ✅ Log

#     def on_deleted(self, event):
#         log_event("DELETED", f"Deleted: {event.src_path}")  # ✅ Log + Email


# def start_watch(path="."):
#     event_handler = WatcherHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path, recursive=True)
#     observer.start()
#     print(f"Watching {path}... Press Ctrl+C to stop.")
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()
