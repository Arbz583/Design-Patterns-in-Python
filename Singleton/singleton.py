class ConfigManager:
    __instance = None
    __allow_init = False

       
    def __init__(self):
        if not self.__class__.__allow_init:
            raise ValueError(
                "Private constructor.\
                Use 'get_instance' method."
            )
        self.settings = dict()

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__allow_init = True
            cls.__instance = cls()
            cls.__allow_init = False
        return cls.__instance 

    def set(self, key, value):
        self.settings[key] = value
    
    def get(self, key):
        return self.settings.get(key)
    
config_manager1 = ConfigManager.get_instance()
config_manager1.set('database', 'postgres')    
config_manager2 = ConfigManager.get_instance()
print(config_manager2.get('database')) 
print(config_manager1 is config_manager2) 

