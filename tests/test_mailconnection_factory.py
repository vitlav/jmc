##
## test_mailconnection_factory.py
## Login : <adro8400@claralinux>
## Started on  Fri May 20 10:46:58 2005 adro8400
## $Id: test_mailconnection_factory.py,v 1.1 2005/07/11 20:39:31 dax Exp $
## 
## Copyright (C) 2005 adro8400
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##

import unittest
from jabber.mailconnection_factory import *

class MailConnectionFactory_TestCase(unittest.TestCase):
    def test_new_mail_connection_imap(self):
	mc = get_new_mail_connection("imap")
        self.assertEquals(mc, mc)

    def test_new_mail_connection_imaps(self):
	mc = get_new_mail_connection("imaps")
        self.assertEquals(mc, mc)

    def test_new_mail_connection_pop3(self):
	mc = get_new_mail_connection("pop3")
        self.assertEquals(mc, mc)

    def test_new_mail_connection_pop3s(self):
	mc = get_new_mail_connection("pop3s")
        self.assertEquals(mc, mc)

    def test_str_to_mail_connection_imap(self):
	mc = str_to_mail_connection("imap#login#passwd#host#193#nothing#nothing#nothing#nothing#retrieve#INBOX")
        self.assertEquals(mc.get_type(), "imap")
        self.assertEquals(mc.login, "login")
        self.assertEquals(mc.password, "passwd")
        self.assertEquals(mc.host, "host")
        self.assertEquals(mc.port, 193)
        self.assertEquals(mc.mailbox, "INBOX")
        self.assertEquals(mc.ffc_action, "nothing")
        self.assertEquals(mc.online_action, "nothing")
        self.assertEquals(mc.away_action, "nothing")
        self.assertEquals(mc.ea_action, "nothing")
        self.assertEquals(mc.offline_action, "retrieve")

    def test_str_to_mail_connection_imaps(self):
	mc = str_to_mail_connection("imaps#login#passwd#host#993#nothing#nothing#nothing#nothing#retrieve#INBOX.SubDir")
        self.assertEquals(mc.get_type(), "imaps")
        self.assertEquals(mc.login, "login")
        self.assertEquals(mc.password, "passwd")
        self.assertEquals(mc.host, "host")
        self.assertEquals(mc.port, 993)
        self.assertEquals(mc.mailbox, "INBOX.SubDir")
        self.assertEquals(mc.ffc_action, "nothing")
        self.assertEquals(mc.online_action, "nothing")
        self.assertEquals(mc.away_action, "nothing")
        self.assertEquals(mc.ea_action, "nothing")
        self.assertEquals(mc.offline_action, "retrieve")

    def test_str_to_mail_connection_pop3(self):
	mc = str_to_mail_connection("pop3#login#passwd#host#110#nothing#nothing#nothing#nothing#retrieve")
        self.assertEquals(mc.get_type(), "pop3")
        self.assertEquals(mc.login, "login")
        self.assertEquals(mc.password, "passwd")
        self.assertEquals(mc.host, "host")
        self.assertEquals(mc.port, 110)
        self.assertEquals(mc.ffc_action, "nothing")
        self.assertEquals(mc.online_action, "nothing")
        self.assertEquals(mc.away_action, "nothing")
        self.assertEquals(mc.ea_action, "nothing")
        self.assertEquals(mc.offline_action, "retrieve")

    def test_str_to_mail_connection_pop3s(self):
	mc = str_to_mail_connection("pop3s#login#passwd#host#995#nothing#nothing#nothing#nothing#retrieve")
        self.assertEquals(mc.get_type(), "pop3s")
        self.assertEquals(mc.login, "login")
        self.assertEquals(mc.password, "passwd")
        self.assertEquals(mc.host, "host")
        self.assertEquals(mc.port, 995)
        self.assertEquals(mc.ffc_action, "nothing")
        self.assertEquals(mc.online_action, "nothing")
        self.assertEquals(mc.away_action, "nothing")
        self.assertEquals(mc.ea_action, "nothing")
        self.assertEquals(mc.offline_action, "retrieve")

