"""Health check response formatter. Clean file."""
import json
def format_health_response(result):
    return json.dumps(result, default=str, indent=2)
