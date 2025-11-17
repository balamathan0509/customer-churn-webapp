import numpy as np


def compute_churn_probability(
    tenure: int,
    monthly_charges: float,
    contract: int,
    support_calls: int,
) -> float:
    """Simple handcrafted logistic-style formula for churn probability.

    This replaces the scikit-learn model to avoid heavy dependencies.
    The coefficients encode common-sense business rules:
    - Shorter tenure → higher churn risk
    - Higher monthly charges → slightly higher churn risk
    - Month-to-month contracts (contract=0) → higher churn risk
    - More support calls → higher churn risk
    """

    tenure = np.clip(tenure, 1, 60)
    monthly_charges = np.clip(monthly_charges, 20.0, 150.0)
    contract = 1 if contract else 0
    support_calls = np.clip(support_calls, 0, 20)

    logit = (
        -3.0
        + 0.04 * (70.0 - monthly_charges)
        + 0.03 * (12.0 - float(tenure))
        + 0.25 * float(support_calls)
        + 0.8 * (1 - contract)
    )

    prob = 1.0 / (1.0 + np.exp(-logit))
    return float(prob)


if __name__ == "__main__":
    example = compute_churn_probability(tenure=6, monthly_charges=90.0, contract=0, support_calls=5)
    print(f"Example churn probability: {example:.3f}")
