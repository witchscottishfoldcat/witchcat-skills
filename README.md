# Installable Skills

witchcat 可安装技能包集合。每个子目录是一个独立的技能（skill），可通过兼容工具加载，为 AI 编程助手提供结构化的工作流、规范和约束。

## 技能一览

| 技能 | 用途 | 关键词 |
|---|---|---|
| **witchcat-core** | 基础人格、模式状态、任务分级、技术栈路由，所有工作流技能的前置依赖 | 人格、模式、路由 |
| **arch-workflow** | 架构规划工作流——跨模块拆分、模块边界定义、ADR 决策、宏/微计划 | 架构、ADR、计划 |
| **build-workflow** | 功能开发工作流——需求澄清、风险分析、微计划、TDD 优先、最终审查 | 构建、TDD、实现 |
| **debug-workflow** | 根因调试工作流——先复现、再追踪、最小修复、回归覆盖 | 调试、复现、根因 |
| **engineering-review** | 工程审查与质量门禁——回归风险、可观测性、安全边界、缺失测试 | 审查、质量门禁 |
| **repo-conventions** | 仓库规范——文件命名、代码风格、输出纪律 | 命名、风格 |
| **react-conventions** | React + TypeScript 组件规范——类型定义、样式约束、性能模式、可访问性 | React、TSX、组件 |
| **e2e-testing** | Playwright E2E 测试——选择器策略、等待纪律、网络 Mock、CI 集成 | E2E、Playwright |
| **breakpoint-logging** | 断点式日志注入——在关键分支/外部调用处添加诊断日志 | 日志、可观测性 |
| **create-pr** | 创建 PR/MR——自动检测 GitHub / GitLab，推送分支并提交审查 | PR、Git |

## 目录结构

```
installable-skills/
├── arch-workflow/        # 架构规划
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── references/       # ADR 模板、风险清单、微计划模板
│   └── scripts/          # 渲染脚本
├── breakpoint-logging/   # 断点日志
├── build-workflow/       # 功能开发
├── create-pr/            # PR 创建
├── debug-workflow/       # 根因调试
├── e2e-testing/          # E2E 测试
├── engineering-review/   # 工程审查
├── react-conventions/    # React 规范
├── repo-conventions/     # 仓库规范
└── witchcat-core/        # 基础核心
```

每个技能目录通常包含：

- `SKILL.md` — 技能定义（frontmatter 元数据 + 规范正文）
- `agents/openai.yaml` — 代理接口配置
- `references/` — 参考资料（模板、检查清单等，可选）
- `scripts/` — 渲染/输出脚本（可选）

## 技能组合推荐

| 场景 | 推荐组合 |
|---|---|
| 新功能开发 | witchcat-core → build-workflow + repo-conventions → engineering-review |
| 大型架构变更 | witchcat-core → arch-workflow → build-workflow → engineering-review |
| Bug 修复 | witchcat-core → debug-workflow + breakpoint-logging → engineering-review |
| React 项目开发 | witchcat-core → build-workflow + react-conventions + repo-conventions |
| E2E 测试编写 | witchcat-core → e2e-testing |
| 提交代码审查 | create-pr → engineering-review |
