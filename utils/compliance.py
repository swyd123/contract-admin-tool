def check_rate(employee_rate, minimum_rate):
    if employee_rate < minimum_rate:
        return {
            "result": "fail",
            "message": "The hourly rate is below the award minimum."
        }

    return {
        "result": "pass",
        "message": "The hourly rate meets or exceeds the award minimum."
    }


def check_employment_type(employment_type, ordinary_hours):
    if employment_type == "part-time" and not ordinary_hours:
        return {
            "result": "fail",
            "message": "Part-time contracts must specify agreed ordinary hours."
        }

    if employment_type == "casual" and ordinary_hours:
        return {
            "result": "warning",
            "message": "Casual contracts should not look like fixed guaranteed ordinary hours unless reviewed."
        }

    return {
        "result": "pass",
        "message": "Employment type looks acceptable."
    }


def check_information_statements(employment_type):
    required = ["Fair Work Information Statement"]

    if employment_type == "casual":
        required.append("Casual Employment Information Statement")

    if employment_type == "fixed-term":
        required.append("Fixed Term Contract Information Statement")

    return required
