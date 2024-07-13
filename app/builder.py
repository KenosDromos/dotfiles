class Assembling:
    @staticmethod
    def start(params: dict):
        Logger.add_record(f"Starting assembly. Options {params}")

        if params: 
            Assembling.building()

            end_text = f"Installation Completed Successfully"
            Logger.add_record(end_text)
        else:
            end_text =  f"Installation Canceled"
            Logger.add_record(end_text)
    
    @staticmethod
    def procesor():
        pass

    @staticmethod
    def building():
        # SystemBuild.create_default_foleders()
        Logger.add_record("Create default directories")
