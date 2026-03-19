# Mock 使用规范

## 只在系统边界处 Mock

允许 mock 的场景：
- 外部 API（支付、邮件、短信等）
- 数据库（优先使用测试数据库，mock 作为次选）
- 时间 / 随机数
- 文件系统（视情况）

不应 mock 的场景：
- 自己编写的类/模块
- 内部协作者
- 任何受自己控制的代码

## 为可 Mock 性设计接口

### 使用依赖注入

将外部依赖作为参数传入，而非在内部创建：

```typescript
// 易于 mock
function processPayment(order, paymentClient) {
  return paymentClient.charge(order.total);
}

// 难以 mock
function processPayment(order) {
  const client = new StripeClient(process.env.STRIPE_KEY);
  return client.charge(order.total);
}
```

### 使用 SDK 风格接口，而非通用 fetcher

为每个外部操作创建独立函数，而非一个带条件逻辑的通用函数：

```typescript
// 好：每个函数可独立 mock
const api = {
  getUser: (id) => fetch(`/users/${id}`),
  getOrders: (userId) => fetch(`/users/${userId}/orders`),
  createOrder: (data) => fetch('/orders', { method: 'POST', body: data }),
};

// 坏：mock 内部需要条件逻辑
const api = {
  fetch: (endpoint, options) => fetch(endpoint, options),
};
```

SDK 风格的优势：
- 每个 mock 只返回一种特定形状的数据
- 测试 setup 中无需条件逻辑
- 清晰可见每个测试使用了哪些接口
- 每个接口有独立的类型安全保障
