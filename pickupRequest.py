
class PickupRequest:
    def __init__(self, passengerID, passengerName,
                 driverID, driverName,
                 pickupLocation,
                 membershipTier,
                 estimatedTime,
                 priority):

        self.passengerID = passengerID
        self.passengerName = passengerName

        self.driverID = driverID
        self.driverName = driverName

        self.pickupLocation = pickupLocation

        self.membershipTier = membershipTier
        self.estimatedTime = estimatedTime
        self.priority = priority

    def getEstimatedPickupTime(self):
        return self.estimatedTime
    
    def getPassengerID(self):
        return self.passengerID
    
    def getPickupLocation(self):
        return self.pickupLocation
    
    def getDriverID(self):
        return self.driverID
    
    def getPriority(self):
        return self.priority
    
    def __str__(self):
        return (
            f"[Passenger={self.passengerName}({self.passengerID}), "
            f"Driver={self.driverName}({self.driverID}), "
            f"Location={self.pickupLocation}, "
            f"M={self.membershipTier}, "
            f"T={self.estimatedTime}, "
            f"Priority={round(self.priority,2)}]"
        )