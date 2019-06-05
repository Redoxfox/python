"""import uuid
import hashlib
 
def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
 
new_pass = input('Please enter a password: ')
hashed_password = hash_password(new_pass)
print('The string to store in the db is: ' + hashed_password)
old_pass = input('Now please enter the password again to check: ')
if check_password(hashed_password, old_pass):
    print('You entered the right password')
else:
    print('I am sorry but the password does not match')
   Tusers= dict()
    Tusers= {'TABLE':'users', 
        'id':'INT AUTO_INCREMENT',
        'nick':'VARCHAR(100) NOT NULL',
        'nombre':'VARCHAR(100) NOT NULL',
        'email':'VARCHAR(100) NOT NULL',
        'direccion':'VARCHAR(100) ',
        'telefono':'VARCHAR(100) ',
        'password':'VARCHAR(150) NOT NULL',
        'salt':'VARCHAR(100) NOT NULL',
        'PK':'id'
        }
    TUsers= Model(Tusers)
    titulo = TUsers.CT_TABLE()"""

from html.parser import HTMLParser
import sys
import re
import urllib.request
import urllib.parse
class LinkParser(HTMLParser):
    
    '''Analizador HTML que imprime el valor de el atributo
        href en las etiquetas de anclaje'''
    def handle_starttag(self, tag, attrs):
            'Imprime el valor del atributo href, si existe'
            if tag == 'a':
                for attr in attrs:
                    if attr[0] == 'href':
                        print(attr[1])




def download(url):
    """Returns the HTML source code from the given URL
        :param url: URL to get the source from.
    """
    try:
        x = urllib.request.urlopen(url)
        #print(x.read())

        saveFile = open('url.txt','w')
        saveFile.write(str(x.read()))
        #saveFile.close()
    except Exception as e:
        print(str(e))
   
    return saveFile

if __name__ == '__main__':

    url = "https://www.resultados-futbol.com/ligue_12017"
    r = download(url)
    content = r.read()
    linkparser = LinkParser()
    linkparser.feed(content)