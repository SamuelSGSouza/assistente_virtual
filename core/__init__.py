import datetime



class SystemInfo:
    @staticmethod
    def __init__():
        pass

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = f"São {now.hour} horas e {now.minute} minutos."
        return answer
