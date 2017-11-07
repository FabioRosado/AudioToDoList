"""A Voice Controlled To-Do List"""

import os
import subprocess
import speech_recognition as speech


class ToDo:
    """To-do list object"""
    def __init__(self):
        self.text = ''
        self.audio = speech.Recognizer()
        self.todo = ''

    def say(self, sentence):
        """
        Creates a subprocess in the shell that uses the
        command: 'say <response>'
        """
        print(sentence)
        subprocess.call(["say", sentence])

    def understand(self):
        """
        Listens to microphone and uses google to recognize
        What was said. If google can't recognize the text
        the To-Do list will let the user know.
        """
        print("Listening...")

        with speech.Microphone() as source:
            print("Say Something")
            voice = self.audio.listen(source)

        command = ""

        try:
            command = self.audio.recognize_google(voice)
        except:
            self.say("Sorry, I couldn't understand you.")

        print("You said: %s" % (command,))

        self.text = command

    def todo_exists(self):
        """
        Checks if a to-do list exists. If it doesn't it will ask the
        user if he wants to create a new to-do list.
        """
        if not os.path.isfile('./todo.txt'):
            self.say("There isn't a todo list available yet. Create one?")
            self.understand()
            if "yes" in self.text:
                open('todo.txt', 'w').close()
            if 'no' in self.text:
                self.say("Okay, but you won't be able to create a new to "
                         "do list.")
                return False
        return True

    def create_new_item(self):
        """
        Asks the user what should be added to the to do list.
        Tries to understand what was said.
        Asks confirmation from the user if he wants to add the
        text to the to-do list.
        """
        self.todo_exists()
        with open('todo.txt', 'a') as todo:
            self.say("Please, tell me what I should add to the to do list.")
            self.understand()

            to_add = self.text
            self.say("Do you wish to add: {}".format(to_add))
            self.understand()

            if "yes" in self.text:
                todo.write(to_add + '\n')
                self.say("You added the following to do item: {} to  the to "
                         "do list".format(to_add))
            elif "no" in self.text:
                self.say("You chose not to add the task {} to your to do"
                         "list.".format(to_add))
            else:
                self.say("Sorry, I couldn't understand you. No task was added "
                         "to your list.")

    def read_todo(self):
        """Reads every line of todo.txt"""
        self.todo_exists()
        with open('todo.txt', 'r') as todo:
            self.say("This is what you have on your to do list for today")
            lines = todo.readlines()
            for line in lines:
                self.say(line)

    def get_todo_tasks(self):
        """Get the number of todo items"""
        def _make_gen(reader):
            b = reader(1024 * 1024)
            while b:
                yield b
                b = reader(1024 * 1024)

        todo = open('todo.txt', 'rb')
        f_gen = _make_gen(todo.raw.read)
        return sum(buf.count(b'\n') for buf in f_gen)

    def complete_or_delete(self):
        """
        If a task is completed or deleted it should be deleted from the list.
        This will ask the user which task to be deleted/completed and finally
        asks for confirmation if the user wants to delete that task.
        """
        if "complete" in self.text:
            self.say("Which task would you like to mark as complete?")
        else:
            self.say("Which task would you like to delete?")
        self.understand()

        with open('todo.txt', 'r+') as todo:
            todo_list = todo.read().splitlines()
        text = self.text
        if text in todo_list:
            for line in todo_list:
                if self.text in line:
                    self.say("You chose the following task: {}, "
                             "continue?".format(self.text))
                    self.understand()
                    if "yes" in self.text:
                        todo_list.remove(text)
                        with open('todo.txt', 'a') as todo:
                            todo.seek(0)
                            todo.truncate()
                            for item in todo_list:
                                todo.write(str(item + "\n"))
                        todo.close()
                        self.say("The task {} was removed from the "
                                 "list".format(text))
                    else:
                        self.say("No changes were saved on your to do list.")
        else:
            self.say("Sorry, I couldn't find that task.")

    def run_todo(self):
        """Main function to run the todo list"""
        if self.todo_exists():
            total_todos = self.get_todo_tasks()
            self.say("You currently have {} to do to be completed. "
                     "Available commands:  Create. Listen. Complete. "
                     "Delete and Help. ".format(str(total_todos)))
        else:
            self.say("To do list not found.")

        while True:
            self.understand()

            if "quit" in self.text or "exit" in self.text:
                break
            elif "help" in self.text:
                self.say("To add a new to do say: Insert. "
                         "To listen to your to do list say: Listen. "
                         "To complete or delete a to do say: "
                         "Complete or Delete and then the number of "
                         "the to do list to be completed.")
                self.say("To exit the to do application say Exit "
                         "or Quit at any time.")
            elif "create" in self.text:
                self.create_new_item()
            elif 'listen' in self.text:
                self.read_todo()
            elif "complete" in self.text or "delete" in self.text:
                self.complete_or_delete()
            else:
                self.say("Sorry, I couldn't understand that command.")


if __name__ == "__main__":
    todo = ToDo()
    todo.run_todo()
