# Document Management Tool Sequences

## Tools (15+)
| Tool | Platform | Purpose |
|------|----------|---------|
| `google_list_docs` | Google | List documents |
| `google_search_docs` | Google | Search by query |
| `google_get_doc` | Google | Document metadata |
| `google_get_text` | Google | Full text content |
| `google_create_doc` | Google | Create new document |
| `google_insert_text` | Google | Append text |
| `google_replace_text` | Google | Find and replace |
| `google_export_doc` | Google | Export to PDF/DOCX |
| `google_list_comments` | Google | View comments |
| `google_add_comment` | Google | Add comment |
| `google_share_doc` | Google | Share with permissions |
| `google_delete_doc` | Google | Delete document |
| `notion_search` | Notion | Search pages |
| `notion_list_pages` | Notion | List pages in workspace |
| `notion_get_page` | Notion | Get page content |

## Sequence: Create and Share (3 calls)
```
1. google_create_doc(title: "Q1 Planning", body: "# Q1 Goals\n...")
   → {id: "doc_123", url: "https://docs.google.com/..."}
2. google_share_doc(id: "doc_123", email: "team@company.com", role: "writer")
3. google_add_comment(id: "doc_123", text: "Please review by Friday")
```

## Sequence: Search and Export (2 calls)
```
1. google_search_docs(query: "Q4 revenue report")
   → [{id: "doc_456", title: "Q4 Revenue Report 2024"}]
2. google_export_doc(id: "doc_456", format: "pdf")
   → {download_url: "..."}
```
