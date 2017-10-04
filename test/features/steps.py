# -*- coding: utf-8 -*-
from lettuce import step, world
from edades import Edades


@step(u'Dado que tengo la edad "([^"]*)"')
def dado_que_tengo_la_edad_group1(step, edad):
    world.ed = Edades()
    world.res = world.ed.edad(int(edad))

@step(u'cuando ingreso este numero')
def cuando_ingreso_este_numero(step):
    pass
@step(u'entonces obtengo el resultado "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
	assert esperado == world.res,'El resultado esperado de '+esperado+" y el obtenido es "+world.res