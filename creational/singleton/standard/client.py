from preferences import Preferences

Preferences.global_preference.get_preference_details()

preference_2 = Preferences("Second one created.")

Preferences.global_preference = preference_2

Preferences.global_preference.get_preference_details()