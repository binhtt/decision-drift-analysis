from src.evaluator import evaluate_policy


def compute_drift_set(policy_old, policy_new, request_set):
    delta = []

    for i, r in enumerate(request_set):
        d1 = evaluate_policy(policy_old, r)
        d2 = evaluate_policy(policy_new, r)

        if d1 != d2:
            delta.append((r, d1, d2))

        if i < 5:
            print(f"  Request {i}: role={r.get('role')}, emergency={r.get('emergency')} -> {d1} -> {d2}")

    return delta


def classify_drift(delta):
    exp, res, div = [], [], []

    for r, d1, d2 in delta:
        if d2 == "Permit" and d1 != "Permit":
            exp.append(r)
        elif d1 == "Permit" and d2 == "Deny":
            res.append(r)
        else:
            div.append(r)

    return exp, res, div
