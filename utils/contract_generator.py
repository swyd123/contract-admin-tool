from pathlib import Path

def generate_contract(template_name, employee):
    template_path = Path("templates") / template_name
    body = template_path.read_text()

    for key, value in employee.items():
        body = body.replace("{{ " + key + " }}", str(value or ""))

    return body
