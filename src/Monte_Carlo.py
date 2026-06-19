# ============================================================
# MONTE-CARLO DRIFT ANALYSIS
# Reviewer #1 Comment 2,4,6
# ============================================================

import random
import time
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# POLICY V1
# ============================================================

def policy_v1(r):

    if r["resource"] == "report":
        return "Permit"

    return "NotApplicable"


# ============================================================
# POLICY V2
# ============================================================

def policy_v2(r):

    if r["resource"] == "report":
        return "Permit"

    if r["department"] == "finance":
        return "Permit"

    return "NotApplicable"


# ============================================================
# POLICY V3
# ============================================================

def policy_v3(r):

    if r["action"] == "write":
        return "Deny"

    if r["resource"] == "report":
        return "Permit"

    return "NotApplicable"


# ============================================================
# POLICY V4
# ============================================================

def policy_v4(r):

    if r["action"] == "write":
        return "Deny"

    if r["department"] == "finance":
        return "Permit"

    return "NotApplicable"


# ============================================================
# MONTE CARLO REQUEST GENERATION
# ============================================================

def generate_mc_requests(n):

    roles = [
        "admin",
        "manager",
        "staff",
        "guest"
    ]

    actions = [
        "read",
        "write"
    ]

    resources = [
        "report",
        "record"
    ]

    departments = [
        "finance",
        "hr"
    ]

    requests = []

    for _ in range(n):

        requests.append({

            "role":
                random.choice(roles),

            "action":
                random.choice(actions),

            "resource":
                random.choice(resources),

            "department":
                random.choice(departments)

        })

    return requests


# ============================================================
# DRIFT CLASSIFICATION
# ============================================================

def analyze_transition(
    requests,
    old_policy,
    new_policy
):

    drift = 0
    expansion = 0
    restriction = 0
    divergence = 0

    for r in requests:

        d1 = old_policy(r)
        d2 = new_policy(r)

        if d1 != d2:

            drift += 1

            # Expansion
            if (
                d2 == "Permit"
                and d1 != "Permit"
            ):
                expansion += 1

            # Restriction
            elif (
                d1 == "Permit"
                and d2 == "Deny"
            ):
                restriction += 1

            # Divergence
            else:
                divergence += 1

    return (
        drift,
        expansion,
        restriction,
        divergence
    )


# ============================================================
# TABLE 1
# SCALABILITY
# ============================================================

def scalability_experiment():

    sizes = [
        1000,
        10000,
        100000,
        500000,
        1000000
    ]

    results = []

    print("=" * 70)
    print("SCALABILITY EVALUATION")
    print("=" * 70)

    for n in sizes:

        requests = generate_mc_requests(n)

        start = time.perf_counter()

        drift, exp, res, div = \
            analyze_transition(
                requests,
                policy_v2,
                policy_v3
            )

        runtime = (
            time.perf_counter()
            - start
        )

        results.append([
            n,
            drift,
            runtime
        ])

        print(
            f"N={n:>10,} "
            f" Drift={drift:>10,}"
            f" Runtime={runtime:.4f}s"
        )

    return pd.DataFrame(
        results,
        columns=[
            "Requests",
            "Drift",
            "Runtime"
        ]
    )


# ============================================================
# TABLE 2
# DRIFT CATEGORY ANALYSIS
# ============================================================

def category_experiment():

    N = 1000000

    requests = generate_mc_requests(N)

    transitions = [

        (
            "v1→v2",
            policy_v1,
            policy_v2
        ),

        (
            "v2→v3",
            policy_v2,
            policy_v3
        ),

        (
            "v3→v4",
            policy_v3,
            policy_v4
        )
    ]

    rows = []

    print("\n")
    print("=" * 70)
    print("DRIFT CATEGORY ANALYSIS")
    print("=" * 70)

    for name, p1, p2 in transitions:

        drift, exp, res, div = \
            analyze_transition(
                requests,
                p1,
                p2
            )

        rows.append([
            name,
            drift,
            exp,
            res,
            div
        ])

        print(
            name,
            drift,
            exp,
            res,
            div
        )

    return pd.DataFrame(
        rows,
        columns=[
            "Transition",
            "Drift",
            "Expansion",
            "Restriction",
            "Divergence"
        ]
    )


# ============================================================
# FIGURE 1
# ============================================================

def plot_runtime(df):

    plt.figure(figsize=(6,4))

    plt.plot(
        df["Requests"],
        df["Runtime"],
        marker="o"
    )

    plt.xlabel(
        "Number of Requests"
    )

    plt.ylabel(
        "Runtime (seconds)"
    )

    plt.title(
        "Runtime Scalability under Monte-Carlo Sampling"
    )

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "runtime_scalability.png",
        dpi=300
    )

    plt.show()


# ============================================================
# FIGURE 2
# ============================================================

def plot_drift(df):

    plt.figure(figsize=(6,4))

    plt.plot(
        df["Requests"],
        df["Drift"],
        marker="s"
    )

    plt.xlabel(
        "Number of Requests"
    )

    plt.ylabel(
        "Detected Drift Instances"
    )

    plt.title(
        "Detected Drift versus Request Set Size"
    )

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        "drift_growth.png",
        dpi=300
    )

    plt.show()


# ============================================================
# MAIN
# ============================================================

scalability_df = scalability_experiment()

category_df = category_experiment()

print("\n")
print("SCALABILITY TABLE")
print(scalability_df)

print("\n")
print("CATEGORY TABLE")
print(category_df)

scalability_df.to_csv(
    "scalability_results.csv",
    index=False
)

category_df.to_csv(
    "category_results.csv",
    index=False
)

plot_runtime(
    scalability_df
)

plot_drift(
    scalability_df
)

print("\nSaved Files:")
print("runtime_scalability.png")
print("drift_growth.png")
print("scalability_results.csv")
print("category_results.csv")
