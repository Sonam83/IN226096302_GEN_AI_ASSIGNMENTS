from dotenv import load_dotenv

from chains.extraction_chain import extraction_chain
from chains.matching_chain import matching_chain
from chains.scoring_chain import scoring_chain
from chains.explanation_chain import explanation_chain

import os

load_dotenv()

def run_pipeline(resume, jd):

    print("\n--- Extraction ---")
    extracted = extraction_chain.invoke({"resume": resume}).content
    print(extracted)

    print("\n--- Matching ---")
    match = matching_chain.invoke({
        "resume_data": extracted,
        "job_desc": jd
    }).content
    print(match)

    print("\n--- Scoring ---")
    score = scoring_chain.invoke({"match_data": match}).content
    print(score)

    print("\n--- Explanation ---")
    explanation = explanation_chain.invoke({
        "score": score,
        "match_data": match
    }).content
    print(explanation)


if __name__ == "__main__":

    with open("data/job_description.txt") as f:
        jd = f.read()

    print("\n===== STRONG CANDIDATE =====")
    with open("data/resume_weak.txt") as f:
        resume = f.read()
    run_pipeline(resume, jd)