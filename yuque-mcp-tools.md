# Yuque MCP 工具方法说明

共 22 个工具，分为用户、知识库、文档三大类。标注「废弃」的方法请使用括号内推荐的替代方法。

---

## 一、用户相关

### `skylark_user_info`

获取当前登录用户的信息。

无参数。

---

### `skylark_user_recent`

获取用户最近的操作记录。


| 参数       | 类型      | 必填  | 说明                                      |
| -------- | ------- | --- | --------------------------------------- |
| `limit`  | integer | 否   | 每页数量，默认 20，最大 50                        |
| `offset` | integer | 否   | 偏移量，默认 0                                |
| `type`   | string  | 否   | 资源类型过滤，多类型逗号分隔。可选值：`doc`、`book`、`group` |


---

### `skylark_user_groups`

列出用户所属的团队列表。


| 参数       | 类型      | 必填  | 说明                  |
| -------- | ------- | --- | ------------------- |
| `limit`  | integer | 否   | 每页数量，默认 200，最大 200  |
| `offset` | integer | 否   | 偏移量，默认 0            |
| `role`   | integer | 否   | 角色筛选：`0` 管理员，`1` 成员 |


---

## 二、知识库相关

### `skylark_user_book_list`

获取用户的知识库列表，可选择个人或团队知识库。


| 参数          | 类型      | 必填  | 说明                         |
| ----------- | ------- | --- | -------------------------- |
| `user_type` | string  | 否   | `User`（个人，默认）或 `Group`（团队） |
| `limit`     | integer | 否   | 返回最大数量，默认 30，最大 30         |
| `offset`    | integer | 否   | 偏移量，默认 0                   |


---

### `skylark_book_detail`

获取指定知识库的详细信息。


| 参数        | 类型     | 必填  | 说明     |
| --------- | ------ | --- | ------ |
| `book_id` | number | 是   | 知识库 ID |


---

### `skylark_book_create`

创建新的知识库。


| 参数            | 类型     | 必填  | 说明                                    |
| ------------- | ------ | --- | ------------------------------------- |
| `user_id`     | number | 是   | 用户/团队 ID                              |
| `name`        | string | 是   | 知识库名称，1-200 字符                        |
| `slug`        | string | 是   | 知识库路径，1-190 字符，格式：字母、数字、下划线、中划线、点号、加号 |
| `description` | string | 否   | 知识库简介                                 |
| `public`      | string | 否   | 公开性：`0` 私密（默认）、`1` 公开、`2` 企业内公开       |


---

### `skylark_book_update`

更新指定的语雀知识库（id 模式）。


| 参数            | 类型     | 必填  | 说明                                 |
| ------------- | ------ | --- | ---------------------------------- |
| `book_id`     | number | 是   | 知识库 ID                             |
| `name`        | string | 否   | 知识库名称，不修改则不传                       |
| `description` | string | 否   | 知识库简介，不修改则不传                       |
| `public`      | string | 否   | 公开性：`0` 私密、`1` 公开、`2` 企业内公开，不修改则不传 |


---

### `skylark_book_toc`

获取指定知识库的目录树结构。


| 参数        | 类型     | 必填  | 说明     |
| --------- | ------ | --- | ------ |
| `book_id` | number | 是   | 知识库 ID |


---

### `skylark_book_toc_update`

更新指定知识库的目录结构（单操作）。


| 参数            | 类型     | 必填  | 说明                                         |
| ------------- | ------ | --- | ------------------------------------------ |
| `book_id`     | number | 是   | 知识库 ID                                     |
| `action`      | string | 是   | 操作类型，见下方说明                                 |
| `node_uuid`   | string | 否   | 操作节点的 UUID，移动/编辑/删除时必填                     |
| `target_uuid` | string | 否   | 目标/参照节点 UUID，`null` 表示根级，创建/移动时使用          |
| `type`        | string | 否   | 节点类型：`DOC` 文档（默认）、`TITLE` 分组标题、`LINK` 外部链接 |
| `title`       | string | 否   | 节点标题，最大 200 字符，创建/编辑时使用                    |
| `doc_id`      | number | 否   | 文档 ID，创建 DOC 类型节点时使用                       |
| `url`         | string | 否   | 链接地址或文档 slug，LINK 类型必填                     |
| `open_window` | string | 否   | 是否新窗口打开：`0` 当前窗口（默认）、`1` 新窗口               |
| `visible`     | string | 否   | 是否可见：`0` 隐藏、`1` 可见（默认）                     |


`action` 可选值：


| 值                    | 说明               |
| -------------------- | ---------------- |
| `prependChild`       | 使节点成为某节点的首个子节点   |
| `appendChild`        | 使节点成为某节点的最后一个子节点 |
| `moveAfter`          | 使节点成为某节点的下一个同级节点 |
| `moveBefore`         | 使节点成为某节点的上一个同级节点 |
| `insert`             | 创建节点             |
| `insertAfter`        | 末尾创建节点           |
| `insertSibling`      | 创建同级节点           |
| `remove`             | 删除节点             |
| `removeWithChildren` | 删除节点及其子节点        |
| `edit`               | 编辑节点（重命名、更新链接等）  |


---

### `skylark_user_book_update` *(废弃，请改用 `skylark_book_update`)*

更新指定的语雀知识库（namespace 模式）。


| 参数            | 类型     | 必填  | 说明                                 |
| ------------- | ------ | --- | ---------------------------------- |
| `namespace`   | string | 是   | 知识库的 namespace                     |
| `name`        | string | 否   | 知识库名称，不修改则不传                       |
| `description` | string | 否   | 知识库简介，不修改则不传                       |
| `public`      | string | 否   | 公开性：`0` 私密、`1` 公开、`2` 企业内公开，不修改则不传 |


---

## 三、文档相关

### `skylark_doc_list`

获取指定知识库下的文档列表（book_id 模式）。


| 参数        | 类型      | 必填  | 说明                 |
| --------- | ------- | --- | ------------------ |
| `book_id` | number  | 是   | 知识库 ID             |
| `limit`   | integer | 否   | 每页数量，默认 100，最大 100 |
| `offset`  | integer | 否   | 偏移量，默认 0           |


---

### `skylark_doc_detail`

获取指定文档的正文内容（doc_id 模式）。


| 参数       | 类型     | 必填  | 说明                                                                       |
| -------- | ------ | --- | ------------------------------------------------------------------------ |
| `doc_id` | number | 是   | 文档 ID，可通过 `skylark_doc_list`、`skylark_search` 或 `skylark_resolve_url` 获取 |


---

### `skylark_doc_create`

在指定知识库下创建文档（book_id 模式）。


| 参数        | 类型     | 必填  | 说明                              |
| --------- | ------ | --- | ------------------------------- |
| `book_id` | number | 是   | 知识库 ID                          |
| `body`    | string | 是   | 文档正文，Markdown 格式                |
| `title`   | string | 否   | 文档标题，不传则默认"无标题"                 |
| `format`  | string | 否   | body 格式：`markdown`（默认）或 `lake`  |
| `public`  | string | 否   | 公开性：`0` 私密（默认）、`1` 公开、`2` 企业内公开 |


---

### `skylark_doc_update`

更新指定语雀文档（doc_id 模式）。


| 参数       | 类型     | 必填  | 说明                                 |
| -------- | ------ | --- | ---------------------------------- |
| `doc_id` | number | 是   | 文档 ID                              |
| `title`  | string | 否   | 文档标题，不修改则不传                        |
| `body`   | string | 否   | 文档正文，Markdown 格式，不修改则不传            |
| `format` | string | 否   | body 格式：`markdown`（默认）或 `lake`     |
| `public` | string | 否   | 公开性：`0` 私密、`1` 公开、`2` 企业内公开，不修改则不传 |


---

### `skylark_doc_comments`

获取指定文档的评论列表。


| 参数       | 类型      | 必填  | 说明               |
| -------- | ------- | --- | ---------------- |
| `doc_id` | number  | 是   | 文档 ID            |
| `limit`  | integer | 否   | 每页数量，默认 10，最大 20 |
| `lastId` | integer | 否   | 上次最后一条评论 ID，用于分页 |


---

### `skylark_doc_likes`

获取指定文档的点赞列表。


| 参数       | 类型      | 必填  | 说明                |
| -------- | ------- | --- | ----------------- |
| `doc_id` | number  | 是   | 文档 ID             |
| `limit`  | integer | 否   | 每页数量，默认 50，最大 200 |
| `offset` | integer | 否   | 偏移量，默认 0          |


---

### `skylark_user_doc_list` *(废弃，请改用 `skylark_doc_list`)*

获取指定知识库下的文档列表（namespace 模式）。


| 参数          | 类型      | 必填  | 说明                 |
| ----------- | ------- | --- | ------------------ |
| `namespace` | string  | 是   | 知识库的 namespace     |
| `limit`     | integer | 否   | 每页数量，默认 100，最大 100 |
| `offset`    | integer | 否   | 偏移量，默认 0           |


---

### `skylark_user_doc_detail` *(废弃，请改用 `skylark_doc_detail`)*

获取指定文档的正文内容（支持 id 或 namespace + slug，优先 id）。


| 参数          | 类型     | 必填  | 说明                              |
| ----------- | ------ | --- | ------------------------------- |
| `id`        | number | 否   | 文档 ID，与 namespace+slug 二选一，优先使用 |
| `namespace` | string | 否   | 知识库的 namespace，与 slug 共同使用      |
| `slug`      | string | 否   | 文档的 slug，与 namespace 共同使用       |


---

### `skylark_user_doc_create` *(废弃，请改用 `skylark_doc_create`)*

在指定知识库下创建文档（namespace 模式）。


| 参数          | 类型     | 必填  | 说明                              |
| ----------- | ------ | --- | ------------------------------- |
| `namespace` | string | 是   | 知识库的 namespace                  |
| `body`      | string | 是   | 文档正文，Markdown 格式                |
| `title`     | string | 否   | 文档标题，不传则默认"无标题"                 |
| `format`    | string | 否   | body 格式：`markdown`（默认）或 `lake`  |
| `public`    | string | 否   | 公开性：`0` 私密（默认）、`1` 公开、`2` 企业内公开 |


---

### `skylark_user_doc_update` *(废弃，请改用 `skylark_doc_update`)*

更新指定语雀文档（namespace + slug 模式）。


| 参数          | 类型     | 必填  | 说明                                 |
| ----------- | ------ | --- | ---------------------------------- |
| `namespace` | string | 是   | 知识库的 namespace                     |
| `slug`      | string | 是   | 文档的 slug                           |
| `title`     | string | 否   | 文档标题，不修改则不传                        |
| `body`      | string | 否   | 文档正文，不修改则不传                        |
| `format`    | string | 否   | body 格式：`markdown`（默认）或 `lake`     |
| `public`    | string | 否   | 公开性：`0` 私密、`1` 公开、`2` 企业内公开，不修改则不传 |


---

## 四、工具类

### `skylark_resolve_url`

解析语雀 URL，返回对应资源的类型和 ID（`book_id` 或 `doc_id`），可用于其他工具的调用。


| 参数    | 类型     | 必填  | 说明                                       |
| ----- | ------ | --- | ---------------------------------------- |
| `url` | string | 是   | 语雀 URL，例如 `https://yuque.antfin.com/...` |


---

### `skylark_search`

根据关键词搜索用户有权限的语雀文档。


| 参数         | 类型      | 必填  | 说明                                             |
| ---------- | ------- | --- | ---------------------------------------------- |
| `q`        | string  | 是   | 搜索关键词                                          |
| `scope`    | string  | 否   | 搜索范围，不填默认搜索当前用户/团队；填知识库的 namespace 则搜索该知识库下的文档 |
| `pageNo`   | integer | 否   | 页码，默认 1                                        |
| `pageSize` | integer | 否   | 单次返回数量，默认 20，最大 20                             |


