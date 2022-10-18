import tkinter


def main():
    # root is traditional name for main window, should only be one
    root = tkinter.Tk()
    # window title bar name
    root.title('CS 122')

    # create a label widget
    hello = tkinter.Label(root, text="Hello world!")
    # geometry manager places it on screen
    hello.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
