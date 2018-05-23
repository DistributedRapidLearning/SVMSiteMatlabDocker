import SiteExecutorLib
import json, os

baseUrl = "http://sparql.cancerdata.org/namespace/thunder/sparql"
if os.environ.get("SPARQL_ENDPOINT") is not None:
    baseUrl = os.environ.get("SPARQL_ENDPOINT")

with open("/input.txt") as f:
    inputArgs = json.load(f)

print("run ID: %s" % inputArgs["runId"])
print("iteration #: %s" % inputArgs["itNumber"])

site = SiteExecutorLib.initialize()
site.mainSite(inputArgs["runId"], 
        inputArgs["itNumber"], 
        "/input.txt", 
        "/output.txt", 
        "/tmp", 
        "/log.txt", 
        "http://sparql.cancerdata.org/namespace/thunder/sparql",
        "", 
        "", 
        nargout=0)
