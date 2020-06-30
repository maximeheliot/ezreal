import cassiopeia as cass
from cassiopeia import Queue

from ezreal.models.dto import SummonerDTO


def read_summoner_info(name: str, region: str):
    summoner_bo = cass.get_summoner(name=name, region=region)
    summoner_dto = SummonerDTO()
    summoner_dto.name = summoner_bo.name
    summoner_dto.level = summoner_bo.level
    summoner_dto.rank = summoner_bo.ranks[Queue.ranked_solo_fives].tier.value + " " \
                        + summoner_bo.ranks[Queue.ranked_solo_fives].division.value
    summoner_dto.profile_icon_url = summoner_bo.profile_icon.url
    return summoner_dto