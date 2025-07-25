class GlucoseData:
    def __init__(self, sgv: float, timestamp: str, date: int, date_string: str, type: str = "sgv", device: str = "Libreview"):
        self.type = type
        self.date = date
        self.date_string = date_string
        self.sgv = sgv
        self.device = device