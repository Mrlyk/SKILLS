# 可视化组件清单

模板 `assets/template.html` 内置 12 类组件（9 类核心可视化 + 浏览器 mockup 控件族 + 数据模型四段式 + 待确认事项 section）。SKILL.md 的 A.4 节有「何时用哪个」的决策表，这里是图形选型原则 + 每个组件的完整 HTML 代码、CSS 类名约定、注意事项。

复制组件时连同周边 CSS 一起带走（模板里 CSS 都在 `:root` 之后、`/* COMPONENT */` 注释下）。

## 目录

- [图形选型原则](#图形选型原则)（SVG vs HTML vs mermaid，新增图前必读）
- [a. Metric Cards · 指标卡](#a-metric-cards)
- [b. Comparison Grid · 方案对比卡](#b-comparison-grid)
- [c. Architecture SVG · 分层架构图](#c-architecture-svg)
- [d. Flow SVG + Story Walkthrough · 联动一对](#d-flow-svg--story-walkthrough)
- [e. State Machine SVG · 状态机图](#e-state-machine-svg)
- [f. Mermaid · 时序 / ER 兜底](#f-mermaid)
- [g. Risk Matrix · 2×2 风险矩阵（SVG）](#g-risk-matrix)
- [h. Timeline · 甘特里程碑（SVG）](#h-timeline)
- [i. Details · 折叠长内容](#i-details)
- [j. Browser Mockup + demo-ui 控件族 · B 端 UI 演示](#j-browser-mockup--demo-ui-控件族)
- [k. 数据模型四段式 · 数据域 / ER / 表设计 / 隔离](#k-数据模型四段式)
- [l. 待确认事项 section · open questions 集中表](#l-待确认事项-section)

## 图形选型原则

技术方案里"图"和"内容"用不同载体表达，搭错了一定难看。SKILL.md A.4 有口诀，这里展开。

### 三类载体的强项

| 载体 | 强项 | 弱项 |
|---|---|---|
| **SVG** | 坐标精度（任意像素定位）、不规则形状 / 曲线 / 渐变、节点级交互（hover / click）、动画 | 文字处理弱（断行 / 复制 / 选中 / 多行排版） |
| **HTML + CSS** | 文字内容 / 复制 / 断行 / 排版、原生组件（`<details>` / `<a>` / `<form>`）、响应式 grid / flex | 几何精度差（位置只能靠 grid cell 或 absolute）、跨形状连线做不到 |
| **mermaid** | 时序 / ER / 类图等标准化，DSL 一行画一关系 | 自定义视觉受限（颜色 / 字体 / 形状只能用主题变量改） |

### 按需求选

| 需求性质 | 用什么 | 例子 |
|---|---|---|
| **位置即数据**（坐标、距离、面积承载信息） | SVG | 风险矩阵的 dot 位置（概率 × 影响）、甘特任务条的长度和起止 |
| **节点 + 连线 + 关系图** | SVG | 分层架构、流程图、状态机、调用链 |
| **mockup / 简化 UI 模拟** | SVG | Story Walkthrough phone mockup |
| **文字 + 数字 + 卡片排版** | HTML + CSS | metric cards、compare cards、kv 表 |
| **可复制 / 可选中的代码 / 字段定义** | HTML（`<pre>` / `<code>` / `<table>`） | 错误码表、接口签名、字段定义 |
| **可折叠 / 可展开的辅助内容** | HTML `<details>` | 完整错误码、长配置 |
| **跨服务时序图、数据表关系** | mermaid | sequenceDiagram、erDiagram |

### 反模式（别这么干）

- ❌ **Risk Matrix 用 CSS grid 拼 9 个 cell + dot 居中**
  - 问题：dot 只能落在 cell 中心，3×3 网格丢精度（概率 0.7 / 影响 0.8 和概率 0.55 / 影响 0.65 视觉无区分）；纵轴标签靠 `writing-mode: vertical-rl + transform: rotate(180deg)` 凑合，跨浏览器渲染差异
  - ✓ 正确：SVG 画轴 + dot 按真实 `data-x` / `data-y` (0-1 浮点) 定位 + 渐变警戒区，碰撞避让靠 JS（见 g 节）
- ❌ **甘特图用 CSS bar 带 `--start/--end` 百分比**
  - 问题：任务条能画但 today 竖线要 absolute + calc 凑、milestone 菱形要 CSS 三角形 hack、进度填充要嵌套定位、跨行依赖箭头 CSS 完全做不到
  - ✓ 正确：每行 track 是 SVG，里面画 bar / milestone polygon / progress；today 线作为整个 timeline 的 absolute overlay（见 h 节）
- ❌ **架构图 / 流程图用 HTML 嵌套 div + border 画框**
  - 问题：连线没法画、形状受限（只能矩形 / 圆角）、hover 高亮 ripple 难做
  - ✓ 正确：SVG 节点 + path 连线（见 c / d 节）
- ❌ **metric 卡用 SVG 画**
  - 问题：文字不能复制、断行硬编码、字号 / 字体维护成本高
  - ✓ 正确：HTML + CSS 排版 metric label / value / unit / bar（见 a 节）
- ❌ **mermaid 画自定义品牌风格架构图**
  - 问题：mermaid 主题变量有限，复杂自定义视觉做不到
  - ✓ 正确：手写 SVG，按设计系统的颜色 / 字体调

### 选型决策树

新加一个图表前，问三个问题：

1. **位置 / 几何关系是否承载语义？**（dot 在哪里 = 风险等级；bar 长短 = 任务时长）
   - 是 → **SVG**
   - 否 → 问 2
2. **主要内容是文字 + 列表 + 卡片排版？**
   - 是 → **HTML + CSS**
   - 否 → 问 3
3. **是标准的时序图 / ER 图 / 类图？**
   - 是 → **mermaid**
   - 否 → 默认 **SVG**（写一个新自定义图）

---

## a. Metric Cards

**何时用**：业务目标、性能指标、任何需要突出数字的地方。

**为什么**：大数字 + 单位 + 目标 + 进度条，一眼看到现状和差距，比 bullet 高效一个数量级。

```html
<div class="metrics">
  <div class="metric">
    <span class="metric-label">处理时长</span>
    <span class="metric-value">3.2<span class="metric-unit">h</span></span>
    <span class="metric-delta down"><strong>→ 15 min</strong> 目标</span>
    <div class="metric-bar"><div class="metric-bar-fill" style="width: 8%; background: var(--good)"></div></div>
  </div>
</div>
```

`metric-delta` 可加 `up` / `down` 类控制颜色；`metric-bar-fill` 的 `width` 用百分比，颜色用 CSS 变量。

## b. Comparison Grid

**何时用**：技术选型、方案 PK、做了二选一 / 三选一时。

**为什么**：每个方案有独立卡片，优 / 缺点用 `+` / `−` 列出，评分用 `●○` 点数，推荐方案加 `is-pick` 类显示「采用」角标。比 4 列表格的视觉冲击力强很多。

```html
<div class="compare">
  <div class="compare-card is-pick">
    <h4>方案 A · 父子退款单</h4>
    <span class="compare-tag">Refund Svc 内部拆单</span>
    <ul class="compare-list pros"><li>下游对账零改造</li></ul>
    <ul class="compare-list cons"><li>多笔串行调用</li></ul>
    <div class="compare-score">
      <div><span>开发成本</span><span class="dots">●●○</span></div>
    </div>
  </div>
</div>
```

未定结论时所有卡片都不加 `is-pick`，让评审决定。

## c. Architecture SVG

**何时用**：系统分层、模块拓扑、有清晰上下层关系时。

**为什么**：hover 单层会高亮、其他层淡化；hover 单节点显示 tooltip。视觉清晰、可交互。

模板里是「Clients → Gateway → Services → Storage」四层，每层 `<g class="layer-group">` 内含若干 `<g class="node-group" data-detail="...">`。改节点名 / 数量 / 分层即可。

层数建议 ≤ 4 层。每层节点数建议 ≤ 5 个。超过这个规模考虑拆图。

## d. Flow SVG + Story Walkthrough

**模板里这两个组件是配对使用的**——上方是全景流程图（一眼看清整体路径 + 分支判断），下方是 Story Walkthrough（步骤 ↔ 界面 mockup ↔ 后端 meta 的三联动走查）。点击流程图节点会让下方 Story 跳到对应步骤；Story 切换步骤时，流程图当前节点会高亮 + 微脉冲。

### 何时只用 Flow SVG（不开 Story）

流程本身简单（≤ 4 步）、没有界面交互、没有需要展开说明的步骤细节。比如：MQ 消息处理流程、定时任务执行链路、批处理调度顺序。

### 何时配 Story 走查

流程涉及用户交互、或每一步都有值得展开的「用户看到什么 + 后端做什么 + 校验什么」。比如：用户操作流、跨多个服务的业务流程、有审批 / 状态变化的工作流。

### 联动机制

两个组件通过 `data-step="N"` 关联——流程图节点的 `data-step` 数字必须和 Story 里的 `.story-step` / `.story-screen` / `.story-card` 的 `data-step` 一致。判断节点（菱形）不带 `data-step`，因为它是分支条件不是步骤。

### Story 走查的两种变体

#### (d.1) 客户端变体

模板里的默认样式：左侧是 phone / browser mockup（SVG 画的简化 UI），适合有界面的需求——前端改造、APP 新功能、用户操作流。

#### (d.2) 服务端变体（无 UI 场景）

把 `.story-mockup` 里的 phone SVG 替换成下面三种之一：

- **调用链时序图**：左侧画 vertical timeline，每一行是一个服务（用户 / Gateway / Service / DB / MQ），当前步骤对应的调用箭头加 `is-active` 类高亮
- **数据流图**：左侧画"数据从哪里来 → 经过哪些处理 → 落到哪里"的 SVG，当前步骤对应的链路段高亮
- **状态前后对比卡**：左侧上下两张卡，「操作前」和「操作后」的关键字段值对比，当前步骤决定对比的内容

服务端变体示例骨架：

```html
<div class="story-mockup">
  <svg viewBox="0 0 240 480">
    <!-- 4 个服务节点纵向排列，当前 step 对应的箭头 stroke-width 加粗 -->
    <text x="20" y="40">Client</text>
    <text x="20" y="120">Gateway</text>
    <text x="20" y="200">Order Svc</text>
    <text x="20" y="280">Redis</text>
    <g class="call-arrow" data-step="1">
      <path d="..." stroke="..." />
      <text>GET /order/123</text>
    </g>
    <g class="call-arrow" data-step="2">...</g>
  </svg>
</div>
```

关键：每个调用链片段都加 `data-step="N"`，CSS 写 `.call-arrow[data-step]:not(.is-current) { opacity: 0.3; }`，然后让 Story 的 render 函数在切 step 时给对应的 `.call-arrow` 加 `is-current` 类（参考模板 JS 里 `flow-master` 节点联动的写法）。

### 纯运营 / 数据需求

如果连"服务调用"都没有（比如「批量推送补偿」「数据修复脚本」），用一个 Flow SVG + 旁边的 callout 列「输入 / 输出 / 副作用」就够了，不用上 Story。

### Flow SVG 基础语法

节点用 `<g class="flow-node [start|end|decision]" data-step="N" data-detail="...">`，箭头用 `<path class="flow-arrow" marker-end="url(#arrow-flow)">`。

## e. State Machine SVG

**何时用**：订单 / 退款 / 工单 / 工作流状态流转。

**为什么**：圆形状态 + 弧形 transition + 终态深色填充，能直观看到所有路径和终点。

状态用 `<g class="state-node [terminal]">`，transition 用 `<path class="state-trans">` + `<text class="state-trans-label">`。

终态加 `terminal` 类（深色填充表示流程结束）。

## f. Mermaid

**何时用**：sequenceDiagram 时序图、erDiagram 数据表关系，这些 mermaid 表达力比手写 SVG 高。

**注意**：能用 a-e 内置组件的，优先用内置；mermaid 是兜底。

```html
<pre class="mermaid">
sequenceDiagram
  U->>W: 点击
  W->>B: 调用
</pre>
```

mermaid 写中文节点没问题，但节点 ID 用英文（某些版本中文 ID 渲染会出问题）。模板已经引入 mermaid CDN。

## g. Risk Matrix（SVG）

**何时用**：风险章节，风险数 ≥ 3 个时。

**为什么用 SVG 而不是 CSS grid**：风险 dot 的位置承载语义（横轴 = 概率，纵轴 = 影响），评审会按 dot 在矩阵的位置判断优先级。CSS grid 只能把 dot 居中在 9 个 cell 之一，丢失了概率 / 影响的连续精度。SVG 用 `data-x` / `data-y` (0-1 浮点) 真实坐标定位 dot，碰撞避让靠 JS。

**HTML 用法**：

```html
<div class="diagram" data-label="Risk Matrix · 风险二维评估">
  <svg class="risk-matrix-svg" viewBox="0 0 560 360" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="riskGrad" x1="0%" y1="100%" x2="100%" y2="0%">
        <stop offset="0%"   stop-color="#6a9b6c" stop-opacity="0.18"/>
        <stop offset="50%"  stop-color="#c9a96e" stop-opacity="0.18"/>
        <stop offset="100%" stop-color="#b8553c" stop-opacity="0.22"/>
      </linearGradient>
    </defs>

    <!-- 警戒区域（左下绿 → 右上红 渐变） -->
    <rect x="80" y="20" width="460" height="280" fill="url(#riskGrad)" stroke="var(--rule)"/>

    <!-- 3×3 网格线（虚线） -->
    <line x1="80"  y1="113" x2="540" y2="113" class="risk-gridline"/>
    <line x1="80"  y1="207" x2="540" y2="207" class="risk-gridline"/>
    <line x1="233" y1="20"  x2="233" y2="300" class="risk-gridline"/>
    <line x1="386" y1="20"  x2="386" y2="300" class="risk-gridline"/>

    <!-- 坐标轴 + 刻度 -->
    <line x1="80" y1="20" x2="80" y2="300" class="risk-axis"/>
    <line x1="80" y1="300" x2="540" y2="300" class="risk-axis"/>
    <text x="40" y="160" text-anchor="middle" transform="rotate(-90 40 160)" class="risk-axis-label">影响 ▲</text>
    <text x="310" y="340" text-anchor="middle" class="risk-axis-label">概率 ▶</text>
    <text x="70" y="300" text-anchor="end" class="risk-axis-tick">低</text>
    <text x="70" y="160" text-anchor="end" class="risk-axis-tick">中</text>
    <text x="70" y="30"  text-anchor="end" class="risk-axis-tick">高</text>
    <text x="156" y="318" text-anchor="middle" class="risk-axis-tick">低</text>
    <text x="310" y="318" text-anchor="middle" class="risk-axis-tick">中</text>
    <text x="463" y="318" text-anchor="middle" class="risk-axis-tick">高</text>

    <!-- dots: data-x / data-y 是 0-1 浮点数，JS 自动转 cx/cy 坐标 -->
    <g class="risk-dot" data-x="0.78" data-y="0.85" data-sev="high"   data-detail="对账系统未及时联动 schema 变更"><circle r="14"/><text>1</text></g>
    <g class="risk-dot" data-x="0.55" data-y="0.55" data-sev="medium" data-detail="多笔串行调用耗时长"><circle r="14"/><text>2</text></g>
    <g class="risk-dot" data-x="0.50" data-y="0.28" data-sev="low"    data-detail="多文案版本不一致"><circle r="14"/><text>3</text></g>
  </svg>
  <div class="diagram-legend">
    <span><span class="swatch" style="background:#b8553c"></span>高严重度</span>
    <span><span class="swatch" style="background:#c9a96e"></span>中严重度</span>
    <span><span class="swatch" style="background:#6a9b6c"></span>低严重度</span>
    <span>渐变 = 风险区域（右上更危险）</span>
  </div>
</div>
```

**关键约定**：

- `data-x`：风险**概率** 0-1（0 = 几乎不会发生，1 = 一定发生），粒度 0.2 / 0.5 / 0.8 即可，不必很精确
- `data-y`：风险**影响** 0-1（0 = 无关紧要，1 = 致命）
- `data-sev`：`low` / `medium` / `high` 控制 dot 颜色（绿/黄/红）—— 通常和位置相关（右上多是 high）
- dot 里的 `<text>` 是编号（1, 2, 3...），对应下方风险表格的行号
- `data-detail` 提供 hover tooltip
- circle 的 `cx` / `cy` 不用手写，JS 在 DOM ready 时按公式 `cx = 80 + 460 * dataX; cy = 300 - 280 * dataY` 自动算
- 两个 dot 距离 < 28px 时 JS 自动避让

**搭配下方表格**（dot 编号 = 表格行号）：

```html
<table>
  <thead><tr><th>#</th><th>风险</th><th>概率</th><th>影响</th><th>缓解方案</th></tr></thead>
  <tbody>
    <tr><td>1</td><td>对账系统未及时联动</td><td>高</td><td>高</td><td>预先与对账方同步 schema，灰度时双跑</td></tr>
    <tr><td>2</td><td>多笔串行调用超时</td><td>中</td><td>中</td><td>子单上限 N=10，超出走异步</td></tr>
    <tr><td>3</td><td>多文案版本不一致</td><td>中</td><td>低</td><td>退款页统一渲染，文案沉淀到字典</td></tr>
  </tbody>
</table>
```

## h. Timeline · 甘特里程碑（SVG）

**何时用**：产研计划的里程碑章节，固定替换里程碑表格。

**为什么用 SVG 而不是 CSS bar**：CSS bar 能画任务条，但画不出 today 竖线（要 absolute + calc 凑）、milestone 菱形（CSS 三角形 hack）、任务进度填充（嵌套定位别扭）。SVG 一次全做了，还能扩展依赖箭头 / 关键路径（见下方"可选扩展"）。

**HTML 用法**：

```html
<div class="timeline" style="--cols: 4; --today: 62%">
  <div class="timeline-axis">
    <span>06 月 W1</span><span>06 月 W2</span><span>06 月 W3</span><span>06 月 W4</span>
  </div>
  <div class="timeline-rows">
    <div class="timeline-row">
      <span class="timeline-task">方案评审</span>
      <svg class="timeline-track" viewBox="0 0 1000 30" preserveAspectRatio="none">
        <rect class="timeline-bar is-review" x="0" y="6" width="80" height="18" rx="2"/>
        <text class="timeline-bar-text" x="8" y="20">2d</text>
      </svg>
    </div>
    <div class="timeline-row">
      <span class="timeline-task">后端开发</span>
      <svg class="timeline-track" viewBox="0 0 1000 30" preserveAspectRatio="none">
        <rect class="timeline-bar" x="100" y="6" width="500" height="18" rx="2"/>
        <rect class="timeline-bar-progress" x="100" y="6" width="180" height="18" rx="2"/>
        <text class="timeline-bar-text" x="108" y="20">10d · 36%</text>
      </svg>
    </div>
    <div class="timeline-row">
      <span class="timeline-task">⬥ 灰度上线</span>
      <svg class="timeline-track" viewBox="0 0 1000 30" preserveAspectRatio="none">
        <polygon class="timeline-milestone" points="850,15 866,5 882,15 866,25"/>
      </svg>
    </div>
  </div>
  <!-- today 竖线：跨所有 track 行的 absolute overlay -->
  <div class="timeline-today" aria-hidden="true"><span>今天</span></div>
</div>
```

**坐标约定**：

- track viewBox 是 `0 0 1000 30`，`preserveAspectRatio="none"` 让 SVG 撑满列宽
- 任务条 `x` / `width` 用 viewBox 单位（0-1000 直接等于 0%-100% 时间窗）。比如时间窗 W1-W4，任务 W1.5 开始 W3 结束就是 `x="125" width="375"`
- `is-review` / `is-test` / `is-milestone` / `is-launch` 类控制颜色
- 进度填充用 `.timeline-bar-progress` 嵌套，`width` 是已完成的 viewBox 单位（< 主 bar 的 width）
- milestone 用 polygon 菱形（4 个顶点：左 / 上 / 右 / 下）
- today 线通过 `--today` CSS 变量（百分比，相对 track 列宽）定位，模板用 absolute overlay 跨所有行画虚线 + 标签

**可选扩展（按需手写，不在默认模板里）**：

- **任务依赖箭头**（跨行连线）：在 `.timeline-rows` 上覆盖一个 absolute 的 SVG overlay，画 `path` 从 task A 的右端连到 task B 的左端，stroke-dasharray 表示软依赖
- **关键路径高亮**：依赖链上的所有任务统一加 `is-critical` 类（红色描边 + 加粗）
- **任务详情卡 hover**：点 / hover 任务条弹出 detail card（成员、依赖、产出物）

这三个不在主模板里，因为不是每个方案都需要；如果方案有 10+ 任务、依赖复杂的关键路径甘特，再按需扩展。

## i. Details

**何时用**：完整错误码、字段定义、长配置示例、可选阅读的辅助信息。

**为什么**：折叠后主线干净，需要的人点开看；summary 里的 `.count` 标明内含多少项。

```html
<details class="fold">
  <summary>错误码完整列表 <span class="count">12 项</span></summary>
  <div class="fold-body">...</div>
</details>
```

> 30 行的代码块、字段定义表格超过 8 行、错误码列表超过 5 项，建议都用 `<details class="fold">` 折叠。

## j. Browser Mockup + demo-ui 控件族

**何时用**：B 端 / 后台 / 中台系统方案要演示"用户这一步看到的 UI 界面"。手机端用 Story Walkthrough 的 `.story-mockup`；PC 端用本组件。

**为什么不写截图 / 用 Figma 链接**：截图过时快、改一处要替全部图；评审同事打开方案就能看到界面。本组件用 HTML + CSS 模拟桌面浏览器壳 + 表单 / 列表 / tabs / 按钮，文字可复制、可在评审会上实时改。

### 浏览器壳 + 单页 demo

```html
<div class="browser-mockup">
  <div class="bm-bar">
    <span class="bm-title">https://rfp.example.com/project/123/quote</span>
  </div>
  <div class="bm-body">
    <h4 style="margin:0 0 4px">报价评标 · 第 2 轮</h4>
    <p class="speak" style="margin:0 0 14px">勾选要采纳的报价，提交后系统生成中标版本。</p>

    <!-- tabs 切换 -->
    <div class="demo-ui-tabs">
      <div class="demo-ui-tab active">待评标 (12)</div>
      <div class="demo-ui-tab">已淘汰 (3)</div>
      <div class="demo-ui-tab">已中标 (1)</div>
    </div>

    <!-- 步骤进度 -->
    <div class="demo-ui-progress">
      <span class="is-done"></span>
      <span class="is-done"></span>
      <span class="is-active"></span>
      <span></span>
    </div>

    <!-- 列表行 -->
    <div class="demo-ui-row">
      <div class="col">浦东希尔顿</div>
      <div class="col col-muted">高级大床房</div>
      <div class="col col-num">¥ 680</div>
      <div class="col"><span class="demo-ui-tag ok">最低价</span></div>
      <div class="col"><button class="demo-ui-btn is-primary">采纳</button></div>
    </div>
    <div class="demo-ui-row">
      <div class="col">外滩华尔道夫</div>
      <div class="col col-muted">高级大床房</div>
      <div class="col col-num">¥ 920</div>
      <div class="col"><span class="demo-ui-tag warn">高于均价</span></div>
      <div class="col"><button class="demo-ui-btn">采纳</button></div>
    </div>

    <!-- 表单字段示例 -->
    <div class="demo-ui-field">
      <span class="demo-ui-field-label">议价话术</span>
      <input class="demo-ui-field-input" value="希望可以降到 ¥ 850 以内" />
    </div>

    <!-- 操作按钮组 -->
    <div style="display:flex; gap:8px; justify-content:flex-end; margin-top:14px">
      <button class="demo-ui-btn">取消</button>
      <button class="demo-ui-btn is-primary">提交定标</button>
    </div>
  </div>
</div>
```

### 控件清单

| 类 | 用途 | 变体 |
|---|---|---|
| `.browser-mockup` | 桌面浏览器壳（圆点 + 地址栏 + 内容区） | — |
| `.bm-bar` / `.bm-title` | 地址栏 + URL | — |
| `.bm-body` | 内容区（padding 16/18） | — |
| `.demo-ui-tabs` / `.demo-ui-tab` | 横向 tab 切换 | `.active` |
| `.demo-ui-row` | 表格 / 列表行（flex 多列） | 子列 `.col` `.col-muted` `.col-num` |
| `.demo-ui-field` | 表单字段（label + input） | — |
| `.demo-ui-btn` | 按钮 | `.is-primary` `.is-danger` |
| `.demo-ui-tag` | inline 状态标签（业务态） | `.ok` `.warn` `.info` |
| `.demo-ui-progress` | 步骤进度条 | 子 `<span>` 加 `.is-done` `.is-active` |

### 与 Story Walkthrough 的边界

- **`.story-mockup`（手机壳 + 状态栏）**：C 端 / 移动端用户场景，配 Flow SVG 三联动。
- **`.browser-mockup`（桌面壳 + 地址栏）**：B 端 / 后台 / 中台，一般独立用，不必联动 Flow，因为 B 端流程更碎。

如果 B 端也想跑 Flow + browser-mockup 联动（三联动结构），可以照搬 `.story` 的步骤切换 JS，把 `.story-mockup` 容器替换成 `.browser-mockup`。

### 反模式

- 不要用 `.browser-mockup` 装大段文字段落——这等于把它当一个加了边框的 div 用，浪费了 mockup 的"还原 UI"语义。文字段落放外面。
- 不要在一个 mockup 里塞 > 30 行交互（完整表单 + 10 行表格 + 5 个 tab）——拆成两个 mockup，分别演示"前 / 后"状态。

## k. 数据模型四段式

**何时用**：方案涉及独立数据存储（自建 DB / 数据域 / 表结构变更）时必备。无独立存储的纯流程方案可省略。

**为什么四段而不是直接贴建表 SQL**：评审同事的关注点不在 SQL 语法。**数据域** 让人看清"模型边界"，**ER 关系** 让人看清"基数与外键"，**表设计** 让人看清"字段与索引"，**多租户隔离** 让人看清"安全边界"。少任何一段都会被追问。

### 四段式标准结构

```html
<section id="data-model">
  <h3 id="data-model">3.4 数据模型</h3>
  <p>本节涵盖：数据域 / 实体清单、核心实体关系、表字段与索引、多企业隔离。</p>

  <!-- 段 1: 数据域 + 实体清单 -->
  <h4 id="data-domain">3.4.1 数据域 + 实体清单</h4>
  <table>
    <thead><tr><th>数据域</th><th>实体</th><th>一句话职责</th></tr></thead>
    <tbody>
      <tr><td rowspan="3">项目</td><td><code>rfp_project</code></td><td>RFP 项目主表</td></tr>
      <tr><td><code>city_plan</code></td><td>城市维度计划</td></tr>
      <tr><td><code>invitation</code></td><td>对单酒店发出的邀请</td></tr>
      <tr><td rowspan="2">报价</td><td><code>quote</code></td><td>多轮报价头表（含 round / version）</td></tr>
      <tr><td><code>room_rate</code></td><td>报价房型行表</td></tr>
    </tbody>
  </table>

  <!-- 段 2: 核心实体关系（推荐 mermaid erDiagram，关系一目了然） -->
  <h4 id="data-er">3.4.2 核心实体关系（PK / FK 视图）</h4>
  <pre class="mermaid">
erDiagram
    RFP_PROJECT ||--o{ CITY_PLAN : "1:N · 城市计划"
    RFP_PROJECT ||--o{ INVITATION : "1:N · 邀请"
    INVITATION ||--o{ QUOTE : "1:N · 多轮报价"
    QUOTE ||--o{ ROOM_RATE : "1:N · 房型行"
    QUOTE ||--o| AWARD : "1:0..1 · 中标"
    AWARD ||--|| CONTRACT : "1:1 · 合同"
    CONTRACT ||--o{ CONTRACT_RATE : "1:N · 生效价版本"
  </pre>
  <p class="speak">关键基数：1 项目 → N 邀请 → N 报价；1 报价 → 0..1 中标；中标 1:1 合同；合同 1:N 价格版本。</p>

  <!-- 段 3: 表设计 -->
  <h4 id="data-schema">3.4.3 表设计 · 字段与索引</h4>
  <p>核心字段在主线展示，全字段 / 完整索引 / 约束在 <code>&lt;details class="fold"&gt;</code> 折叠。</p>

  <h5><code>rfp_project</code> · RFP 项目主表</h5>
  <table>
    <thead><tr><th>字段</th><th>类型</th><th>说明</th></tr></thead>
    <tbody>
      <tr><td><code>id</code></td><td>bigint</td><td>PK</td></tr>
      <tr><td><code>corp_id</code></td><td>bigint</td><td>所属企业，所有查询必带</td></tr>
      <tr><td><code>name</code></td><td>varchar(256)</td><td>项目名</td></tr>
      <tr><td><code>status</code></td><td>varchar(32)</td><td>DRAFT / IN_PROGRESS / COMPLETED</td></tr>
      <tr><td><code>deadline</code></td><td>datetime</td><td>报价截止时间</td></tr>
    </tbody>
  </table>
  <details class="fold">
    <summary>完整字段 + 索引 + 约束 <span class="count">18 项</span></summary>
    <div class="fold-body">
      <!-- 完整 CREATE TABLE 或字段列表 -->
    </div>
  </details>

  <!-- 段 4: 多租户 / 多企业隔离 -->
  <h4 id="data-isolation">3.4.4 多企业数据隔离</h4>
  <p>所有自建业务表均以 <code>corp_id</code> 为分区键。MyBatis 拦截器在 SQL 执行前统一注入 <code>corp_id = ?</code> 条件，业务代码无法绕过；<code>corp_id</code> 仅从登录态 ThreadLocal 取。</p>
  <p>测试覆盖：构造 A 企业用户访问 B 企业数据的越权用例，所有读写接口必须拒绝。</p>
</section>
```

### 段落选择规则

- **无独立存储**（纯流程编排 / 仅修改已有表 1-2 个字段）：省略整节，在"详细设计"里直接讲改了哪个字段。
- **有独立存储但只 1-2 张表**：段 1 + 段 3，省段 2 段 4。
- **多表 / 涉及关系**：四段全要。
- **多租户 SaaS**：段 4 必须，且作为安全设计独立节叙述。

### 反模式

- **直接贴 SQL 不画 ER**：评审同事读不出 1:N 还是 N:N。先 ER 图，再 SQL。
- **ER 图画了所有字段**：ER 只画实体 + 关系，字段细节是表设计的事。
- **表设计每个字段都写一段说明**：用三列表（字段 / 类型 / 说明），一行一字段。复杂约束放 details fold。
- **`corp_id` 在表设计的 details fold 里**：隔离方案是**安全设计**，必须在主线，不能折叠。

## l. 待确认事项 section

**何时用**：方案体量 > 1000 字、有 ≥ 3 处未定项（产品 / 外部依赖 / 基础设施 / 技术选型 任一类）时必备。短方案 / 无未定项可省略。

**为什么集中表而不是散落 `<p class="todo">`**：长方案评审完，每位 owner 关心的只是"我负责哪几项 + 什么时候要"。散在正文里找不到，按类别 + owner 排好就一目了然。

### 标准结构

放在「03 · Solution」之后、「05 · Risks」之前（作为 `04 · Open`）。

```html
<section id="open-questions">
  <h2><span class="num">04 · Open</span>待确认事项</h2>
  <p class="speak">正文以 <code>&lt;p class="todo"&gt;</code> 或 <code>&lt;span class="todo-tag"&gt;</code> 标注的开放问题汇总于此，按类别分组便于按 owner 分头推进。</p>
  <table>
    <thead><tr><th style="width:48px">#</th><th style="width:140px">类别</th><th>事项</th><th style="width:110px">责任人</th><th style="width:120px">预期完成时间</th></tr></thead>
    <tbody>
      <tr><td>1</td><td>产品 · M6</td><td>智能需求洞察模块的产品形态、推荐算法、与 M1 创建向导集成方式</td><td></td><td></td></tr>
      <tr><td>2</td><td>产品 · 调价</td><td>调价审批方案：状态机 / 审批级数 / 上下调差异化路径（详见 <a href="#state-machine">3.4.2</a>）</td><td></td><td></td></tr>
      <tr><td>3</td><td>外部依赖</td><td>飞猪 C 端价格（PriceBaseline）是否接入 + 对接方式</td><td></td><td></td></tr>
      <tr><td>4</td><td>基础设施 · 中间件</td><td>Redis / Diamond / MetaQ / SchedulerX 实例申请 + 配额 + 三套环境隔离</td><td></td><td></td></tr>
      <tr><td>5</td><td>产研 · 计划</td><td>7.1 角色补全 + 7.2 里程碑日期细化（待 #1-#4 落定后）</td><td></td><td></td></tr>
    </tbody>
  </table>
</section>
```

### 类别建议

按 owner 维度分类，常见的有：

- **产品 · {模块名}**：产品形态 / 业务规则 / 状态机分支 待产品确认
- **外部依赖**：上下游对接形式 / SLA / 限流配额 待外部团队对齐
- **基础设施 · {中间件 / 存储 / 网关}**：资源申请 / 命名 / 配额 / 监控告警 待运维确认
- **技术选型 · {模块名}**：选型未定 / 性能阈值 / 库版本 待技术对齐
- **产研 · 流程**：角色补全 / 里程碑细化 / 灰度策略 等 PMO 类事项

### 与正文 inline TODO 的协作

- 正文里就地标 `<span class="todo-tag">TODO</span>`（标在 h4 / 表格行）或 `<p class="todo">`（段落级），让读者读到上下文时立刻看到未定项。
- 同时**汇总进本表**，配上 `<a href="#xxx">` 链回正文具体位置。

### 反模式

- **只起表不在正文标**：评审在读到具体场景时不知道这里有未定项。
- **只在正文标不汇总**：长方案 owner 找不全自己的 TODO。
- **责任人和预期完成时间字段空着不维护**：表退化成"已知问题列表"，失去推进价值。每次评审都要逼出 owner + 时间。
