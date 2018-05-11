from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

from mysqlQueries import make_a_query

chatbot = ChatBot("Botishal")
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.corpus.hebrew.conversations",
              "chatterbot.corpus.hebrew.greetings",
              "chatterbot.corpus.hebrew.botprofile")

chatbot.set_trainer(ListTrainer)

list_of_teachers = ["אראל סגל הלוי", "בועז בן מושה"]
list_of_teachers_first_name = ['אראל', 'בעוז']
list_of_teachers_last_name = ['סגל הלוי', 'בן מושה']
list_of_lessons = ['c++', 'מונחה עצמים', 'אוטומטיים 2']


def train_mail():
    for teacher in list_of_teachers_first_name:
        chatbot.train(["מה המייל של " +
                       teacher,
                       "המייל של " +
                       teacher +
                       " הוא " +
                       make_a_query("SELECT email FROM Teachers WHERE firstName = '" + teacher + "'") + " :)"])


def train_conversation():
    chatbot.train(
        ["שלום",
         "שלום גם לך"])
    chatbot.train(
        ["מה נשמע",
         "הכל בסדר, מה בקשתך?"])
    chatbot.train(
        ["תודה רבה",
         "בכיף המשך יום נעים"])
    chatbot.train(
        ["תודה",
         "בכיף המשך יום נעים"])


'''
def trainMail(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            conversation = []
            conversation.append("מה המייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a +" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)

def trainMail1(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            st=a+b
            conversation = []
            conversation.append("מה המייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a+" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)
def trainMail1(ListOfTeachers, FieldName):
    for teacher in ListOfTeachers:
            conversation = []
            conversation.append("מה המיל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName+" = " + teacher,1))
            chatbot.train(conversation)

def trainMail2(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            conversation = []
            conversation.append("מה המיל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a+" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)

def trainMail3(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            st=a+b
            conversation = []
            conversation.append("מה המיל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a+" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)

def trainMail2(ListOfTeachers, FieldName):
    for teacher in ListOfTeachers:
            conversation = []
            conversation.append(" תן לי את המייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName+" = " + teacher,1))
            chatbot.train(conversation)

def trainMail4(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            conversation = []
            conversation.append("תן לי את המייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a+" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)

def trainMail5(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            st=a+b
            conversation = []
            conversation.append("תן לי את המייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a+" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)
def trainMail3(ListOfTeachers, FieldName):
    for teacher in ListOfTeachers:
            conversation = []
            conversation.append("מה החייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName+" = " + teacher,1))
            chatbot.train(conversation)

def trainMail6(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            conversation = []
            conversation.append("מה החייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a+" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)

def trainMail7(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            st=a+b
            conversation = []
            conversation.append("מה החייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a+" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)
def trainMail4(ListOfTeachers, FieldName):
    for teacher in ListOfTeachers:
            conversation = []
            conversation.append("תן לי את החייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName+" = " + teacher,1))
            chatbot.train(conversation)

def trainMail8(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            conversation = []
            conversation.append("תן לי את החייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a+" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)

def trainMail9(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            st=a+b
            conversation = []
            conversation.append("תן לי את החייל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a+" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)
def trainMail5(ListOfTeachers, FieldName):
    for teacher in ListOfTeachers:
            conversation = []
            conversation.append("תן לי את החיל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName+" = " + teacher,1))
            chatbot.train(conversation)

def trainMail10(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            conversation = []
            conversation.append("תן לי את החיל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a+" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)

def trainMail11(ListOfTeachers, FieldName1,FieldName2):
    for teacher in ListOfTeachers:
            a,b=teacher.split(" ")
            st=a+b
            conversation = []
            conversation.append("תן לי את החיל של " + teacher)
            conversation.append(query("select mail from Teachers where "+FieldName1+" = " + a+" and "+FieldName2+" = "+b,1))
            chatbot.train(conversation)
############################################################################
############################################################################
###############lesson Querries Train########################################

def trainLesson(ListOfLesson):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append("איפה ומתי " + lesson)
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)
def trainLesson1(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append("איפה ומתי קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)
def trainLesson2(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append("מתי קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)
def trainLesson3(ListOfLesson, ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append("איפה קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)

def trainLesson4(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append("מתי ואיפה קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)

def trainLesson5(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append("מתי והיכן קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)

def trainLesson6(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append("היכן קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)

def trainLesson7(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append("באיזה שעה " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)

def trainLesson8(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append("באיזה שעה " + lesson)
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)

def trainLesson9(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append("באיזה שעה ואיפה" + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)

def trainLesson10(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append( lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)

def trainLesson11(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append( lesson)
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)

def trainLesson12(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append( "היכן"+lesson)
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)

def trainLesson13(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append( "היכן"+lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)

def trainLesson14(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append( "היכן ומתי "+lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)
      #######################################remember ask about split(mavo)
def trainLesson15(ListOfLesson ):
    for lesson in ListOfLesson:
        a,b=lesson.split(lesson)
        conversation = []
        conversation.append( "היכן ומתי "+lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)

def trainLesson(ListOfLesson):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append("איפה ומתי " + lesson)
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson,4))
        chatbot.train(conversation)
def trainLesson1(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append("איפה ומתי קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)
def trainLesson2(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append("מתי קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)
def trainLesson3(ListOfLesson, ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append("איפה קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)

def trainLesson4(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append("מתי ואיפה קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)

def trainLesson5(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append("מתי והיכן קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)

def trainLesson6(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append("היכן קורס " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)

def trainLesson7(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append("באיזה שעה " + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)

def trainLesson8(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append("באיזה שעה " + lesson)
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)

def trainLesson9(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append("באיזה שעה ואיפה" + lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)

def trainLesson10(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append( lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)

def trainLesson11(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append( lesson)
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)

def trainLesson12(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append( "היכן"+lesson)
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)

def trainLesson13(ListOfLesson ):
    for lesson in ListOfLesson:
        conversation = []
        conversation.append( "היכן"+lesson+"?")
        conversation.append(query("select FirstName,LastName,Date,idClassRoom from ClassRooms join teachers where idCourse in(select idCourse from Courses where name="+lesson))
        chatbot.train(conversation)

###########################################################################################
###########################################################################################
###########################Conversation train##############################################



def trainConversation1():
    conversation = []
    conversation.append("מה המייל של אראל סגל?")
    conversation.append("erelsgl@gmail.com")
    chatbot.train(conversation)


def trainConversation2():
    conversation = []
    conversation.append("מתי אוטומטיים?")
    conversation.append("Thuesday morning")
    chatbot.train(conversation)

trainLesson(listOfLessons)
trainLesson1(listOfLessons)
trainLesson2(listOfLessons)
trainLesson3(listOfLessons)
trainLesson4(listOfLessons)
trainLesson5(listOfLessons)
trainLesson6(listOfLessons)
trainLesson7(listOfLessons)
trainLesson8(listOfLessons)
trainLesson9(listOfLessons)
trainLesson10(listOfLessons)
trainLesson11(listOfLessons)
trainLesson12(listOfLessons)
trainLesson13(listOfLessons)
trainLesson14(listOfLessons)
trainLesson15(listOfLessons)

trainMail1()
trainMail2()
trainMail3()
trainMail4()
trainMail5()
trainMail6()
trainMail7()
trainMail8()
trainMail9()
trainMail10()
trainMail11()
'''


train_mail()
train_conversation()
