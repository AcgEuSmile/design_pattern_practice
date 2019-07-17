
## Command Interface
class ICommand(object):
    def execute(self):
        raise NotImplementedError()
    def undo(self):
        raise NotImplementedError()

## void object
class NoCommand(ICommand):
    def execute(self):
        print("No command")
    def undo(self):
        print("No command")

## Concrete Command
class LightOn(ICommand):
    def __init__(self, light):
        self.light = light
    def execute(self):
        self.light.on()
    def undo(self):
        self.light.off()

class LightOff(ICommand):
    def __init__(self, light):
        self.light = light
    def execute(self):
        self.light.off()
    def undo(self):
        self.light.on()

## Invoker
class Invoker(object):
    def __init__(self):
        self.on_command = NoCommand()
        self.off_command = NoCommand()
        self.undo_command = NoCommand()

    def setCommand(self, on_command, off_command):
        self.on_command = on_command
        self.off_command = off_command

    def onInvokerAction(self):
        command = self.on_command
        command.execute()
        self.undo_command = command

    def offInvokerAction(self):
        command = self.off_command
        command.execute()
        self.undo_command = command

    def undoAction(self):
        command = self.undo_command
        command.undo()

## Receiver
class Light(object):
    def on(self):
        print("light on")
    def off(self):
        print("light off")

## Client
class Client(object):
    def __init__(self):
        receiver = Light()
        light_on_cmd = LightOn(receiver)
        light_off_cmd = LightOff(receiver)
        invoker = Invoker()
        
        invoker.setCommand(light_on_cmd, light_off_cmd)
        invoker.onInvokerAction()
        invoker.undoAction()
        invoker.offInvokerAction()
        invoker.undoAction()

if __name__ == "__main__":
    client = Client()
