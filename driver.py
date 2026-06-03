class Driver:
    def __init__(self, driverID, name, location, status):
        if status not in ["Available", "Busy", "Offline"]:
            raise ValueError("Invalid driver status")

        if name=="":
            raise ValueError("Name Cannot be Empty")
        
        if location=="":
            raise ValueError("Location cannot be Empty")

        self.driverID = driverID
        self.name = name
        self.location = location
        self.status = status

    def getDriverID(self):
        return self.driverID
    
    def getName(self):
        return self.name
    
    def getCurrentLocation(self):
        return self.location
    
    def getAvailabilityStatus(self):
        return self.status

    def __str__(self):
        return f"DriverID: {self.driverID}, DriverName: {self.name}, Location: {self.location}, Status: {self.status}"