def domain_name(url):
    starts = ["http://", "https://", "www."]
    for start in starts:
        url = url.replace(start, "")
    return url.split(".")[0]

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"