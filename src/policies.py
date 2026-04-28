import os


def create_policies():
    print("Creating policies...")

    policies = {

        # ================= RBAC =================
        "rbac_v1": """
package authz
default decision := "NotApplicable"

decision := "Permit" if input.role == "admin"
decision := "Deny" if input.role == "guest"
""",

        "rbac_v2": """
package authz
default decision := "NotApplicable"

decision := "Permit" if input.role == "admin"
decision := "Permit" if input.role == "manager"
decision := "Deny" if input.role == "guest"
""",

        "rbac_v3": """
package authz
default decision := "NotApplicable"

decision := "Permit" if input.role == "admin"
decision := "Deny" if input.role == "manager"
""",

        "rbac_v4": """
package authz
default decision := "NotApplicable"

decision := "Permit" if input.role == "admin"
decision := "Permit" if input.role == "staff" and input.action == "read"
decision := "Deny" if input.role == "manager"
""",

        # ================= ABAC =================
        "abac_v1": """
package authz
default decision := "NotApplicable"

decision := "Permit" if input.resource == "report"
""",

        "abac_v2": """
package authz
default decision := "NotApplicable"

decision := "Permit" if input.resource == "report"
decision := "Permit" if input.department == "finance"
""",

        "abac_v3": """
package authz
default decision := "NotApplicable"

decision := "Deny" if input.action == "write"
decision := "Permit" if input.resource == "report"
""",

        "abac_v4": """
package authz
default decision := "NotApplicable"

decision := "Deny" if input.action == "write"
decision := "Permit" if input.department == "finance"
""",

        # ================= HEALTH =================
        "health_v1": """
package authz
default decision := "NotApplicable"

# Only doctor allowed
decision := "Permit" if input.role == "doctor"
""",

        "health_v2": """
package authz
default decision := "NotApplicable"

# Allow doctor and nurse
decision := "Permit" if input.role == "doctor"
decision := "Permit" if input.role == "nurse"
""",

        "health_v3": """
package authz
default decision := "NotApplicable"

# Only nurse allowed, doctor denied
decision := "Permit" if input.role == "nurse"
decision := "Deny" if input.role == "doctor"
""",

        "health_v4": """
package authz
default decision := "NotApplicable"

# Only emergency allowed
decision := "Permit" if input.emergency == true
decision := "Deny" if input.emergency == false
"""
    }

    # Ghi file giống y như code gốc của bạn
    for name, content in policies.items():
        filename = f"{name}.rego"
        with open(filename, "w") as f:
            f.write(content)
