import cassiopeia as cass
from cassiopeia import Queue

from ezreal.models.dto import SummonerDTO


class MissingParameterError(Exception):
    """Exception class for handling missing parameter error."""
    pass


def read_summoner_info(name: str = None, region: str = None, id: str = None):
    if name is None:
        summoner_bo = cass.get_summoner(account_id=id, region=region)
    elif id is None:
        summoner_bo = cass.get_summoner(name=name, region=region)
    else:
        raise MissingParameterError("Parameter's missing, name or id are mandatory.")
    summoner_dto = SummonerDTO()
    summoner_dto.id = summoner_bo.account_id
    summoner_dto.name = summoner_bo.name
    summoner_dto.region = summoner_bo.region.value
    summoner_dto.level = summoner_bo.level

    ranks = summoner_bo.ranks
    if ranks:
        summoner_dto.rank = ranks[Queue.ranked_solo_fives].tier.value + " " \
                            + ranks[Queue.ranked_solo_fives].division.value
    else:
        summoner_dto.rank = "Unranked"

    summoner_dto.profile_icon_url = summoner_bo.profile_icon.url

    return summoner_dto
