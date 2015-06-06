#!/usr/bin/env python
# -*- coding: utf-8 -*-

LISTING_TYPE_CHOICES = (
    ('free', 'Gratuita'),
    ('bronze', 'Bronce'),
    ('silver', 'Plata'),
    ('gold', 'Oro'),
    ('gold_premium', 'Oro Premium'),
)
LISTING_TYPES = [t[0] for t in LISTING_TYPE_CHOICES]

BUYING_MODE_CHOICES = (
    ('buy_it_now', 'Venta directa'),
)
BUYING_MODES = [t[0] for t in BUYING_MODE_CHOICES]

CONDITION_CHOICES = (
    ('new', 'Articulo nuevo'),
    ('used', 'Articulo usado'),
    ('unespecified', 'Sin especificar'),
)
CONDITIONS = [t[0] for t in CONDITION_CHOICES]

LOCAL_PICKUP_CHOICES = (
    ('yes', 'Sí'),
    ('no', 'No')
)
FREE_SHIPPING_CHOICES = (
    ('yes', 'Sí'),
    ('no', 'No')
)

FREE_SHIPPING_OPTIONS = ("yes", "")

COLUMNS = [
    {'name': 'sub', 'required': True},
    {'name': 'category_ml', 'required': False},
    {'name': 'title', 'required': True},
    {'name': 'description', 'required': True},
    {'name': 'quantity', 'required': True},
    {'name': 'price', 'required': True},
    {
        'name': 'buying_mode',
        'required': True,
        'choices': BUYING_MODES
    },
    {
        'name': 'listing_type',
        'required': True,
        'choices': LISTING_TYPES
    },
    {
        'name': 'condition',
        'required': True,
        'choices': CONDITIONS
    },
    {
        'name': 'envio_gratis',
        'choices': FREE_SHIPPING_OPTIONS
    },
    {
        'name': 'image_1',
        'required': False
    },
    {'name': 'image_2', 'required': False},
    {'name': 'image_3', 'required': False},
]

import os
from os.path import dirname, join
import smartcsv

current_path = dirname(os.path.realpath(__file__))
count = 0
with open(join(current_path, 'lpnk-data.csv'), 'r') as f:
    reader = smartcsv.reader(f, columns=COLUMNS, fail_fast=False)
    for obj in reader:
        count += 1
    assert count == 70
    assert reader.errors == {}
