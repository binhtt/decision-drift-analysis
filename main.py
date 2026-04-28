import time

from src.evaluator import install_opa
from src.policies import create_policies
from src.generator import generate_requests, generate_full_requests
from src.drift import compute_drift_set, classify_drift


def run_domain(domain):
    print(f"\n=== DOMAIN: {domain.upper()} ===")

    if domain == "health":
        versions = ["health_v1.rego", "health_v2.rego", "health_v3.rego", "health_v4.rego"]
        requests = generate_requests()
    else:
        versions = [f"{domain}_v1.rego", f"{domain}_v2.rego", f"{domain}_v3.rego", f"{domain}_v4.rego"]
        requests = generate_full_requests()

    for i in range(len(versions) - 1):
        p_old = versions[i]
        p_new = versions[i + 1]

        print(f"\n--- Testing {p_old} -> {p_new} ---")

        start = time.time()

        delta = compute_drift_set(p_old, p_new, requests)
        exp, res, div = classify_drift(delta)

        end = time.time()

        print(f"\n{p_old} -> {p_new}")
        print("total_requests:", len(requests))
        print("drift:", len(delta))
        print("rate:", round(len(delta)/len(requests), 4))
        print("expansion:", len(exp))
        print("restriction:", len(res))
        print("divergence:", len(div))
        print("time:", round(end - start, 2))


def main():
    install_opa()
    create_policies()

    run_domain("rbac")
    run_domain("abac")
    run_domain("health")


if __name__ == "__main__":
    main()
