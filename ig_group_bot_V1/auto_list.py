from main import *

import StringIO
import json
import logging
import random
import urllib
import urllib2
from auto_start import *
from auto_leech import *
from auto_list import *
from auto_h import *
from auto_hlist import *
from collections import defaultdict

# for sending images
from PIL import Image
import multipart

# standard app engine imports
from google.appengine.api import urlfetch
from google.appengine.ext import ndb
import webapp2
excl =  u"\u203C"
class autolist(webapp2.RequestHandler):
	def get(self):
	    for p in chatList:
	        chat_id = p
	        def reply2(msg=None, img=None):
	            if msg:
	                resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
	                    'chat_id': str(chat_id),
	                    'text': msg.encode('utf-8'),
	                    #'disable_web_page_preview': 'true',
	                    #'reply_to_message_id': str(message_id),
	                })).read() 
            xu = len(mainlist[chat_id])
            if xu < 15:
                list_one = "\n".join(list1[chat_id])
                reply2("LIST 1\n" + list_one)
            elif xu < 30:
                list_one = "\n".join(list1[chat_id])
                reply2("LIST 1\n%s", list_one)
                list_two = "\n".join(list2[chat_id])
                reply2("LIST 2\n%s", list_two)
            elif xu < 45:
                list_one = "\n".join(list1[chat_id])
                reply2("LIST 1\n%s", list_one)
                list_two = "\n".join(list2[chat_id])
                reply2("LIST 2\n%s", list_two)             
                list_three = "\n".join(list3[chat_id])
                reply2("LIST 3\n%s", list_three)
            elif xu < 60:
                list_one = "\n".join(list1[chat_id])
                reply2("LIST 1\n%s", list_one)
                list_two = "\n".join(list2[chat_id])
                reply2("LIST 2\n%s", list_two)             
                list_three = "\n".join(list3[chat_id])
                reply2("LIST 3\n%s", list_three)                   
                list_four = "\n".join(list4[chat_id])
                reply2("LIST 4\n%s", list_four)
            elif xu < 75:
                list_one = "\n".join(list1[chat_id])
                reply2("LIST 1")
                reply2(list_one)                    
                list_two = "\n".join(list2[chat_id])
                reply2("LIST 2")                    
                list_three = "\n".join(list3[chat_id])
                reply2("LIST 3")
                reply2(list_three)  
                list_four = "\n".join(list4[chat_id])
                reply2("LIST 4")
                reply2(list_four)                                      
                list_five = "\n".join(list5[chat_id])
                reply2("LIST 5")
                reply2(list_five)
            elif xu < 90:
                list_one = "\n".join(list1[chat_id])
                reply2("LIST 1")
                reply2(list_one)                    
                list_two = "\n".join(list2[chat_id])
                reply2("LIST 2")                    
                list_three = "\n".join(list3[chat_id])
                reply2("LIST 3")
                reply2(list_three) 
                list_four = "\n".join(list4[chat_id])
                reply2("LIST 4")
                reply2(list_four)                                       
                list_five = "\n".join(list5[chat_id])
                reply2("LIST 5")                   
                list_six = "\n".join(list6[chat_id])
                reply2("LIST 6")
                reply2(list_six)
            elif xu < 105:
                list_one = "\n".join(list1[chat_id])
                reply2("LIST 1")
                reply2(list_one)                    
                list_two = "\n".join(list2[chat_id])
                reply2("LIST 2")                    
                list_three = "\n".join(list3[chat_id])
                reply2("LIST 3")
                reply2(list_three) 
                list_four = "\n".join(list4[chat_id])
                reply2("LIST 4")
                reply2(list_four)                                       
                list_five = "\n".join(list5[chat_id])
                reply2("LIST 5")                   
                list_six = "\n".join(list6[chat_id])
                reply2("LIST 6")
                reply2(list_six)                    
                list_seven = "\n".join(list7[chat_id])
                reply2("LIST 7")
                reply2(list_seven)
            elif xu < 120:
                list_one = "\n".join(list1[chat_id])
                reply2("LIST 1")
                reply2(list_one)                    
                list_two = "\n".join(list2[chat_id])
                reply2("LIST 2")                    
                list_three = "\n".join(list3[chat_id])
                reply2("LIST 3")
                reply2(list_three) 
                list_four = "\n".join(list4[chat_id])
                reply2("LIST 4")
                reply2(list_four)                                       
                list_five = "\n".join(list5[chat_id])
                reply2("LIST 5")                   
                list_six = "\n".join(list6[chat_id])
                reply2("LIST 6")
                reply2(list_six)                    
                list_seven = "\n".join(list7[chat_id])
                reply2("LIST 7")                    
                list_eight = "\n".join(list8[chat_id])
                reply2("LIST 8")
                reply2(list_eight)
            elif xu < 135:
                list_one = "\n".join(list1[chat_id])
                reply2("LIST 1")
                reply2(list_one)                    
                list_two = "\n".join(list2[chat_id])
                reply2("LIST 2")                    
                list_three = "\n".join(list3[chat_id])
                reply2("LIST 3")
                reply2(list_three)
                list_four = "\n".join(list4[chat_id])
                reply2("LIST 4")
                reply2(list_four)                                        
                list_five = "\n".join(list5[chat_id])
                reply2("LIST 5")                   
                list_six = "\n".join(list6[chat_id])
                reply2("LIST 6")
                reply2(list_six)                    
                list_seven = "\n".join(list7[chat_id])
                reply2("LIST 7")                    
                list_eight = "\n".join(list8[chat_id])
                reply2("LIST 8")
                reply2(list_eight)                    
                list_nine = "\n".join(list9[chat_id])
                reply2("LIST 9")
                reply2(list_nine)
            elif xu < 150:
                list_one = "\n".join(list1[chat_id])
                reply2("LIST 1")
                reply2(list_one)                    
                list_two = "\n".join(list2[chat_id])
                reply2("LIST 2")                    
                list_three = "\n".join(list3[chat_id])
                reply2("LIST 3")
                reply2(list_three) 
                list_four = "\n".join(list4[chat_id])
                reply2("LIST 4")
                reply2(list_four)                                       
                list_five = "\n".join(list5[chat_id])
                reply2("LIST 5")                   
                list_six = "\n".join(list6[chat_id])
                reply2("LIST 6")
                reply2(list_six)                    
                list_seven = "\n".join(list7[chat_id])
                reply2("LIST 7")                    
                list_eight = "\n".join(list8[chat_id])
                reply2("LIST 8")
                reply2(list_eight)                    
                list_nine = "\n".join(list9[chat_id])
                reply2("LIST 9")
                reply2(list_nine)                    
                list_ten = "\n".join(list10[chat_id])
                reply2("LIST 10")
                reply2(list_ten)
            elif xu < 165:
                list_one = "\n".join(list1[chat_id])
                reply2("LIST 1")
                reply2(list_one)                    
                list_two = "\n".join(list2[chat_id])
                reply2("LIST 2")                    
                list_three = "\n".join(list3[chat_id])
                reply2("LIST 3")
                reply2(list_three) 
                list_four = "\n".join(list4[chat_id])
                reply2("LIST 4")
                reply2(list_four)                                       
                list_five = "\n".join(list5[chat_id])
                reply2("LIST 5")                   
                list_six = "\n".join(list6[chat_id])
                reply2("LIST 6")
                reply2(list_six)                    
                list_seven = "\n".join(list7[chat_id])
                reply2("LIST 7")                    
                list_eight = "\n".join(list8[chat_id])
                reply2("LIST 8")
                reply2(list_eight)                    
                list_nine = "\n".join(list9[chat_id])
                reply2("LIST 9")
                reply2(list_nine)                    
                list_ten = "\n".join(list10[chat_id])
                reply2("LIST 10")
                reply2(list_ten)
                list_eleven = "\n".join(list11[chat_id])
                reply2("LIST 11")
                reply2(list_eleven)
            elif xu < 180:
                list_one = "\n".join(list1[chat_id])
                reply2("LIST 1")
                reply2(list_one)                    
                list_two = "\n".join(list2[chat_id])
                reply2("LIST 2")                    
                list_three = "\n".join(list3[chat_id])
                reply2("LIST 3")
                reply2(list_three)   
                list_four = "\n".join(list4[chat_id])
                reply2("LIST 4")
                reply2(list_four)                                     
                list_five = "\n".join(list5[chat_id])
                reply2("LIST 5")                   
                list_six = "\n".join(list6[chat_id])
                reply2("LIST 6")
                reply2(list_six)                    
                list_seven = "\n".join(list7[chat_id])
                reply2("LIST 7")                    
                list_eight = "\n".join(list8[chat_id])
                reply2("LIST 8")
                reply2(list_eight)                    
                list_nine = "\n".join(list9[chat_id])
                reply2("LIST 9")
                reply2(list_nine)                    
                list_ten = "\n".join(list10[chat_id])
                reply2("LIST 10")
                reply2(list_ten)
                list_eleven = "\n".join(list11[chat_id])
                reply2("LIST 11")
                reply2(list_eleven)                    
                list_twelve = "\n".join(list12[chat_id])
                reply2("LIST 12")
                reply2(list_twelve)
            elif xu < 195:
                list_one = "\n".join(list1[chat_id])
                reply2("LIST 1")
                reply2(list_one)                    
                list_two = "\n".join(list2[chat_id])
                reply2("LIST 2")                    
                list_three = "\n".join(list3[chat_id])
                reply2("LIST 3")
                reply2(list_three) 
                list_four = "\n".join(list4[chat_id])
                reply2("LIST 4")
                reply2(list_four)                                       
                list_five = "\n".join(list5[chat_id])
                reply2("LIST 5")                   
                list_six = "\n".join(list6[chat_id])
                reply2("LIST 6")
                reply2(list_six)                    
                list_seven = "\n".join(list7[chat_id])
                reply2("LIST 7")                    
                list_eight = "\n".join(list8[chat_id])
                reply2("LIST 8")
                reply2(list_eight)                    
                list_nine = "\n".join(list9[chat_id])
                reply2("LIST 9")
                reply2(list_nine)                    
                list_ten = "\n".join(list10[chat_id])
                reply2("LIST 10")
                reply2(list_ten)
                list_eleven = "\n".join(list11[chat_id])
                reply2("LIST 11")
                reply2(list_eleven)                    
                list_twelve = "\n".join(list12[chat_id])
                reply2("LIST 12")                    
                list_thirteen = "\n".join(list13[chat_id])
                reply2("LIST 13")
                reply2(list_thirteen)
            elif xu < 210:
                list_one = "\n".join(list1[chat_id])
                reply2("LIST 1")
                reply2(list_one)                    
                list_two = "\n".join(list2[chat_id])
                reply2("LIST 2")                    
                list_three = "\n".join(list3[chat_id])
                reply2("LIST 3")
                reply2(list_three) 
                list_four = "\n".join(list4[chat_id])
                reply2("LIST 4")
                reply2(list_four)                                       
                list_five = "\n".join(list5[chat_id])
                reply2("LIST 5")                   
                list_six = "\n".join(list6[chat_id])
                reply2("LIST 6")
                reply2(list_six)                    
                list_seven = "\n".join(list7[chat_id])
                reply2("LIST 7")                    
                list_eight = "\n".join(list8[chat_id])
                reply2("LIST 8")
                reply2(list_eight)                    
                list_nine = "\n".join(list9[chat_id])
                reply2("LIST 9")
                reply2(list_nine)                    
                list_ten = "\n".join(list10[chat_id])
                reply2("LIST 10")
                reply2(list_ten)
                list_eleven = "\n".join(list11[chat_id])
                reply2("LIST 11")
                reply2(list_eleven)                    
                list_twelve = "\n".join(list12[chat_id])
                reply2("LIST 12")                    
                list_thirteen = "\n".join(list13[chat_id])
                reply2("LIST 13")
                reply2(list_thirteen)                    
                list_fourteen = "\n".join(list14[chat_id])
                reply2("LIST 14")
                reply2(list_fourteen)
            elif xu < 250:
                list_one = "\n".join(list1[chat_id])
                reply2("LIST 1")
                reply2(list_one)                    
                list_two = "\n".join(list2[chat_id])
                reply2("LIST 2")                    
                list_three = "\n".join(list3[chat_id])
                reply2("LIST 3")
                reply2(list_three) 
                list_four = "\n".join(list4[chat_id])
                reply2("LIST 4")
                reply2(list_four)                                       
                list_five = "\n".join(list5[chat_id])
                reply2("LIST 5")                   
                list_six = "\n".join(list6[chat_id])
                reply2("LIST 6")
                reply2(list_six)                    
                list_seven = "\n".join(list7[chat_id])
                reply2("LIST 7")                    
                list_eight = "\n".join(list8[chat_id])
                reply2("LIST 8")
                reply2(list_eight)                    
                list_nine = "\n".join(list9[chat_id])
                reply2("LIST 9")
                reply2(list_nine)                    
                list_ten = "\n".join(list10[chat_id])
                reply2("LIST 10")
                reply2(list_ten)
                list_eleven = "\n".join(list11[chat_id])
                reply2("LIST 11")
                reply2(list_eleven)                    
                list_twelve = "\n".join(list12[chat_id])
                reply2("LIST 12")                    
                list_thirteen = "\n".join(list13[chat_id])
                reply2("LIST 13")
                reply2(list_thirteen)                    
                list_fourteen = "\n".join(list14[chat_id])
                reply2("LIST 14")                    
                list_fifteen = "\n".join(list15[chat_id])
                reply2("LIST 15\n %s", list_fifteen)
            reply2('%s When done, say D @username.\nEngage on latest photo', excl)
            reply2('%sIf you engaged with a different account, D @droppedIG then reply to that post with \'engaged with @engagedIG\'')

app = webapp2.WSGIApplication([
    ('/auto_list', autolist),
], debug=True)