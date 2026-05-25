# Document Management Skill

> Multi-platform document operations for AI agents — create, search, edit, export, comment, and share across Google Docs, Google Drive, Notion, and Microsoft OneDrive/SharePoint.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--document-green)](https://github.com/zavora-ai/mcp-document)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

This skill orchestrates 15+ document tools across Google Docs and Notion into **governed document workflows** — ensuring proper sharing permissions, version tracking, and structured content creation.

| Workflow | Tool Calls | What It Achieves |
|----------|-----------|------------------|
| Create & Share | 2-3 | New doc with proper permissions |
| Search & Read | 1-2 | Find across Google + Notion |
| Edit | 1-2 | Insert or replace text |
| Export | 1 | PDF/DOCX download |
| Comment & Review | 1-2 | Collaborative feedback |

### Without this skill:
- Documents shared with "anyone with link" (security risk)
- No templates — every doc starts from scratch
- Can't find documents across platforms
- No version awareness when editing

### With this skill:
- Sharing permissions verified before granting access
- Templates for meeting notes, project briefs, status updates
- Cross-platform search (Google Docs + Notion)
- Version-aware editing with change tracking

## Installation

```bash
git clone https://github.com/zavora-ai/skill-document-management.git \
  ~/.skills/skills/document-management
```

## Requirements

**Required:** `mcp-document` (15+ tools — Google Docs, Notion)

**Cross-MCP:**
- `mcp-crm` — create deal proposals and share with customers
- `mcp-slack` — post document links to team channels

## Folder Structure

```
document-management/
├── SKILL.md                       # Decision tree + 5 workflows + sharing rules
├── scripts/
│   └── format_doc.py              # Template-based document generation
├── references/
│   ├── tool-sequences.md          # 15 tools (Google + Notion)
│   ├── cross-mcp-workflows.md     # Document + CRM + Slack
│   └── examples.md                # 3 real scenarios
├── README.md
└── LICENSE
```

## Example

**User:** "Create a project brief for Project Alpha and share with engineering"

**Agent behavior:**
1. Uses `format_doc.py` template to generate structured content
2. Creates doc via `google_create_doc`
3. Shares with engineering team via `google_share_doc` (commenter access)

**Result:**
```
✅ Created "Project Alpha Brief" and shared with engineering (comment access)
```

## Scripts

### `format_doc.py`
Generates structured documents from templates:
```bash
python scripts/format_doc.py '{"template": "project_brief", "variables": {"title": "Alpha", "objective": "..."}}'
```

Available templates: `meeting_notes`, `project_brief`, `status_update`

## Success Criteria

| Metric | Target |
|--------|--------|
| Trigger rate | 90% on document queries |
| Permission safety | Never share externally without approval |
| Cross-platform | Search finds docs in both Google and Notion |

## MCP Server Compatibility

| Platform | Tools |
|----------|-------|
| Google Docs | list, search, get, create, insert, replace, export, comments, share, delete |
| Notion | search, list_pages, get_page |

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0

---

Part of the [ADK-Rust Enterprise](https://enterprise.adk-rust.com) skills ecosystem. Built with ❤️ by [Zavora AI](https://zavora.ai)
