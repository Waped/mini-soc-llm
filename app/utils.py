import time


def retry(fn, retries=2, delay=1):

    last_error = None

    for i in range(retries):

        try:
            return fn()

        except Exception as e:
            last_error = e
            time.sleep(delay)

    raise last_error


def fallback_response():

    return {
        "incident_type": "unknown",
        "severity": "medium",
        "mitre_technique": "unknown",
        "confidence": 0.3,
        "summary": "Fallback triggered due to LLM failure",
        "investigation_steps": [
            "Check logs manually",
            "Verify alert source",
            "Escalate to SOC analyst"
        ],
        "remediation_actions": [
            "Isolate host if needed",
            "Collect forensic data"
        ]
    }