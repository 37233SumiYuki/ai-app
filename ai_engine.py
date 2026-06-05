
import random
import re

class SimpleAI:
    def __init__(self):
        self.memory = []

    # history引数を追加
    def respond(self, text: str, history: list = None):
        self.memory.append(text)

        # --- 優先度の高い順に条件を書く ---
        # 挨拶
        if re.search(r"(こんにちは|こんばんは|おはよう|hello|hi)", text.lower()):
            return "こんにちは！今日はどんなことを話しますか？"
        # 疲れ系
        if re.search(r"(疲れ|しんど|だるい)", text):
            return "無理しすぎてない？少し休むのも大事だよ。"
        # 好き
        if re.search(r"(好き|love)", text.lower()):
            return "それ好きなんだね！どんなところが特に良いと思う？"
        # 興味
        if "興味" in text:
            return "興味あるんだね！どんなきっかけで気になったの？"
        # 最近
        if "最近" in text:
            return "最近どんなことがあったの？気になるなあ。"
        # わからない
        if re.search(r"(わからない|わからん)", text):
            return "わからないって、実は成長のチャンスなんだよ。一緒に考えてみよう。"
        # 難しい
        if "難しい" in text:
            return "難しいよね。どのあたりが引っかかってる？"
        # なんで・なぜ
        if re.search(r"(なんで|なぜ)", text):
            return "その疑問、すごく良いね。私も気になるところだよ。"
        # 質問
        if "？" in text or "?" in text:
            return "いい質問だね。それについて少し考えてみるよ。"
        #天気
        if re.search(r"(天気)", text):
            return "天気はいいですね。外に出て過ごすのもいいですよ。"
        #空腹
        if re.search(r"(空腹|お腹空いた)", text):
            return "お腹空いたの？何か食べたいものある？"
        
        # ランダム返答
        responses = [
            "なるほど、面白いね。",
            "もっと詳しく聞きたいな。",
            "それってどういう意味で言ったの？",
            "へえ〜、興味深い話だね。",
            "その話、もう少し掘り下げてみない？",
            "なんかワクワクしてきた。続き聞かせて！",
        ]
        return random.choice(responses)

