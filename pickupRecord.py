class PickupRecord:

    def __init__(self, requestID, passengerName,
                 pickupLocation, driverName,
                 estimatedPickupTime):

        self.requestID = requestID
        self.passengerName = passengerName
        self.pickupLocation = pickupLocation
        self.driverName = driverName
        self.estimatedPickupTime = float(estimatedPickupTime)

    def getEstimatedPickupTime(self):
        return self.estimatedPickupTime

    def __str__(self):
        return (
            f"[{self.requestID}] {self.passengerName} |{self.pickupLocation} | Driver: {self.driverName} | T={self.estimatedPickupTime}")
    
    def __lt__(self, other):
        return self.estimatedPickupTime < other.estimatedPickupTime

    def __le__(self, other):
        return self.estimatedPickupTime <= other.estimatedPickupTime
    
    