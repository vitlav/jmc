# -*- coding: utf-8 -*-
##
## test_lang.py
## Login : David Rousselie <david.rousselie@happycoders.org>
## Started on  Fri May 20 10:46:58 2005 
## $Id: test_lang.py,v 1.1 2005/07/11 20:39:31 dax Exp $
## 
## Copyright (C) 2005 
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

import jcl.tests.lang

import jmc.lang
from jmc.lang import Lang

from pyxmpp.iq import Iq

class Lang_TestCase(unittest.TestCase):
    def setUp(self):
        self.lang = Lang()

    def tearDown(self):
        self.lang = None
        
    def test_get_lang_class_exist(self):
        lang_class = self.lang.get_lang_class("fr")
        self.assertEquals(lang_class, Lang.fr)

    def test_get_lang_class_not_exist(self):
        lang_class = self.lang.get_lang_class("not_exist")
        self.assertEquals(lang_class, Lang.en)
        
    def test_get_lang_class_long_code(self):
        lang_class = self.lang.get_lang_class("fr_FR")
        self.assertEquals(lang_class, Lang.fr)
        
    def test_get_lang_from_node(self):
        iq = Iq(from_jid = "test@test.com", \
                to_jid = "test2@test.com", \
                stanza_type = "get")
        iq_node = iq.get_node()
        iq_node.setLang("fr")
        lang = self.lang.get_lang_from_node(iq_node)
        self.assertEquals(lang, "fr")

    def test_get_lang_class_from_node(self):
        iq = Iq(from_jid = "test@test.com", \
                to_jid = "test2@test.com", \
                stanza_type = "get")
        iq_node = iq.get_node()
        iq_node.setLang("fr")
        lang = self.lang.get_lang_class_from_node(iq_node)
        self.assertEquals(lang, Lang.fr)

class Language_TestCase(jcl.tests.lang.Language_TestCase):
    """Test language classes"""

    def setUp(self):
        """must define self.lang_class. Lang.en is default"""
        self.lang_class = Lang.en

    def test_strings(self):
        jcl.tests.lang.Language_TestCase.test_strings(self)

        self.assertNotEquals(self.lang_class.field_login, None)
        self.assertNotEquals(self.lang_class.field_host, None)
        self.assertNotEquals(self.lang_class.field_port, None)
        self.assertNotEquals(self.lang_class.field_ssl, None)
        self.assertNotEquals(self.lang_class.field_tls, None)
        self.assertNotEquals(self.lang_class.field_store_password, None)
        self.assertNotEquals(self.lang_class.field_live_email_only, None)
        self.assertNotEquals(self.lang_class.field_interval, None)
        self.assertNotEquals(self.lang_class.field_mailbox, None)

        self.assertNotEquals(self.lang_class.field_action_1, None)
        self.assertNotEquals(self.lang_class.field_chat_action_1, None)
        self.assertNotEquals(self.lang_class.field_online_action_1, None)
        self.assertNotEquals(self.lang_class.field_away_action_1, None)
        self.assertNotEquals(self.lang_class.field_xa_action_1, None)
        self.assertNotEquals(self.lang_class.field_dnd_action_1, None)
        self.assertNotEquals(self.lang_class.field_offline_action_1, None)

        self.assertNotEquals(self.lang_class.field_action_2, None)
        self.assertNotEquals(self.lang_class.field_chat_action_2, None)
        self.assertNotEquals(self.lang_class.field_online_action_2, None)
        self.assertNotEquals(self.lang_class.field_away_action_2, None)
        self.assertNotEquals(self.lang_class.field_xa_action_2, None)
        self.assertNotEquals(self.lang_class.field_dnd_action_2, None)
        self.assertNotEquals(self.lang_class.field_offline_action_2, None)

        self.assertNotEquals(self.lang_class.field_default_from, None)
        self.assertNotEquals(self.lang_class.field_default_account, None)

        self.assertNotEquals(self.lang_class.new_mail_subject, None)
        self.assertNotEquals(self.lang_class.new_digest_subject, None)

        self.assertNotEquals(self.lang_class.type_imap_name, None)
        self.assertNotEquals(self.lang_class.type_pop3_name, None)
        self.assertNotEquals(self.lang_class.type_smtp_name, None)

        self.assertNotEquals(self.lang_class.send_mail_error_no_to_header_subject,
                             None)
        self.assertNotEquals(self.lang_class.send_mail_error_no_to_header_body,
                             None)
        self.assertNotEquals(self.lang_class.send_mail_ok_subject, None)
        self.assertNotEquals(self.lang_class.send_mail_ok_body, None)
        self.assertNotEquals(self.lang_class.help_message_body, None)
        self.assertNotEquals(self.lang_class.command_force_check, None)
        self.assertNotEquals(self.lang_class.command_force_check_1_description, None)
        self.assertNotEquals(self.lang_class.command_get_email, None)
        self.assertNotEquals(self.lang_class.command_get_email_1_description, None)
        self.assertNotEquals(self.lang_class.command_get_email_2_description, None)
        self.assertNotEquals(self.lang_class.field_email_subject, None)
        self.assertNotEquals(self.lang_class.mail_subject, None)
        self.assertNotEquals(self.lang_class.field_select_more_emails, None)

class SubLanguage_TestCase(Language_TestCase):
    """
    Test translation fallback mecanism :
    jmc.lang.Lang.{translation class} -> jmc.lang.Lang.en -> jcl.lang.Lang.{translation class} -> jcl.lang.Lang.en
    """

    def test_fallback_jmc_en(self):
        """
        if a translation does not exist in JMC. It falls back to the English
        translation.
        """
        value = self.lang_class.register_title
        del self.lang_class.register_title
        self.assertEquals(self.lang_class.register_title,
                          jmc.lang.Lang.en.register_title)
        self.lang_class.register_title = value

    def test_fallback_jcl_current(self):
        """
        if an attribut does not exist in JMC translation class nor in JMC
        English class, it falls back to the current language in JCL.
        """
        lang_class_value = self.lang_class.register_title
        jmc_lang_en_value = jmc.lang.Lang.en.register_title
        del self.lang_class.register_title
        del jmc.lang.Lang.en.register_title
        self.assertEquals(\
            self.lang_class.register_title,
            jcl.lang.Lang.__dict__[self.lang_class.__name__].register_title)
        jmc.lang.Lang.en.register_title = jmc_lang_en_value
        self.lang_class.register_title = lang_class_value

    def test_fallback_jcl_en(self):
        """
        if an attribut does not exist in JMC and is not translated in JCL,
        it falls back to English in JCL
        """
        lang_class_value = self.lang_class.register_title
        jmc_lang_en_value = jmc.lang.Lang.en.register_title
        jcl_lang_class_value = jcl.lang.Lang.__dict__[self.lang_class.__name__].register_title
        del self.lang_class.register_title
        del jmc.lang.Lang.en.register_title
        del jcl.lang.Lang.__dict__[self.lang_class.__name__].register_title
        self.assertEquals(\
            self.lang_class.register_title,
            jcl.lang.Lang.en.register_title)
        jcl.lang.Lang.__dict__[self.lang_class.__name__].register_title = jcl_lang_class_value
        jmc.lang.Lang.en.register_title = jmc_lang_en_value
        self.lang_class.register_title = lang_class_value
    
class Language_fr_TestCase(SubLanguage_TestCase):
    def setUp(self):
        self.lang_class = Lang.fr

class Language_nl_TestCase(Language_TestCase):
    def setUp(self):
        self.lang_class = Lang.nl

class Language_es_TestCase(Language_TestCase):
    def setUp(self):
        self.lang_class = Lang.es

class Language_pl_TestCase(Language_TestCase):
    def setUp(self):
        self.lang_class = Lang.pl

class Language_cs_TestCase(Language_TestCase):
    def setUp(self):
        self.lang_class = Lang.cs

class Language_ru_TestCase(Language_TestCase):
    def setUp(self):
        self.lang_class = Lang.ru

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Lang_TestCase, 'test'))
    suite.addTest(unittest.makeSuite(Language_TestCase, 'test'))
    suite.addTest(unittest.makeSuite(Language_fr_TestCase, 'test'))
    suite.addTest(unittest.makeSuite(Language_nl_TestCase, 'test'))
    suite.addTest(unittest.makeSuite(Language_es_TestCase, 'test'))
    suite.addTest(unittest.makeSuite(Language_pl_TestCase, 'test'))
    suite.addTest(unittest.makeSuite(Language_cs_TestCase, 'test'))
    suite.addTest(unittest.makeSuite(Language_ru_TestCase, 'test'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
