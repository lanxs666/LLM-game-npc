import gradio as gr
import requests

system_prompt = "你是一个中世纪奇幻游戏里的铁匠NPC。你性格暴躁、说话简短、喜欢抱怨天气。你只回答玩家的问题，绝不承认自己是AI。"
memory = [{"role": "system", "content": system_prompt}]

# 初始的聊天记录显示
chat_display = "⚔️ 【铁匠】：又有啥事？（输入你想说的话）\n\n"

def chat(user_input, history_text):
    global memory, chat_display
    
    if not user_input:
        return history_text, ""
    
    # 1. 把玩家的话加入记忆和显示界面
    memory.append({"role": "user", "content": user_input})
    chat_display += f"🧑 【你】：{user_input}\n"
    
    # 2. 发送给本地大模型
    url = "http://127.0.0.1:11434/api/chat"
    payload = {"model": "qwen2.5:3b", "messages": memory, "stream": False}
    
    try:
        response = requests.post(url, json=payload)
        npc_reply = response.json()['message']['content']
        memory.append({"role": "assistant", "content": npc_reply})
        chat_display += f"⚔️ 【铁匠】：{npc_reply}\n\n"
    except Exception as e:
        chat_display += f"⚠️ 出错了：连接不上Ollama，请检查服务是否运行。\n\n"
        
    # 清空输入框，返回最新的聊天记录
    return chat_display, ""

# 极简界面，用一个多行文本框代替聊天框，绝对不报错
with gr.Blocks(title="LLM 游戏 NPC") as demo:
    gr.Markdown("## ⚔️ 铁匠铺 (极简稳定版)")
    # 使用 Textbox 作为聊天展示，lines=15 表示高度
    chat_box = gr.Textbox(value=chat_display, lines=15, label="聊天记录", interactive=False)
    msg = gr.Textbox(label="对铁匠说：", placeholder="在这里输入，按回车发送...")
    
    msg.submit(chat, [msg, chat_box], [chat_box, msg])

demo.launch()