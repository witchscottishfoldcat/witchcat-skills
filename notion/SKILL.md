---
name: notion
description: Integrates with Notion API to manage pages, databases, and content. Invoke when user needs to interact with Notion workspaces, create/update pages, move pages, or query databases.
---

# Notion Integration Skill

This skill provides full integration with Notion API using the official MCP server (@modelcontextprotocol/server-notion).

## Available Operations

### Page Operations
| Tool | Description |
|------|-------------|
| `mcp_notion_create-page` | Create a new page with optional content |
| `mcp_notion_update-page` | Update page properties (title, etc.) |
| `mcp_notion_move-page` | Move page to a different parent |
| `mcp_notion_append-block-children` | Append content blocks to a page |
| `mcp_notion_retrieve-block-children` | Get page content blocks |

### Database Operations
| Tool | Description |
|------|-------------|
| `mcp_notion_query-a-data-source` | Query database with filters |
| `mcp_notion_create-a-data-source` | Create a new database |
| `mcp_notion_update-a-data-source` | Update database schema |
| `mcp_notion_list-databases` | List all databases |
| `mcp_notion_retrieve-a-data-source` | Get database info |

### Search & Discovery
| Tool | Description |
|------|-------------|
| `mcp_notion_search` | Search pages and databases |
| `mcp_notion_list-users` | List workspace users |
| `mcp_notion_get-user` | Get user by ID |
| `mcp_notion_get-self` | Get bot info |

## When to Invoke

Invoke this skill when:
- User wants to search Notion content
- User needs to create, update, or move pages
- User wants to organize Notion workspace
- User needs to query databases
- User mentions "Notion", "我的Notion", "Notion页面", "Notion数据库", "整理Notion"

## Usage Examples

### Create a new page
```
User: "Create a new page called 'Project Notes' in my workspace"
```
Use `mcp_notion_create-page` with title "Project Notes"

### Move page to another location
```
User: "Move 'API文档' to 'AiQT' folder"
```
Use `mcp_notion_move-page` with page_id and new parent_id

### Query database
```
User: "Show me all tasks in my database"
```
Use `mcp_notion_query-a-data-source` with database_id

### Search content
```
User: "Search for '股票' in my Notion"
```
Use `mcp_notion_search` with query "股票"

## API Version

Default Notion API version: 2025-09-03

## Important Notes

1. **Authorization Required**: Pages must be shared with the integration in Notion
   - Go to page → `...` → `Connect to integration` → Select your integration

2. **Rate Limits**: Notion API has rate limits (3 requests/second)

3. **Permissions**: The integration needs appropriate capabilities:
   - Read content
   - Update content
   - Insert content

## Configuration

The Notion MCP server is configured in `.mcp.json`:
```json
{
  "notion": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-notion"],
    "env": {
      "NOTION_API_TOKEN": "your-token-here"
    }
  }
}
```
