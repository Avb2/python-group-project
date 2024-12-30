import tkinter as tk


class Widgets:
    def __init__(self, title):
        self.root = tk.Tk()
        self.root.title(title)
        self.mainFrame = tk.Frame(self.root)
        self.mainFrame.grid(row=0, column=0)

    def frame(self, **kwargs):
        frame = tk.Frame(self.mainFrame)
        if 'row' in kwargs:
            frame.grid(row=kwargs['row'])
        if 'column' in kwargs:
            frame.grid(column=kwargs['column'])
        if 'columnspan' in kwargs:
            frame.grid(columnspan=kwargs['columnspan'])
        frame.grid()

        return frame

    def label(self, frame, **kwargs):
        label = tk.Label(frame)

        if 'text' in kwargs:
            label.configure(text=kwargs['text'])
        if 'row' in kwargs:
            label.grid(row=kwargs['row'])
        if 'column' in kwargs:
            label.grid(column=kwargs['column'])

        return label

    def textField(self, **kwargs) -> tk.Entry:
        entry = tk.Entry(self.mainFrame)

        if 'row' in kwargs:
            entry.grid(row=kwargs['row'])
        if 'column' in kwargs:
            entry.grid(column=kwargs['column'])

        return entry

    def button(self, **kwargs):
        button = tk.Button(self.mainFrame)

        if 'text' in kwargs:
            button.configure(text=kwargs['text'])
        if 'row' in kwargs:
            button.grid(row=kwargs['row'])
        if 'column' in kwargs:
            button.grid(column=kwargs['column'])

        if 'onClick' in kwargs:
            button.configure(command=kwargs['onClick'])

    def LabelButton(self, labelText: str, labelPosition: tuple, textFieldPosition: tuple, frame) -> tk.Entry:
        self.label(frame=frame, text=labelText, row=labelPosition[0], column=labelPosition[1])
        return self.textField(row=textFieldPosition[0], column=textFieldPosition[1])

    def dropdown(self, defaultVal: str, options: list, **kwargs):
        stringVar = tk.StringVar()
        stringVar.set(defaultVal)

        dropdownMenu = tk.OptionMenu(self.mainFrame, stringVar, *options)

        if 'row' in kwargs and 'column' in kwargs:
            dropdownMenu.grid(row=kwargs['row'], column=kwargs['column'])

        return stringVar