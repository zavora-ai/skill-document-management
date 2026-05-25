---
name: document-management
description: Manage documents across Google Docs, Drive, Notion, and OneDrive/SharePoint — create, search, edit, export, comment, and share. Use when creating documents, searching files, editing content, sharing with teams, or exporting to PDF/DOCX.
version: "1.0.0"
license: Apache-2.0
allowed-tools: [google_list_docs, google_search_docs, google_get_doc, google_get_text, google_create_doc, google_insert_text, google_replace_text, google_export_doc, google_list_comments, google_add_comment, google_share_doc, google_delete_doc, notion_search, notion_list_pages, notion_get_page]
tags: [communication, documents, collaboration, google-docs, notion]
metadata:
  author: Zavora AI
  mcp-server: mcp-document
---

# Document Management

Create, search, edit, and share documents across Google Docs and Notion. Always verify sharing permissions before granting access.

## Decision Tree
```
├── "create doc", "write", "draft"? → google_create_doc / google_insert_text
├── "find", "search doc"? → google_search_docs / notion_search
├── "edit", "update", "replace"? → google_replace_text
├── "share", "give access"? → google_share_doc (verify permissions first)
├── "export", "PDF", "download"? → google_export_doc
├── "comment", "feedback"? → google_add_comment / google_list_comments
└── "notion", "page", "wiki"? → notion_search / notion_get_page
```

## MUST DO
- Verify sharing permissions before granting access
- Never share confidential docs externally without approval
- Maintain version history

## MUST NOT DO
- Don't delete documents under legal hold
- Don't share with "anyone with link" for sensitive content
