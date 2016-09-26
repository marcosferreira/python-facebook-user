#!/usr/bin/env python

import sys
import cookielib
import urllib2
import mechanize
#############################################################
#                                                           #
#   By Marcos Ferreira                                      #
#   For Community                                           #
# Antes de testar o Script instale os modulo e use python2  #
#                                                           #
#  Ex.:                                                     #
#    sudo pip2 install mechanize                            #
#    python2 robot_fb.py                                    #
#                                                           #
#    contato: marcosferreira.developer@gmail.com            #
#                                                           #
#############################################################
    
browser = mechanize.Browser()
cookiejar = cookielib.CookieJar()
browser.set_cookiejar( cookiejar )
browser.set_handle_equiv( True )
browser.set_handle_gzip( True )
browser.set_handle_redirect( True ) 
browser.set_handle_referer( True )
browser.set_handle_robots( False )

browser.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 90)
browser.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ]


#ESTE BLOCO SERA EXECULTADO CASO TODOS OS PARAMETROS SEJA INFORMADOS CORRETAMENTE
print"\n\n\nOs argumentos foram satisfeitos com sucesso!"

#Open URL and submit
browser.open("https://m.facebook.com")

#Open Select Form Login
browser.select_form(nr=0)
browser.form['email']=raw_input("\nDigite seu login: ")
browser.form['pass']=raw_input("\nDigite sua senha: ")
browser.submit(name='login', label='Entrar')

##USADO PARA DEBUG
#for form in browser.forms():
    #print form

#Select form post status
msg = raw_input("\nDigite seu status no facebook: ")

browser.select_form(nr=1)
browser.form["xc_message"] = msg
browser.submit(name='view_post', label='Publicar')

while msg != "sair":
    browser.select_form(nr=1)
    browser.form["xc_message"] = msg
    browser.submit(name='view_post', label='Publicar')
    msg = raw_input("\nDigite seu status no facebook: ")


print"SUCESS!!!"
