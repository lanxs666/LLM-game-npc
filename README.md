# LLM-Game-NPC
基于本地大语言模型（Ollama + Qwen2.5）的带记忆游戏 NPC 演示项目。

## 项目功能
- 基于自然语言与 NPC 进行对话。
- 实现了多轮对话上下文记忆机制（Long-term Memory），NPC 可记住玩家之前的发言。
- 通过 Prompt Engineering 构建了 NPC 的特定人设（如暴躁铁匠）。
- 使用 Gradio 搭建了轻量级的 Web 测试界面。

## 运行环境要求
- Python 3.12+
- [Ollama](https://ollama.com/) 已安装并运行

## 快速开始
1. 安装依赖：
   pip install -r requirements.txt
2. 确保本地 Ollama 已启动，并拉取了模型：
   ollama run qwen2.5:3b
3. 运行终端版 NPC：
   python npc_chat.py
4. 运行网页版 NPC：
   python npc_web.py
