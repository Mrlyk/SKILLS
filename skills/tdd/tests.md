# 好测试与坏测试

## 好测试

**集成风格**：通过真实接口测试，不 mock 内部模块。

```typescript
// 好：测试可观测行为
test("有效购物车_结账_返回已确认状态", async () => {
  const cart = createCart();
  cart.add(product);
  const result = await checkout(cart, paymentMethod);
  expect(result.status).toBe("confirmed");
});
```

特征：
- 测试调用方关心的行为
- 只使用公共 API
- 内部重构后测试仍然通过
- 描述"做什么"，不描述"怎么做"
- 每个测试只有一个逻辑断言

```typescript
// 好：通过接口验证（不绕过接口查数据库）
test("createUser_创建用户_用户可被检索", async () => {
  const user = await createUser({ name: "Alice" });
  const retrieved = await getUser(user.id);
  expect(retrieved.name).toBe("Alice");
});
```

## 坏测试

**实现细节测试**：与内部结构耦合。

```typescript
// 坏：测试实现细节
test("结账调用 paymentService.process", async () => {
  const mockPayment = jest.mock(paymentService);
  await checkout(cart, payment);
  expect(mockPayment.process).toHaveBeenCalledWith(cart.total);
});
```

红旗信号：
- Mock 内部协作者
- 测试私有方法
- 断言调用次数/顺序
- 重构后测试失败但行为未变
- 测试名称描述"怎么做"而非"做什么"
- 绕过接口直接查询数据库/外部存储

```typescript
// 坏：绕过接口验证
test("createUser 保存到数据库", async () => {
  await createUser({ name: "Alice" });
  const row = await db.query("SELECT * FROM users WHERE name = ?", ["Alice"]);
  expect(row).toBeDefined();
});
```

## 最小粒度判断标准

一个测试是否足够小，标准是：

1. **单一原因失败**：测试只因一种行为变化而失败
2. **名称即规格**：测试名称完整描述了被测场景，不需要读代码才能理解
3. **无隐式依赖**：不依赖测试执行顺序，可以单独运行
4. **断言精确**：只断言与当前行为相关的属性，不断言无关字段
