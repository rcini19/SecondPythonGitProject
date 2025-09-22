from decimal import Decimal, DivisionByZero, InvalidOperation
from django.shortcuts import render
from .forms import CalcForm

def _safe_divide(x: Decimal, y: Decimal) -> Decimal:
    if y == 0:
        raise DivisionByZero("Division by zero")
    return x / y

def index(request):
    result = None
    error = None

    if request.method == "POST":
        form = CalcForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data["a"]
            b = form.cleaned_data["b"]
            op = form.cleaned_data["op"]
            try:
                if op == "+":
                    result = a + b
                elif op == "-":
                    result = a - b
                elif op == "*":
                    result = a * b
                elif op == "/":
                    result = _safe_divide(a, b)
                else:
                    error = "Unknown operation."
            except (DivisionByZero, InvalidOperation):
                error = "Cannot divide by zero."
        else:
            error = "Please correct the highlighted fields."
    else:
        form = CalcForm()

    return render(
        request,
        "calc/index.html",
        {"form": form, "result": result, "error": error, "title": "Simple Calculator"},
    )
