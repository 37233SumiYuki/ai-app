
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
        
        if "最近" in text:
            return "最近どんなことが気になってますか？いろいろ教えてほしいです！"

        if "好き" in text:
            return "それ、好きなんですね！どんなところが好きですか？"

        if "興味" in text:
            return "興味があること、もっと聞かせてください。一緒に考えてみましょう！"

        if "わからない" in text or "わからん" in text:
            return "わからないって、実は一番面白いスタート地点だと思います。一緒に考えましょう！"

        if "難しい" in text:
            return "難しいですよね。でもどのへんが引っかかってますか？"

        if re.search(r"なんで|なぜ", text):
            return "いい「なんで？」ですね。そこ、私も気になります！"

        # キーワードランダム返答
        responses = [
            "なるほど、興味深いですね。",
            "もう少し詳しく教えてください。",
            "それは面白い視点です。",
            "別の見方もありそうですね。",
            "それってもっと詳しく聞かせてもらえませんか？すごく気になります！",
            "へえ〜、そういう考え方もあるんですね。どこからそう思いました？",
            "おもしろい！それ、もう少し掘り下げてみましょうか？",
            "それって、最近のことですか？それとも前からずっとそう感じてました？",
            "聞いてて、ちょっとワクワクしてきました。続きを教えてください！",
            "なんかその話、もっと広がりそうな気がします！",
        ]
        return random.choice(responses)
