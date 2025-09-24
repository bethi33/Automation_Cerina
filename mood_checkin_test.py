import pytest

class MockApp:
    def __init__(self):
        self.entries = []
        self.online = True

    def set_offline(self):
        self.online = False

    def set_online(self):
        self.online = True
        # sync deduplicated entries
        self.entries = list(dict.fromkeys(self.entries))

    def submit_mood(self, mood, note):
        self.entries.append((mood, note))
        return True

def test_mood_checkin_offline_sync():
    app = MockApp()

    # step 1: offline mode
    app.set_offline()
    app.submit_mood(5, "Feeling great")

    # step 2: app relaunch + go online
    app.set_online()

    # step 3: verify sync has one entry, no duplicates
    assert len(app.entries) == 1
    assert app.entries[0] == (5, "Feeling great")
