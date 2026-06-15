# Witchcat Skills

Witchcat 可安装 Agent Skills 集合。每个顶层目录都是一个可独立加载的 Skill，`witchcat-core` 负责基础行为和完整路由。

## 安装

将需要的 Skill 目录复制到 Agent 的 Skills 目录，或使用兼容 Agent Skills 的安装工具加载本仓库。

Trae 本地目录示例：

```text
C:\Users\Administrator\.trae\skills
```

## 核心与工程工作流

- `witchcat-core`：基础行为、模式、任务分级与 Skills 路由
- `build-workflow`：功能开发与代码修改流程
- `arch-workflow`：大型或跨模块架构规划
- `debug-workflow`：普通代码缺陷、测试失败、性能和并发诊断
- `root-cause-debugging`：部署环境、接口错误、配置和构建产物根因诊断
- `engineering-review`：工程审查与质量门禁
- `repo-conventions`：仓库结构、命名和代码规范
- `breakpoint-logging`：关键路径诊断日志
- `create-pr`：推送分支并创建 PR/MR

## 技术栈、测试与设计

- `react-conventions`：React 与 TypeScript 组件规范
- `e2e-testing`：Playwright E2E 测试规范
- `ui-ux-pro-max`：产品 UI、仪表盘、后台和数据密集界面设计
- `design-taste-frontend`：落地页、营销网站和作品集视觉设计
- `redesign-existing-projects`：已有网站和应用的视觉审查与升级

## 文档与集成

- `docx`、`pdf`、`pptx`、`xlsx`：文档与办公文件处理
- `mcp-builder`：MCP Server 与 MCP Tool 构建
- `notion`：Notion 工作区操作
- `knowledge-capture`：将讨论和决策整理为 Notion 知识
- `ssh-essentials-1.0.0`：SSH、隧道和远程文件传输
- `skill-creator`：Skill 创建、修改和校验

## 量化与市场数据

- `quant-research-audit`：量化研究、因子和回测可信度审查
- `quant-strategy-validation`：策略报告、源码和样本外验证
- `tushare`、`tushare-data`：Tushare 市场数据获取与分析

## 路由原则

- 每次只选择一个主要工作流或调试 Skill。
- 根据任务组合最小数量的技术栈、设计、文件和专业领域 Skill。
- 已有界面视觉升级由 `redesign-existing-projects` 主导。
- 数据密集型产品界面优先使用 `ui-ux-pro-max`。
- 展示型网站和营销页面优先使用 `design-taste-frontend`。

具体路由规则见 [`witchcat-core/SKILL.md`](witchcat-core/SKILL.md)。

## 第三方来源

部分 Skills 基于第三方开源项目，相关许可证随对应目录或 `licenses/` 目录一并保留：

- [`Leonxlnx/taste-skill`](https://github.com/Leonxlnx/taste-skill)：`design-taste-frontend`、`redesign-existing-projects`
