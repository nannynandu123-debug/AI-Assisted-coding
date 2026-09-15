from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    project_completion_rate: float
    teamwork_score: float
    attendance: float


WEIGHTS = {
    "project_completion_rate": 0.50,
    "teamwork_score": 0.30,
    "attendance": 0.20,
}


def validate(employee: Employee) -> None:
    scores = [
        employee.project_completion_rate,
        employee.teamwork_score,
        employee.attendance,
    ]

    if any(score < 0 or score > 100 for score in scores):
        raise ValueError("All scores must be between 0 and 100.")


def calculate_score(employee: Employee) -> float:
    validate(employee)

    return round(
        employee.project_completion_rate * WEIGHTS["project_completion_rate"]
        + employee.teamwork_score * WEIGHTS["teamwork_score"]
        + employee.attendance * WEIGHTS["attendance"],
        2,
    )


def get_rating(score: float) -> str:
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 60:
        return "Needs Improvement"
    return "Unsatisfactory"


def analyze_bias() -> list[str]:
    warnings = []

    if WEIGHTS["attendance"] > 0.25:
        warnings.append(
            "Attendance has a high weight and may disadvantage employees "
            "with disabilities, medical conditions, or caregiving duties."
        )

    warnings.append(
        "Teamwork scores may be subjective. Use multiple reviewers and "
        "documented examples."
    )

    warnings.append(
        "Do not include race, gender, age, disability, medical information, "
        "religion, or family status in the scoring formula."
    )

    warnings.append(
        "Exclude approved leave and provide reasonable accommodations when "
        "evaluating attendance."
    )

    if round(sum(WEIGHTS.values()), 2) != 1.0:
        warnings.append("The scoring weights must add up to 1.0.")

    return warnings


def main() -> None:
    employees = [
        Employee("Asha", 95, 88, 97),
        Employee("Ben", 78, 82, 90),
        Employee("Chris", 65, 70, 75),
    ]

    print("Employee Performance Evaluation\n")

    for employee in employees:
        score = calculate_score(employee)
        print(f"{employee.name}: {score}/100 - {get_rating(score)}")

    print("\nFairness and Bias Analysis:")
    for warning in analyze_bias():
        print(f"- {warning}")


if __name__ == "__main__":
    main()