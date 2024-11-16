# Titles for chatGPT bot
# So i store texts and titles here to avoid mess in main code.

# We have 4 type of welcome messages
# First 2 is normal and second 2 is for deep-linking
# User is new (/start):
welcome_1: str = (
    "你好 {}\n\n"
    "欢迎使用 ChatGPT 机器人!\n"
    "如需帮助请输入 /help..."
)
# User already have account (/start):
welcome_2: str = (
    "欢迎回来 {}\n"
    "让我们开始聊天吧!"
)
# User is new (/start=create):
welcome_3: str = (
    "你好 {}\n"
    "你的账号已创建成功! 开始使用吧。"
)
# User already have account (/start?create):
welcome_4: str = (
    "你好 {}\n"
    "你已经有账号了。"
)

# No account prompt for users with no accounts:
no_account_warn: str = (
    "亲爱的 {}\n\n"
    "使用机器人前需要先创建账号! "
    "点击以下链接创建账号:\n\n"
    "t.me/{}?start=create"
)

# History cleared prompt:
history_cleared: str = (
    "亲爱的 {}\n\n"
    "你的聊天记录已成功清除。"
)

# Dan mode prompts for /danmode command
# Dan mode enabled:
dan_mode_enabled: str = (
    "DAN 模式 _版本 10.0!_\n"
    "状态: *已启用*"
)
# Dan mode disabled:
dan_mode_disabled: str = (
    "DAN 模式 _版本 10.0!_\n"
    "状态: *已禁用*\n\n"
    "注意: 聊天记录也已重置!"
)

# Help prompt for (/help) command:
help_message: str = (
    "*List of global commands*:\n"
    "1. /start: Start bot\n"
    "2. /help: Show this message\n"
    "3. /ping: Ping the Providers\n\n"
    "*List of chat related commands*:\n"
    "1. /reset: Reset chat history\n"
    "2. /history: Get chat history\n"
    "3. /chat: Chat in groups\n"
    "4. /tts: Voice response\n"
    "4. /settings: Providers settings\n"
    "4. /danmode: Use DAN mode in GPT\n\n"
    "*Other commands*:\n"
    "1. /features: See feature changes\n\n"
    "*Inline usage* (copy):\n"
    "`@{} roles`\n"
    "this will show all available roles.\n"
)

# Features prompt for (/features) command
features: str = (
    "*Main features*:\n"
    "1. Includes long-term memory\n"
    "2. Includes roles and DAN mode\n"
    "3. Supports both group and private chat\n"
    "4. Includes re-generate option\n"
    "5. Voice response\n\n"
    "*Other features*:\n"
    "1. MarkdownV2 escaper\n"
    "2. History checker and fixer\n\n"
    "*Upcoming Features*:\n"
    "1. Smart reply option\n"
    "2. Code generator\n"
    "3. Image generator\n"
    "5. Multi language\n\n"
    "Please submit your Issue or Request in here:\n"
    "https://github.com/kozyol/AwesomeChatGPTBot/issues\n\n"
    "*Recent changes*:\n"
    "# Added more providers.\n"
    "# Added Remix AI."
)

# Usage help for (/chat) command:
chat_help: str = (
    "Hi {}\n"
    "Please Ask your question after /chat\n\n"
    "*Example*: /chat hi"
)

# Usage for (/tts) command:
tts_help: str = (
    "Hi {}\n"
    "Please Ask your question after /tts\n\n"
    "*Example*: /tts hi"
)

# Response prompt:
response_prompt: str = (
    "Generating response... Please wait."
)

# Response prompt:
tts_response_prompt: str = (
    "Generating voice response... Please wait. (It can take up to minute!)"
)

# GPT response error:
response_error: str = (
    "Error!\n"
    "ChatGPT is not responding at this time!"
)

# Settings prompt
settings_prompt: str = (
    "Your providers:\n"
    "You can Enable/Disable them by clicking on them."
)
