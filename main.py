import onnx
import json
from tkinter.filedialog import askopenfilename
import customtkinter as ctk

FONT_TYPE = "Arial"


class ONNXCheckerApp(ctk.CTk):
    supported_operators = [
        "Add", "And", "ArgMax", "ArgMin", "AveragePool", "BatchNormalization",
        "Cast", "Concat", "Constant", "ConstantOfShape", "Conv", "ConvTranspose",
        "DepthToSpace", "Div", "Dropout", "Equal", "Expand", "Flatten", "Gather",
        "Gemm", "GlobalAveragePool", "GlobalMaxPool", "Greater", "Identity", "ImageScaler",
        "InstanceNormalization", "Less", "LessOrEqual", "LRN", "LSTM", "MatMul", "Max",
        "MaxPool", "Mean", "Min", "Mul", "Multinomial", "NonMaxSuppression", "NonZero",
        "Not", "OneHot", "Or", "Pad", "Pow", "RandomNormal", "RandomNormalLike",
        "RandomUniform", "RandomUniformLike", "ReduceMax", "ReduceMean", "ReduceMin",
        "ReduceProd", "ReduceSum", "Reshape", "Resize", "Shape", "Slice", "SpaceToDepth",
        "Split", "Squeeze", "Sub", "Sum", "Tile", "TopK", "Transpose", "Unsqueeze", "Upsample",
        "Where", "Xor"
    ]

    supported_activations = [
        "Abs", "Acos", "Acosh", "Asin", "Asinh", "Atan", "Atanh", "Ceil", "Clip", "Cos",
        "Cosh", "Elu", "Exp", "Floor", "LeakyRelu", "Log", "LogSoftmax", "Neg", "PRelu",
        "Reciprocal", "Relu", "Round", "Selu", "Sigmoid", "Sin", "Sinh", "Softmax", "Sqrt",
        "Tan", "Tanh"
    ]

    def __init__(self):
        super().__init__()

        ctk.set_default_color_theme("dark-blue")

        # Set title
        self.title("ONNX Operators and Activations Checker for Barracuda")

        # Setup the form elements
        self.setup_form()

    def setup_form(self):
        # Load model button
        self.load_button = ctk.CTkButton(
            self, text="Load ONNX Model", command=self.load_model, font=(FONT_TYPE, 20))
        self.load_button.grid(row=0, column=0, columnspan=2, pady=20)

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

    def load_model(self):
        file_path = askopenfilename(filetypes=[("ONNX files", "*.onnx")])
        if file_path:
            self.progress.start()

            onnx_model = onnx.load(file_path)
            unsupported_operators, unsupported_activations = self.check_model(
                onnx_model)
            self.result_label.configure(
                text="Unsupported Operators and Activation Functions:")
            self.result_text.delete("1.0", "end")
            self.result_text.insert("end", "Unsupported Operators:\n")
            self.result_text.insert("end", json.dumps(
                unsupported_operators, indent=4))
            self.result_text.insert(
                "end", "\nUnsupported Activation Functions:\n")
            self.result_text.insert("end", json.dumps(
                unsupported_activations, indent=4))

            self.progress.set(1)
            self.progress.stop()

    def check_model(self, onnx_model):
        unsupported_operators = []
        unsupported_activations = []
        for node in onnx_model.graph.node:
            if node.op_type not in self.supported_operators and node.op_type not in self.supported_activations:
                if node.op_type in self.supported_activations:
                    unsupported_activations.append(node.op_type)
                else:
                    unsupported_operators.append(node.op_type)

        return unsupported_operators, unsupported_activations


app = ONNXCheckerApp()
app.mainloop()
