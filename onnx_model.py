import onnx


class ONNXModel:
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

    def load_model(self, file_path):
        onnx_model = onnx.load(file_path)
        return self.check_model(onnx_model)

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
