from dataclasses import dataclass


@dataclass
class Feedback:
    name: str
    rating: str
    category: str
    comments: str
    contact_permission: str


RATINGS = [
    "Very satisfied",
    "Satisfied",
    "Neutral",
    "Dissatisfied",
    "Very dissatisfied",
    "Prefer not to say",
]

CATEGORIES = [
    "Product or service",
    "Website or application",
    "Customer support",
    "Accessibility",
    "Other",
    "Prefer not to say",
]


def choose_option(prompt: str, options: list[str]) -> str:
    print(f"\n{prompt}")

    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")

    while True:
        choice = input("Enter the option number: ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]

        print("Please select a valid option.")


def collect_feedback() -> Feedback:
    print("User Feedback Form")
    print("You may skip optional questions by pressing Enter.\n")

    name = input("Name (optional): ").strip() or "Anonymous"

    rating = choose_option(
        "How satisfied are you with our product or service?",
        RATINGS,
    )

    category = choose_option(
        "What is your feedback mainly about?",
        CATEGORIES,
    )

    comments = input(
        "\nComments or suggestions (optional): "
    ).strip()

    contact_permission = choose_option(
        "May we contact you about this feedback?",
        ["Yes", "No", "Prefer not to say"],
    )

    return Feedback(
        name=name,
        rating=rating,
        category=category,
        comments=comments,
        contact_permission=contact_permission,
    )


def review_inclusivity() -> list[str]:
    return [
        "All questions use neutral and respectful language.",
        "Users may remain anonymous and skip optional questions.",
        "Options include 'Other' and 'Prefer not to say'.",
        "No unnecessary personal or sensitive information is requested.",
        "The form uses clear prompts, numbered choices, and simple validation.",
        "For broader accessibility, provide keyboard navigation, labels, "
        "screen-reader support, sufficient color contrast, and translations "
        "in a graphical or web version.",
    ]


def main() -> None:
    feedback = collect_feedback()

    print("\nThank you for your feedback!")
    print(f"Category: {feedback.category}")
    print(f"Rating: {feedback.rating}")

    if feedback.comments:
        print(f"Comments: {feedback.comments}")

    print("\nInclusivity and Accessibility Review:")
    for item in review_inclusivity():
        print(f"- {item}")


if __name__ == "__main__":
    main()