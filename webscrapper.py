#features is our list
class LinkedListNode:
    def __init__(self,name,price=None,review=None,takingSaftyMeasure=None,features=None,pic=None):
        self.name=name
        self.pic=pic
        self.price=price
        self.review=review
        self.features=features
        self.takingSaftyMeasure=takingSaftyMeasure
        self.next=None
from selenium import webdriver
driver = webdriver.Chrome("/Users/manshusharma/Downloads/chromedriver")
driver.get("https://www.tripadvisor.in/Hotels-g304551-New_Delhi_National_Capital_Territory_of_Delhi-Hotels.html")


def LinkedList():
    hotelName = driver.find_elements_by_class_name("property_title")
    price = driver.find_elements_by_class_name("price,__resizeWatch")
    review=driver.find_elements_by_class_name("review_count")

    head=None
    tail=None

    for i,j,k in zip(hotelName,price,review):
        NewNode=LinkedListNode(i.get_attribute("innerHTML"),j.get_attribute("innerHTML")[7:],k.get_attribute("innerHTML")[0:-7])
        if head is None:
            head=NewNode
            tail=NewNode
        else:
            tail.next=NewNode
            tail=NewNode
    return head
def printLL(head):
    while head is not None:
        print(head.name,head.price,head.review)
        head=head.next
    print()







#features=driver.find_elements_by_class_name("text")
#takingSaftyMeasure=driver.find_elements_by_class_name("_1shPZD63")

printLL(LinkedList())



driver.close()