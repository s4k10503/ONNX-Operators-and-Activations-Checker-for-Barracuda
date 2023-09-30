import customtkinter as ctk

FONT_TYPE = "Arial"


class ONNXCheckerView(ctk.CTk):
    def __init__(self, presenter):
        super().__init__()

        ctk.set_default_color_theme("dark-blue")
        self.presenter = presenter

        # Set title
        self.title("ONNX Operators and Activations Checker for Barracuda")

        # Setup the form elements
        self.setup_form()

    def setup_form(self):
        # Load model button
        self.load_button = ctk.CTkButton(
            self, text="Load ONNX Model", command=self.presenter.load_model, font=(FONT_TYPE, 20))
        self.load_button.grid(row=0, column=0, columnspan=2, pady=20)

        # Display the file name label
        self.file_name_label = ctk.CTkLabel(
            self, text="", font=(FONT_TYPE, 15))
        self.file_name_label.grid(row=4, column=0, columnspan=2, pady=10)

        # Display the result label
        self.result_label = ctk.CTkLabel(
            self, text="", font=(FONT_TYPE, 15))
        self.result_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Display the result text box
        self.result_text = ctk.CTkTextbox(
            self, width=500, height=200, font=(FONT_TYPE, 15))
        self.result_text.grid(row=2, column=0, columnspan=2, pady=10)

        # Initialize the progress bar
        self.progress = ctk.CTkProgressBar(
            master=self,
            width=500,
            height=20,
            border_width=2,
            corner_radius=5,
            mode="determinate",
            determinate_speed=1,
            indeterminate_speed=1
        )
        self.progress.grid(row=3, column=0, columnspan=2, pady=20)
        self.progress.set(0)
