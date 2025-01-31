import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_file_states = {}  # Stores the last known content of files

    def read_file(self, file_path):
        """ Read file content safely """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            return None  # Return None if the file is unreadable or deleted

    def process_event(self, event_type, event):
        if event.is_directory:
            return

        file_path = event.src_path
        new_content = self.read_file(file_path)

        if event_type == "Modified":
            old_content = self.last_file_states.get(file_path, None)
            if new_content and old_content and new_content != old_content:
                print(f"\nModified: {file_path} at {time.ctime()}")
                self.show_changes(old_content, new_content)

            self.last_file_states[file_path] = new_content  # Update stored content

        elif event_type == "Created":
            print(f"\nCreated: {file_path} at {time.ctime()}")
            if new_content:
                print(f"New Content:\n{new_content}")

            self.last_file_states[file_path] = new_content  # Store new file content

        elif event_type == "Deleted":
            print(f"\nDeleted: {file_path} at {time.ctime()}")
            self.last_file_states.pop(file_path, None)  # Remove from tracking

    def show_changes(self, old, new):
        """ Display the difference between old and new content """
        old_lines = old.splitlines()
        new_lines = new.splitlines()

        for i, (old_line, new_line) in enumerate(zip(old_lines, new_lines)):
            if old_line != new_line:
                print(f"Line {i+1} changed:\n- {old_line}\n+ {new_line}")

        if len(new_lines) > len(old_lines):
            print("New lines added:")
            for line in new_lines[len(old_lines):]:
                print(f"+ {line}")

    def on_modified(self, event):
        self.process_event("Modified", event)

    def on_created(self, event):
        self.process_event("Created", event)

    def on_deleted(self, event):
        self.process_event("Deleted", event)

def setup_directories():
    main_folder = "MainFolder"
    subfolder1 = os.path.join(main_folder, "SubFolder1")
    subfolder2 = os.path.join(main_folder, "SubFolder2")

    os.makedirs(subfolder1, exist_ok=True)
    os.makedirs(subfolder2, exist_ok=True)

    text_file1 = os.path.join(subfolder1, "file1.txt")
    text_file2 = os.path.join(subfolder1, "file2.txt")

    if not os.path.exists(text_file1):
        with open(text_file1, "w") as f:
            f.write("This is file 1.")

    if not os.path.exists(text_file2):
        with open(text_file2, "w") as f:
            f.write("This is file 2.")

    print(f"Folder structure created inside {main_folder}")
    return subfolder1

if __name__ == "__main__":
    folder_to_monitor = setup_directories()
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_monitor, recursive=True)
    observer.start()

    print(f"Monitoring changes in: {folder_to_monitor}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

