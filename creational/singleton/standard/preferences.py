class Preferences:

    preference = None
    global_preference = Preferences("First one created.")

    def __init__(self, preference):
        self.preference = preference

    def get_preference_details(self):
        return self.preference