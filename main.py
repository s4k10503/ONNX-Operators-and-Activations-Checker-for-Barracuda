from onnx_model import ONNXModel
from onnx_checker_view import ONNXCheckerView
from onnx_checker_presenter import ONNXCheckerPresenter


def main():
    model = ONNXModel()
    presenter = ONNXCheckerPresenter(None, model)
    view = ONNXCheckerView(presenter)
    presenter.view = view
    view.mainloop()


if __name__ == "__main__":
    main()
