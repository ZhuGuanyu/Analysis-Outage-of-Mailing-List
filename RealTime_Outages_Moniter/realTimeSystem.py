import imaplib
import email
import os,sys
import math 
import string
import re

phrase = ["in order to", "data centers", "customer service router", "federal reserve", "hosting router", "email address", "call center", "opticalflare observed in h-alpha", "out of the ordinary", "an embedded and charset-unspecified text was scrubbed", 
"this message has been scanned for viruses and dangerous content by mailscanner, and is believed to be clean", "proton flux graph", "in addition to", "in progress", "opposite side", "due to", "pure sinusoid", "In fact", "this message is not an official statement of osis center policies", "bit off-topic",
"black out", "wrong mailing list", "deep impact", "outages mailing list", "outages at isotf.org", "paging companies", "ellular operators", "telephone snswering service", "emergency dispatch", "public safety", "optic fusion", "cell towers", "snstitute of earth's magnetism", 
"took place", "take place", "asean restorer", "flag fea sub system", "cs kdd ocean link"]

def removePhrase(row):
    for string in phrase:
        row = row.replace(string,'')
    return row

def get_subjects(email_id,username, password):
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(username, password)
    mail.list()
    mail.select('inbox')
    subject = ""
    result, data = mail.fetch(email_id, '(BODY[HEADER.FIELDS (SUBJECT)])')
    for letter in data[0][1]:
        if letter!= '\n' and letter!='\r':
            subject+=letter
    subject = subject.replace("Subject: ",'')
    return subject


def removeUnrelatedWords(data):
    output = open("intergratedThreads_database.txt", 'a')
    print "################ Begin remove unrelated words ##################"
    contain = ""
    i = 0
    while i< len(data):
        row = data[i]
        if re.search("<http:", row):
            while (">" not in data[i]):
                i += 1
            i += 1
        elif re.search("<mailto:", row):
            while (">" not in data[i]):
                i += 1
            i += 1
        elif re.search("\[mailto:", row):
            while ("]" not in data[i]):
                i += 1
            i += 1
        elif ("BEGIN PGP SIGNED MESSAGE" in data[i] or "Hash: SHA1" in data[i] or "Original Message" in data[i] or "---" in data[i] or "__" in data[i] or " Name:" in data[i] or ":" in data[i] or "wrote:" in data[i] or "..." in data[i]):
            i += 1
        elif ("Subject:" in data[i] or "Date:" in data[i] or "From:" in data[i] or "http:" in data[i] or " Reply-To:" in data[i] or "URL:" in data[i] or "Sent:" in data[i] or "Cc:" in data[i]):
            i += 1
        else:
            row = data[i].lower()
            row = removePhrase(row)
            if ( data[i].find('<') >=0 and data[i].find('>')>=0 ):
    			row = data[i][:data[i].find('<') ]
    			row += data[i][data[i].find('>')+1:]
            if ( data[i].find('|') >=0 and data[i].find('|')>=0 ):
                row = row[:row.find('|') ]
                row += row[row.find('|')+1:]

            word = re.findall(r"[\w']+|[.,!?;_']",row)
            #word = row.split()  # as default using the ' ' to split item
            for j in range(len(word)):
                if (word[j].lower() not in stop_words) and (word[j] not in string.punctuation) and word[j].isdigit()==False and re.search(r'[0-9]',word[j])==None :
                    contain += word[j].lower()+" "
            i += 1
    print "############# End and Add this Email to Database ###############"
    output.write(contain + "\n")
    output.close()
    print contain
    os.system("python tf_idf.py intergratedThreads_database.txt")



with open("stop_words_en.txt", "r") as f:
    stop_words = f.read().splitlines()

with open("people_names.txt", "r") as f:
    people_names = f.read().splitlines()




for j in range(len(stop_words)):
    stop_words[j] = stop_words[j].lower()

for k in range(len(people_names)):
    stop_words.append(people_names[k].lower())


username = 'zhuguanyu2010@gmail.com'
password = '200519903327'
targetEmailAddress = 'zhuguanyu2010@hotmail.com'
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(username, password)
while True:
    mail.list()
    mail.select('inbox')
    result, data = mail.search(None, '(UNSEEN)', '(FROM "%s")' % (targetEmailAddress))
    ids = data[0]
    id_list = ids.split()
    for email_id in id_list:
        result, data = mail.fetch(email_id, "(RFC822)")
        raw_email = email.message_from_string(data[0][1])
        for part in raw_email.walk():
            if part.get_content_maintype()=='multipart':
                continue
            if part.get_content_subtype()!='plain':
                continue
            payload = part.get_payload()
            lines = payload.split('\n')
            subject = get_subjects(email_id, username, password)
            email_list = []
            email_list.append(subject)
            print "################### Received an Email Outage ######################\n"
            #lines.insert(0,subject)
            print subject
            for line in lines:
                if '> On' in line:
                    break
                else:
                    email_list.append(line)
                    print line
            mail.store(email_id, '+FLAGS', '\Seen')
            removeUnrelatedWords(email_list)
