import os
import json
from tkinter.filedialog import askopenfilename


class ONNXCheckerPresenter:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def load_model(self):
        file_path = askopenfilename(filetypes=[("ONNX files", "*.onnx")])
        if file_path:
            self.view.progress.start()

            file_name = os.path.basename(file_path)
            self.view.file_name_label.configure(
                text=f"Loaded file: {file_name}")

            unsupported_operators, unsupported_activations = self.model.load_model(
                file_path)
            self.view.result_label.configure(
                text="Unsupported Operators and Activation Functions:")
            self.view.result_text.delete("1.0", "end")
            self.view.result_text.insert("end", "Unsupported Operators:\n")
            self.view.result_text.insert("end", json.dumps(
                unsupported_operators, indent=4))
            self.view.result_text.insert(
                "end", "\nUnsupported Activation Functions:\n")
            self.view.result_text.insert("end", json.dumps(
                unsupported_activations, indent=4))

            self.view.progress.set(1)
            self.view.progress.stop()
