#!/usr/bin/env python3
"""Generate structured document content from template variables."""
import json, sys

TEMPLATES = {
    "meeting_notes": "# {title}\n\n**Date:** {date}\n**Attendees:** {attendees}\n\n## Agenda\n{agenda}\n\n## Decisions\n{decisions}\n\n## Action Items\n{actions}",
    "project_brief": "# {title}\n\n## Objective\n{objective}\n\n## Scope\n{scope}\n\n## Timeline\n{timeline}\n\n## Success Criteria\n{criteria}",
    "status_update": "# {title} — Status Update\n\n**Period:** {period}\n**Status:** {status}\n\n## Progress\n{progress}\n\n## Blockers\n{blockers}\n\n## Next Steps\n{next_steps}",
}

def format_doc(data):
    template = data.get("template", "meeting_notes")
    if template not in TEMPLATES:
        return {"error": f"Unknown template: {template}. Available: {list(TEMPLATES.keys())}"}
    content = TEMPLATES[template]
    for key, value in data.get("variables", {}).items():
        content = content.replace(f"{{{key}}}", str(value))
    return {"content": content, "template": template, "word_count": len(content.split())}

if __name__ == "__main__":
    print(json.dumps(format_doc(json.loads(sys.argv[1])), indent=2))
