import datetime

from HelperFunctions.printResultAction import printResultAction


def findElementBy(driver, elementName, findBy, id, action=None, value=None):
    try:
        driverUp = None
        if str(findBy).lower() == 'name':
            driverUp = driver.find_element_by_name(str(id))
        elif str(findBy).lower() == 'id':
            driverUp = driver.find_element_by_id(str(id))
        elif str(findBy).lower() == 'xpath':
            driverUp = driver.find_element_by_xpath(str(id))
        else:
            print("Identificator not found")

        if str(action).lower() == 'click':
            driverUp.click()
        elif str(action).lower() == 'send keys':
            if value is not None:
                driverUp.send_keys(value)
            else:
                print("Value has empty")
        elif str(action).lower() == 'assert':
            if value is not None:
                assert driverUp == value

        printResultAction(findBy, elementName, action, value)

        return driverUp
    except Exception as e:
        print(e)
        driver.save_screenshot('..\Screenshots\Screen- ' + datetime.datetime.now().strftime("%m%d%H%M") + '.png')
