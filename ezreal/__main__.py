import cassiopeia as cass
from cassiopeia import Summoner
from ezreal.utils import engine
from ezreal.core.query import read_summoner_info, read_matches_history


def print_summoner(name: str, region: str):
    summoner = read_summoner_info(name, region)
    print("Name:", summoner.name)
    print("ID:", summoner.id)
    print("Account ID:", summoner.account_id)
    print("Level:", summoner.level)
    print("Revision date:", summoner.revision_date)
    print("Profile icon ID:", summoner.profile_icon.id)
    print("Profile icon name:", summoner.profile_icon.name)
    print("Profile icon URL:", summoner.profile_icon.url)
    print("Profile icon image:", summoner.profile_icon.image)
    return summoner


def print_match_history(name: str, region: str):
    summoner = read_summoner_info(name, region)
    match_history = read_matches_history(summoner, 20)
    return match_history


if __name__ == "__main__":
    summoner = print_match_history("Kassout", "EUW")
    # print(summoner)