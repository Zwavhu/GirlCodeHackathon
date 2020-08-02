def on_chat():
    agent.teleport_to_player()
    agent.move(FORWARD, 5)
    agent.set_slot(1)
    agent.set_assist(PLACE_ON_MOVE, True)
    agent.set_assist(DESTROY_OBSTACLES, True)
    for i in range(15):
        for j in range(4):
            agent.set_item(GLASS, 16, 1)
            agent.move(FORWARD, 10)
            agent.turn(LEFT_TURN)
        agent.move(UP, 1)
player.on_chat("tank", on_chat)
