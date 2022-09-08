import random
class Event():
    def __init__(self, date, user, machine, eventType):
        self.date = date
        self.user = user
        self.machine = machine
        self.eventType = eventType
    def __str__(self):
        return "Date: {}, User: {}, Machine: {}, Event-Type: {}".format(self.date, self.user, self.machine, self.eventType)

class Report():
    def report_generator(self, eventList):
        resultDict = {}
        for event in eventList:
            if event.date == 2:
                if event.machine in resultDict:
                    if event.eventType.__eq__("Login"):
                        if event.user not in resultDict[event.machine]:
                            resultDict[event.machine].append(event.user)
                    else:
                        if event.user in resultDict[event.machine]:
                            resultDict[event.machine].remove(event.user)
                else:
                    if event.eventType.__eq__("Login"):
                        resultDict[event.machine] = list(event.user)
        return resultDict

    def print_report(self, resultDict):
        for key, value in resultDict.items():
            print(".........................")
            print(key)
            print(value, sep="|", end = " ", flush=True)
            print()
            print(".........................")
        print(resultDict)
    
    def auto_event_generator(self, flag):
        eventList = []
        if flag == 1:
            dates = [1,2,3]
            users = ["A", "B", "C", "D", chr(69), "F", "G", "H", "I", "J", "K", "L", "M", "N"]
            machines = ["M1", "M2", "M3"]
            eventTypes = ["Login", "Logout"]
            i = 0
            while (i < 200):
                eventList.append(Event(random.choice(dates), random.choice(users), random.choice(machines), random.choice(eventTypes)))
                if (i % 20 == 0):
                    print(eventList[-1])
                i += 1
        else:
            eventList.append(Event(2, "A", "M1", "Logout"))
            eventList.append(Event(2, "A", "M1", "Login"))
            eventList.append(Event(2, "A", "M1", "Login"))
            eventList.append(Event(2, "B", "M2", "Login"))
            eventList.append(Event(2, "C", "M1", "Login"))
            eventList.append(Event(2, "A", "M1", "Logout"))
        return eventList

report = Report();
report.print_report(report.report_generator(report.auto_event_generator(1)))