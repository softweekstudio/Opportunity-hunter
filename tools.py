"""
Approved tool boundary for V1.
All external actions are disabled by default.
"""

def permission_check(action, config):
    safety = config.get("safety", {})
    blocked = {
        "spend_money": not safety.get("spend_money", False),
        "send_messages": not safety.get("send_messages", False),
        "publish_content": not safety.get("publish_content", False),
        "make_purchases": not safety.get("make_purchases", False),
        "login_to_accounts": not safety.get("login_to_accounts", False),
    }
    return not blocked.get(action, True)

def available_tools():
    return [
        "analyze_manual_research",
        "save_memory",
        "create_report"
    ]
