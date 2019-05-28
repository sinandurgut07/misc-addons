# -*- coding: utf-8 -*-
#
#
#    Copyright (c) 2008 Camtocamp SA
#    @author JB Aubort, Nicolas Bessi, Joel Grand-Guillaume
#    European Central Bank and Polish National Bank invented by Grzegorz Grzelak
#    Ported to OpenERP 7.0 by Lorenzo Battistini <lorenzo.battistini@agilebg.com>
#    Banxico implemented by Agustin Cruz openpyme.mx
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
{
    "name": "Currency Rate Update",
    "version": "0.7",
    "author": "Camptocamp, IT-Projects LLC, Ivan Yelizariev",
    "website": "http://camptocamp.com",
    "category": "Financial Management/Configuration",
    "depends": [
        "base",
        "account",  # Added to ensure account security groups are present
    ],
    "data": [
        "currency_rate_update.xml",
        "company_view.xml",
        "security/security.xml",
    ],
    "demo": [],
    "active": False,
    'installable': False
}