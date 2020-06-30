import cassiopeia as cass
from cassiopeia import Summoner
from ezreal.utils import engine


def print_summoner(name: str, region: str):
    cass.set_riot_api_key("RGAPI-3458e491-3eb1-49f0-b077-afd3af8a1f55")
    summoner = Summoner(name=name, region=region)
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


if __name__ == "__main__":
    summoner = print_summoner("Kassout", "EUW")
    # print(summoner)