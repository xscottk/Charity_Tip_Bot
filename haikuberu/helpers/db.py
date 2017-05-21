"""
    dogetipbot is a bot that lets you tip dogecoins on the internets
    Copyright (C) 2014-2017 Wow Such Business, Inc. and other contributors
    Portions of this software were derived from ALTcointip by Dmitriy Vi - https://github.com/vindimy/altcointip

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, Numeric, UnicodeText
from sqlalchemy.pool import SingletonThreadPool

import logging

lg = logging.getLogger('haikuberu')

class HaikuberuDatabase:

    metadata = MetaData()
    
    def __init__(self, dsn_url):
        '''Pass a DSN URL conforming to the SQLAlchemy API'''
        self.dsn_url = dsn_url
    
    def connect(self):
        '''Return a connection object'''
        engine = create_engine(self.dsn_url, echo_pool=True, poolclass=SingletonThreadPool)
        self.metadata.create_all(engine)
        return engine

    
