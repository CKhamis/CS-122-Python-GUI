import tkinter

class GenApp:
    """
    a general purpose GUI

    Argument:
    parent: (tkinter.Tk) the root window object
    """

    def __init__(self, parent):
        parent.title('CS 122')

        # define components
        start_button = tkinter.Button(parent, text='Start', width=20,
                                      command=self.start)
        start_button.grid()

        stop_button = tkinter.Button(parent, text='Stop', width=20,
                                      command=self.stop)
        stop_button.grid()
        self.status = tkinter.Label(parent, text='Ready to start')
        self.status.grid()

    def start(self):
        """
        Updates the label
        :return: None
        """
        self.status.configure(text='In progress', foreground='green')


if __name__ == '__main__':
    main()