def on_chat():
    agent.teleport_to_player()
    agent.move(BACK, 4)
    agent.set_slot(1)
    agent.set_assist(PLACE_ON_MOVE, True)
    agent.set_assist(DESTROY_OBSTACLES, True)
    for i in range(14):
        agent.set_item(SANDSTONE, 4, 1)
        agent.move(BACK, 30)
        agent.move(UP, 1)
        agent.turn(RIGHT_TURN)
        agent.turn(RIGHT_TURN)
player.on_chat("wall", on_chat)
