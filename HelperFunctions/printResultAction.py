def printResultAction(findBy, elementName, action=None, value=None):
    if action is not None and value is not None:
        print(findBy + " - " + elementName + " - " + action + " - " + str(value) + " - PASSED")
    elif action is not None and value is None:
        print(findBy + " - " + elementName + " - " + action + " - PASSED")
    else:
        print(findBy + " - " + elementName + " - PASSED")