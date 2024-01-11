import os
import json
import Inventory

# Currencies included in the game:
# Copper, Silver, Electrum, Gold, Platinum

def cu_ag(amt):
    return amt / 10
def cu_es(amt):
    return amt / 50
def cu_au(amt):
    return amt / 100
def cu_pt(amt):
    return amt / 1000

def ag_cu(amt):
    return amt * 10
def ag_es(amt):
    return amt / 5
def ag_au(amt):
    return amt / 10
def ag_pt(amt):
    return amt / 1000

def es_cu(amt):
    return amt * 50
def es_ag(amt):
    return amt * 5
def es_au(amt):
    return amt / 2
def es_pt(amt):
    return amt / 20

def au_cu(amt):
    return amt * 100
def au_ag(amt):
    return amt * 10
def au_es(amt):
    return amt * 2
def au_pt(amt):
    return amt /10

def pt_cu(amt):
    return amt * 1000
def pt_ag(amt):
    return amt * 100
def pt_es(amt):
    return amt * 20
def pt_ag(amt):
    return amt * 10

def forex(amt,cur):
    if cur == "cp":
        return amt - 250
    elif cur == "sp":
        return amt - 100
    elif cur == "ep":
        return amt - 50
    elif cur == "gp":
        return amt - 10
    elif cur == "pp":
        return amt - 5




