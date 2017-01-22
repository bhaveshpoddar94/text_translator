import json
import requests
import urllib
from xml.etree import ElementTree
import sys

def GetToken(): #Get the access token from ADM, token is good for 10 minutes
    urlArgs = {
        'Ocp-Apim-Subscription-Key': 'EncryptedAAAAABAAhVWnlc67fUEK5VrAhl4GUiAATkJS0Yvwaawf6yx37IY/11vEA6Bu2o9h57RkpOo79AcwAAo3Vm0eP5zYx2q7DQXE3/eITcQd2U+KoOs7/efjsK2EVcr19Vm9c81lK+fuy8J5Kw==',
    }

    oauthUrl = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'

    try:
        oauthToken = requests.post(oauthUrl, headers = urlArgs).text #make call to get ADM token and parse json
        finalToken = "Bearer " + oauthToken #prepare the token
    except Exception as e:
        print str(e)

    return finalToken
#End GetToken


def GetTextAndTranslate(textToTranslate, fromLangCode, toLangCode):
    finalToken = GetToken()
    print "Text--->"+textToTranslate
    print "FromCode--->"+fromLangCode
    print "ToCode--->"+toLangCode
    payload = {'appid': finalToken, 'text': textToTranslate, 'from': fromLangCode, 'to': toLangCode}
    translateUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate"
    try:
        reload(sys)
        sys.setdefaultencoding('utf-8')
        translationData = requests.get(translateUrl, params=payload) #make request
        translation = ElementTree.fromstring(translationData.text.encode('utf-8')) # parse xml return values
        print "The translation is---> ", translation.text #display translation
        return translation.text
    except Exception as e:
        print str(e)
        return str(e)
        pass

#End GetTextAndTranslate()