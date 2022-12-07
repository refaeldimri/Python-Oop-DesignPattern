class Singleton():

    def __new__(cls):
        if cls._instance is None:
            print("create...")
            cls._instance = super(Singleton, cls).__init__(cls)
        return cls._instance