import cassiopeia as cass
from cassiopeia import Queue, MatchHistory, Summoner, Match

from ezreal.models.dto import SummonerDTO, FinalAveragedStatsDTO


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


def read_matches_history(summoner, match_number: int):
    summoner = Summoner(account_id=summoner.id, region=summoner.region)
    match_history = MatchHistory(summoner=summoner, queues={Queue.normal_draft_fives}, end_index=match_number)
    match_ids = [match.id for match in match_history]
    player_stat = list()
    for id in match_ids:
        match = Match(id=id, region=summoner.region)
        for participant in match.participants:
            if participant.summoner.account_id == summoner.account_id:
                statsBO = participant.stats

                duration_minutes = match.duration.seconds / 60.0

                statsDTO = dict()
                statsDTO['kda'] = statsBO.kda
                statsDTO['gold_earned_per_min'] = statsBO.gold_earned / duration_minutes
                statsDTO['total_damage_dealt_to_champions_per_min'] = statsBO.total_damage_dealt_to_champions / duration_minutes
                statsDTO['total_minions_killed_per_min'] = statsBO.total_minions_killed / duration_minutes
                statsDTO['vision_score_per_min'] = statsBO.vision_score / duration_minutes
                player_stat.append(statsDTO)
                break
    statsDTO = FinalAveragedStatsDTO(**dict_mean(player_stat))
    return statsDTO


def dict_mean(dict_list):
    mean_dict = {}
    for key in dict_list[0].keys():
        mean_dict[key] = sum(d[key] for d in dict_list) / len(dict_list)
    return mean_dict
