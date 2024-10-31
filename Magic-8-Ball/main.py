#
# Haydin Davis
# 10/31
# Magic 8 Ball Programming Project
# COSC 2409 DNT
#
import random

awnsers=["Yes, of course!",
        "Without a doubt, yes.",
        "You can count on it.",
        "For sure!",
        "Ask me later.",
        "I’m not sure.",
        "I can’t tell you right now.",
        "I’ll tell you after my nap.",
        "No way!",
        "I don’t think so.",
        "Without a doubt, no.",
        "The answer is clearly NO."]

question=input("Ask me anything: ")
print(random.choice(awnsers))
