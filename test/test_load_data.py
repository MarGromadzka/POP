from src.load_data import load_nodes, load_links, load_demands, load_paths


def test_load_nodes():
    nodes_us = load_nodes("../data/janos_us_ca/")
    assert len(nodes_us) == 39
    assert nodes_us[38].name == "SanDiego"
    nodes_pl = load_nodes("../data/polska/")
    assert len(nodes_pl) == 12
    assert nodes_pl[7].name == "Poznan"


def test_load_links():
    links_us = load_links("../data/janos_us_ca/")
    assert len(links_us) == 122
    assert links_us[9].link_id == "L9"
    assert links_us[9].source == "LasVegas"
    assert links_us[9].target == "SaltLakeCity"
    assert links_us[121].link_id == "L121"
    assert links_us[121].source == "SanDiego"
    assert links_us[121].target == "Phoenix"
    links_pl = load_links("../data/polska/")
    assert len(links_pl) == 18
    assert links_pl[9].link_id == "Link_4_8"
    assert links_pl[9].source == "Krakow"
    assert links_pl[9].target == "Rzeszow"


def test_load_demands():
    demands_us = load_demands("../data/janos_us_ca/")
    assert len(demands_us) == 1482
    assert demands_us[1000].demand_id == "D1000"
    assert demands_us[1000].source == "Philadelphia"
    assert demands_us[1000].target == "Chicago"
    demands_pl = load_demands("../data/polska/")
    assert len(demands_pl) == 66
    assert demands_pl[10].demand_id == "Demand_0_11"
    assert demands_pl[10].source == "Gdansk"
    assert demands_pl[10].target == "Wroclaw"


def test_load_paths():
    # no predefined paths for us
    demand_paths_pl = load_paths("../data/polska/")
    assert len(demand_paths_pl) == 66
    assert demand_paths_pl[4].demand_id == "Demand_0_5"
    assert demand_paths_pl[4].paths[5].path_id == "P_5"
    assert len(demand_paths_pl[4].paths[5].links) == 8
    assert demand_paths_pl[4].paths[5].links[5] == "Link_3_4"