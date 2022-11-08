import requests


url = "https://api.duckduckgo.com"

def test_ddg0():
    response = requests.get(url + "/?q=presidents+of+the+united+states&format=json")
    response_dt = response.json()
    
    assert "Presidents of the United" in response_dt["Heading"]

    assert "Lincoln" in response_dt["RelatedTopics"][0]["Result"]

    assert "Jackson" in response_dt["RelatedTopics"][2]["Result"]

    assert "Johnson" in response_dt["RelatedTopics"][3]["Result"]

    assert "Obama" in response_dt["RelatedTopics"][4]["Result"]

    assert "Harrison" in response_dt["RelatedTopics"][5]["Result"]

    assert "Buren" in response_dt["RelatedTopics"][6]["Result"]

    assert "Jefferson" in response_dt["RelatedTopics"][7]["Result"]

    assert "Coolidge" in response_dt["RelatedTopics"][8]["Result"]

    assert "Arthur" in response_dt["RelatedTopics"][9]["Result"]

    assert "Wilson" in response_dt["RelatedTopics"][-2]["Result"]

    assert "Taylor" in response_dt["RelatedTopics"][-1]["Result"]

    assert "McKinley" in response_dt["RelatedTopics"][-3]["Result"]

    assert "Taft" in response_dt["RelatedTopics"][-4]["Result"]

    assert "Harrison" in response_dt["RelatedTopics"][-5]["Result"]

    assert "Harding" in response_dt["RelatedTopics"][-7]["Result"]

    assert "Trump" in response_dt["RelatedTopics"][12]["Result"]

    assert "Adams" in response_dt["RelatedTopics"][14]["Result"]

    assert "Roosevelt" in response_dt["RelatedTopics"][15]["Result"]

    assert "Pierce" in response_dt["RelatedTopics"][16]["Result"]

    assert "Bush" in response_dt["RelatedTopics"][18]["Result"]

    assert "Washington" in response_dt["RelatedTopics"][19]["Result"]

    assert "Nixon" in response_dt["RelatedTopics"][-17]["Result"]

    assert "Reagan" in response_dt["RelatedTopics"][-16]["Result"]

    assert "Hayes" in response_dt["RelatedTopics"][-15]["Result"]

    assert "Roosevelt" in response_dt["RelatedTopics"][-12]["Result"]

    assert "Bush" in response_dt["RelatedTopics"][20]["Result"]

    assert "Ford" in response_dt["RelatedTopics"][21]["Result"]

    assert "Cleveland" in response_dt["RelatedTopics"][22]["Result"]

    assert "Truman" in response_dt["RelatedTopics"][23]["Result"]

    assert "Hoover" in response_dt["RelatedTopics"][24]["Result"]

    assert "Garfield" in response_dt["RelatedTopics"][27]["Result"]

    assert "Buchanan" in response_dt["RelatedTopics"][28]["Result"]

    assert "Polk" in response_dt["RelatedTopics"][29]["Result"]

    assert "Madison" in response_dt["RelatedTopics"][30]["Result"]

    assert "Monroe" in response_dt["RelatedTopics"][32]["Result"]

    assert "Carter" in response_dt["RelatedTopics"][33]["Result"]

    assert "Biden" in response_dt["RelatedTopics"][34]["Result"]

    assert "Adams" in response_dt["RelatedTopics"][35]["Result"]

    assert "Kennedy" in response_dt["RelatedTopics"][36]["Result"]

    assert "Tyler" in response_dt["RelatedTopics"][38]["Result"]

    assert "Johnson" in response_dt["RelatedTopics"][41]["Result"]

    assert "Fillmore" in response_dt["RelatedTopics"][44]["Result"]

































