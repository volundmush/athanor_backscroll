def init(settings, plugins):
    settings.INSTALLED_APPS.append("athanor_backscroll")
    settings.AT_SERVER_STARTSTOP_MODULE.append("athanor_backscroll.startup_hooks")
    settings.CMD_MODULES_CHARACTER.append("athanor_backscroll.commands")
