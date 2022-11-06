from abc import ABCMeta, abstractstaticmethod

class Light:

    def Switch_On(self):
        print("The Light is ON")

    def Switch_OFF(self):
        print("The Light is OFF")

class ICommand(metaclass=ABCMeta):

    @abstractstaticmethod
    def execute():
        """"A static interace method"""

class SwitchOnCommand(ICommand):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.Switch_On()

class SwitchOffCommand(ICommand):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.Switch_OFF()




class Switch:
    """"The Invoker Class"""


    def __init__(self):
        self._commands = {}
        self._history = []


    def register(self, command_name, command):
        self._commands[command_name] = command


    def execute(self, command_name):
        if command_name in self._commands:
            self._commands[command_name].execute()
            self._history.append(command_name)
        else:
            print("command not found")

    @property
    def history(self):
        return self._history




if __name__ == "__main__":
    LIGHT = Light()

    SWITCH_ON = SwitchOnCommand(LIGHT)
    SWITCH_OFF = SwitchOffCommand(LIGHT)

    SWITCH = Switch()

    SWITCH.register("ON", SWITCH_ON)
    SWITCH.register("OFF", SWITCH_OFF)

    SWITCH.execute("ON")
    SWITCH.execute("OFF")

    print(SWITCH.history)




