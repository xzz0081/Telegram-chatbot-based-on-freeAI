#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard library imports
import typing

# Related third party imports
from telebot import types, util
import telebot
import requests

# Local application/library specific imports
import utils

# Connect to bot
# Token placed in utils.py file. You can change it with your token
GPTbot: typing.ClassVar[typing.Any] = telebot.TeleBot(utils.TOKEN)
print(f"机器人已启动 (id: {GPTbot.get_me().id}) 版本 {utils.CURRENT_VERSION} \33[0;31m[初始模式]\33[m...")

# Set bot commands
print("[!] Configuring bot commands...")
GPTbot.set_my_commands(
    commands=[
        types.BotCommand(
            command="start",
            description="启动机器人"
        ),
        types.BotCommand(
            command="help",
            description="显示帮助信息"
        ),
        types.BotCommand(
            command="ping",
            description="测试提供商连接"
        ),
        types.BotCommand(
            command="settings",
            description="Provider settings"
        ),
        types.BotCommand(
            command="chat",
            description="Chat in groups using this command"
        ),
        types.BotCommand(
            command="tts",
            description="Brian Text To Speech response"
        ),
        types.BotCommand(
            command="history",
            description="Get your chat history"
        ),
        types.BotCommand(
            command="reset",
            description="Reset you chat history"
        ),
        types.BotCommand(
            command="danmode",
            description="Enable/Disable DAN mode v 10.0"
        ),
        types.BotCommand(
            command="features",
            description="See features changes"
        )
    ]
)
print("[!] Commands successfully configured.\n[!] Run main.py")
