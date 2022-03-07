class Story:
    def __init__(self, code, title, words, text):
        self.code = code
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


story1 = Story(
    "history",
    "A History Tale",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    "omg",
    "An Excited Adventure",
    ["noun", "verb"],
    """OMG!! OMG!! I love to {verb} a {noun}!"""
)

stories = {s.code: s for s in [story1, story2]}