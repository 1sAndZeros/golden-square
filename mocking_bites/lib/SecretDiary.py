class SecretDiary:
    def __init__(self, diary):
        # diary is an instance of Diary
        self.diary = diary
        self.locked = True

    def read(self):
        # Raises the error "Go away!" if the diary is locked
        # Returns the diary's contents if the diary is unlocked
        # The diary starts off locked
        if self.locked:
            raise Exception("Go away!")
        return self.diary.contents

    def lock(self):
        # Locks the diary
        # Returns nothing
        self.locked = True

    def unlock(self):
        # Unlocks the diary
        # Returns nothing
        self.locked = False
