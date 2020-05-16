#!/usr/bin/env python3

import logging
import yaml
import sys
import os

logging.basicConfig(
    level=logging.INFO,
    #level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )

target_dir = sys.argv[1]

jobs_on_platform={}

class AWS_GCP:
    def __init__(self, aws=0, gcp=0, both=0):
        self.aws = aws
        self.gcp = gcp
        self.both = both


def check(jobs):
    aws=0
    gcp=0
    for j in jobs:
        for c in j.get('spec', {}).get('containers',[]):
            for e in c.get('env',[]):
                if e.get('name', '') == 'CLUSTER_TYPE':
                    v=e.get('value', '').lower().strip()
                    if v == 'aws':
                        aws +=1
                    if v == 'gcp':
                        gcp +=1
    return (aws, gcp)

aws_only=0
gcp_only=0
both=0
neither=0

for root, dirs, files in os.walk(target_dir):
    for file in files:
        path=os.path.join(root, file)
        logging.debug('handling %s', path)
        if path.endswith(".yaml"):
            with open(path) as f:
                all = yaml.load(f, Loader=yaml.FullLoader)
                i=0
                for t in ("presubmits", "postsubmits"):
                    if t!='presubmits':
                        continue
                    if i>1:
                        logging.error("something is wrong %d", i)
                    i+=1
                    if t not in path:
                        continue
                    for repo in all[t]:
                        aws,gcp = check(all[t][repo])
                        if aws>0 and gcp>0:
                            logging.debug("both path: %s", path)
                            both += 1
                        if aws>0 and gcp==0:
                            logging.debug("aws path: %s", path)
                            aws_only += 1               
                        if aws==0 and gcp>0:
                            logging.debug("gcp path: %s", path)
                            gcp_only += 1    
                        if aws==0 and gcp==0:
                            logging.debug("neither path: %s", path)
                            neither += 1   
                if "periodics" in path:
                    for job in all["periodics"]:
                        pass

logging.info("aws_only: %d", aws_only)
logging.info("gcp_only: %d", gcp_only)
logging.info("both: %d", both)
logging.info("neither: %d", neither)