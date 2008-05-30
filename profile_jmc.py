# -*- coding: utf-8 -*-
##
## profile_jmc.py
## Login : David Rousselie <dax@happycoders.org>
## Started on  Thu May 29 19:09:02 2008 David Rousselie
## $Id$
##
## Copyright (C) 2008 David Rousselie
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

import profile
import jmc.runner as runner

profile.run("runner.main()", "jmc.prof")