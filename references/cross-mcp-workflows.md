# Document Cross-MCP Workflows

## Document + CRM: Deal Docs
```
CRM: get_deal(id: "d_123") → {name: "Acme Enterprise", value: 75000}
DOCUMENT: google_create_doc(title: "Proposal — Acme Enterprise", body: "...")
DOCUMENT: google_share_doc(id: "doc_new", email: "sarah@acme.com", role: "viewer")
EMAIL: send_email(to: "sarah@acme.com", subject: "Proposal attached", body: "Link: ...")
```

## Document + Slack: Meeting Notes
```
DOCUMENT: google_create_doc(title: "Sprint 14 Retro Notes", body: "## What went well\n...")
SLACK: send_message(channel: "#team", text: "📝 Sprint 14 retro notes: [doc_link]")
```
