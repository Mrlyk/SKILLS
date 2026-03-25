---
name: yuque-ali
description: 读取、搜索、创建、更新阿里语雀文档，并安装或配置语雀 MCP。用于处理语雀文档、语雀知识库、安装或配置语雀 MCP，或在语雀中查找、写入、更新内容等请求。
---

# 语雀 MCP（阿里内部）

## 第一步：检测连接状态

调用 `skylark_user_info` 探测 MCP 连接状态：

**情况 A：调用成功** → 直接跳到第三步执行操作

**情况 B：工具不存在（MCP 未注册）** → 进入第二步安装配置

**情况 C：工具存在但返回鉴权错误或连接失败** → 进入 `references/setup.md` 的授权步骤，按当前工具对应的方式提示用户完成授权；完成后重新调用 `skylark_user_info` 验证，成功再继续。

## 第二步：安装配置（仅情况 B 触达）

先根据自身身份确定当前工具类型；仅当无法确定时才询问用户。

然后读 `references/setup.md`，按其中的路径查找、`--tool` 映射、安装命令和授权规则执行。

进入安装分支后，**主动使用 Shell 工具逐步执行每一步**，不要只是描述步骤或告知用户去操作。

## 第三步：执行操作

使用 `yuque-ali` MCP server 提供的工具完成用户请求。

### 获取 ID 规则

几乎所有操作都依赖 `book_id` 或 `doc_id`，获取方式分两类：

- **指定知识库或文档：** 必须请用户提供语雀 URL，调用 `skylark_resolve_url` 解析出 ID。禁止猜测或假设 ID。
- **浏览用户自己的知识库：** 直接调用 `skylark_user_book_list`，返回结果中包含 `book_id`，无需 URL。

### 常见操作链路

- **读取指定文档：** 用户提供文档 URL → `skylark_resolve_url` 得 `doc_id` → `skylark_doc_detail`
- **在指定知识库新建文档：** 用户提供知识库 URL → `skylark_resolve_url` 得 `book_id` → `skylark_doc_create`
- **更新指定文档：** 用户提供文档 URL → `skylark_resolve_url` 得 `doc_id` → `skylark_doc_update`
- **关键词搜索：** `skylark_search(q=关键词)` → 结果含 `doc_id` → 按需调用 `skylark_doc_detail`
- **浏览个人知识库：** `skylark_user_book_list` → 返回列表含 `book_id`

### URL 域名注意

调用 `skylark_resolve_url` 时，`url` 参数必须使用 `yuque.antfin.com` 域名。若用户提供的链接是 `aliyuque.antfin.com` 开头，先将域名替换为 `yuque.antfin.com` 再传入，否则会报参数校验错误。
