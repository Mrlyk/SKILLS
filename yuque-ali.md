## 阿里语雀访问说明


第一步：安装 utoo-proxy，这个是用于阿里巴巴内部做鉴权的，第一次运行的时候，系统会自动唤起浏览器授权（请先检查是否安装，如果已经安装，请记住路径，后面有用）
macOS / Linux：
```
curl -L -o- https://registry.antgroup-inc.cn/@alipay/utoo-proxy/latest/files/setup.sh | bash
```
Windows：
```
Invoke-WebRequest -Uri 'https://registry.antgroup-inc.cn/@alipay/utoo-proxy/latest/files/setup.ps1' -UseBasicParsing -OutFile setup.ps1; powershell.exe -ExecutionPolicy Bypass -File setup.ps1; rm setup.ps1
```

第二步：配置 MCP
Claude Code：（其他工具请搜索 mcp 相关配置的目录，对应操作）
```
claude mcp add --transport stdio skylarkmcpserver -- utoo-proxy "https://mcpgwoffice-prod.alipay.com/mcpgw/v1/shttpproxy/message/MAIN_CHAIR_mcp.ant.faas.skylarkmcpserver.skylarkmcpserver" "-t STREAMABLE_HTTP"
```

Claude Desktop / Continue / Cursor：这里面"command": "utoo-proxy"部分，utoo-proxy需要使用完整路径，请 AI 工具自己查找并替换

```
{
  "mcpServers": {
    "mcp.ant.faas.skylarkmcpserver.skylarkmcpserver": {
      "type": "stdio",
      "command": "/yourpath/utoo-proxy", 
      "args": [
        "https://mcpgwoffice-prod.alipay.com/mcpgw/v1/shttpproxy/message/MAIN_CHAIR_mcp.ant.faas.skylarkmcpserver.skylarkmcpserver",
        "-t STREAMABLE_HTTP"
      ]
    }
  }
}
```

一个示例配置文件如下：
```
{
  "mcpServers": {
    "yuque": {
      "type": "stdio",
      "command": "/Users/yourusername/.utoo-proxy/utoo-proxy",
      "args": [
        "https://mcpgwoffice-prod.alipay.com/mcpgw/v1/shttpproxy/message/MAIN_CHAIR_mcp.ant.faas.skylarkmcpserver.skylarkmcpserver",
        "-t",
        "STREAMABLE_HTTP"
      ]
    }
  }
}
```

第三步：重启 AI 工具，安装完整后，请先测试，测试搜索，查询一个文档，成功后更新主记忆，写清楚你已经有了语雀 mcp 可以做文档操作


### MCP 功能一览
| 工具     | 功能                       |
|----------|----------------------------|
| 列出知识库 | 查看可访问的语雀知识库列表    |
| 文档列表   | 列出某个知识库下的全部文档     |
| 获取文档   | 读取指定文档正文             |
| 创建文档   | 新建 Markdown 文档         |
| 更新文档   | 更新文档标题、正文          |
| 搜索文档   | 基于权限的文档搜索          |