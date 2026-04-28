def generate_requests():
    requests = []

    roles = ["doctor", "nurse", "patient"]
    emergencies = [True, False]

    for role in roles:
        for emergency in emergencies:
            requests.append({
                "role": role,
                "emergency": emergency,
                "action": "treat",
                "resource": "patient"
            })

    for role in roles:
        requests.append({
            "role": role,
            "emergency": False,
            "action": "read",
            "resource": "record"
        })

    print(f"Generated {len(requests)} requests for health domain")
    return requests


def generate_full_requests():
    requests = []

    roles = ["admin", "manager", "staff", "guest"]
    actions = ["read", "write"]
    resources = ["report", "record"]
    departments = ["finance", "hr"]

    for r in roles:
        for a in actions:
            for res in resources:
                for d in departments:
                    requests.append({
                        "role": r,
                        "action": a,
                        "resource": res,
                        "department": d
                    })

    return requests
