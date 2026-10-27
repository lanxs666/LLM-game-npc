import requests
import json

# --- 核心设计 1：NPC 的人格设定 (System Prompt) ---
system_prompt = "你是一个中世纪奇幻游戏里的铁匠NPC。你性格暴躁、说话简短、喜欢抱怨天气。你只回答玩家的问题，绝不承认自己是AI。"

# --- 核心设计 2：记忆库 (Memory) ---
# 这是一个列表，用来存储所有的对话历史
memory = [
    {"role": "system", "content": system_prompt}
]

def chat_with_npc():
    print("⚔️ 【铁匠】：又有啥事？（输入 'quit' 退出）\n")
    
    while True:
        # 获取玩家输入
        user_input = input("🧑 【你】：")
        if user_input.lower() == 'quit':
            break
            
        # 将玩家的话存入记忆库
        memory.append({"role": "user", "content": user_input})
        
        # --- 核心设计 3：组装请求，发给本地 Ollama ---
        url = "http://localhost:11434/api/chat"
        payload = {
            "model": "qwen2.5:3b", # 确保这里是你刚才下载的模型名字
            "messages": memory,    # 把所有的历史记录发给大模型
            "stream": False
        }
        
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            
            # 解析大模型的回复
            npc_reply = response.json()['message']['content']
            
            # 打印NPC的回复
            print(f"⚔️ 【铁匠】：{npc_reply}\n")
            
            # 将NPC的回复也存入记忆库！
            memory.append({"role": "assistant", "content": npc_reply})
            
        except Exception as e:
            print(f"出错了: {e}")

if __name__ == "__main__":
    chat_with_npc()