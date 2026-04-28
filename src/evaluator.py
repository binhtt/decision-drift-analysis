import os
import json
import tempfile
import subprocess


def install_opa():
    print("Installing OPA...")
    os.system("wget -q https://openpolicyagent.org/downloads/latest/opa_linux_amd64 -O opa")
    os.system("chmod +x opa")
    os.system("cp opa /usr/local/bin/opa")
    os.system("/usr/local/bin/opa version")


def evaluate_policy(policy_file, request):
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmp:
        json.dump(request, tmp)
        tmp_path = tmp.name

    try:
        cmd = [
            "/usr/local/bin/opa",
            "eval",
            "-f", "json",
            "-d", policy_file,
            "-i", tmp_path,
            "data.authz.decision"
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0 or not result.stdout.strip():
            return "NotApplicable"

        data = json.loads(result.stdout)

        if "result" in data and len(data["result"]) > 0:
            return data["result"][0]["expressions"][0]["value"]

        return "NotApplicable"

    except Exception as e:
        print(f"Error evaluating {policy_file}: {e}")
        return "NotApplicable"

    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
