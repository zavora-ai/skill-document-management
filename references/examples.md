# Document Skill Examples

## Example 1: "Create a project brief"
```
google_create_doc(title: "Project Alpha Brief", body: "# Project Alpha\n## Objective\n...")
google_share_doc(id: "doc_new", email: "engineering@company.com", role: "commenter")
```
Response: "✅ Created 'Project Alpha Brief' and shared with engineering team (comment access)."

## Example 2: "Find the onboarding doc"
```
google_search_docs(query: "employee onboarding checklist")
→ [{title: "New Hire Onboarding Checklist", id: "doc_789"}]
google_get_text(id: "doc_789") → full content
```

## Example 3: "Search Notion for the API spec"
```
notion_search(query: "API specification v2")
→ [{title: "API Spec v2.0", id: "page_abc"}]
notion_get_page(id: "page_abc") → content
```
