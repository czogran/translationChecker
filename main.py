import json
from pyjavaproperties import Properties

coreMessagesData: Properties = Properties()
coreMessagesData.load(open('data/coreMessages'))

coreEnumData = Properties()
coreEnumData.load(open('data/coreEnum'))

afoFile = open('data/afo', 'r')
afoData = json.load(afoFile)

conflictTranslations = Properties()
missingCoreEnum = Properties()
missingCoreMessages = Properties()
missingAfo = {}

for element in afoData:
    value = afoData[element]

    if coreMessagesData[element] is None:
        missingCoreMessages[element] = value

    elif coreMessagesData[element] is not None and value != coreMessagesData[element]:
        conflictTranslations[element] = value

    elif coreEnumData[element] is None:
        missingCoreEnum[element] = value

    elif (coreEnumData[element] != None and value != coreEnumData[element]):
        conflictTranslations[element] = value

for element in coreMessagesData.items():
    if element[0] not in afoData:
        missingAfo[element[0]] = element[1]


missingCoreMessages.store(open('results/missingCoreMessages.properties', 'w'))
missingCoreEnum.store(open('results/missingCoreEnum.properties', 'w'))
conflictTranslations.store(open('results/conflictTranslations.properties', 'w'))
missingAfoFile = open("results/missingAfo.json", "w")
json.dump(missingAfo, missingAfoFile)
missingAfoFile.close()
