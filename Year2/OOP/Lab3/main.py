from folder_operations import FolderOperations
import time
import threading
class FolderManager():
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.folder_operations = FolderOperations(folder_path)

    def schedule_detection(self):
        while True:
            self.folder_operations.detection()
            time.sleep(5)  # Schedule detection every 5 seconds

    def run(self):
        # Create a thread for scheduled detection
        detection_thread = threading.Thread(target=self.schedule_detection)
        detection_thread.daemon = True  # Set the thread as a daemon, so it doesn't block program exit

        # Start the detection thread
        detection_thread.start()

        while True:
            print("What do you want to do?")
            print("1 - Commit")
            print("2 - Status")
            print("3 - Get file info")
            print("4 - Quit the program")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == 1:
                self.folder_operations.commit()
            elif choice == 2:
                self.folder_operations.status()
            elif choice == 3:
                self.folder_operations.info()
            elif choice == 4:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    folder_path = r"C:\Users\Simion\Desktop\OOP\Lab3\Test"
    file = FolderManager(folder_path)
    file.run()
