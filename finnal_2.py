import tank_2

tank1 = tank_2.Tank('Tiger', 100, 30, 50, 100)
super_tank2 = tank_2.SuperTank('Leopard', 100, 30, 50, 100)

tank1.shot(super_tank2)
tank1.shot(super_tank2)
tank1.shot(super_tank2)

super_tank2.shot(tank1)
super_tank2.shot(tank1)
super_tank2.shot(tank1)
super_tank2.shot(tank1)