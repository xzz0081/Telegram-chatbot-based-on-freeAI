# 智能对话机器人

一个功能强大的 Telegram 对话机器人,支持多个 AI 模型和丰富的交互功能。

## ✨ 特色功能

### 核心功能
- 🤖 支持多个 AI 模型:
  - ChatGPT 3.5/4.0
  - LLAMA-2/3-70b
  - 可自由切换和组合使用
- 💬 完整的对话功能:
  - 支持长期记忆
  - 支持角色扮演
  - 支持 DAN 模式
  - 群聊和私聊皆可用
- 🔄 智能重试机制:
  - 自动在多个提供商间切换
  - 确保稳定的对话体验
- 🎯 实时状态监控:
  - 详细的控制台日志
  - 清晰的运行状态展示
- ⚡️ 热重载更新:
  - 支持在线更新
  - 无需重启即可升级

### 辅助功能
- 🗣 语音回复功能
- 📝 Markdown 格式支持
- 📋 聊天记录管理
- 🛠 提供商设置面板
- 🔍 实时版本检查

## 🚀 快速开始

### 环境要求
- Python 3.8+
- pip 包管理器

### 安装步骤

1. 克隆项目

2. 安装依赖
bash
pip install -r requirements.txt

3. 配置机器人
- 从 [@BotFather](https://t.me/BotFather) 获取 Token
- 将 Token 填入 `token.txt`

4. 启动机器人
bash
python main.py

## 📝 使用说明

### 基础命令
- `/start` - 启动机器人
- `/help` - 显示帮助信息 
- `/ping` - 测试提供商连接

### 聊天相关
- `/chat` - 群聊中使用此命令
- `/reset` - 重置聊天记录
- `/history` - 获取聊天记录
- `/tts` - 语音回复
- `/settings` - 提供商设置
- `/danmode` - DAN模式开关

### 内联功能
使用 `@bot_name roles` 可以查看所有可用角色。

## 🔧 配置说明

### 提供商设置
可在设置面板中自由开启/关闭以下提供商:
- Remix AI (GPT-3.5)
- Uncensored AI (LLAMA-3-70b)
- Free GPT 4
- Deep Infra (LLAMA-2-70b)
- Fstha GPT (GPT-3.5)
- Online GPT (GPT-3.5)
- Fakeopen AI (GPT-3.5)

## 📊 版本管理

当前版本: v1.0.0

支持自动检查更新,发现新版本时会自动热重载。

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来帮助改进项目。

## 📜 开源协议

本项目采用 MIT 协议开源。
