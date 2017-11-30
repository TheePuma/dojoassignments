class Patient(object):
    patID = []
    patQueue = []
    def __init__(self):
        self.patID = self.__class__.patID
        self.__class__.patID += 1


    def newPat(self,patName, patPhone, bedNumber, allergies):
        self.patQueue = self.__class__.patQueue
        self.__class__.patQueue.append(patName)
        self.patName = patName
        self.patPhone = patPhone
        self.bedNumber = bedNumber
        self.allergies = allergies
        return self

    def displayPat(self):
        print.pID,self.patName,self.patPhone,self.bedNumber,self.allergies
        if len(self.callQueue) == 1:
            print len(self.callQueue), "Patient in the queue", self.callQueue
            return self
        else:
            print len(self.callQueue) "Patients in the queue", self.callQueue
            return self

        return self
randomPat1 = Patient()
randomPAt1.newPAt("Blaine", 7147545545, 118, "None")
randomPat1.displayPat()
