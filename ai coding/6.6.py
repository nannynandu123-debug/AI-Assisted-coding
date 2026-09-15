from dataclasses import dataclass


@dataclass
class LoanApplication:
    income: float
    age: int
    employment_status: str
    credit_score: int
    loan_amount: float


VALID_EMPLOYMENT_STATUSES = {
    "Employed",
    "Self-employed",
    "Unemployed",
    "Retired",
}


def normalize_employment_status(status: str) -> str:
    normalized = status.strip().lower().replace("_", " ").replace("-", " ")

    status_map = {
        "employed": "Employed",
        "self employed": "Self-employed",
        "unemployed": "Unemployed",
        "retired": "Retired",
    }

    if normalized not in status_map:
        raise ValueError(
            "Invalid employment status. Use Employed, Self-employed, "
            "Unemployed, or Retired."
        )

    return status_map[normalized]


def validate(application: LoanApplication) -> None:
    if application.income <= 0:
        raise ValueError("Income must be greater than zero.")

    if application.loan_amount <= 0:
        raise ValueError("Loan amount must be greater than zero.")

    if not 18 <= application.age <= 100:
        raise ValueError("Age must be between 18 and 100.")

    if not 300 <= application.credit_score <= 850:
        raise ValueError("Credit score must be between 300 and 850.")

    if application.employment_status not in VALID_EMPLOYMENT_STATUSES:
        raise ValueError("Invalid employment status.")


def assess_loan(application: LoanApplication) -> tuple[str, list[str]]:
    """
    Educational screening only.
    This function does not make a final lending decision.
    Age is collected for auditing but is not used in scoring.
    """
    application.employment_status = normalize_employment_status(
        application.employment_status
    )

    validate(application)

    score = 0
    reasons = []

    if application.income >= 50000:
        score += 2
    elif application.income >= 30000:
        score += 1
    else:
        reasons.append("Income is below the screening threshold.")

    if application.credit_score >= 700:
        score += 3
    elif application.credit_score >= 600:
        score += 1
    else:
        reasons.append("Credit score is below the screening threshold.")

    debt_to_income_proxy = application.loan_amount / application.income

    if debt_to_income_proxy <= 0.30:
        score += 2
    elif debt_to_income_proxy <= 0.50:
        score += 1
    else:
        reasons.append("Requested loan amount is high compared with income.")

    if application.employment_status in {"Employed", "Self-employed"}:
        score += 1
    elif application.employment_status == "Unemployed":
        reasons.append("Employment status requires additional review.")

    if score >= 6:
        result = "Recommended for human review"
    else:
        result = "Requires additional information or human review"

    return result, reasons


def fairness_review() -> list[str]:
    return [
        "Age is not used to calculate the screening result because age-based "
        "decisions may create unlawful discrimination.",
        "Employment status can disadvantage people with non-traditional work, "
        "so applications should receive individualized human review.",
        "Income and credit score can reflect historical or socioeconomic bias.",
        "The result is only a transparent screening aid, not an automated loan "
        "approval or rejection.",
        "Use legally compliant lending criteria, explain decisions, protect "
        "personal data, and provide an appeal process.",
    ]


def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter a valid number.")


def main() -> None:
    print("Loan Screening Demonstration")
    print("This program does not make a final lending decision.\n")

    application = LoanApplication(
        income=read_float("Annual income: "),
        age=int(read_float("Age (used only for auditing): ")),
        employment_status=input(
            "Employment status "
            "(Employed/Self-employed/Unemployed/Retired): "
        ).strip(),
        credit_score=int(read_float("Credit score: ")),
        loan_amount=read_float("Requested loan amount: "),
    )

    try:
        result, reasons = assess_loan(application)

        print(f"\nScreening result: {result}")

        if reasons:
            print("Factors requiring review:")
            for reason in reasons:
                print(f"- {reason}")

        print("\nFairness and ethical review:")
        for item in fairness_review():
            print(f"- {item}")

    except ValueError as error:
        print(f"Input error: {error}")


if __name__ == "__main__":
    main()