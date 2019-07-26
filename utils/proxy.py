import imoocdjango.settings


def proxy():
    if imoocdjango.settings.USE_PROXY:
        # add your proxy here
        return {}
    else:
        return {}
