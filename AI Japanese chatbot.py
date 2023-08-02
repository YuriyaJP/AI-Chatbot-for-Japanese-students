import random

# Japanese question and answer database for English class
english_database = {
    "english": {
        "question": "英語の授業についての質問を教えてください。",
        "answers": [
            "確かに！英語の質問をどうぞ。",
            "英語の授業が好きなんですね。何か特定のトピックがあれば教えてください。",
            "英語の質問ならお任せください！",
        ]
    },
    "vocabulary": {
        "question": "語彙について教えてください。",
        "answers": [
            "もちろん、語彙に関する質問ならどんなことでもお答えします。",
            "語彙の勉強が苦手な人は多いですね。どんな単語を学びたいですか？",
            "語彙の増やし方についてお話ししましょう！",
        ]
    },
    "grammar": {
        "question": "文法について教えてください。",
        "answers": [
            "文法についての質問なら、どんなことでもお聞きください。",
            "文法の勉強が難しいですよね。具体的な文法ルールについて知りたいですか？",
            "文法の練習方法についてお話ししましょう！",
        ]
    },
}

def chatbot_response(subject):
    """Generate a response based on the English class subject asked."""
    if subject in english_database:
        answers = english_database[subject]["answers"]
        return random.choice(answers)
    else:
        return "申し訳ありませんが、その英語のトピックについての情報はありません。他の質問をお願いします。"

# Main loop for chatbot interaction
print("こんにちは！英語の授業についての質問に答えるチャットボットです。終了するには「終了」と入力してください。")

while True:
    user_input = input("質問を入力してください：")
    user_input = user_input.strip().lower()

    if user_input == "終了":
        print("チャットを終了します。ありがとうございました！")
        break
    else:
        response = chatbot_response(user_input)
        print(response)
