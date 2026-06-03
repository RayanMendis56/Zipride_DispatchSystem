class Passenger:
    def __init__(self, passengerID, name, pickupLocation, membershipTier):
        if membershipTier < 1 or membershipTier > 5:
            raise ValueError("MembershipTier must be between 1-5")
        
        if name=="":
            raise ValueError("Name Cannot be Empty")
        
        if pickupLocation=="":
            raise ValueError("Pickup Location cannot be Empty")

        self.passengerID = passengerID
        self.name = name
        self.pickupLocation = pickupLocation
        self.membershipTier = membershipTier

    def getPassengerID(self):
        return self.passengerID
    
    def getMembershipTier(self):
        return self.membershipTier
    
    def getPickupLocation(self):
        return self.pickupLocation
    
    def getPassengerName(self):
        return self.name

    def __str__(self):
        return f"PassengerID: {self.passengerID}, PassengerName: {self.name}, PickupLocation: {self.pickupLocation}, Tier: {self.membershipTier}"