def at_server_start():
    import athanor

    from .events import character_at_post_msg_receive

    athanor.EVENTS["character_at_post_msg_receive"].connect(
        character_at_post_msg_receive
    )
