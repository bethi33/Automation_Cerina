import pytest

class MockApp:
    def __init__(self):
        self.entries = []
        self.online = True

    def set_offline(self):
        self.online = False

    def set_online(self):
        self.online = True
        self.entries = list(dict.fromkeys(self.entries))

    def submit_mood(self, mood, note):
        self.entries.append((mood, note))
        return True

def test_mood_checkin_offline_sync():
    app = MockApp()

    app.set_offline()
    app.submit_mood(5, "Feeling great")

    app.set_online()

    assert len(app.entries) == 1
    assert app.entries[0] == (5, "Feeling great")

def test_mood_checkin_duplicate_prevention():
    app = MockApp()

    app.set_offline()
    app.submit_mood(3, "Okay")
    app.submit_mood(3, "Okay") 

    app.set_online()

    assert len(app.entries) == 1
    assert app.entries[0] == (3, "Okay")


