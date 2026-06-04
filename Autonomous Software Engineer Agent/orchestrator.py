from agents.planner_agent import planner_agent
from agents.coder_agent import coder_agent
from agents.reviewer_agent import reviewer_agent

def execute_task(prompt):

    plan = planner_agent(prompt)

    generated_code = coder_agent(plan)

    review = reviewer_agent(generated_code)

    return {
        "plan": plan,
        "generated_code": generated_code,
        "review": review
    }
