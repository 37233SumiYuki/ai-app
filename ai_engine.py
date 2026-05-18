# ai_engine.py

import random
import re

class SimpleAI:
    def __init__(self):
        self.memory = []

    def respond(self, text: str):
        self.memory.append(text)

        # 挨拶
        if re.search(r"こんにちは|hello|hi", text.lower()):
            return "こんにちは！今日はどんなことを知りたいですか？"

        # 質問
        if "？" in text or "?" in text:
            return "いい質問ですね。それについて少し考えてみます。"

        # 気分系
        if "楽しい" in text:
            return "楽しさは大事ですね！最近ハマっていることはありますか？"

        if "疲れた" in text:
            return "お疲れ様です。少し休むことも大切ですよ。"

        # キーワードランダム返答
        responses = [
            "なるほど、興味深いですね。",
            "もう少し詳しく教えてください。",
            "それは面白い視点です。",
            "別の見方もありそうですね。",
        ]

        return random.choice(responses)

