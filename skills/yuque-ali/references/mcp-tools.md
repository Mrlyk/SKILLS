# 语雀 MCP 工具参考

## 获取 ID 的核心规则

几乎所有操作都依赖 `book_id` 或 `doc_id`，获取方式分两类：

**针对指定的知识库或文档：** 必须请用户提供目标的语雀 URL，调用 `skylark_resolve_url` 解析出对应 ID，再传入后续工具。禁止猜测或假设 ID。

**浏览用户自己的知识库列表：** 直接调用 `skylark_user_book_list`，返回结果中包含 `book_id`，无需 URL。

---

## 常见操作链路

- **读取指定文档** → 请用户提供文档 URL → `skylark_resolve_url` 得 `doc_id` → `skylark_doc_detail`
- **在指定知识库新建文档** → 请用户提供知识库 URL → `skylark_resolve_url` 得 `book_id` → `skylark_doc_create`
- **更新指定文档** → 请用户提供文档 URL → `skylark_resolve_url` 得 `doc_id` → `skylark_doc_update`
- **关键词搜索（无需 URL）** → `skylark_search(q=关键词)` → 结果含 `doc_id` → 按需调用 `skylark_doc_detail`
- **浏览个人知识库（无需 URL）** → `skylark_user_book_list` → 返回列表含 `book_id`

---

## 一、用户相关

### `skylark_user_info`

获取当前登录用户信息。无参数。常用于验证 MCP 连接是否正常。

---

### `skylark_user_recent`

获取用户最近的操作记录。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `limit` | integer | 否 | 每页数量，默认 20，最大 50 |
| `offset` | integer | 否 | 偏移量，默认 0 |
| `type` | string | 否 | 资源类型过滤，多类型逗号分隔。可选值：`doc`、`book`、`group` |

---

### `skylark_user_groups`

列出用户所属的团队列表。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `limit` | integer | 否 | 每页数量，默认 200，最大 200 |
| `offset` | integer | 否 | 偏移量，默认 0 |
| `role` | integer | 否 | 角色筛选：`0` 管理员，`1` 成员 |

---

## 二、知识库相关

### `skylark_user_book_list`

获取用户的知识库列表，可选个人或团队知识库。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `user_type` | string | 否 | `User`（个人，默认）或 `Group`（团队） |
| `limit` | integer | 否 | 返回最大数量，默认 30，最大 30 |
| `offset` | integer | 否 | 偏移量，默认 0 |

---

### `skylark_book_detail`

获取指定知识库的详细信息。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `book_id` | number | 是 | 知识库 ID |

---

### `skylark_book_create`

创建新的知识库。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `user_id` | number | 是 | 用户/团队 ID |
| `name` | string | 是 | 知识库名称，1-200 字符 |
| `slug` | string | 是 | 路径标识，字母/数字/下划线/中划线/点/加号，1-190 字符 |
| `description` | string | 否 | 知识库简介 |
| `public` | string | 否 | `0` 私密（默认）、`1` 公开、`2` 企业内公开 |

---

### `skylark_book_update`

更新指定知识库。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `book_id` | number | 是 | 知识库 ID |
| `name` | string | 否 | 知识库名称 |
| `description` | string | 否 | 知识库简介 |
| `public` | string | 否 | `0` 私密、`1` 公开、`2` 企业内公开 |

---

### `skylark_book_toc`

获取指定知识库的目录树结构。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `book_id` | number | 是 | 知识库 ID |

---

### `skylark_book_toc_update`

更新知识库目录结构（单操作）。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `book_id` | number | 是 | 知识库 ID |
| `action` | string | 是 | 操作类型（见下表） |
| `node_uuid` | string | 否 | 操作节点 UUID，移动/编辑/删除时必填 |
| `target_uuid` | string | 否 | 目标/参照节点 UUID，`null` 表示根级 |
| `type` | string | 否 | 节点类型：`DOC`（默认）、`TITLE`、`LINK` |
| `title` | string | 否 | 节点标题，最大 200 字符 |
| `doc_id` | number | 否 | 文档 ID，创建 DOC 类型节点时使用 |
| `url` | string | 否 | 链接地址，LINK 类型必填 |
| `open_window` | string | 否 | `0` 当前窗口（默认）、`1` 新窗口 |
| `visible` | string | 否 | `0` 隐藏、`1` 可见（默认） |

`action` 可选值：`prependChild`、`appendChild`、`moveAfter`、`moveBefore`、`insert`、`insertAfter`、`insertSibling`、`remove`、`removeWithChildren`、`edit`

---

## 三、文档相关

### `skylark_doc_list`

获取指定知识库下的文档列表。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `book_id` | number | 是 | 知识库 ID |
| `limit` | integer | 否 | 每页数量，默认 100，最大 100 |
| `offset` | integer | 否 | 偏移量，默认 0 |

---

### `skylark_doc_detail`

获取指定文档的正文内容。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `doc_id` | number | 是 | 文档 ID，可通过 `skylark_doc_list`、`skylark_search` 或 `skylark_resolve_url` 获取 |

---

### `skylark_doc_create`

在指定知识库下创建文档。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `book_id` | number | 是 | 知识库 ID |
| `body` | string | 是 | 文档正文，Markdown 格式 |
| `title` | string | 否 | 文档标题，不传则默认"无标题" |
| `format` | string | 否 | `markdown`（默认）或 `lake` |
| `public` | string | 否 | `0` 私密（默认）、`1` 公开、`2` 企业内公开 |

---

### `skylark_doc_update`

更新指定文档。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `doc_id` | number | 是 | 文档 ID |
| `title` | string | 否 | 文档标题 |
| `body` | string | 否 | 文档正文，Markdown 格式 |
| `format` | string | 否 | `markdown`（默认）或 `lake` |
| `public` | string | 否 | `0` 私密、`1` 公开、`2` 企业内公开 |

---

### `skylark_doc_comments`

获取指定文档的评论列表。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `doc_id` | number | 是 | 文档 ID |
| `limit` | integer | 否 | 每页数量，默认 10，最大 20 |
| `lastId` | integer | 否 | 上次最后一条评论 ID，用于分页 |

---

### `skylark_doc_likes`

获取指定文档的点赞列表。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `doc_id` | number | 是 | 文档 ID |
| `limit` | integer | 否 | 每页数量，默认 50，最大 200 |
| `offset` | integer | 否 | 偏移量，默认 0 |

---

## 四、工具类

### `skylark_resolve_url`

解析语雀 URL，返回对应资源的类型和 ID（`book_id` 或 `doc_id`）。**获取 ID 的首选方式。**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `url` | string | 是 | 语雀 URL，必须使用 `yuque.antfin.com` 域名 |

**注意：** 域名必须是 `yuque.antfin.com`，使用 `aliyuque.antfin.com` 会报参数校验错误。如果用户提供的是 `aliyuque.antfin.com` 开头的链接，自动替换为 `yuque.antfin.com` 再调用。

---

### `skylark_search`

根据关键词搜索用户有权限的语雀文档。

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `q` | string | 是 | 搜索关键词 |
| `scope` | string | 否 | 搜索范围：不填默认全局；填知识库 namespace 则限定该知识库 |
| `pageNo` | integer | 否 | 页码，默认 1 |
| `pageSize` | integer | 否 | 单次返回数量，默认 20，最大 20 |
